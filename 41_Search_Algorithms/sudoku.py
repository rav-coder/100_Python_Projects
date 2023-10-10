"""
References:

https://levelup.gitconnected.com/csp-algorithm-vs-backtracking-sudoku-304a242f96d0
https://github.com/StevenSalazarM/CSP-Sudoku-Solver/blob/master/original.py
"""


class SudokuCSP:

    # variables, domains and constraints for the problem
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.variables = [(i, j) for i in range(9) for j in range(9)]
        self.domain = {var: self.get_domain(var) for var in self.variables}
        self.constraints = self.get_constraints()

    # if initial puzzle doesnt contain zero i.e. empty cell, return the specified value
    def get_domain(self, var):
        if self.puzzle[var[0]][var[1]] == 0:
            return list(range(1, 10))
        else:
            return [self.puzzle[var[0]][var[1]]]

    # constrains for variables in the same row, column and the 3x3 squares for a sudoku problem
    @staticmethod
    def get_constraints():
        constraints = []
        for i in range(9):
            row_vars = [(i, j) for j in range(9)]
            col_vars = [(j, i) for j in range(9)]
            box_vars = [(i // 3 * 3 + j // 3, i % 3 * 3 + j % 3) for j in range(9)]
            constraints.append(row_vars)
            constraints.append(col_vars)
            constraints.append(box_vars)
        return constraints

    # make sure no constraint is violated with a specific move
    def is_valid(self, var, assignment):
        for constraint in self.constraints:
            if var in constraint:
                values = [assignment[other_var] for other_var in constraint if other_var != var]
                if assignment[var] in values:
                    return False
        return True

    # make sure all variables have been assigned
    def is_complete(self, assignment):
        return all(assignment[var] != 0 for var in self.variables)

    def select_unassigned_variable(self, assignment):
        unassigned_vars = [var for var in self.variables if assignment[var] == 0]
        return min(unassigned_vars, key=lambda var: len(self.domain[var]))

    # recursively select an unassigned variable and return a solution if found
    def backtrack(self, assignment):
        if self.is_complete(assignment):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for value in self.domain[var]:
            assignment[var] = value
            if self.is_valid(var, assignment):
                result = self.backtrack(assignment)
                if result is not None:
                    return result
            assignment[var] = 0

        return None

    def backtracking_search(self):
        assignment = {var: 0 for var in self.variables}
        return self.backtrack(assignment)

    def solve(self):
        solution = self.backtracking_search()
        if solution is None:
            print("Please provide a valid sudoku problem.")
        else:
            self.out_puzzle(solution)

    # print the solved puzzle
    @staticmethod
    def out_puzzle(valid_solution):
        for i in range(9):
            for j in range(9):
                print(valid_solution[(i, j)], end=" ")
                if (j + 1) % 3 == 0 and j != 8:
                    print("¦", end=" ")

            print('')

            if (i + 1) % 3 == 0 and i != 8:
                print("-" * 21)


in_puzzle = [
    [0, 0, 0, 7, 0, 0, 0, 4, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [5, 0, 0, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

csp = SudokuCSP(in_puzzle)
csp.solve()
