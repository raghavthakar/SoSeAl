import random
import numpy as np
import math
from csv_processing import processCSV

# mutates a given solution by swapping the supplued number of cities
def mutateBySwapping(solution, swap_deg):
    # Make a copy of the original solution to avoid modifying it directly
    mutated_solution = solution.copy()
    
    # Check that swap_deg is not greater than the length of the solution
    if swap_deg > len(solution):
        raise ValueError("swap_deg cannot be greater than the length of the solution.")
    
    # Generate unique random indices to swap
    
    for i in range(swap_deg):
        index1, index2 = random.sample(range(len(solution)), 2)
        mutated_solution[index1], mutated_solution[index2] = mutated_solution[index2], mutated_solution[index1] 

    return mutated_solution

# takes a solution and calculates its cost
def calculateCost(solution, adjacency_matrix):
    # right now the solution is a list of position of each city
    # transform the solution to a list of cities based on the order
    # solution[i] = position of city i
    # pos_based_solution[i] = city at position i
    pos_based_solution = [0 for i in range(len(solution))]
    for city in range(len(solution)):
        position = solution[city]
        pos_based_solution[position] = city
    
    cost_score = 0
    # loop through positions, and the find the edge weight between cities at consecutive positions
    for pos_num in range(len(pos_based_solution)):
        if pos_num < len(pos_based_solution) - 1:
            cost_score += adjacency_matrix[pos_based_solution[pos_num]][pos_based_solution[pos_num+1]]
        else:
            cost_score += adjacency_matrix[pos_based_solution[pos_num]][pos_based_solution[0]]

    return cost_score

# selects k solutions from the popoulation based on the cost (proportional selection)
# returns the index
def proportionalSelection(population, cost_dist, POPULATION_SIZE):
    exp_cost_dist = [math.pow(2.71, -cost*1000) for cost in cost_dist]
    exp_cost_dist_sum = sum(exp_cost_dist)
    exp_cost_prob_dist = [x / exp_cost_dist_sum for x in exp_cost_dist]
    selected_solution_indices  = np.random.choice(range(len(population)), size=(1, POPULATION_SIZE), p=exp_cost_prob_dist)[0]
    return selected_solution_indices


def stochasticBeamSearch(filename, POPULATION_SIZE, NUM_GENERATIONS, MUTATION_DEGREE):
    points, adjacency_matrix = processCSV(filename)

    # Control parameters
    NUM_CITIES = len(points)

    # Population initialisation
    population = []
    starting_min_fit = 0
    for i in range(POPULATION_SIZE):
        # random_solution[i] = position of city i
        random_solution = random.sample(range(NUM_CITIES), NUM_CITIES)
        population.append(random_solution)


    tracked_iteration_solution_cost_tuple_list = []
    for generation_num in range(NUM_GENERATIONS):
        # generate as many mutated solutions (sucessor states)
        for i in range(len(population)):
            population.append(mutateBySwapping(population[i], MUTATION_DEGREE))

        cost_distribution = [calculateCost(sol, adjacency_matrix) for sol in population]
        # print("Cost distribution: ", cost_distribution)
        min_cost = min(cost_distribution)
        minimum_cost_solution = population[cost_distribution.index(min_cost)]
        tracked_iteration_solution_cost_tuple_list.append((minimum_cost_solution, generation_num, min_cost))

        # starting_min_fit = min(cost_distribution) if generation_num == 0 else starting_min_fit
        total_cost = sum(cost_distribution)
        normalised_cost_distribution = [x / total_cost for x in cost_distribution]
        # print("Normalised cost distribution: ", normalised_cost_distribution)
        selected_solutions_indices = proportionalSelection(population, normalised_cost_distribution, POPULATION_SIZE)
        selected_solutions=[]
        for x in selected_solutions_indices:
            selected_solutions.append(population[x])
        population = selected_solutions
    
    return tracked_iteration_solution_cost_tuple_list