import matplotlib.pyplot as plt

def computeStatMeasuresAndPlot(tours_and_costs):
    # Extract the solution costs from the list of tuples
    solution_costs = [cost for _, cost in tours_and_costs]

    # Calculate the mean and standard deviation of solution costs
    mean_cost = sum(solution_costs) / len(solution_costs)
    std_deviation = (sum((cost - mean_cost) ** 2 for cost in solution_costs) / len(solution_costs)) ** 0.5

    # Plot a box plot of solution costs
    plt.figure(figsize=(8, 6))
    plt.boxplot(solution_costs, vert=False)
    plt.title('Solution Costs')
    plt.xlabel('Cost')
    plt.yticks([])

    # Add a scatter plot of solution costs
    plt.scatter(solution_costs, [1] * len(solution_costs), marker='o', color='blue', label='Solution Costs', alpha=0.5)

    # Display mean and standard deviation
    plt.text(0.7, 0.8, f'Mean: {mean_cost:.2f}', transform=plt.gca().transAxes, fontsize=12, color='black')
    plt.text(0.7, 0.7, f'Standard Deviation: {std_deviation:.2f}', transform=plt.gca().transAxes, fontsize=12, color='black')

    plt.show()