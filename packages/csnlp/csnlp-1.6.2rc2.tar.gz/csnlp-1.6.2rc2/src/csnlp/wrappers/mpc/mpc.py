from inspect import signature
from math import ceil
from typing import Callable, Literal, Optional, TypeVar, Union

import casadi as cs
import numpy as np
import numpy.typing as npt

from ...util.math import repeat
from ..wrapper import Nlp, NonRetroactiveWrapper

SymType = TypeVar("SymType", cs.SX, cs.MX)


def _n(statename: str) -> str:
    """Internal utility for naming initial states."""
    return f"{statename}_0"


class Mpc(NonRetroactiveWrapper[SymType]):
    """A wrapper to easily turn an NLP scheme into an MPC controller. Most of the theory
    for MPC is taken from :cite:`rawlings_model_2017`.

    Parameters
    ----------
    nlp : Nlp
        NLP scheme to be wrapped
    prediction_horizon : int
        A positive integer for the prediction horizon of the MPC controller.
    control_horizon : int, optional
        A positive integer for the control horizon of the MPC controller. If not given,
        it is set equal to the control horizon.
    input_spacing : int, optional
        Spacing between independent input actions. This argument allows to reduce the
        number of free actions along the control horizon by allowing only the first
        action every ``n`` to be free, and the following ``n-1`` to be fixed equal to
        that action (where ``n`` is given by ``input_spacing``). By default, no spacing
        is allowed, i.e., ``1``.
    shooting : 'single' or 'multi', optional
        Type of approach in the direct shooting for parametrizing the control
        trajectory. See Section 8.5 in :cite:`rawlings_model_2017`. By default, direct
        shooting is used.

    Raises
    ------
    ValueError
        Raises if the shooting method is invalid; or if any of the horizons are invalid.
    """

    def __init__(
        self,
        nlp: Nlp[SymType],
        prediction_horizon: int,
        control_horizon: Optional[int] = None,
        input_spacing: int = 1,
        shooting: Literal["single", "multi"] = "multi",
    ) -> None:
        super().__init__(nlp)

        if not isinstance(prediction_horizon, int) or prediction_horizon <= 0:
            raise ValueError("Prediction horizon must be positive and > 0.")
        if shooting == "single":
            self._is_multishooting = False
        elif shooting == "multi":
            self._is_multishooting = True
        else:
            raise ValueError("Invalid shooting method.")

        self._prediction_horizon = prediction_horizon
        if control_horizon is None:
            self._control_horizon = self._prediction_horizon
        elif not isinstance(control_horizon, int) or control_horizon <= 0:
            raise ValueError("Control horizon must be positive and > 0.")
        else:
            self._control_horizon = control_horizon

        if not isinstance(input_spacing, int) or input_spacing <= 0:
            raise ValueError("Input spacing factor must be positive and > 0.")
        else:
            self._input_spacing = input_spacing

        self._states: dict[str, SymType] = {}
        self._initial_states: dict[str, SymType] = {}
        self._actions: dict[str, SymType] = {}
        self._actions_exp: dict[str, SymType] = {}
        self._slacks: dict[str, SymType] = {}
        self._disturbances: dict[str, SymType] = {}
        self._dynamics_already_set = False

    @property
    def prediction_horizon(self) -> int:
        """Gets the prediction horizon of the MPC controller."""
        return self._prediction_horizon

    @property
    def control_horizon(self) -> int:
        """Gets the control horizon of the MPC controller."""
        return self._control_horizon

    @property
    def states(self) -> dict[str, SymType]:
        """Gets the states of the MPC controller."""
        return self._states

    @property
    def initial_states(self) -> dict[str, SymType]:
        """Gets the initial states (parameters) of the MPC controller."""
        return self._initial_states

    @property
    def first_states(self) -> dict[str, SymType]:
        """Gets the first (along the prediction horizon) states of the controller."""
        return {n: s[:, 0] for n, s in self._states.items()}

    @property
    def first_actions(self) -> dict[str, SymType]:
        """Gets the first (along the prediction horizon) actions of the controller."""
        return {n: a[:, 0] for n, a in self._actions.items()}

    @property
    def ns(self) -> int:
        """Gets the number of states of the MPC controller."""
        return sum(x0.shape[0] for x0 in self._initial_states.values())

    @property
    def actions(self) -> dict[str, SymType]:
        """Gets the control actions of the MPC controller."""
        return self._actions

    @property
    def actions_expanded(self) -> dict[str, SymType]:
        """Gets the expanded control actions of the MPC controller."""
        return self._actions_exp

    @property
    def na(self) -> int:
        """Gets the number of actions of the MPC controller."""
        return sum(a.shape[0] for a in self._actions.values())

    @property
    def slacks(self) -> dict[str, SymType]:
        """Gets the slack variables of the MPC controller."""
        return self._slacks

    @property
    def nslacks(self) -> int:
        """Gets the number of slacks of the MPC controller."""
        return sum(s.shape[0] for s in self._slacks.values())

    @property
    def disturbances(self) -> dict[str, SymType]:
        """Gets the disturbance parameters of the MPC controller."""
        return self._disturbances

    @property
    def nd(self) -> int:
        """Gets the number of disturbances in the MPC controller."""
        return sum(d.shape[0] for d in self._disturbances.values())

    def state(
        self,
        name: str,
        size: int = 1,
        discrete: bool = False,
        lb: Union[npt.ArrayLike, cs.DM] = -np.inf,
        ub: Union[npt.ArrayLike, cs.DM] = +np.inf,
        bound_initial: bool = True,
        bound_terminal: bool = True,
    ) -> tuple[Optional[SymType], SymType]:
        """Adds a state variable to the MPC controller along the whole prediction
        horizon. Automatically creates the constraint on the initial conditions for this
        state.

        Parameters
        ----------
        name : str
            Name of the state.
        size : int
            Size of the state (assumed to be a vector).
        discrete : bool, optional
            Flag indicating if the state is discrete. Defaults to ``False``.
        lb : array_like, casadi.DM, optional
            Hard lower bound of the state, by default ``-np.inf``.
        ub : array_like, casadi.DM, optional
            Hard upper bound of the state, by default ``+np.inf``.
        bound_initial : bool, optional
            If ``False``, then the upper and lower bounds on the initial state are not
            imposed, i.e., set to ``+/- np.inf`` (since the initial state is constrained
            to be equal to the current state of the system, it is sometimes advantageous
            to remove its bounds). By default ``True``.
        bound_terminal : bool, optional
            Same as above, but for the terminal state. By default ``True``.

        Returns
        -------
        state : casadi.SX or MX or None
            The state symbolic variable. If ``shooting=single``, then ``None`` is
            returned since the state will only be available once the dynamics are set.
        initial state : casadi.SX or MX
            The initial state symbolic parameter.

        Raises
        ------
        ValueError
            Raises if there exists already a state with the same name.
        RuntimeError
            Raises in single shooting if lower or upper bounds have been specified,
            since these can only be set after the dynamics have been set via the
            :meth:`constraint` method.
        """
        x0_name = _n(name)
        if self._is_multishooting:
            shape = (size, self._prediction_horizon + 1)
            lb = np.broadcast_to(lb, shape).astype(float)
            ub = np.broadcast_to(ub, shape).astype(float)
            if not bound_initial:
                lb[:, 0] = -np.inf
                ub[:, 0] = +np.inf
            if not bound_terminal:
                lb[:, -1] = -np.inf
                ub[:, -1] = +np.inf

            # create state variable and initial state constraint
            x = self.nlp.variable(name, shape, discrete, lb, ub)[0]
            x0 = self.nlp.parameter(x0_name, (size, 1))
            self.nlp.constraint(x0_name, x[:, 0], "==", x0)
        else:
            if np.any(lb != -np.inf) or np.any(ub != +np.inf):
                raise RuntimeError(
                    "in single shooting, lower and upper state bounds can only be "
                    "created, after the dynamics have been set, via the `constraint` "
                    "method"
                )
            x = None
            x0 = self.nlp.parameter(x0_name, (size, 1))
        self._states[name] = x
        self._initial_states[x0_name] = x0
        return x, x0

    def action(
        self,
        name: str,
        size: int = 1,
        discrete: bool = False,
        lb: Union[npt.ArrayLike, cs.DM] = -np.inf,
        ub: Union[npt.ArrayLike, cs.DM] = +np.inf,
    ) -> tuple[SymType, SymType]:
        """Adds a control action variable to the MPC controller along the whole control
        horizon. Automatically expands this action to be of the same length of the
        prediction horizon by padding with the final action.

        Parameters
        ----------
        name : str
            Name of the control action.
        size : int, optional
            Size of the control action (assumed to be a vector). Defaults to ``1``.
        discrete : bool, optional
            Flag indicating if the action is discrete. Defaults to ``False``.
        lb : array_like, casadi.DM, optional
            Hard lower bound of the control action, by default ``-np.inf``.
        ub : array_like, casadi.DM, optional
            Hard upper bound of the control action, by default ``+np.inf``.

        Returns
        -------
        action : casadi.SX or MX
            The control action symbolic variable.
        action_expanded : casadi.SX or MX
            The same control  action variable, but expanded to the same length of the
            prediction horizon.
        """
        nu_free = ceil(self._control_horizon / self._input_spacing)
        u = self.nlp.variable(name, (size, nu_free), discrete, lb, ub)[0]

        u_exp: SymType = (
            u
            if self._input_spacing == 1
            else repeat(u, (1, self._input_spacing))[:, : self._control_horizon]
        )
        gap = self._prediction_horizon - u_exp.shape[1]
        u_last = u_exp[:, -1]
        u_exp = cs.horzcat(u_exp, *(u_last for _ in range(gap)))

        self._actions[name] = u
        self._actions_exp[name] = u_exp
        return u, u_exp

    def disturbance(self, name: str, size: int = 1) -> SymType:
        """Adds a disturbance parameter to the MPC controller along the whole prediction
        horizon.

        Parameters
        ----------
        name : str
            Name of the disturbance.
        size : int, optional
            Size of the disturbance (assumed to be a vector). Defaults to ``1``.

        Returns
        -------
        casadi.SX or MX
            The symbol for the new disturbance in the MPC controller.
        """
        d = self.nlp.parameter(name, (size, self._prediction_horizon))
        self._disturbances[name] = d
        return d

    def constraint(
        self,
        name: str,
        lhs: Union[SymType, np.ndarray, cs.DM],
        op: Literal["==", ">=", "<="],
        rhs: Union[SymType, np.ndarray, cs.DM],
        soft: bool = False,
        simplify: bool = True,
    ) -> tuple[SymType, ...]:
        """See :meth:`csnlp.Nlp.constraint`."""
        out = self.nlp.constraint(name, lhs, op, rhs, soft, simplify)
        if soft:
            self._slacks[f"slack_{name}"] = out[2]
        return out

    def set_nonlinear_dynamics(
        self,
        F: Union[
            cs.Function,
            Callable[[tuple[npt.ArrayLike, ...]], tuple[npt.ArrayLike, ...]],
        ],
    ) -> None:
        """Sets nonlinear dynamics of the controller's prediction model and creates the
        corresponding dynamics constraints.

        Parameters
        ----------
        F : casadi.Function or callable
            A CasADi function of the form :math:`x_+ = F(x,u)` or :math:`x+ = F(x,u,d)`,
            where :math:`x,u,d` are the state, action, disturbances respectively,
            :math:`F` is a generic nonlinear function and :math:`x_+` is the next state.
            The function can have multiple outputs, in which case :math:`x_+` is assumed
            to be the first one.

        Raises
        ------
        ValueError
            When setting, raises if the dynamics do not accept 2 or 3 input arguments.
        RuntimeError
            When setting, raises if the dynamics have been already set; or if the
            function ``F`` does not take accept the expected input sizes.
        """
        if self._dynamics_already_set:
            raise RuntimeError("Dynamics were already set.")
        n_in = F.n_in() if isinstance(F, cs.Function) else len(signature(F).parameters)
        if n_in < 2 or n_in > 3:
            raise ValueError(
                "The dynamics function must accepted 2 or 3 arguments; got "
                f"{n_in} inputs."
            )
        if self._is_multishooting:
            self._set_multishooting_nonlinear_dynamics(F, n_in)
        else:
            self._set_singleshooting_nonlinear_dynamics(F, n_in)
        self._dynamics_already_set = True

    def _set_multishooting_nonlinear_dynamics(self, F: cs.Function, n_in: int) -> None:
        """Internal utility to create nonlinear dynamics constraints in multiple
        shooting."""
        X = cs.vcat(self._states.values())
        U = cs.vcat(self._actions_exp.values())
        if n_in < 3:
            args_at = lambda k: (X[:, k], U[:, k])
        else:
            D = cs.vcat(self._disturbances.values())
            args_at = lambda k: (X[:, k], U[:, k], D[:, k])
        xs_next = []
        for k in range(self._prediction_horizon):
            x_next = F(*args_at(k))
            if isinstance(x_next, (tuple, list)):
                x_next = x_next[0]
            xs_next.append(x_next)
        self.constraint("dyn", cs.hcat(xs_next), "==", X[:, 1:])

    def _set_singleshooting_nonlinear_dynamics(self, F: cs.Function, n_in: int) -> None:
        """Internal utility to create nonlinear dynamics constraints and states in
        single shooting."""
        Xk = cs.vcat(self._initial_states.values())
        U = cs.vcat(self._actions_exp.values())
        if n_in < 3:
            args_at = lambda k: (U[:, k],)
        else:
            D = cs.vcat(self._disturbances.values())
            args_at = lambda k: (U[:, k], D[:, k])
        X = [Xk]
        for k in range(self._prediction_horizon):
            Xk = F(Xk, *args_at(k))
            if isinstance(Xk, (tuple, list)):
                Xk = Xk[0]
            X.append(Xk)
        X = cs.hcat(X)
        cumsizes = np.cumsum([0] + [s.shape[0] for s in self._initial_states.values()])
        self._states = dict(zip(self._states.keys(), cs.vertsplit(X, cumsizes)))
