import sympy
import numpy as np
import scipy.integrate

cos = sympy.cos
sin = sympy.sin
tan = sympy.tan

class Model:
    """
    Flattened Modelica Model
    """

    def __init__(self):
        # ============================================
        # Declare time
        time = sympy.symbols('time')

        # ============================================
        # Declare u
        u = sympy.symbols('u')
        self.u = sympy.Matrix([[
            u]]).T
        self.u0 = { 
            'u': 0.0}
        
        # ============================================
        # Declare p
        m1_tau = sympy.symbols('m1_tau')
        m2_tau = sympy.symbols('m2_tau')
        m3_tau = sympy.symbols('m3_tau')
        m4_tau = sympy.symbols('m4_tau')
        self.p = sympy.Matrix([[
            m1_tau, 
            m2_tau, 
            m3_tau, 
            m4_tau]]).T
        self.p0 = { 
            'm1_tau': 1.0, 
            'm2_tau': 1.0, 
            'm3_tau': 1.0, 
            'm4_tau': 1.0}
        
        # ============================================
        # Declare cp
        self.cp = sympy.Matrix([[]]).T
        self.cp0 = { }
        
        # ============================================
        # Declare x
        m1_omega = sympy.symbols('m1_omega')
        m2_omega = sympy.symbols('m2_omega')
        m3_omega = sympy.symbols('m3_omega')
        m4_omega = sympy.symbols('m4_omega')
        self.x = sympy.Matrix([[
            m1_omega, 
            m2_omega, 
            m3_omega, 
            m4_omega]]).T
        self.x0 = { 
            'm1_omega': 0.0, 
            'm2_omega': 0.0, 
            'm3_omega': 0.0, 
            'm4_omega': 0.0}
        
        # ============================================
        # Declare m
        a = sympy.symbols('a')
        self.m = sympy.Matrix([[
            a]]).T
        self.m0 = { 
            'a': 0.0}
        
        # ============================================
        # Declare y
        m1_omega_ref = sympy.symbols('m1_omega_ref')
        m2_omega_ref = sympy.symbols('m2_omega_ref')
        m3_omega_ref = sympy.symbols('m3_omega_ref')
        m4_omega_ref = sympy.symbols('m4_omega_ref')
        self.y = sympy.Matrix([[
            m1_omega_ref, 
            m2_omega_ref, 
            m3_omega_ref, 
            m4_omega_ref]]).T
        self.y0 = { 
            'm1_omega_ref': 0.0, 
            'm2_omega_ref': 0.0, 
            'm3_omega_ref': 0.0, 
            'm4_omega_ref': 0.0}
        
        # ============================================
        # Declare z
        self.z = sympy.Matrix([[]]).T
        self.z0 = { }
        
        

        # ============================================
        # Declare x_dot
        der_m1_omega = sympy.symbols('der_m1_omega')
        der_m2_omega = sympy.symbols('der_m2_omega')
        der_m3_omega = sympy.symbols('der_m3_omega')
        der_m4_omega = sympy.symbols('der_m4_omega')
        self.x_dot = sympy.Matrix([[
            der_m1_omega, 
            der_m2_omega, 
            der_m3_omega, 
            der_m4_omega]]).T

        # ============================================
        # Define Continous Update Function: fx
        self.fx = sympy.Matrix([[
            m1_omega_ref - (u), 
            m2_omega_ref - (u), 
            m3_omega_ref - (u), 
            m4_omega_ref - (u), 
            der_m1_omega - (1 / m1_tau * m1_omega_ref - m1_omega), 
            der_m2_omega - (1 / m2_tau * m2_omega_ref - m2_omega), 
            der_m3_omega - (1 / m3_tau * m3_omega_ref - m3_omega), 
            der_m4_omega - (1 / m4_tau * m4_omega_ref - m4_omega)]]).T

        # ============================================
        # Events and Event callbacks
        self.events = []
        self.event_callback = {}

        # ============================================
        # Solve for explicit ODE
        try:
            v = sympy.Matrix.vstack(self.x_dot, self.y)
            sol = sympy.solve(self.fx, v)
        except Exception as e:
            print('solving failed')
            for k in self.__dict__.keys():
                print(k, self.__dict__[k])
            raise(e)
        self.sol_x_dot = self.x_dot.subs(sol)
        self.sol_y = self.y.subs(sol)
        self.f_x_dot = sympy.lambdify([time, self.x, self.m, self.u, self.p], list(self.sol_x_dot))
        self.f_y = sympy.lambdify([time, self.x, self.m, self.u, self.p], list(self.sol_y))

    def __repr__(self):
        return repr(self.__dict__)

    def simulate(self, t=None, u=None):
        """
        Simulate the modelica model
        """
        if t is None:
            t = np.arange(0, 1, 0.01)
        if u is None:
            def u(t):
                return np.zeros(self.u.shape[0])

        # ============================================
        # Declare initial vectors
        u0 = np.array([self.u0[k] for k in self.u0.keys()])
        p0 = np.array([self.p0[k] for k in self.p0.keys()])
        cp0 = np.array([self.cp0[k] for k in self.cp0.keys()])
        x0 = np.array([self.x0[k] for k in self.x0.keys()])
        m0 = np.array([self.m0[k] for k in self.m0.keys()])
        y0 = np.array([self.y0[k] for k in self.y0.keys()])
        z0 = np.array([self.z0[k] for k in self.z0.keys()])
        

        # ============================================
        # Solve IVP
        res = scipy.integrate.solve_ivp(
            y0=x0,
            fun=lambda ti, x: self.f_x_dot(ti, x, m0, u(ti), p0),
            t_span=[t[0], t[-1]],
            t_eval=t,
        )

        # check for event
        y0 = res['y'][:, -1]
        if res.t_events is not None:
            for i, t_event in enumerate(res.t_events):
                if len(t_event) > 0:
                    print('event', i)
                    if i in self.event_callback:
                        print('detected event', i, t_event[i])
                        y0 = self.event_callback[i](t_event[i], y0)

        x = res['y']
        #y = [ self.f_y(ti, xi, u(ti), p0) for (ti, xi) in zip(t, x) ]
        #y = self.f_y(0, [1, 2, 3, 4], [1], [1, 2, 3, 4])

        return {
            't': t,
            'x': x,
            'u': u(t),
            #'y': y,
        }
