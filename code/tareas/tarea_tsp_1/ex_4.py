# -*- coding: utf-8 -*-
"""
Ejercicio 4

Vector de posición del Manipulador SCARA RRRP

"""
from cinemat import Cinematica
from ex_1 import *

# Constants
l1,l2,l3,l4 = 1,1,2,1

thetas = [0,90,-90,0]
alphas = [0,0,0,0]
ds = [l3,l4,0,2]
a_s = [l1,l2,0,0]

def main():
    # Initialize Dh matrix transformation as I
    A_0n = np.eye(4)
    for i,v in enumerate(thetas):
        # Multiply the computed values for each DH matrix
        print("Params A"+str(i)+str(i+1))
        print(thetas[i],ds[i],a_s[i],alphas[i])
        Ti = Cinematica(thetas[i],ds[i],a_s[i],alphas[i]).compute_dh()
        print(Ti)
        A_0n = mat_x_mat(A_0n,Ti)
    print('Transformation Matrix A04:')
    print(A_0n)
    print('End Effector Position Vector:')
    # multiply Transformation matrix times n = (0,0,0,1)
    x_0n = mat_x_vec(A_0n,np.array([0,0,0,1]).reshape(4,1))
    print(x_0n)

    
if __name__ == '__main__':
    main()