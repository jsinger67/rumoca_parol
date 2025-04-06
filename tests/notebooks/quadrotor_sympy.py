"""
Automatically generated by Rumoca
"""
import sympy
from sympy import Matrix, ImmutableDenseMatrix, Piecewise, Tuple
import numpy as np
import scipy.integrate

cos = sympy.cos
sin = sympy.sin
tan = sympy.tan


def flatten_piecewise_with_nested_matrices(matrix):
    assert isinstance(matrix, (Matrix, ImmutableDenseMatrix, Tuple)), "Input must be a Matrix object or Tuple"
    piecewise = sympy.piecewise_fold(sympy.Piecewise((matrix, True)))

    if isinstance(piecewise, (Matrix, ImmutableDenseMatrix, Tuple)):
        return piecewise

    def flatten_matrix(matrix):
        """Recursively flatten nested matrices."""
        if isinstance(matrix, (Matrix, ImmutableDenseMatrix, Tuple)):
            flattened = []
            for elem in matrix:
                if isinstance(elem, (Matrix, ImmutableDenseMatrix, Tuple)):
                    flattened.extend(flatten_matrix(elem))
                else:
                    flattened.append(elem)
            return Matrix(flattened)
        return matrix

    flattened_conditions = []
    for expr, cond in piecewise.args:
        flattened_expr = flatten_matrix(expr) if isinstance(expr, (Matrix, ImmutableDenseMatrix, Tuple)) else expr
        flattened_conditions.append((flattened_expr, cond))
    return sympy.piecewise_exclusive(Piecewise(*flattened_conditions))


class Model:
    """
    Flattened Modelica Model
    """

    def __init__(self):
        # ============================================
        # Initialize
        self.solved = False

        # ============================================
        # Declare time
        self.time = sympy.symbols('time')

        # ============================================
        # Declare u
        a = sympy.symbols('a')
        e = sympy.symbols('e')
        r = sympy.symbols('r')
        t = sympy.symbols('t')
        self.u = sympy.Matrix([
            a, 
            e, 
            r, 
            t])
        self.u0 = { 
            'a': 0.0, 
            'e': 0.0, 
            'r': 0.0, 
            't': 0.0}
        self.u_index = { 
            'a': 0, 
            'e': 1, 
            'r': 2, 
            't': 3}
        self.u_index_rev = [ 
            'a', 
            'e', 
            'r', 
            't']
        # ============================================
        # Declare p
        l = sympy.symbols('l')
        mix_a = sympy.symbols('mix_a')
        mix_e = sympy.symbols('mix_e')
        mix_r = sympy.symbols('mix_r')
        mix_t = sympy.symbols('mix_t')
        m = sympy.symbols('m')
        g = sympy.symbols('g')
        J_x = sympy.symbols('J_x')
        J_y = sympy.symbols('J_y')
        J_z = sympy.symbols('J_z')
        J_xz = sympy.symbols('J_xz')
        Lambda = sympy.symbols('Lambda')
        m_1_Cm = sympy.symbols('m_1_Cm')
        m_1_Ct = sympy.symbols('m_1_Ct')
        m_1_tau = sympy.symbols('m_1_tau')
        m_2_Cm = sympy.symbols('m_2_Cm')
        m_2_Ct = sympy.symbols('m_2_Ct')
        m_2_tau = sympy.symbols('m_2_tau')
        m_3_Cm = sympy.symbols('m_3_Cm')
        m_3_Ct = sympy.symbols('m_3_Ct')
        m_3_tau = sympy.symbols('m_3_tau')
        m_4_Cm = sympy.symbols('m_4_Cm')
        m_4_Ct = sympy.symbols('m_4_Ct')
        m_4_tau = sympy.symbols('m_4_tau')
        self.p = sympy.Matrix([
            l, 
            mix_a, 
            mix_e, 
            mix_r, 
            mix_t, 
            m, 
            g, 
            J_x, 
            J_y, 
            J_z, 
            J_xz, 
            Lambda, 
            m_1_Cm, 
            m_1_Ct, 
            m_1_tau, 
            m_2_Cm, 
            m_2_Ct, 
            m_2_tau, 
            m_3_Cm, 
            m_3_Ct, 
            m_3_tau, 
            m_4_Cm, 
            m_4_Ct, 
            m_4_tau])
        self.p0 = { 
            'l': 1.0, 
            'mix_a': 1.0, 
            'mix_e': 1.0, 
            'mix_r': 10.0, 
            'mix_t': 32.0, 
            'm': 1.0, 
            'g': 9.81, 
            'J_x': 1.0, 
            'J_y': 1.0, 
            'J_z': 1.0, 
            'J_xz': 0.0, 
            'Lambda': 1.0, 
            'm_1_Cm': 0.01, 
            'm_1_Ct': 0.01, 
            'm_1_tau': 0.1, 
            'm_2_Cm': 0.01, 
            'm_2_Ct': 0.01, 
            'm_2_tau': 0.1, 
            'm_3_Cm': 0.01, 
            'm_3_Ct': 0.01, 
            'm_3_tau': 0.1, 
            'm_4_Cm': 0.01, 
            'm_4_Ct': 0.01, 
            'm_4_tau': 0.1}
        self.p_index = { 
            'l': 0, 
            'mix_a': 1, 
            'mix_e': 2, 
            'mix_r': 3, 
            'mix_t': 4, 
            'm': 5, 
            'g': 6, 
            'J_x': 7, 
            'J_y': 8, 
            'J_z': 9, 
            'J_xz': 10, 
            'Lambda': 11, 
            'm_1_Cm': 12, 
            'm_1_Ct': 13, 
            'm_1_tau': 14, 
            'm_2_Cm': 15, 
            'm_2_Ct': 16, 
            'm_2_tau': 17, 
            'm_3_Cm': 18, 
            'm_3_Ct': 19, 
            'm_3_tau': 20, 
            'm_4_Cm': 21, 
            'm_4_Ct': 22, 
            'm_4_tau': 23}
        self.p_index_rev = [ 
            'l', 
            'mix_a', 
            'mix_e', 
            'mix_r', 
            'mix_t', 
            'm', 
            'g', 
            'J_x', 
            'J_y', 
            'J_z', 
            'J_xz', 
            'Lambda', 
            'm_1_Cm', 
            'm_1_Ct', 
            'm_1_tau', 
            'm_2_Cm', 
            'm_2_Ct', 
            'm_2_tau', 
            'm_3_Cm', 
            'm_3_Ct', 
            'm_3_tau', 
            'm_4_Cm', 
            'm_4_Ct', 
            'm_4_tau']
        # ============================================
        # Declare c
        c0 = sympy.symbols('c0')
        self.c = sympy.Matrix([
            c0])
        self.c0 = { 
            'c0': False}
        self.c_index = { 
            'c0': 0}
        self.c_index_rev = [ 
            'c0']
        # ============================================
        # Declare cp
        self.cp = sympy.Matrix([])
        self.cp0 = { }
        self.cp_index = { }
        self.cp_index_rev = [ ]
        # ============================================
        # Declare x
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        h = sympy.symbols('h')
        P = sympy.symbols('P')
        Q = sympy.symbols('Q')
        R = sympy.symbols('R')
        U = sympy.symbols('U')
        V = sympy.symbols('V')
        W = sympy.symbols('W')
        phi = sympy.symbols('phi')
        theta = sympy.symbols('theta')
        psi = sympy.symbols('psi')
        m_1_omega = sympy.symbols('m_1_omega')
        m_2_omega = sympy.symbols('m_2_omega')
        m_3_omega = sympy.symbols('m_3_omega')
        m_4_omega = sympy.symbols('m_4_omega')
        self.x = sympy.Matrix([
            x, 
            y, 
            h, 
            P, 
            Q, 
            R, 
            U, 
            V, 
            W, 
            phi, 
            theta, 
            psi, 
            m_1_omega, 
            m_2_omega, 
            m_3_omega, 
            m_4_omega])
        self.x0 = { 
            'x': 0.0, 
            'y': 0.0, 
            'h': 0.0, 
            'P': 0.0, 
            'Q': 0.0, 
            'R': 0.0, 
            'U': 0.0, 
            'V': 0.0, 
            'W': 0.0, 
            'phi': 0.0, 
            'theta': 0.0, 
            'psi': 0.0, 
            'm_1_omega': 0.0, 
            'm_2_omega': 0.0, 
            'm_3_omega': 0.0, 
            'm_4_omega': 0.0}
        self.x_index = { 
            'x': 0, 
            'y': 1, 
            'h': 2, 
            'P': 3, 
            'Q': 4, 
            'R': 5, 
            'U': 6, 
            'V': 7, 
            'W': 8, 
            'phi': 9, 
            'theta': 10, 
            'psi': 11, 
            'm_1_omega': 12, 
            'm_2_omega': 13, 
            'm_3_omega': 14, 
            'm_4_omega': 15}
        self.x_index_rev = [ 
            'x', 
            'y', 
            'h', 
            'P', 
            'Q', 
            'R', 
            'U', 
            'V', 
            'W', 
            'phi', 
            'theta', 
            'psi', 
            'm_1_omega', 
            'm_2_omega', 
            'm_3_omega', 
            'm_4_omega']
        # ============================================
        # Declare m
        self.m = sympy.Matrix([])
        self.m0 = { }
        self.m_index = { }
        self.m_index_rev = [ ]
        # ============================================
        # Declare y
        m_1_moment = sympy.symbols('m_1_moment')
        m_2_moment = sympy.symbols('m_2_moment')
        m_3_moment = sympy.symbols('m_3_moment')
        m_4_moment = sympy.symbols('m_4_moment')
        R_z = sympy.symbols('R_z')
        F_x = sympy.symbols('F_x')
        F_y = sympy.symbols('F_y')
        F_z = sympy.symbols('F_z')
        M_x = sympy.symbols('M_x')
        M_y = sympy.symbols('M_y')
        M_z = sympy.symbols('M_z')
        m_1_omega_ref = sympy.symbols('m_1_omega_ref')
        m_1_thrust = sympy.symbols('m_1_thrust')
        m_2_omega_ref = sympy.symbols('m_2_omega_ref')
        m_2_thrust = sympy.symbols('m_2_thrust')
        m_3_omega_ref = sympy.symbols('m_3_omega_ref')
        m_3_thrust = sympy.symbols('m_3_thrust')
        m_4_omega_ref = sympy.symbols('m_4_omega_ref')
        m_4_thrust = sympy.symbols('m_4_thrust')
        self.y = sympy.Matrix([
            m_1_moment, 
            m_2_moment, 
            m_3_moment, 
            m_4_moment, 
            R_z, 
            F_x, 
            F_y, 
            F_z, 
            M_x, 
            M_y, 
            M_z, 
            m_1_omega_ref, 
            m_1_thrust, 
            m_2_omega_ref, 
            m_2_thrust, 
            m_3_omega_ref, 
            m_3_thrust, 
            m_4_omega_ref, 
            m_4_thrust])
        self.y0 = { 
            'm_1_moment': 0.0, 
            'm_2_moment': 0.0, 
            'm_3_moment': 0.0, 
            'm_4_moment': 0.0, 
            'R_z': 0.0, 
            'F_x': 0.0, 
            'F_y': 0.0, 
            'F_z': 0.0, 
            'M_x': 0.0, 
            'M_y': 0.0, 
            'M_z': 0.0, 
            'm_1_omega_ref': 0.0, 
            'm_1_thrust': 0.0, 
            'm_2_omega_ref': 0.0, 
            'm_2_thrust': 0.0, 
            'm_3_omega_ref': 0.0, 
            'm_3_thrust': 0.0, 
            'm_4_omega_ref': 0.0, 
            'm_4_thrust': 0.0}
        self.y_index = { 
            'm_1_moment': 0, 
            'm_2_moment': 1, 
            'm_3_moment': 2, 
            'm_4_moment': 3, 
            'R_z': 4, 
            'F_x': 5, 
            'F_y': 6, 
            'F_z': 7, 
            'M_x': 8, 
            'M_y': 9, 
            'M_z': 10, 
            'm_1_omega_ref': 11, 
            'm_1_thrust': 12, 
            'm_2_omega_ref': 13, 
            'm_2_thrust': 14, 
            'm_3_omega_ref': 15, 
            'm_3_thrust': 16, 
            'm_4_omega_ref': 17, 
            'm_4_thrust': 18}
        self.y_index_rev = [ 
            'm_1_moment', 
            'm_2_moment', 
            'm_3_moment', 
            'm_4_moment', 
            'R_z', 
            'F_x', 
            'F_y', 
            'F_z', 
            'M_x', 
            'M_y', 
            'M_z', 
            'm_1_omega_ref', 
            'm_1_thrust', 
            'm_2_omega_ref', 
            'm_2_thrust', 
            'm_3_omega_ref', 
            'm_3_thrust', 
            'm_4_omega_ref', 
            'm_4_thrust']
        # ============================================
        # Declare z
        self.z = sympy.Matrix([])
        self.z0 = { }
        self.z_index = { }
        self.z_index_rev = [ ]
        

        # ============================================
        # Declare pre_x
        pre_x = sympy.symbols('pre_x')
        pre_y = sympy.symbols('pre_y')
        pre_h = sympy.symbols('pre_h')
        pre_P = sympy.symbols('pre_P')
        pre_Q = sympy.symbols('pre_Q')
        pre_R = sympy.symbols('pre_R')
        pre_U = sympy.symbols('pre_U')
        pre_V = sympy.symbols('pre_V')
        pre_W = sympy.symbols('pre_W')
        pre_phi = sympy.symbols('pre_phi')
        pre_theta = sympy.symbols('pre_theta')
        pre_psi = sympy.symbols('pre_psi')
        pre_m_1_omega = sympy.symbols('pre_m_1_omega')
        pre_m_2_omega = sympy.symbols('pre_m_2_omega')
        pre_m_3_omega = sympy.symbols('pre_m_3_omega')
        pre_m_4_omega = sympy.symbols('pre_m_4_omega')
        self.pre_x = sympy.Matrix([
            pre_x, 
            pre_y, 
            pre_h, 
            pre_P, 
            pre_Q, 
            pre_R, 
            pre_U, 
            pre_V, 
            pre_W, 
            pre_phi, 
            pre_theta, 
            pre_psi, 
            pre_m_1_omega, 
            pre_m_2_omega, 
            pre_m_3_omega, 
            pre_m_4_omega])

        # ============================================
        # Declare pre_m
        self.pre_m = sympy.Matrix([])

        # ============================================
        # Declare pre_z
        self.pre_z = sympy.Matrix([])

        # ============================================
        # Declare x_dot
        der_x = sympy.symbols('der_x')
        der_y = sympy.symbols('der_y')
        der_h = sympy.symbols('der_h')
        der_P = sympy.symbols('der_P')
        der_Q = sympy.symbols('der_Q')
        der_R = sympy.symbols('der_R')
        der_U = sympy.symbols('der_U')
        der_V = sympy.symbols('der_V')
        der_W = sympy.symbols('der_W')
        der_phi = sympy.symbols('der_phi')
        der_theta = sympy.symbols('der_theta')
        der_psi = sympy.symbols('der_psi')
        der_m_1_omega = sympy.symbols('der_m_1_omega')
        der_m_2_omega = sympy.symbols('der_m_2_omega')
        der_m_3_omega = sympy.symbols('der_m_3_omega')
        der_m_4_omega = sympy.symbols('der_m_4_omega')
        self.x_dot = sympy.Matrix([
            der_x, 
            der_y, 
            der_h, 
            der_P, 
            der_Q, 
            der_R, 
            der_U, 
            der_V, 
            der_W, 
            der_phi, 
            der_theta, 
            der_psi, 
            der_m_1_omega, 
            der_m_2_omega, 
            der_m_3_omega, 
            der_m_4_omega])

        # ============================================
        # Define Continous Update Function: fx
        self.fx = sympy.Matrix([
            sympy.Piecewise(
            (
                sympy.Matrix([R_z - ((10.0 * h))]),
                c0,
            ),
            (
                sympy.Matrix([R_z - (0.0)]),
                True,
            )), 
            F_x - (-((((m * g) - R_z) * sin(theta)))), 
            F_y - (((((m * g) - R_z) * sin(phi)) * cos(theta))), 
            F_z - ((((((m * g) - R_z) * cos(phi)) * cos(theta)) - (((m_1_thrust + m_2_thrust) + m_3_thrust) + m_4_thrust))), 
            M_x - ((l * (((-(m_1_thrust) + m_2_thrust) - m_3_thrust) + m_4_thrust))), 
            M_y - ((l * (((-(m_1_thrust) + m_2_thrust) + m_3_thrust) - m_4_thrust))), 
            M_z - ((((m_1_moment + m_2_moment) - m_3_moment) - m_4_moment)), 
            m_1_omega_ref - (((((t * mix_t) - (a * mix_a)) + (e * mix_e)) + (r * mix_r))), 
            m_2_omega_ref - (((((t * mix_t) + (a * mix_a)) - (e * mix_e)) + (r * mix_r))), 
            m_3_omega_ref - (((((t * mix_t) - (a * mix_a)) - (e * mix_e)) - (r * mix_r))), 
            m_4_omega_ref - (((((t * mix_t) + (a * mix_a)) + (e * mix_e)) - (r * mix_r))), 
            der_x - (((((U * cos(theta)) * cos(psi)) + (V * (-((cos(phi) * sin(psi))) + ((sin(phi) * sin(theta)) * cos(psi))))) + (W * ((sin(phi) * sin(psi)) + ((cos(phi) * sin(theta)) * cos(psi)))))), 
            der_y - (((((U * cos(theta)) * sin(psi)) + (V * ((cos(phi) * cos(psi)) + ((sin(phi) * sin(theta)) * sin(psi))))) + (W * (-((sin(phi) * cos(psi))) + ((cos(phi) * sin(theta)) * sin(psi)))))), 
            der_h - ((((U * sin(theta)) - ((V * sin(phi)) * cos(theta))) - ((W * cos(phi)) * cos(theta)))), 
            der_U - ((((R * V) - (Q * W)) + (F_x / m))), 
            der_V - (((-((R * U)) + (P * W)) + (F_y / m))), 
            der_W - ((((Q * U) - (P * V)) + (F_z / m))), 
            der_phi - ((P + (tan(theta) * ((Q * sin(phi)) + (R * cos(phi)))))), 
            der_theta - (((Q * cos(phi)) - (R * sin(phi)))), 
            der_psi - ((((Q * sin(phi)) + (R * cos(phi))) / cos(theta))), 
            (Lambda * der_P) - (((((((J_xz * ((J_x - J_y) + J_z)) * P) * Q) - ((((J_z * (J_z - J_y)) + (J_xz * J_xz)) * Q) * R)) + (J_z * M_x)) + (J_xz * M_z))), 
            (J_y * der_Q) - ((((((J_z - J_x) * P) * R) - (J_xz * ((P * P) - (R * R)))) + M_y)), 
            (Lambda * der_R) - (((((((((J_x - J_y) * J_x) + (J_xz * J_xz)) * P) * Q) - (((J_xz * ((J_x - J_y) + J_z)) * Q) * R)) + (J_xz * M_x)) + (J_x * M_z))), 
            der_m_1_omega - (((1.0 / m_1_tau) * (m_1_omega_ref - m_1_omega))), 
            m_1_thrust - (((m_1_Ct * m_1_omega) * m_1_omega)), 
            m_1_moment - ((m_1_Cm * m_1_thrust)), 
            der_m_2_omega - (((1.0 / m_2_tau) * (m_2_omega_ref - m_2_omega))), 
            m_2_thrust - (((m_2_Ct * m_2_omega) * m_2_omega)), 
            m_2_moment - ((m_2_Cm * m_2_thrust)), 
            der_m_3_omega - (((1.0 / m_3_tau) * (m_3_omega_ref - m_3_omega))), 
            m_3_thrust - (((m_3_Ct * m_3_omega) * m_3_omega)), 
            m_3_moment - ((m_3_Cm * m_3_thrust)), 
            der_m_4_omega - (((1.0 / m_4_tau) * (m_4_omega_ref - m_4_omega))), 
            m_4_thrust - (((m_4_Ct * m_4_omega) * m_4_omega)), 
            m_4_moment - ((m_4_Cm * m_4_thrust))])
        self.fx = flatten_piecewise_with_nested_matrices(self.fx)

        # ============================================
        # Define Reset Functions: fr

        # ============================================
        # Define Condition Update Function: fc
        self.fc = sympy.Tuple(*[
            (h < 0.0)])
        self.f_c = sympy.lambdify(
            args=[self.time, self.x],
            expr=self.fc,
            modules=['numpy'])

        # ============================================
        # Events and Event callbacks
        self.zc_c0 = sympy.lambdify([self.time, self.x], h - 0.0)
        self.zc_c0.terminal = True

    def solve(self):
        # ============================================
        # Solve for explicit ODE
        v = sympy.Matrix(list(self.x_dot) + list(self.y))

        if isinstance(self.fx, sympy.Piecewise):
            sol_x_dot = []
            sol_y = []
            for arg in self.fx.args:
                condition = arg[1]
                sol_i = sympy.solve(arg[0], v)
                x_dot_i = sympy.Tuple(* [xi for xi in self.x_dot.subs(sol_i)])
                sol_x_dot.append((x_dot_i, condition))
                y_i = sympy.Tuple(* [yi for yi in self.y.subs(sol_i)])
                sol_y.append((y_i, condition))
            self.sol_x_dot = sympy.Piecewise(*sol_x_dot)
            self.sol_y = sympy.Piecewise(*sol_y)
        else:
            sol = sympy.solve(self.fx, v)
            self.sol_x_dot = sympy.Tuple(* [xi for xi in self.x_dot.subs(sol)])
            self.sol_y = sympy.Tuple(* [yi for yi in self.y.subs(sol)])
        
        self.f_x_dot = sympy.lambdify(
            args=[self.time, self.x, self.m, self.u, self.p, self.c],
            expr=self.sol_x_dot,
            modules=['numpy'])

        self.f_y = sympy.lambdify(
            args=[self.time, self.x, self.m, self.u, self.p, self.c],
            expr=self.sol_y,
            modules=['numpy'])

        self.solved = True

    def __repr__(self):
        return repr(self.__dict__)

    def simulate(self, t0, tf, dt, x0=None, f_u=None, max_events=100):
        """
        Simulate the modelica model
        """
        if not self.solved:
            self.solve()
        
        if f_u is None:
            def f_u(t):
                return np.zeros(self.u.shape[0])

        # ============================================
        # Declare initial vectors
        u0 = np.array([self.u0[k] for k in self.u0.keys()])
        p0 = np.array([self.p0[k] for k in self.p0.keys()])
        cp0 = np.array([self.cp0[k] for k in self.cp0.keys()])
        c0 = np.array([self.c0[k] for k in self.c0.keys()])
        m0 = np.array([self.m0[k] for k in self.m0.keys()])
        y0 = np.array([self.y0[k] for k in self.y0.keys()])
        z0 = np.array([self.z0[k] for k in self.z0.keys()])
        
        if x0 is None:
            x0 = np.array([self.x0[k] for k in self.x0.keys()])

        # ============================================
        # Declare Events
        events = [
            self.zc_c0
        ]

        event_callback = {}

        # ============================================
        # Solve IVP
        event_count = 0
        t1 = tf
        data = {
            't': [],
            'x': [],
            'u': [],
            'y': [],
            'c': [],
        }

        while t0 < tf - dt:
            # check for max events
            if event_count > max_events:
                raise RuntimeError("Max events reached")
            
            # update conditions
            c0 = self.f_c(t0, x0)

            # solve ivp
            t_eval = np.arange(t0, tf, dt)
            res = scipy.integrate.solve_ivp(
                y0=x0,
                fun=lambda ti, x: self.f_x_dot(ti, x, m0, f_u(ti), p0, c0),
                t_span=[t_eval[0], t_eval[-1]],
                t_eval=t_eval,
                events=events,
            )

            # check for event
            x1 = res['y'][:, -1]
            t1 = res['t'][-1]
            if res.t_events is not None:
                event_count += 1
                for i, t_event in enumerate(res.t_events):
                    if len(t_event) > 0:
                        if i in event_callback:
                            x1 = event_callback[i](t_event[i], x1)

            # store data
            x = res['y']
            t = res['t']
            u = np.array([ f_u(ti) for ti in t ]).T
            y = np.array([ self.f_y(ti, xi, m0, ui, p0, c0) for (ti, xi, ui) in zip(t, x.T, u.T) ]).T
            data['x'].append(x)
            data['t'].append(t)
            data['u'].append(u)
            data['y'].append(y)
            data['c'].append(c0)

            # update for next step
            t0 = t1 + dt
            x0 = x1
        
        # convert lists to numpy array
        for k in data.keys():
            if len(data[k]) > 0:
                data[k] = np.hstack(data[k])
                
        return data
