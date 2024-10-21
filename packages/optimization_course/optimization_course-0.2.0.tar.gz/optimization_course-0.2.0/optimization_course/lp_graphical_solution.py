"""Solving and visualizing linear programming problems graphically."""

# %%
# import libraries

import matplotlib.pyplot as plt
import numpy as np
import pulp as pl
from scipy.spatial import ConvexHull

# %%
# functions for lp graphical solution


def is_feasible(A: np.ndarray, b: np.ndarray, point: tuple[float, float]) -> bool:
    """Check if a point is feasible for a given set of constraints (A and b)."""
    for i in range(len(b)):
        if A[i][0] * point[0] + A[i][1] * point[1] > b[i]:
            return False
    return True


def plot_feasible_region(
    c: np.ndarray,
    A: np.ndarray,
    b: np.ndarray,
    plot_feasible: bool = True,
    plot_gradient: bool = True,
    plot_iso_profit: bool = True,
    plot_optimal: bool = True,
) -> None:
    """Plot the feasible region, constraints, and optimal solution.

    for a linear programming problem.

    Parameters
    ----------
    c : np.ndarray
        Coefficients of the objective function.
    A : np.ndarray
        Coefficients of the constraints.
    b : np.ndarray
        Right-hand side values of the constraints.
    plot_feasible : bool
        Flag to plot the feasible region. Default is True.
    plot_gradient : bool
        Flag to plot the gradient of the objective function. Default is True.
    plot_iso_profit : bool
        Flag to plot iso-profit lines. Default is True.
    plot_optimal : bool
        Flag to highlight the optimal solution. Default is True.

    Returns
    -------
    None

    """
    # Number of decision variables and constraints
    num_constraints = len(b)

    # Define the LP problem
    lp_problem = pl.LpProblem("LP_Problem", pl.LpMaximize)

    # Define decision variables
    x1 = pl.LpVariable("x1", lowBound=0)
    x2 = pl.LpVariable("x2", lowBound=0)

    # Objective function: c[0] * x1 + c[1] * x2
    lp_problem += c[0] * x1 + c[1] * x2

    # Add constraints: A[i][0] * x1 + A[i][1] * x2 <= b[i]
    for i in range(num_constraints):
        lp_problem += A[i][0] * x1 + A[i][1] * x2 <= b[i]

    # Solve the LP
    lp_problem.solve()

    # Initialize list for corner points
    corner_points = [(0, 0)]  # Include (0, 0) explicitly as a potential corner point

    # Check for intersections between constraint pairs to find corner points
    for i in range(num_constraints):
        for j in range(i + 1, num_constraints):
            A_matrix = np.array([A[i], A[j]])
            b_vector = np.array([b[i], b[j]])
            if np.linalg.det(A_matrix) != 0:  # Check if the system is solvable
                corner_point = np.linalg.solve(A_matrix, b_vector)
                if (
                    corner_point[0] >= 0 and corner_point[1] >= 0
                ):  # Only consider non-negative quadrant
                    corner_points.append(corner_point)

    # Add the axes (x1 = 0 and x2 = 0) intersections
    for i in range(num_constraints):
        if A[i][0] != 0:  # x2 = 0
            x_intercept = b[i] / A[i][0]
            if x_intercept >= 0:
                corner_points.append((x_intercept, 0))
        if A[i][1] != 0:  # x1 = 0
            y_intercept = b[i] / A[i][1]
            if y_intercept >= 0:
                corner_points.append((0, y_intercept))

    # Filter corner points to keep only feasible points
    feasible_points = [point for point in corner_points if is_feasible(A, b, point)]

    # If there are at least 3 feasible points, we form a polygon
    if len(feasible_points) >= 3:
        feasible_points = np.array(feasible_points)
        hull = ConvexHull(feasible_points)
        polygon_points = feasible_points[hull.vertices]
    else:
        polygon_points = np.array(feasible_points)

    # Plot setup
    plt.figure(figsize=(8, 8))
    x1_range = np.linspace(0, max([p[0] for p in feasible_points]) * 1.1, 400)

    # Create an array to store constraints plots
    constraint_lines = []

    # Plot the constraints and label them with their equations
    for i in range(num_constraints):
        constraint_label = f"{A[i][0]}x1 + {A[i][1]}x2 <= {b[i]}"
        (constraint_line,) = plt.plot(
            x1_range, (b[i] - A[i][0] * x1_range) / A[i][1], label=constraint_label
        )
        constraint_lines.append(constraint_line)

    # Plot the feasible region if the flag is set
    if plot_feasible:
        plt.fill(
            polygon_points[:, 0],
            polygon_points[:, 1],
            color="gray",
            alpha=0.3,
            label="Feasible Region",
        )

    # Plot corner points
    plt.scatter(feasible_points[:, 0], feasible_points[:, 1], color="red", zorder=5)
    for x, y in feasible_points:
        plt.text(
            x, y, f"({x:.2f}, {y:.2f})", fontsize=12, verticalalignment="bottom"
        )

    # Plot gradient of objective function (vector c) from the origin
    # if the flag is set
    if plot_gradient:
        scale_factor = (
            max([p[0] for p in feasible_points] + [p[1] for p in feasible_points])
            * 0.2
        )
        gradient_x = c[0] * scale_factor
        gradient_y = c[1] * scale_factor
        plt.quiver(
            0,
            0,
            gradient_x,
            gradient_y,
            angles="xy",
            scale_units="xy",
            scale=1,
            color="blue",
            label=f"Gradient: ({c[0]:.2f}, {c[1]:.2f})",
        )

    # Highlight the optimal solution if the flag is set
    if plot_optimal:
        opt_x1 = pl.value(x1)
        opt_x2 = pl.value(x2)
        plt.scatter(
            [opt_x1],
            [opt_x2],
            color="green",
            s=100,
            zorder=5,
            label="Optimal Solution",
        )
        plt.text(opt_x1, opt_x2, "Optimal", fontsize=12, verticalalignment="top")

    # Plot iso-profit lines (objective function contours) if the flag is set
    if plot_iso_profit:
        for z in range(1, 5):
            plt.plot(x1_range, (z - c[0] * x1_range) / c[1], "k--", alpha=0.5)

        # Add iso-profit line passing through the optimal solution
        optimal_profit = c[0] * opt_x1 + c[1] * opt_x2
        plt.plot(
            x1_range,
            (optimal_profit - c[0] * x1_range) / c[1],
            "g--",
            linewidth=2,
            label="Iso-Profit (Optimal)",
        )

    # Labels and formatting
    plt.xlim(0, max([p[0] for p in feasible_points]) * 1.1)
    plt.ylim(0, max([p[1] for p in feasible_points]) * 1.1)
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title("Feasible Region")

    # Set equal scaling for x and y axes
    plt.axis("equal")

    # Show legend
    plt.legend()
    plt.grid(True)
    plt.show()
