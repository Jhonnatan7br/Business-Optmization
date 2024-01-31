%matplotlib notebook
from scipy.optimize import linprog
import matplotlib.pyplot as plt
import numpy as np

# Coefficients for the objective function
c = [-20, -30]

# Coefficients for the inequality constraints (lhs)
A = [[1, 0], [0, 1], [20, 40]]

# Right-hand side values for the inequality constraints
b = [60, 50, 2400]

# Bounds for each variable
x0_bounds = (0, None)
x1_bounds = (0, None)

# Solve the problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Sensitivity Analysis
sensitivity_results = []
for a_capacity in range(40, 81, 5):
    for b_capacity in range(30, 71, 5):
        for labor_available in range(2000, 2801, 100):
            b_temp = [a_capacity, b_capacity, labor_available]
            result_temp = linprog(c, A_ub=A, b_ub=b_temp, bounds=[x0_bounds, x1_bounds], method='highs')
            if result_temp.success:
                sensitivity_results.append((-result_temp.fun, a_capacity, b_capacity, labor_available))

# Plotting the results
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Unpacking the results for plotting
profits, a_capacities, b_capacities, labor_availabilities = zip(*sensitivity_results)

# Scatter plot for the sensitivity analysis results
ax.scatter(a_capacities, b_capacities, profits, c='r', marker='o')

ax.set_xlabel('Capacity of A')
ax.set_ylabel('Capacity of B')
ax.set_zlabel('Profit')

plt.show()