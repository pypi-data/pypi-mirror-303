import numpy as np

def plurigaussian_simulation(dim, tree, fields, ldim=100):
    if len(dim) == 2:
        Z1 = fields[0]
        Z2 = fields[1]
        L = np.zeros((ldim,ldim))
        P = np.zeros_like(Z1)
        for ix in range(ldim):
            for iy in range(ldim):
                data = {
                    'Z1' : -3+(ix/ldim)*6,
                    'Z2' : -3+(iy/ldim)*6,
                }
                L[iy, ix] = tree.decide(data)
        for ix in range(dim[0]):
            for iy in range(dim[1]):
                data = {
                    'Z1' : Z1[ix,iy],
                    'Z2' : Z2[ix,iy],
                }
                P[ix,iy] = tree.decide(data)
    elif len(dim) == 3:
        Z1 = fields[0]
        Z2 = fields[1]
        Z3 = fields[2]
        L = np.zeros((ldim,ldim,ldim))
        P = np.zeros_like(Z1)
        for ix in range(ldim):
            for iy in range(ldim):
                for iz in range(ldim):
                    data = {
                        'Z1' : -3+(ix/ldim)*6,
                        'Z2' : -3+(iy/ldim)*6,
                        'Z3' : -3+(iz/ldim)*6,
                    }
                    L[iz, iy, ix] = tree.decide(data)
        for ix in range(dim[0]):
            for iy in range(dim[1]):
                for iz in range(dim[2]):
                    data = {
                        'Z1' : Z1[ix,iy,iz],
                        'Z2' : Z2[ix,iy,iz],
                        'Z3' : Z3[ix,iy,iz],
                    }
                    P[ix,iy,iz] = tree.decide(data)


    return L, P