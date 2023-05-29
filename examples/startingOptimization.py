import numpy as np

from scipy.optimize import minimize


#def rosen(x):
#    """The Rosenbrock function"""
#    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)
#generate data
input=np.linspace(-5,5)
def simulation(a):
    return a * input**2

TRUE_VAL_A=4
np.linspace
output=simulation(TRUE_VAL_A)




from matplotlib import pyplot as plt

plt.plot(input, output)
plt.show()

def f(x):
    return sum((output -simulation(x))**2)
res=minimize(f,2,options={ 'disp': True})
res.x
print(res.x)


x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])

res = minimize(rosen, 0, method='nelder-mead',
               options={'xatol': 1e-8, 'disp': True})

print('a')