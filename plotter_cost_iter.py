import matplotlib.pyplot as plt
import matplotlib.cm as cm

def plotCostvsIterationLoggedDataList(logged_data_list, NUM_RUNS):
    cmap = cm.get_cmap('viridis', NUM_RUNS)
    i = 0
    for logged_data in logged_data_list:
        # Assuming 'data' is your list of tuples
        iteration_numbers = [t[1] for t in logged_data]
        costs = [t[2] for t in logged_data]
        # plt.figure(figsize=(8, 8))
        plt.plot(iteration_numbers, costs, label='run #'+str(i), color=cmap(i))
        i += 1

    plt.title('Cost vs Iteration Number')
    plt.xlabel('Iteration Number')
    plt.ylabel('Cost')
    plt.grid(True)
    plt.legend()
    plt.show()