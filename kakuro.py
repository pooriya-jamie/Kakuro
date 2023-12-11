from csp import *
from time import time
from itertools import permutations


######### Kakuro class implementation

class Kakuro(CSP):
	def __init__(self, kakuro_puzzle):
			variables = []
			domains = {}
			neighbors = {}
			self.puzzle = kakuro_puzzle

			def add_hidden_variable(hidden_var, i, j, direction, length, total_sum):
				variables.append(hidden_var)

				cell_counter = 0
				for step in range(1, length + 1):
					if direction == 'down':
						x, y = i + step, j
					else:
						x, y = i, j + step

					if x >= len(kakuro_puzzle) or y >= len(kakuro_puzzle[x]) or kakuro_puzzle[x][y] != "_":
						break

					nei = f"X{x},{y}"

					neighbors.setdefault(hidden_var, []).append(nei)
					neighbors.setdefault(nei, []).append(hidden_var)

					cell_counter += 1

				perms = [''.join(p) for p in permutations('123456789', cell_counter) if sum(map(int, p)) == total_sum]
				domains[hidden_var] = perms

			for i in range(len(kakuro_puzzle)):
				for j in range(len(kakuro_puzzle[i])):
					if kakuro_puzzle[i][j] == "_":
						var = f"X{i},{j}"
						variables.append(var)
						domains[var] = list(map(str, range(1, 10)))

					elif kakuro_puzzle[i][j] != '_' and kakuro_puzzle[i][j] != '*':
						if kakuro_puzzle[i][j][0] != "":
							hidden_var = f"C_d{i},{j}"
							add_hidden_variable(hidden_var, i, j, 'down', len(kakuro_puzzle) - i - 1, kakuro_puzzle[i][j][0])

						if kakuro_puzzle[i][j][1] != "":
							hidden_var = f"C_r{i},{j}"
							add_hidden_variable(hidden_var, i, j, 'right', len(kakuro_puzzle[i]) - j - 1, kakuro_puzzle[i][j][1])

			CSP.__init__(self, variables, domains, neighbors, self.kakuro_constraint)

	def kakuro_constraint(self, cell_1, val_1, cell_2, val_2):
		cell_1_type = cell_1[0]
		cell_2_type = cell_2[0]

		if cell_1_type == "X" and cell_2_type == "C":
			cell_1_coords = list(map(int, cell_1[1:].split(",")))
			cell_2_coords = list(map(int, cell_2[3:].split(",")))

			if cell_2[2] == "d":
				index = cell_1_coords[0] - cell_2_coords[0] - 1
				hidden_value = f"C_d{cell_2_coords[0]},{cell_2_coords[1]}"

				if val_2[index] == val_1:
					return True

			else:
				index = cell_1_coords[1] - cell_2_coords[1] - 1
				hidden_value = f"C_r{cell_2_coords[0]},{cell_2_coords[1]}"

				if val_2[index] == val_1:
					return True

		elif cell_1_type == "C" and cell_2_type == "X":
			cell_1_coords = list(map(int, cell_1[3:].split(",")))
			cell_2_coords = list(map(int, cell_2[1:].split(",")))

			if cell_1[2] == "d":
				index = cell_2_coords[0] - cell_1_coords[0] - 1
				hidden_value = f"C_d{cell_1_coords[0]},{cell_1_coords[1]}"

				if val_1[index] == val_2:
					return True

			else:
				index = cell_2_coords[1] - cell_1_coords[1] - 1
				hidden_value = f"C_r{cell_1_coords[0]},{cell_1_coords[1]}"

				if val_1[index] == val_2:
					return True

		return False




	def display(self, assigned_values=None):
		for i in range(len(self.puzzle)):
			line = ""
			for j in range(len(self.puzzle[i])):
				if self.puzzle[i][j] == '*':
					line += " * \t"
				elif self.puzzle[i][j] == "_":
					cell_id = "X" + str(i) + "," + str(j)
					if assigned_values is not None:
						if cell_id in assigned_values:
							line += " " + assigned_values[cell_id] + " \t"
						else:
							line += " _ \t"
					else:
						line += " _ \t"
				else:
					sum1 = str(self.puzzle[i][j][0]) if self.puzzle[i][j][0] else " "
					sum2 = str(self.puzzle[i][j][1]) if self.puzzle[i][j][1] else " "
					line += sum1 + "\\" + sum2 + "\t"
			print(line)
			print()


######### Kakuro puzzles

# Given, 4x3
kakuro_given4x3 = [
	['*', '*', '*', [6, ''], [3, '']],
	['*', [4, ''], [3, 3], '_', '_'],
	[['', 10], '_', '_', '_', '_'],
	[['', 3], '_', '_', '*', '*']
	]


# Given, 14x14
kakuro_given14x14 = [
    ['*', '*', '*', '*', '*', [4, ''], [24, ''], [11, ''], '*', '*', '*', [11, ''], [17, ''], '*', '*'],
    ['*', '*', '*', [17, ''], [11, 12], '_', '_', '_', '*', '*', [24, 10], '_', '_', [11, ''], '*'],
    ['*', [4, ''], [16, 26], '_', '_', '_', '_', '_', '*', ['', 20], '_', '_', '_', '_', [16, '']],
    [['', 20], '_', '_', '_', '_', [24, 13], '_', '_', [16, ''], ['', 12], '_', '_', [23, 10], '_', '_'],
    [['', 10], '_', '_', [24, 12], '_', '_', [16, 5], '_', '_', [16, 30], '_', '_', '_', '_', '_'],
    ['*', '*', [3, 26], '_', '_', '_', '_', ['', 12], '_', '_', [4, ''], [16, 14], '_', '_', '*'],
    ['*', ['', 8], '_', '_', ['', 15], '_', '_', [34, 26], '_', '_', '_', '_', '_', '*', '*'],
    ['*', ['', 11], '_', '_', [3, ''], [17, ''], ['', 14], '_', '_', ['', 8], '_', '_', [7, ''], [17, ''], '*'],
    ['*', '*', '*', [23, 10], '_', '_', [3, 9], '_', '_', [4, ''], [23, ''], ['', 13], '_', '_', '*'],
    ['*', '*', [10, 26], '_', '_', '_', '_', '_', ['', 7], '_', '_', [30, 9], '_', '_', '*'],
    ['*', [17, 11], '_', '_', [11, ''], [24, 8], '_', '_', [11, 21], '_', '_', '_', '_', [16, ''], [17, '']],
    [['', 29], '_', '_', '_', '_', '_', ['', 7], '_', '_', [23, 14], '_', '_', [3, 17], '_', '_'],
    [['', 10], '_', '_', [3, 10], '_', '_', '*', ['', 8], '_', '_', [4, 25], '_', '_', '_', '_'],
    ['*', ['', 16], '_', '_', '_', '_', '*', ['', 23], '_', '_', '_', '_', '_', '*', '*'],
    ['*', '*', ['', 6], '_', '_', '*', '*', ['', 15], '_', '_', '_', '*', '*', '*', '*']
    ]

# Easy, 6x6
kakuro_intermediate6x6 = [
	['*', [11, ''], [16, ''], [30, ''], '*', [24, ''], [11, '']],
	[['', 24], '_', '_', '_', ['', 9], '_', '_'],
	[['', 16], '_', '_', '_', [14, 17], '_', '_'],
	['*', '*', [22, 20], '_', '_', '_', '*'],
	['*', [3, 24], '_', '_', '_', [10, ''], [13, '']],
	[['', 7], '_', '_', ['', 19], '_', '_', '_'],
	[['', 11], '_', '_', ['', 7], '_', '_', '_']
	]

# Hard, 8x8
kakuro_hard8x8 = [
	['*', [28, ''], [15, ''], '*', [9, ''], [15, ''], '*', [9, ''], [12, '']],
	[['', 10], '_', '_', [15, 6], '_', '_', [10, 4], '_', '_'],
	[['', 38], '_', '_', '_', '_', '_', '_', '_', '_'],
	[['', 17], '_', '_', '_', ['', 4], '_', '_', [27, ''], '*'],
	[['', 13], '_', '_', [7, ''], [17, 19], '_', '_', '_', [15, '']],
	['*', ['', 8], '_', '_', '_', '*', [16, 3], '_', '_'],
	['*', [11, ''], [4, 4], '_', '_', [3, 24], '_', '_', '_'],
	[['', 44], '_', '_', '_', '_', '_', '_', '_', '_'],
	[['', 3], '_', '_', ['', 6], '_', '_', ['', 10], '_', '_']
	]


#####################################################kakuro_given4x3############################################################


print("\n\nKakuro puzzle: kakuro_given4x3\n")
board = kakuro_given4x3

# BT
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem)
total_time = time() - start_time
Kakuro_problem.display(assignments)
print("\tHeuristic and CSP algorithms: BT")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + FC
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem, inference=forward_checking)
total_time = time() - start_time
print("\tHeuristic and CSP algorithms: BT + FC")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")


# BT + FC + MRV
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, inference=forward_checking)
total_time = time() - start_time
print("\tHeuristic and CSP algorithms: BT + FC + MRV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + FC + MRV + LCV
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, order_domain_values=lcv, inference=forward_checking)
total_time = time() - start_time
print("\tHeuristic and CSP algorithms: BT + FC + MRV + LCV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + AR3
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem, inference=AC3_inference)
total_time = time() - start_time
print("\tHeuristic and CSP algorithms: BT + AR3")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

###################################################kakuro_intermediate6x6###########################################################

print("\n\nKakuro puzzle: kakuro_intermediate6x6\n")
board = kakuro_intermediate6x6

# BT
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem)
total_time = time() - start_time
Kakuro_problem.display(assignments)
print("\tHeuristic and CSP algorithms: BT")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + FC
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem, inference=forward_checking)
total_time = time() - start_time
print("\tHeuristic and CSP algorithms: BT + FC")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + FC + MRV
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, inference=forward_checking)
total_time = time() - start_time
print("\tHeuristic and CSP algorithms: BT + FC + MRV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + FC + MRV + LCV
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, order_domain_values=lcv, inference=forward_checking)
total_time = time() - start_time
print("\tHeuristic and CSP algorithms: BT + FC + MRV + LCV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + AR3
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem, inference=AC3_inference)
total_time = time() - start_time
print("\tHeuristic and CSP algorithms: BT + AR3")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")
##################################################kakuro_given14x14###############################################################
print("\n\nKakuro puzzle: kakuro_given14x14\n")
board = kakuro_given14x14


# BT + FC + MRV
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, inference=forward_checking)
total_time = time() - start_time
Kakuro_problem.display(assignments)
print("\tHeuristic and CSP algorithms: BT + FC + MRV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + FC + MRV + LCV
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, order_domain_values=lcv, inference=forward_checking)
total_time = time() - start_time
print("\tHeuristic and CSP algorithms: BT + FC + MRV + LCV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + AR3
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem, inference=AC3_inference)
total_time = time() - start_time
print("\tHeuristic and CSP algorithms: BT + AR3")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

##############################################kakuro_hard8x8#####################################################################
print("\n\nKakuro puzzle: kakuro_hard8x8\n")
board = kakuro_hard8x8

# BT + FC + MRV
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, inference=forward_checking)
total_time = time() - start_time
Kakuro_problem.display(assignments)
print("\tHeuristic and CSP algorithms: BT + FC + MRV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + FC + MRV + LCV
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, order_domain_values=lcv, inference=forward_checking)
total_time = time() - start_time
print("\tHeuristic and CSP algorithms: BT + FC + MRV + LCV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + AR3
Kakuro_problem = Kakuro(board)
start_time = time()
assignments = backtracking_search(Kakuro_problem, inference=AC3_inference)
total_time = time() - start_time
print("\tHeuristic and CSP algorithms: BT + AR3")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")
######################################################################################################################################
