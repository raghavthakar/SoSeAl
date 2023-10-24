import matplotlib.pyplot as plt
import matplotlib.cm as cm


def plotAvgCostvsIterationLoggedDataList(logged_data_list, NUM_RUNS):
    cmap = cm.get_cmap('viridis', NUM_RUNS)
    i = 0
    iteration_numbers = [t[1] for t in logged_data_list[0]]  # Assuming the iteration numbers are the same for all runs
    average_costs = [0] * len(iteration_numbers)

    for i in range(NUM_RUNS):
        logged_data = logged_data_list[i]
        costs = [t[2] for t in logged_data]
        average_costs = [avg + cost for avg, cost in zip(average_costs, costs)]

    average_costs = [avg / NUM_RUNS for avg in average_costs]

    plt.figure(figsize=(8, 6))
    plt.plot(iteration_numbers, average_costs, label='Average Cost', color='blue')
    plt.title('Average Cost vs Iteration Number')
    plt.xlabel('Iteration Number')
    plt.ylabel('Average Cost')
    plt.grid(True)
    plt.legend()
    plt.show()