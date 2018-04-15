# -*- coding: utf-8 -*-
"""
Clase Cinematica

"""

import numpy as np
import math as m

class Cinematica(object):
    """
    Forward Kinematics implementation over Denavit-Hartemberg parameters:

    - theta: Angle rotating over Z(i) axis  (° - Degrees)
    - d: Displacement along Z(i) axis
    - alpha: Angle rotation over X(i+1) axis. (° - Degrees)
    - a: Displacement along X(i+1) axis.

    Example:

        from cinemat import Cinematica
        theta_1 = 0 # degrees
        d_1 = 1
        alpha_1 = 0 #degrees
        a_1 = 1

        A_01 = Cinematica(theta_1,d_1,alpha_1,a_1).compute_dh()
    """

    def __init__(self,theta_i,d_i,a_i,alpha_i):
        self.theta = m.radians(theta_i)
        self.d = d_i
        self.alpha = m.radians(alpha_i)
        self.a = a_i

    def compute_dh(self):
        """
            Method computing Denavit-Hartemberg matrix over instance params.
            
        """
        c_th,s_th = m.cos(self.theta), m.sin(self.theta)
        c_alp,s_alp = m.cos(self.alpha), m.sin(self.alpha)
        return np.array([[c_th,(-1*s_th*c_alp),(s_th*s_alp),(self.a*c_th)],
                        [s_th,(c_th*c_alp),(-1*c_th*s_th),(self.a*s_th)],
                        [0,s_alp,c_alp,self.d],
                        [0,0,0,1]])