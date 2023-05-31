from column_transport_parameters import optimization_problem
from column_transport_parameters import simulator
from column_transport_parameters import process
from column_transport_parameters import comparator
from bayes_opt import BayesianOptimization
import numpy as np
from bayes_opt import UtilityFunction
import matplotlib.pyplot as plt



x_0=[0.3,0.04]
def loss(x,y):
    return -optimization_problem.evaluate_objectives([x,y],untransform=True)[0]

#pbounds = {'x': (0,1), 'y': (0,1)}
#optimizer=BayesianOptimization(f=loss ,pbounds=pbounds,verbose=1,random_state=1)
#optimizer.maximize(init_points=10,n_iter=50)

#print(optimizer.max)
#x=np.array([0.6238399862987729, 0.3705124614673245])
#print(optimization_problem.untransform(x))
optimizer = BayesianOptimization(
    f=None,
    pbounds={'x': (0,1), 'y': (0,1)},
    verbose=2,
    random_state=1,
)

kappa1=5
iteration1=30

kappa2=0.1
iteration2=30
utility = UtilityFunction(kind="ucb", kappa=kappa1, xi=0.0)
iteration=50

for i in range(iteration):
    kappa=5 - (5*i)// iteration
    utility = UtilityFunction(kind="ucb", kappa=kappa, xi=0.0)
    next_point_0 = optimizer.suggest(utility)
    target = loss(**next_point_0)
    optimizer.register(params=next_point_0, target=target)
    print(target, next_point_0)
x_0=optimization_problem.untransform(np.array([next_point_0['x'],next_point_0['y']]))

process.flow_sheet.units_dict["column"].bed_porosity=x_0[0]
process.flow_sheet.units_dict["column"].axial_dispersion=x_0[1]
simulation_results = simulator.simulate(process)
simulation_results.solution.outlet.inlet.plot()
comparator.plot_comparison(simulation_results)


fig = plt.gcf()
for _ in range(iteration1):
    next_point = optimizer.suggest(utility)
    target = loss(**next_point)
    optimizer.register(params=next_point, target=target)
    print(target, next_point)

utility = UtilityFunction(kind="ucb", kappa=kappa2, xi=0.0)

for _ in range(iteration2):
    next_point = optimizer.suggest(utility)
    target = loss(**next_point)
    optimizer.register(params=next_point, target=target)
    print(target, next_point)

x_1=optimization_problem.untransform(np.array([next_point['x'],next_point['y']]))

#print("iterations: " , iteration1 , "kappa=" , kappa1 , ", iterations: " , iteration2 , "kappa=" , kappa2  , " res: " , x)

#iterations:  10 kappa= 5 , iterations:  25 kappa= 0.5  res:  [5.47613496e-01 1.71195992e-06]
#iterations:  10 kappa= 5 , iterations:  25 kappa= 0.1  res:  [5.47613496e-01 1.71195992e-06]
#iterations:  30 kappa= 5 , iterations:  25 kappa= 0.1  res:  [4.11949766e-01 2.18309059e-07]
#iterations:  25 kappa= 5 , iterations:  5 kappa= 0.1  res:  [4.18928273e-01 1.20363236e-06]


process.flow_sheet.units_dict["column"].bed_porosity=x_1[0]
process.flow_sheet.units_dict["column"].axial_dispersion=x_1[1]
simulation_results = simulator.simulate(process)
comparator.plot_comparison(simulation_results)



#print(optimizer.max)


print('a')