# csv_processing.py

import csv
import numpy as np
from scipy.spatial import distance

def processCSV(filename):
    data = []

    # Load data from the CSV file
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            x, y = map(float, row)
            data.append((x, y))

    # Create a list of points as tuples
    points = data

    # Compute the pairwise distances between points
    n = len(points)
    adjacency_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            dist = distance.euclidean(points[i], points[j])
            adjacency_matrix[i, j] = dist
            adjacency_matrix[j, i] = dist  # The matrix is symmetric

    return points, adjacency_matrix
