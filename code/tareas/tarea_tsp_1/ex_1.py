# -*- coding: utf-8 -*-
"""
Ejercicio 1 

Múltiplicación de Matrices y vectores en coordenadas homogéneas.

"""

import numpy as np

def mat_x_mat(M,N):
    """ 
    Method to compute matrix multiplication over two 4x4 matrices.

    Parameters:  

     - M : np.array((4,4)) 
     - N : np.array((4,4)) 

    Returns:

     - L : np.array((4,4))
    
    """
    if M.shape != (4,4) or N.shape != (4,4):
        raise Exception('Not valid: Matrices must be 4x4')
    return M.dot(N)

def mat_x_vec(M,x):
    """ 
    Method to compute matrix (4x4 ) by (4x1) vector multiplication.

    Parameters:  

     - M : np.array((4,4)) 
     - x : np.array((4,1)) 

    Returns:

     - y : np.array((4,1))
    
    """
    if M.shape != (4,4) or x.shape != (4,1):
        raise Exception('Not valid: Matrix must be 4x4 and vector 4x1')
    return M.dot(x)


if __name__ == '__main__':
    # Initialize Ex 1. Values
    A_01 = np.array([[0.45,1.3,0.94,1.23],
                    [0,0.83,0.2,2.37],
                    [0.2,0.65,0.4,0.3],
                    [0,0,0,1]])
    A_12 = np.array([[1,0.2,0.85,2.467],
                    [0.54,1.3,0,0.77],
                    [0.12,0.68,1,0.8],
                    [0,0,0,1]])
    x_2 = np.array([2.3,0,24.4,1]).reshape(4,1)
    # Matrices multiplication
    A_02 = mat_x_mat(A_01,A_12)
    # Matrix times vector 
    x_0 = mat_x_vec(A_02,x_2)
    print('X0 = \n', x_0)