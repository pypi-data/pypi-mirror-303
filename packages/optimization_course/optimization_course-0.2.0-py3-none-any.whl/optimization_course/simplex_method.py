"""Simplex Module."""
import numpy as np
import pandas as pd
from IPython.display import display  # Import display for Jupyter notebook output


class Simplex:
    """Revised Simplex Method for Linear Programming Problems."""

    def __init__(
        self,
        c: np.ndarray,
        A: np.ndarray,
        b: np.ndarray,
        max_problem: bool = True,
        save_excel: bool = False,
    ) -> None:
        """Initialize the Revised Simplex Method."""
        self.c = c  # Objective function coefficients
        self.A = A  # Constraint coefficients matrix
        self.b = b  # Right-hand side vector
        self.m, self.n = A.shape  # Number of constraints (m) and variables (n)
        self.max_problem = max_problem  # Flag for maximization or minimization
        self.save_excel = save_excel  # Flag to save tableaux as Excel file

        # List to store DataFrames for each tableau
        self.tableau_history = []

        # Initialize the basis and non-basis variables
        self.basis_indices = list(range(self.n - self.m, self.n))  # Slack variables
        self.non_basis_indices = list(range(self.n - self.m))  # Decision variables

        self.iteration = 0  # Iteration counter
        self.optimal = False  # Flag to check for optimality

        # Update B and N matrices
        self._update_B_N()

    def _update_B_N(self) -> None:
        """Update the basic and non-basic matrices B and N."""
        self.B = self.A[:, self.basis_indices]
        self.N = self.A[:, self.non_basis_indices]

    def set_basis(self, new_basis_indices: list[int]) -> None:
        """Set a new basis and update necessary matrices."""
        self.basis_indices = new_basis_indices
        self.non_basis_indices = [
            i for i in range(self.n) if i not in self.basis_indices
        ]
        self._update_B_N()

    def _get_tableau(self) -> None:
        """Compute and return the current tableau."""
        self.B_inv = np.linalg.inv(self.B)  # Inverse of the basis matrix
        self.x_B = np.dot(self.B_inv, self.b)  # Current basic solution

        # Reduced costs for the non-basic variables
        self.c_B = self.c[self.basis_indices]
        self.reduced_costs = -self.c[self.non_basis_indices] + np.dot(
            np.dot(self.c_B.T, self.B_inv), self.N
        )

        # Compute the current value of the objective function
        self.z = np.dot(self.c_B, self.x_B)

    def _pivot(self) -> None:
        """Perform a single pivot operation and update the basis."""
        reduced_cost = (
            self.reduced_costs if self.max_problem else -self.reduced_costs
        )

        # Check for optimality: if all reduced costs >= 0, we are done
        if np.all(reduced_cost >= -1e-8):  # Tolerance for floating-point errors
            self.optimal = True
            return

        # Choose the entering variable (most negative reduced cost)
        entering_idx = np.argmin(reduced_cost)
        entering_var = self.non_basis_indices[entering_idx]

        # Compute the direction vector
        direction = np.dot(self.B_inv, self.A[:, entering_var])

        # Perform the minimum ratio test to choose the leaving variable
        positive_direction_indices = np.where(direction > 1e-8)[0]
        if positive_direction_indices.size == 0:
            raise ValueError("The problem is unbounded.")

        ratios = (
            self.x_B[positive_direction_indices]
            / direction[positive_direction_indices]
        )
        leaving_idx_in_positive = np.argmin(ratios)
        leaving_idx = positive_direction_indices[leaving_idx_in_positive]
        leaving_var = self.basis_indices[leaving_idx]

        # Swap entering and leaving variables
        self.basis_indices[leaving_idx] = entering_var
        self.non_basis_indices[entering_idx] = leaving_var

        # Update the basic and non-basic matrices
        self._update_B_N()
        self.iteration += 1

    def next_tableau(self) -> None:
        """Generate the next tableau of the Revised Simplex Method."""
        if self.optimal:
            return None
        self._get_tableau()  # Update the tableau before pivoting
        self._pivot()  # Perform a pivot

    def print_tableau(self) -> None:
        """Display the current simplex tableau using pandas DataFrame."""
        self._get_tableau()

        # Compute B_inv * A (coefficients for all variables)
        tableau_coeffs = np.dot(self.B_inv, self.A)  # This is m x n

        # Compute reduced costs (c - c_B^T * B_inv * A)
        reduced_costs = -self.c + np.dot(self.c_B.T, np.dot(self.B_inv, self.A))

        # Prepare DataFrame for the tableau
        variables = [f"x_{i+1}" for i in range(self.n)]  # Variable names
        df = pd.DataFrame(tableau_coeffs, columns=variables)
        df["RHS"] = self.x_B

        # Set the index to basic variables
        basic_vars = [f"x_{idx+1}" for idx in self.basis_indices]
        df.index = basic_vars

        # Append the objective function row labeled 'Z'
        reduced_costs = reduced_costs.reshape(1, -1)  # Make it 2D
        z_row = pd.DataFrame(reduced_costs, columns=variables)
        z_row["RHS"] = self.z
        z_row.index = ["Z"]

        # Concatenate Z row at the top
        df = pd.concat([z_row, df])

        if self.max_problem:
            is_optimal = df.iloc[0, :-1].min() >= 0
        else:
            is_optimal = df.iloc[0, :-1].max() <= 0

        if not is_optimal:
            # Choose the entering variable (most negative reduced cost)
            entering_idx = np.argmin(self.reduced_costs)
            entering_var = self.non_basis_indices[entering_idx]

            # Compute the direction vector
            direction = np.dot(self.B_inv, self.A[:, entering_var])

            # Perform the minimum ratio test to compute ratios
            ratios = np.full_like(self.x_B, np.inf)
            positive_direction_indices = direction > 1e-8
            ratios[positive_direction_indices] = (
                self.x_B[positive_direction_indices]
                / direction[positive_direction_indices]
            )

            # Add ratios to the dataframe
            ratio_column = np.insert(ratios, 0, np.nan)
            df["ratio"] = ratio_column
            df.ratio = df.ratio.astype(str)
            df.loc[df.index[0], "ratio"] = "-"

        # Append the current tableau to the history
        self.tableau_history.append(df)

        # Display the iteration number and the tableau
        print(f"Iteration {self.iteration}")
        display(df)
        print("\n" + "=" * 60 + "\n")

    def solve(self) -> None:
        """Iterate until the optimal solution is found."""
        try:
            self.print_tableau()  # Print the initial tableau
            while True:
                self.next_tableau()
                if self.optimal:
                    print("Optimal solution reached.")
                    break
                else:
                    self.print_tableau()

            # Save all tableaux to a single Excel sheet after the process is done
            if self.save_excel:
                with pd.ExcelWriter(
                    "simplex_tableaux_all_iterations.xlsx", engine="openpyxl"
                ) as writer:
                    row_offset = 0  # To track where to start writing in the sheet
                    for i, df in enumerate(self.tableau_history):
                        # Add a header before each tableau
                        df.to_excel(
                            writer,
                            sheet_name="Tableaux",
                            startrow=row_offset + 1,
                            startcol=0,
                        )
                        worksheet = writer.sheets["Tableaux"]
                        worksheet.cell(
                            row=row_offset + 1,
                            column=1,
                            value=f"Tableau for Iteration {i}",
                        )
                        row_offset += (
                            df.shape[0] + 3
                        )  # Offset the row for the next tableau with space
                print("All tableaux saved as 'simplex_tableaux_all_iterations.xlsx'")
        except ValueError as e:
            print(f"An exception occurred: {e}")

    def get_dual_values(self) -> np.ndarray:
        """Get the values of the dual variables (shadow prices)."""
        # Dual variables are given by λ = c_B^T * B_inv
        dual_values = np.dot(self.c_B.T, self.B_inv)
        print("Dual variables (shadow prices):", dual_values)
        return dual_values
