import numpy as np

def derivative(x, y):
    dy_dx = np.zeros(y.shape,np.float)

    dy_dx[0:-1] = np.diff(y)/np.diff(x)
    dy_dx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    
    return dy_dx
