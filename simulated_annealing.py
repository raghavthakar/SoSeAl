import random
import numpy as np
import math
from csv_processing import processCSV

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

def simulatedAnnealing(filename, NUM_GENERATIONS, MUTATION_DEGREE, TEMPERATURE, TEMPERATURE_SCALING):
    # Call the processCSV function
    # filename = '/home/raghav/grad_school/quarter_1/ROB_537_Learning_Based_Constrol/hw2/hw2.csv' 
    points, adjacency_matrix = processCSV(filename)

    # Control parameters
    NUM_CITIES = len(points)
    # NUM_GENERATIONS = 5000
    # MUTATION_DEGREE = 2
    # TEMPERATURE = 0.3
    # TEMPERATURE_SCALING = 0.9995

    # Solution initialisation
    # solution[i] = position of city i
    solution = random.sample(range(NUM_CITIES), NUM_CITIES)
    # print(solution)
    tracked_iteration_solution_cost_tuple_list = []
    # mutateByRearrangingSections(solution, MUTATION_DEGREE)
    for i in range(NUM_GENERATIONS):
        solution_cost = calculateCost(solution, adjacency_matrix)
        tracked_iteration_solution_cost_tuple_list.append((solution, i, solution_cost))
        # print("Cost: ", solution_cost)
        random_solution = mutateBySwapping(solution, MUTATION_DEGREE)
        random_solution_cost = calculateCost(random_solution, adjacency_matrix)
        if random_solution_cost < solution_cost:
            solution = random_solution
            continue
        else:
            pick_random_prob = math.exp(-(random_solution_cost - solution_cost)/TEMPERATURE)
            # print("Pick random prob: ", pick_random_prob)
            # print("Delta: ", random_solution_cost - solution_cost)
            # print("Temperature, iteration: ", TEMPERATURE, i)
            if random.random() < pick_random_prob:
                # print("-------------------------")
                solution = random_solution
        
        # TEMPERATURE = 1-i/NUM_GENERATIONS
        TEMPERATURE = TEMPERATURE*TEMPERATURE_SCALING

    tracked_iteration_solution_cost_tuple_list.append((solution, NUM_GENERATIONS-1, calculateCost(solution, adjacency_matrix)))

    return tracked_iteration_solution_cost_tuple_list