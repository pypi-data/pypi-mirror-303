# Simplextep by Keivan Jamal
# Website: KeivanJamali.com
# Email: K1Jamali01@gmail.com
# Versian 1.12.0

"""Examples:
    1) Solve Simplex.
    objective_function = [0, 2, 1]
    constraints = [[4, 1, 1], [2, 1, -1]] ### always write the constraints in the <= situation. Even the right handside is less than zero.
    equality = ["leq", "leq"]
    parameters = [("x1", "+"), ("x2", "+")] ### if you only write "x1", "x2" it assume that the sign is "+" by default.
    mode = "max"

    problem = Problem_Prepration(
                                objective_function=objective_function,
                                constraints=constraints,
                                equality=equality,
                                parameters=parameters,
                                mode=mode)

    simplex = Simplex(problem=problem, number_of_dashes=15)
    simplex.fit()

    simplex.make_table(format_="github") # This line will show all the steps.

    2) Solve Dual Simplex:
    dual_problem = Dual(objective_function=objective_function, constraints=constraints, equality=equality, parameters=parameters, mode=mode)
    dual_problem.fit()
    simplex = Simplex(problem=dual_problem.problem)
    simplex.fit(max_iterations=10)
    simplex.make_table() # This line will show all the steps.

    3) Simplex Analyse:
    objective_function = [0, 5, 4.5, 6]
    constraints = [[60, 6, 5, 8], [150, 10, 20, 10], [8, 1, 0, 0]]
    equality = ["leq", "leq", "leq"]
    parameters = [("x1", "+"), ("x2", "+"), ("x3", "+")]

    problem = Problem_Prepration(objective_function=objective_function,
                             constraints=constraints,
                             equality=equality,
                             parameters=parameters,
                             mode="max")

    simplex = Simplex(problem=problem)
    simplex.fit()
    # simplex.make_table(format_="github")

    analysis = Sensitivity_Analysis(simplex)
    analysis.change_righthand(righthands_at_first=[0, 1, 0, 0])
"""

import numpy as np
from tabulate import tabulate
import pandas as pd
from copy import deepcopy
import matplotlib.pyplot as plt


class Me_Plot:
    def __init__(self, node_lists: list, title: str, decimal: int = 1, font_size: int = 10):
        self.nodes = sorted(node_lists, key=lambda x: x[0])
        self.decimal = decimal
        self.font_size = font_size
        self.title = title
        self.x = None
        self.y = None
        self._make_x_y()
        self._plot_curve()

    def _make_x_y(self):
        self.x = []
        self.y = []

        for x, y in self.nodes:
            self.x.append(x)
            self.y.append(y)

    def _plot_curve(self):
        plt.plot(self.x, self.y, marker='o', linestyle='-')
        for i, (x, y) in enumerate(zip(self.x, self.y)):
            plt.text(x, y, f'({x:.{self.decimal}f},{y:.{self.decimal}f})', fontsize=self.font_size, ha='right')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(self.title)
        plt.grid(True)
        plt.show()


class Problem_Prepration:
    def __init__(self, objective_function: list, constraints: list, equality: list, parameters: list, mode: str, number_of_dashes: int = 20, decimal: int = 1, order_method: bool = True) -> None:
        """Initialize the class with the given constraints and equality lists.

        Args:
            objective_function (list): The objective function. Example [z=0 , c1, c2, c3]
            constraints (list): All your constraints in a list. They all should be = or <=. Example [[b1, a1, a2, a3], [b2, a1, a2, a3]]
            equality (list): Explain each of the constraints in a list. Example ["ineq", "eq"]. This means that the first constraint is <= and the second constraint is =.
            parameters (list): Write all parameters in a list of tuples. Example [('x1', '+'), ('x2', '-'), ('x3', 'n')]. +: greater thatn zero, -: less than zero, n: any number.
            mode (str): If your problem is maximization or minimization.
            number_of_dashes (int, optional): For printing the table. Defaults to 20.
            decimal (int, optional): For printing the table. Defaults to 1.
        """
        self.mode = mode
        self.number_of_dash = number_of_dashes
        self.decimal = decimal
        mode_list_max = ["max", "Max", "Maximum", "maximum"]
        mode_list_min = ["min", "Min", "Minimum", "minimum"]
        self.cons_data = deepcopy(constraints)
        self.equality = equality
        self.objective_addition = []
        self.basic_variables_at_first = []
        self.minus_w = [0 for _ in range(len(constraints[0]))]
        self.slack = 0
        self.artificial = 0
        self.excess = 0
        self.label = []
        if type(parameters[0]) != str:
            self.parameters = []
            self.signs = []
            for p, s in parameters:
                self.parameters.append(p)
                self.signs.append(s)
        else:
            self.parameters = parameters.copy()

        for i in range(len(self.cons_data)):
            self._check_constraints(i)

        self.objective_function = deepcopy(objective_function)
        if self.mode in mode_list_min:
            self.objective_function = [-i for i in self.objective_function]
            print("[INFO] As we have minimize problem, we multiply the objective function by -1.")
        elif self.mode in mode_list_max:
            pass
        else:
            raise ValueError("[ERROR] Mode must be 'min' or 'max'")
        self.objective_function.extend(self.objective_addition)
        if type(parameters[0]) != str:
            self._fit_parameters()
        self.constraints = deepcopy(self.cons_data)
        self.order_c = False
        self.order_o = False
        if order_method:
            self.order_c = []
            for i in range(len(self.constraints)):
                self.order_c.append([self.constraints[i][0]] + [1 if i == j else 0 for j in range(len(self.constraints))])
            self.order_o = [0 for _ in range(len(self.order_c[0]))]
        

    def _check_constraints(self, number: int) -> None:
        """
        Check the constraints based on the given number.

        Parameters:
            number (int): The number to check.

        Returns:
            None
        """
        if self.equality[number] in ["=", "eq"]:
            self._add_artificial(number)
            print("[INFO] Add Artificial")
        elif self.equality[number] in ["<=", "geq"]:
            self._add_excess_artificial(number)
            print("[INFO] Add excess & artificial")
        elif self.equality[number] in [">=", "leq"]:
            self._add_slack(number)
            print("[INFO] Add slack")


    def _add_slack(self, number: int) -> None:
        """
        Add a slack variable to the constraint matrix for the specified number.

        Parameters:
            number (int): The index at which the slack variable should be added.

        Returns:
            None
        """
        for i in range(len(self.cons_data)):
            if i == number:
                self.cons_data[i].append(1)
            else:
                self.cons_data[i].append(0)
        self.objective_addition.append(0)
        self.minus_w.append(0)
        self.slack += 1
        self.label.append(f"s{self.slack}")
        self.parameters.append(f"s{self.slack}")
        self.basic_variables_at_first.append(f"s{self.slack}")

    def _add_artificial(self, number: int) -> None:
        """
        Method to add an artificial variable to the linear program.

        Parameters:
            number (int): The index of the artificial variable to be added.

        Returns:
            None
        """
        for i in range(len(self.cons_data)):
            if i == number:
                self.cons_data[i].append(1)
            else:
                self.cons_data[i].append(0)
        self.objective_addition.append(0)
        self.minus_w.append(-1)
        self.artificial += 1
        self.label.append(f"a{self.artificial}")
        self.parameters.append(f"a{self.artificial}")
        self.basic_variables_at_first.append(f"a{self.artificial}")

    def _add_excess_artificial(self, number: int) -> None:
        """
        Add excess artificial variables to the constraint data for a given number.

        Parameters:
            number (int): The index of the artificial variable to be added.

        Returns:
            None
        """
        for i in range(len(self.cons_data)):
            if i == number:
                self.cons_data[i].extend([-1, 1])
            else:
                self.cons_data[i].extend([0, 0])
        self.objective_addition.extend([0, 0])
        self.minus_w.extend([0, -1])
        self.excess += 1
        self.artificial += 1
        self.label.append(f"e{self.excess}")
        self.label.append(f"a{self.artificial}")
        self.parameters.append(f"e{self.excess}")
        self.parameters.append(f"a{self.artificial}")
        self.basic_variables_at_first.append(f"a{self.artificial}")

    def _fit_parameters(self) -> None:
        """Fit all the setting neccessery for sign of different parameters.
        This function will change all the coefinitions if the sign is - and do nothing if it is + and seprate it to two parameters with ' and '' if the sign be 'n'.
        """
        for i in range(len(self.signs)):
            if self.signs[i] == "+":
                print(f"[INFO] Parameter {self.parameters[i]} remains same.")

            elif self.signs[i] == "-":
                print(f"[INFO] Parameter {self.parameters[i]} changed to -{self.parameters[i]}.")
                self.parameters[i] = "-"+self.parameters[i]
                for j in range(len(self.cons_data)):
                    self.cons_data[j][i+1] *= -1
                self.objective_function[i+1] *= -1
                self.minus_w[i+1] *= -1

            elif self.signs[i] == "n":
                print(f"[INFO] Parameter {self.parameters[i]} changed to {self.parameters[i]}' and {self.parameters[i]}''({self.parameters[i]} = {self.parameters[i]}' - {self.parameters[i]}'')")
                self.parameters[i] = self.parameters[i] + "'"
                self.parameters.append(self.parameters[i]+"'")
                for j in range(len(self.cons_data)):
                    self.cons_data[j].append(-1 * self.cons_data[j][i+1])
                self.objective_function.append(-1 * self.objective_function[i+1])
                self.minus_w.append(-1 * self.minus_w[i+1])

            else:
                raise ValueError("[ERROR] Invalid type of parameters. Expected: n , +, -")

    def __str__(self, format_:str = "github"):
        columns =  ["R.H.S"] + self.parameters
        data = pd.DataFrame(self.constraints, columns=columns)
        temp = self.label.copy()
        temp2 = [f"e{i}" for i in range(1, self.excess + 1)]
        for e in temp2:
            temp.remove(e)
        data["B.V"] = temp
        data_z = pd.DataFrame([self.objective_function], columns=columns)
        data_z["B.V"] = f"-z"

        data_empty = pd.DataFrame([np.array([f"{self.number_of_dash * "-"}" for _ in range(len(columns))])],
                                columns=columns)
        data_empty["B.V"] = f"{self.number_of_dash * "-"}"

        data = pd.concat((data, data_z, data_empty), ignore_index=True)
        self.data = data

        self.data.set_index("B.V", inplace=True)
        return tabulate(self.data, headers="keys", tablefmt=format_, numalign="right", floatfmt=f".{self.decimal}f")
    
    def __repr__(self, format_:str = "github"):
        columns =  ["R.H.S"] + self.parameters
        data = pd.DataFrame(self.constraints, columns=columns)
        data["B.V"] = self.label
        data_z = pd.DataFrame([self.objective_function], columns=columns)
        data_z["B.V"] = f"-z"

        data_empty = pd.DataFrame([np.array([f"{self.number_of_dash * "-"}" for _ in range(len(columns))])],
                                columns=columns)
        data_empty["B.V"] = f"{self.number_of_dash * "-"}"

        data = pd.concat((data, data_z, data_empty), ignore_index=True)
        self.data = data

        self.data.set_index("B.V", inplace=True)
        return tabulate(self.data, headers="keys", tablefmt=format_, numalign="right", floatfmt=f".{self.decimal}f")


class Simplex:
    def __init__(self, problem: Problem_Prepration, decimal: int = 1, number_of_dashes: int = 20, sp_code: float = 3512347615273248231645.12454) -> None:
        """Initialize the Simplex class with the given objective function, mode, parameters, and optional decimal value.

        Args:
            problem (Problem_Prepration): The problem difinded with Problem_Prepration class.
            decimal (int, optional): For printing better. Defaults to 1.
            number_of_dashes (int, optional): for printing better. Defaults to 20.
            sp_code (float, optional): This is a code and you can change it bu be careful it should always be positive. This code prevent from deviding by zero. Defaults to 3512347.4.
        """
        self.two_phase = None
        self.two_phase_done = None
        self.minus_w = None
        self.data = None
        self.result = None
        self.final_table = None
        self.sp_code = sp_code
        self.number_of_dash = number_of_dashes
        self.decimal = decimal
        self.problem_object = problem
        self.order_c = np.array(problem.order_c)
        self.order_o = np.array(problem.order_o)
        self.order_o_transition_list = []
        self.constraints = np.array(problem.constraints.copy(), dtype=float)
        self.objective_function = problem.objective_function.copy()
        self.objective_function = np.array(self.objective_function.copy(), dtype=float)
        self.minus_w = problem.minus_w.copy()
        self.minus_w = np.array(self.minus_w.copy(), dtype=float)
        self.basic_variables_at_first = problem.basic_variables_at_first.copy()
        self.slack = [f"s{i}" for i in range(1, problem.slack + 1)]
        self.artificial = [f"a{i}" for i in range(1, problem.artificial + 1)]
        self.excess = [f"e{i}" for i in range(1, problem.excess + 1)]
        self.label = problem.label.copy()
        self.columns = ["R.H.S"] + problem.parameters.copy()
        self.iteration = 1
        self.max_iterations = 1000
        self.mode = problem.mode
        self.force_stop = False
        try:
            for e in self.excess:
                self.label.remove(e)
        except:
            pass

    def fit(self, max_iterations: int = 1000) -> None:
        """
        A method to fit the constraints to the model and perform optimization.
        """
        self.max_iterations = max_iterations
        if  "a1" in self.label:
            print("[INFO] Two phase solution")
            self.two_phase = True
            self.two_phase_done = False
        else:
            print("[INFO] One phase solution")
            self.two_phase = False
            self.two_phase_done = False
        self._save_data(self.label, self.constraints)
        if self.two_phase:
            print("[INFO] Phase I starts", end=" | ")
            self._transform_two_phase()
            self._save_data(self.label, self.constraints)
            check = False
            while not check and not self.force_stop:
                self._transform()
                self._save_data(self.label, self.constraints)
                check = self._check_phase_two()
                if check == 2:
                    print("Finished")
                    self.data.set_index("B.V", inplace=True)
                    self._make_result_table(format_="github")
                    self.final_table = self.data.iloc[-(len(self.label) + 2):-1, :]
                    return None
            print("Finished")
            # don't remove artificial variables. If you want to remove change this to code.
            # self._remove_two_phase()
            self.two_phase_done = True
            self._save_data(self.label, self.constraints)
            print("[INFO] Phase II Starts", end=" | ")
            self.y_cols = []
            for l_ in range(len(self.columns)):
                if self.columns[l_][0] == "a":
                    self.y_cols.append(l_)
        check = False
        while not check and not self.force_stop:
            self._transform()
            self._save_data(self.label, self.constraints)
            check = self._check_optimization()
        print(f"Finished.")
        self.data.set_index("B.V", inplace=True)
        self._make_result_table(format_="github")
        self.final_table = self.data.iloc[-(len(self.label) + 2):-1, :]

    def _find_pivot_column(self) -> int:
        """
        Find the pivot column in the objective function and return its index.
        """
        temp = self.objective_function.copy()
        if self.two_phase:
            for i in self.y_cols:
                if temp[i] > 0:
                    temp[i] *= -1
        return temp[1:].argmax(axis=0) + 1

    def _find_pivot_column_two_phase(self) -> int:
        """
        Find the pivot column in the two-phase algorithm.
        No parameters.
        Returns:
            int: The index of the pivot column.
        """
        temp = self.minus_w.copy()
        # This is becuase I wanted to make sure that x1 will not change with x1... when the largest is 0.
        # for i in range(len(self.label)):
            # for j in range(len(self.columns)):
                # if self.label[i] == self.columns[j]:
                    # temp[j] -= 100000
        return temp[1:].argmax(axis=0) + 1
    
    def _find_pivot_row(self, column: int) -> int:
        """
        Find the pivot row based on the specified column.

        Parameters:
            column (int): The index of the column to consider.

        Returns:
            int: The index of the pivot row.
        """
        temp_co = self.constraints[:, column].copy()
        temp_co[temp_co == 0] = -1
        temp_ri = self.constraints[:, 0].copy()
        temp = temp_ri / temp_co
        temp[temp_co <= 0] = self.sp_code
        
        if min(temp) == self.sp_code:
            print(f"[Done] Failed to do the ratio test. Your problem is Unlimited. The answer is Inf!")
            self.force_stop = True
            print(f"[DONE] Z = Unbounded-Unlimited!!!")
            return -1

        temp_answers = []
        temp_min = temp.min()
        for i in range(len(temp)):
            if temp[i] == temp_min:
                temp_answers.append(i)
        if len(temp_answers)>1:
            res_min = np.array([np.inf for _ in range(len(self.order_c[0]))])
            res_index_min = 0
            for i in temp_answers:
                if self.compare_if_first_vectors_less_than_second(self.order_c[i], res_min):
                    res_min = self.order_c[i]
                    res_index_min = i
            return res_index_min
        else:
            return temp_answers[0]

    @staticmethod
    def compare_if_first_vectors_less_than_second(v1, v2):
        """It will return True if the v1 is less than v2. Unless it returns Flase. If equal, it returns number 2."""
        for i in range(len(v1)):
            for j in range(len(v2)):
                if i == j:
                    if v1[i] < v2[i]:
                        return True
                    elif v1[i] > v2[i]:
                        return False
        return 2

    def _find_pivot_element(self) -> tuple:
        """
        A function to find the pivot element in a matrix for optimization problems.
        Returns a tuple containing the pivot element value, row index, and column index.
        """
        if self.two_phase and not self.two_phase_done:
            column = self._find_pivot_column_two_phase()
        else:
            column = self._find_pivot_column()
        row = self._find_pivot_row(column)
        return self.constraints[row][column], row, column

    def _transform(self) -> None:
        """
        Find the pivot element in the constraints matrix and perform row operations to transform the matrix.
        """
        element, row, col = self._find_pivot_element()
        if row == -1:
            return None
        for i in range(len(self.constraints)):
            if i == row:
                self.constraints[i, :] = self.constraints[i, :] / element
                self.order_c[i] = self.order_c[i] / element
            else:
                temp = self.constraints[i, col] / self.constraints[row, col]
                for j in range(len(self.constraints[0, :])):
                    self.constraints[i, j] = self.constraints[i, j] - temp * self.constraints[row, j]
                for j in range(len(self.order_c[0])):
                    self.order_c[i, j] = self.order_c[i, j] - temp * self.order_c[row, j]
                temp = self.objective_function[col] / self.constraints[row, col]
                for j in range(len(self.objective_function)):
                    self.objective_function[j] = self.objective_function[j] - temp * self.constraints[row, j]
                for j in range(len(self.order_o)):
                    self.order_o[j] = self.order_o[j] - temp * self.constraints[row, j]
                if self.two_phase and not self.two_phase_done:
                    temp = self.minus_w[col] / self.constraints[row, col]
                    for j in range(len(self.minus_w)):
                        self.minus_w[j] = self.minus_w[j] - temp * self.constraints[row, j]
        self.order_o_transition_list.append(self.order_o.copy())
        self.label[row] = self.columns[col]

    def _transform_two_phase(self) -> None:
        """
        Transform the two-phase method by identifying rows and columns with specific conditions.
        """
        rows_num = []
        columns_num = []

        for i in range(len(self.columns)):
            if self.columns[i][0] == "a":
                columns_num.append(i)

        for i in range(len(self.constraints)):
            for j in columns_num:
                if abs(self.constraints[i][j] - 1) < 0.0001:
                    rows_num.append([i, 1])
                elif abs(self.constraints[i][j] + 1) < 0.0001:
                    rows_num.append([i, -1])

        for i in rows_num:
            self.minus_w = self.minus_w + self.constraints[i[0]] * i[1]

    def _remove_two_phase(self) -> None:
        """
        Remove the columns associated with the two-phase method from the model.
        """
        column_num = []
        for l_ in range(len(self.columns)):
            if self.columns[l_][0] == "a":
                column_num.append(l_)
        self.constraints_phase_i = self.constraints.copy()
        self.constraints = np.delete(self.constraints, column_num, axis=1)
        self.objective_function = np.delete(self.objective_function, column_num, axis=0)
        self.columns = [self.columns[i] for i in range(len(self.columns)) if i not in column_num]

    def _check_optimization(self) -> bool:
        """
        Check if the optimization is successful based on the objective function values.

        Parameters:
            None

        Returns:
            bool: True if optimization is successful, False otherwise.
        """
        temp = self.objective_function.copy()
        if self.two_phase:
            for i in self.y_cols:
                if temp[i] > 0:
                    temp[i] *= -1
        if self.iteration >= self.max_iterations:
            print(f"[ERROR] Limit of iteration exceeded.(iteration={self.max_iterations})")
            return True
        elif temp[1:].max(axis=0) > 1e-10:
            return False
        else:
            return True

    def _check_phase_two(self) -> bool:
        """
        A function to check phase two with specific conditions and return a boolean value.
        """
        if self.iteration >= self.max_iterations:
            print(f"[ERROR] Limit of iteration exceeded.(iteration={self.max_iterations})")
            print(f"[ERROR] It is not possiable to remove a(artificial variable) from BV. Therefore, this problem is Infisibale!")
            return 2
        elif self.minus_w[0] < 1e-5 and self.minus_w[1:].max(axis=0) < 1e-10:
            for l_i in range(len(self.label)):
                if self.label[l_i][0] == "a":
                    if self.constraints[l_i][0] > 0.001:
                        return False
            return True
        else:
            return False

    def _save_data(self, labels: list, values: np.array) -> None:
        """
        Save data to a DataFrame and update self.data with the new data.

        Args:
            labels (list): Labels for the data.
            values (np.array): Values to be saved in the DataFrame.
        """
        data = pd.DataFrame(values, columns=self.columns)
        data["B.V"] = labels
        data[self.columns] = data[self.columns].round(self.decimal)
        data_z = pd.DataFrame([self.objective_function], columns=self.columns)
        data_z["B.V"] = f"-z{self.iteration}"
        data_z[self.columns] = data_z[self.columns].round(self.decimal)
        if self.two_phase and not self.two_phase_done:
            data_w = pd.DataFrame([self.minus_w], columns=self.columns)
            data_w["B.V"] = f"-w{self.iteration}"
            data_w[self.columns] = data_w[self.columns].round(self.decimal)

        data_empty = pd.DataFrame([np.array([f"{self.number_of_dash * "-"}" for _ in range(len(self.columns))])],
                                  columns=self.columns)
        data_empty["B.V"] = f"{self.number_of_dash * "-"}"

        self.iteration += 1

        if self.two_phase and not self.two_phase_done:
            data = pd.concat((data, data_z, data_w, data_empty), ignore_index=True)
        else:
            data = pd.concat((data, data_z, data_empty), ignore_index=True)

        if self.data is not None:
            self.data = pd.concat((self.data, data), ignore_index=True)
        else:
            self.data = data

    def make_table(self, format_: str="github") -> None:
        """
        A function to generate a table in a specified format.

        Parameters:
            format_ (str): The format of the table. It can be "github", "latex", or "excel".

        Returns:
            None if the format is not supported, otherwise it prints a table in the specified format.
        """
        if format_ not in ["github", "latex", "excel"]:
            return None
        print(tabulate(self.data, headers="keys", tablefmt=format_, numalign="right", floatfmt=f".{self.decimal}f"))

    def _make_result_table(self, format_:str = "github") -> None:
        """
        Generates a result table based on the columns and data attributes of the object.

        Parameters:
            format_ (str): The format of the table. It can be "github", "latex", or "excel".

        Returns:
            None if the format is not supported, otherwise it prints a table in the specified format.
        """
        result = {}
        for l_ in self.columns:
            if l_ not in self.label:
                result[l_] = 0
            else:
                result[l_] = self.data[self.data.index == l_].iloc[-1, 0]
        if self.mode == "max":
            result["R.H.S"] = -self.data.iloc[-2, 0]
        else:
            result["R.H.S"] = self.data.iloc[-2, 0]
        self.result = pd.DataFrame(result, index=[0])
        print(tabulate(self.result, headers="keys", tablefmt=format_, numalign="right", floatfmt=f".{self.decimal}f"))


class Sensitivity_Analysis:
    """In this Class we define a Sensitivity analysis.
    """
    def __init__(self, table: Simplex):
        """Here we define a Sensitivity analysis init.

        Args:
            table (Simplex): An object of simplex class.
        """
        self.teta = None
        self.righthand = None
        self.righthand_b = None
        self.shadow_prices = {}
        self.righthand_nodes = []
        self.coefficient_nodes = []
        self.tabulate = table.final_table.copy()
        self.basic_variables_at_first = table.basic_variables_at_first.copy()
        self._set_setting()
        self.make_shadow_prices()

    def _set_setting(self):
        """This function collect nessecery iformation from simplex class.
        """
        self.label = list(self.tabulate.index)
        self.columns = list(self.tabulate.columns[:])
        self.constraints = self.tabulate.iloc[:-1, :].values.copy()
        self.objective_function = self.tabulate.iloc[-1, :].values.copy()

    def make_shadow_prices(self):
        """In this function we find shadow prices.
        """
        for c in range(len(self.columns[1:])):
            temp = -self.tabulate.iloc[-1, c + 1]
            self.shadow_prices[self.columns[1:][c]] = 0 if abs(temp) < 0.001 else temp

    def change_righthand(self, righthands_at_first: list = None, righthands_at_last: list = None):
        """What happens if righthands are changed? This function will help you with that.

        Args:
            righthands_at_first (list, optional): What is the righthands befor solving the simplex table? Defaults to None.
            righthands_at_last (list, optional): What is the righthands after solving the simplex table? Defaults to None.

        Raises:
            ValueError: The len of the input should be equal to the number of rows.
        """
        if righthands_at_first and not righthands_at_last:
            self.righthand_b = self._from_first_to_final(righthand=righthands_at_first).copy()
        elif not righthands_at_first and righthands_at_last:
            self.righthand_b = righthands_at_last.copy()
        else:
            print("[ERROR]")

        self.righthand = self.righthand_b.copy()
        if len(self.righthand) != len(self.label):
            raise ValueError("number of righhands must be equal to the number of rows.")

        self.teta = 0
        self.righthand_nodes.append([self.teta, -(self.objective_function[0] + self.teta * self.righthand[-1])])

        self._set_setting()
        while abs(self.objective_function[0] + self.teta * self.righthand[-1]) > 0.0001:
            self._transform(mode="d")
            self.righthand_nodes.append([self.teta, -(self.objective_function[0] + self.teta * self.righthand[-1])])
            if abs(self.righthand[-1]) < 0.01:
                break

        self._set_setting()
        self.righthand = self.righthand_b.copy()
        self.teta = 0
        while abs(self.objective_function[0] + self.teta * self.righthand[-1]) > 0.0001:
            self._transform(mode="u")
            self.righthand_nodes.append([self.teta, -(self.objective_function[0] + self.teta * self.righthand[-1])])
            if abs(self.righthand[-1]) < 0.01:
                break

        Me_Plot(self.righthand_nodes, title="Righthand limits")

    def _find_pivot_row_righthand(self, mode: str) -> int:
        """To help the function of cange_righthand we need this function to find pivot row.

        Args:
            mode (str): If we are going to larger numbers: u and if we are going to smaller numbers: d.

        Returns:
            int: The index of pivot row.
        """
        temp = []
        for i in range(len(self.constraints[:, 0])):
            if abs(self.righthand[i]) > 0.001:
                temp.append(-self.constraints[i, 0] / self.righthand[i])
            else:
                temp.append(0)
        if mode == "u":
            row = np.argmax(temp)
            self.teta = np.max(temp)
        elif mode == "d":
            row = np.argmin(temp)
            self.teta = np.min(temp)
        return row

    def _find_pivot_column_righthand(self, row: int) -> int:
        """In this part we help to find pivot column to help change_righthand function

        Args:
            row (int): The specified row in the _find_pivot_column_righthand function.

        Returns:
            int: The index of the pivot column.
        """
        temp = []
        for i in range(1, len(self.constraints[row, :])):
            temp2 = 0.0001 if self.constraints[row, i] == 0 else self.constraints[row, i]
            temp.append(self.objective_function[i] / temp2)
        temp = np.array(temp, dtype=float)
        temp[temp < 0.001] = np.inf
        column = np.argmin(temp)
        return column + 1

    def _find_pivot_element_righthand(self, mode: str) -> tuple:
        """To find the pivot element to help the change_righthand function.

        Args:
            mode (str): If we are increasing our numbers then u and if we are decreasing then d.

        Returns:
            tuple: (Value, row, column)
        """
        row = self._find_pivot_row_righthand(mode=mode)
        column = self._find_pivot_column_righthand(row)
        return self.constraints[row][column], row, column

    def _transform(self, mode: str) -> None:
        """The function to do transformation of simplex method.

        Args:
            mode (str): If we are increasing our numbers then u and if we are decreasing then d.
        """
        element, row, col = self._find_pivot_element_righthand(mode=mode)
        for i in range(len(self.constraints)):
            if i == row:
                self.constraints[i, :] = self.constraints[i, :] / element
                self.righthand[row] = self.righthand[row] / element
            else:
                temp = self.constraints[i, col] / self.constraints[row, col]
                for j in range(len(self.constraints[0, :])):
                    self.constraints[i, j] = self.constraints[i, j] - temp * self.constraints[row, j]
                self.righthand[i] = self.righthand[i] - temp * self.righthand[row]

        temp = self.objective_function[col] / self.constraints[row, col]
        for j in range(len(self.objective_function)):
            self.objective_function[j] = self.objective_function[j] - temp * self.constraints[row, j]
        self.righthand[-1] = self.righthand[-1] - temp * self.righthand[row]

        self.label[row] = self.columns[col]

    def _from_first_to_final(self, righthand: list) -> list:
        """Change the righthands of the simplex befor solving it to the final simplex table.

        Args:
            righthand (list): righthands before solving the simplex.

        Returns:
            list: The new righthands.
        """
        new_righthand = []
        columns = []
        for n in self.basic_variables_at_first:
            for j in range(len(self.columns)):
                if n == self.columns[j]:
                    columns.append(j)
                    break

        for i in range(len(righthand) - 1):
            temp = 0
            for j in range(len(righthand) - 1):
                temp += righthand[j] * self.constraints[i, columns[j]]
            new_righthand.append(temp)

        temp = 0
        for j in range(len(righthand) - 1):
            temp += righthand[j] * self.objective_function[columns[j]]
        new_righthand.append(temp)

        return new_righthand
    

class Dual():
    def __init__(self, objective_function: list, constraints: list, equality: list, parameters: list, mode: str, number_of_dashes: int = 15, decimal:int = 1) -> None:
        """Prepare the dual problem for any problem.

        Args:
            objective_function (list): The objective function for the primal problem. Example [z=0 , c1, c2, c3]
            constraints (list): All your constraints in a list for the primal problem. They all should be = or <=. Example [[b1, a1, a2, a3], [b2, a1, a2, a3]]
            equality (list): Explain each of the constraints in a list for the primal problem. Example ["ineq", "eq"]. This means that the first constraint is <= and the second constraint is =.
            parameters (list): Write all parameters in a list of tuples for the primal problem. Example [('x1', '+'), ('x2', '-'), ('x3', 'n')]. +: greater thatn zero, -: less than zero, n: any number.
            mode (str): If your problem is maximization or minimization for the primal problem.
            number_of_dashes (int, optional): For printing the table. Defaults to 20.
            decimal (int, optional): For printing the table. Defaults to 1.
        """
        self.number_of_dash = number_of_dashes
        self.decimal = decimal
        
        self.old_constraints = constraints.copy()
        self.old_equality = equality.copy()
        self.old_objective_function = objective_function.copy()
        self.old_parameters = parameters.copy()
        self.old_mode = mode

        self.new_constraints = []
        self.new_equality = []
        self.new_objective_function = [0]
        self.new_parameters = []
        mode_list_max = ["max", "Max", "Maximum", "maximum"]
        mode_list_min = ["min", "Min", "Minimum", "minimum"]
        if mode in mode_list_max:
            self.new_mode = "min"
            self._max_to_min_cons()
            self._max_to_min_params()
        elif mode in mode_list_min:
            self.new_mode = "max"
            self._min_to_max_cons()
            self._max_to_min_params()
        else:
            raise ValueError("[ERROR] Expected 'max' or 'min' for MODE.")
        self._obj()
        print(f"[INFO] Dual Problem setting is set successfully.")


    def fit(self) -> None:
        """This function will make the Dual Problem in the problem variable. You can access it by writing Dual.problem.
        """
        obj = deepcopy(self.new_objective_function)
        cons = deepcopy(self.new_constraints)
        equ = deepcopy(self.new_equality)
        para = deepcopy(self.new_parameters)
        self.problem = Problem_Prepration(objective_function=obj, constraints=cons, equality=equ, parameters=para, mode=self.new_mode)
        print(f"[INFO] Dual New Problem had been made successfully.")

    def _max_to_min_params(self):
        """Generate parameters for dual problem if we start at max and go to min problem.
        """
        if self.old_parameters[0][0][0] == "x":
            ch = "Y"
        elif self.old_parameters[0][0][0] == "Y":
            ch = "x"
        for i in range(len(self.old_equality)):
            if self.old_equality[i] == "eq":
                sign = "n"
            elif self.old_equality[i] == "ineq":
                sign = "+"
            self.new_parameters.append((f"{ch}{i+1}", sign))

    def _max_to_min_cons(self):
        """Generate constraints for dual problem if we start at max and go to min problem.
        """
        for j in range(len(self.old_parameters)):
            new_r = [self.old_objective_function[j+1]]
            for i in range(len(self.old_constraints)):
                new_r.append(self.old_constraints[i][j+1])
            self.new_constraints.append(new_r)

        for i in range(len(self.old_parameters)):
            if self.old_parameters[i][1] == "+":
                self.new_equality.append("ineq")
                self.new_constraints[i] = [-k for k in self.new_constraints[i]]
            elif self.old_parameters[i][1] == "-":
                self.new_equality.append("ineq")
            elif self.old_parameters[i][1] == "n":
                self.new_equality.append("eq")

    def _min_to_max_params(self):
        """Generate parameters for dual problem if we start at min and go to max problem.
        """
        if self.old_parameters[0][0][0] == "x":
            ch = "Y"
        elif self.old_parameters[0][0][0] == "Y":
            ch = "x"
        for i in range(len(self.old_equality)):
            if self.old_equality[i] == "eq":
                sign = "n"
            elif self.old_equality[i] == "ineq":
                sign = "+"
            self.new_parameters.append((f"{ch}{i+1}", sign))

    def _min_to_max_cons(self):
        """Generate constraints for dual problem if we start at max and go to min problem.
        """
        for j in range(len(self.old_parameters)):
            new_r = [self.old_objective_function[j+1]]
            for i in range(len(self.old_constraints)):
                new_r.append(self.old_constraints[i][j+1])
            self.new_constraints.append(new_r)

        for i in range(len(self.old_parameters)):
            if self.old_parameters[i][1] == "+":
                self.new_equality.append("ineq")
            elif self.old_parameters[i][1] == "-":
                self.new_equality.append("ineq")
                self.new_constraints[i] = [-k for k in self.new_constraints[i]]
            elif self.old_parameters[i][1] == "n":
                self.new_equality.append("eq")

    def _obj(self):
        """Generates the new objective_function for dual problem.
        """
        for i in range(len(self.old_constraints)):
            self.new_objective_function.append(self.old_constraints[i][0])

    def __str__(self, format_:str = "github"):
        columns =  ["R.H.S"] + self.new_parameters
        data = pd.DataFrame(self.new_constraints, columns=columns)
        data["B.V"] = ["s" for _ in range(len(self.new_equality))]
        data_z = pd.DataFrame([self.new_objective_function], columns=columns)
        data_z["B.V"] = f"-z"

        data_empty = pd.DataFrame([np.array([f"{self.number_of_dash * "-"}" for _ in range(len(columns))])],
                                columns=columns)
        data_empty["B.V"] = f"{self.number_of_dash * "-"}"

        data = pd.concat((data, data_z, data_empty), ignore_index=True)
        self.data = data

        self.data.set_index("B.V", inplace=True)
        return tabulate(self.data, headers="keys", tablefmt=format_, numalign="right", floatfmt=f".{self.decimal}f")
    
    def __repr__(self, format_:str = "github"):
        columns =  ["R.H.S"] + self.new_parameters
        data = pd.DataFrame(self.new_constraints, columns=columns)
        data["B.V"] = ["s" for _ in range(len(self.new_equality))]
        data_z = pd.DataFrame([self.new_objective_function], columns=columns)
        data_z["B.V"] = f"-z"

        data_empty = pd.DataFrame([np.array([f"{self.number_of_dash * "-"}" for _ in range(len(columns))])],
                                columns=columns)
        data_empty["B.V"] = f"{self.number_of_dash * "-"}"

        data = pd.concat((data, data_z, data_empty), ignore_index=True)
        self.data = data

        self.data.set_index("B.V", inplace=True)
        return tabulate(self.data, headers="keys", tablefmt=format_, numalign="right", floatfmt=f".{self.decimal}f")
