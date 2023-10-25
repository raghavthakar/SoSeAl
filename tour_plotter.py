import matplotlib.pyplot as plt
import csv
import math

def computeTourCost(city_coords, tour):
    total_cost = 0

    for i in range(len(tour)):
        start_city = tour[i]
        end_city = tour[(i + 1) % len(tour)]  # Ensure the tour is circular

        x1, y1 = city_coords[start_city]
        x2, y2 = city_coords[end_city]

        # Calculate the Euclidean distance between two cities
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        total_cost += distance

    return total_cost

def plotSolutionOnCities(filename, solution):
    # convert from city encoding to position encdoing
    tour = [0 for i in range(len(solution))]
    for city in range(len(solution)):
        position = solution[city]
        tour[position] = city

    # Initialize empty lists to store the x and y coordinates of the cities
    x_coords = []
    y_coords = []

    city_coords = []

    # Read the city coordinates from the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            x_coords.append(float(row[0]))
            y_coords.append(float(row[1]))
            city_coords.append((x_coords[-1], y_coords[-1]))
    
    # Calculate the tour cost
    tour_cost = computeTourCost(city_coords, tour)
    print("Cost: ", tour_cost)

    # Initialize the plot
    plt.figure(figsize=(8, 6))
    plt.title('City Tour')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')

    # Plot the cities
    plt.scatter(x_coords, y_coords, marker='o', color='b', label='Cities')

    # Connect the cities in the tour order
    for i in range(len(tour) - 1):
        start_city = tour[i]
        end_city = tour[i + 1]
        plt.plot([x_coords[start_city], x_coords[end_city]], [y_coords[start_city], y_coords[end_city]], color='r')

    # Connect the last city to the first city to complete the tour
    start_city = tour[-1]
    end_city = tour[0]
    plt.plot([x_coords[start_city], x_coords[end_city]], [y_coords[start_city], y_coords[end_city]], color='r')

    # Show the plot
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage:
# tour = [12, 13, 14, 16, 8, 20, 4, 3, 6, 18, 11, 5, 24, 15, 23, 10, 0, 17, 1, 2, 19, 22, 7, 21, 9]
# plotSolutionOnCities('/home/raghav/grad_school/quarter_1/ROB_537_Learning_Based_Constrol/SoSeAl/hw2.csv', tour)
