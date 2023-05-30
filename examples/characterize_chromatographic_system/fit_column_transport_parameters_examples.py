from column_transport_parameters import optimization_problem
from column_transport_parameters import simulator
from column_transport_parameters import process
from column_transport_parameters import comparator
from scipy.optimize import minimize
x_0=[0.3,0.04]
#res=minimize(optimization_problem.evaluate_objectives,x_0 ,bounds=[(0.1,0.6),(1e-10, 0.1)],method='nelder-mead',options={'xatol': 1e-8, 'disp': True})
#print(res.x)
x=[4.12116728e-01, 2.15880268e-07]
process.flow_sheet.units_dict["column"].bed_porosity=x[0]
process.flow_sheet.units_dict["column"].axial_dispersion=x[1]
simulation_results = simulator.simulate(process)
simulation_results.solution.outlet.inlet.plot()
comparator.plot_comparison(simulation_results)
def loss(x):
    return optimization_problem.evaluate_objectives(x, untransform=True)
#Variablen können auf das Intervall (0,1) transformiert werden. Untransform transformiert zurück

res=minimize(loss, x_0 ,bounds=[(0,1),(0,1)],method='nelder-mead',options={'xatol': 1e-8, 'disp': True})
print(res.x)
print(optimization_problem.untransform(res.x))

print('A')
