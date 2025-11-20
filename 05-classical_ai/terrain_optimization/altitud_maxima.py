import numpy
import pygad
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pygad")
import elevaciones as elev
import numpy as np
mapa = elev.obtener_mapa()
# Vamos a maximizar la altitud para las coordenadas x, y

def fitness_func(ga_instance, solution, solution_idx):
	maxX , maxY = mapa.shape
	x = int(solution[0])
	y = int(solution[1])
	if x >= maxX or y >= maxY:
		return -1000	
	return mapa[x][y]

# Next is to prepare the parameters of PyGAD. Here is an example for a set of parameters


fitness_function = fitness_func

num_generations = 18
num_parents_mating = 60

sol_per_pop = 800
num_genes = 2
mutation_num_genes=2

init_range_low = 0
init_range_high = max(mapa.shape)-1

parent_selection_type = "sss"
keep_parents = 2

crossover_type = "two_points"

mutation_type = "random"
mutation_percent_genes = 60
gene_type = int

# After the parameters are prepared, an instance of the pygad.GA class is created.

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       mutation_num_genes=mutation_num_genes,
                       gene_type=gene_type)

# After creating the instance, the run() method is called to start the optimization.

ga_instance.run()

# After the run() method completes, information about the best solution found by PyGAD can be accessed.

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
ga_instance.plot_fitness()

prediction = mapa[int(solution[0]),int(solution[1])]
print("Solución recibida por el algoritmo genético : {prediction}".format(prediction=prediction))



elev.mostrar_mapa(mapa)

print(f"Altitud máxima del mapa: {np.max(mapa)}")