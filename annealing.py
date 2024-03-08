import math
import random


def change_columns(board, col1, col2):
    board[col1], board[col2] = board[col2], board[col1]


def copy_solution(solution1, solution2):
    solution2 = solution1


def tweak_board(board, n):
    for col in range(n):
        random_number = random.randint(1, n)
        change_columns(board, col, random_number - 1)


def create_board(n):
    board = list(range(1, n + 1))

    tweak_board(board, n)

    return board


def calculate_energy(board, n):
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[j] - board[i]) == j - i:
                conflicts += 1

    return conflicts


def annealing_algorithm(dimensions: int, initial_temp=30, final_temp=.5, alpha=.98, steps_per_drop=2000):
    accepted = 0
    temp = initial_temp
    current = create_board(dimensions)
    best_energy = 100
    best_solution = []

    print("Annealing algorithm")

    energy_current = calculate_energy(current, dimensions)

    print("Starting solution")
    print("Temperature: ", temp)
    print("Current energy: ", energy_current)
    print_board(current, dimensions)

    working = create_board(dimensions)

    copy_solution(working, current)

    while temp > final_temp:
        accepted = 0
        for i in range(steps_per_drop):
            use_new = False

            tweak_board(working, dimensions)
            energy_working = calculate_energy(working, dimensions)

            if energy_working <= energy_current:
                use_new = True
            else:
                test = random.uniform(0, 1)
                delta = energy_working - energy_current
                calc = math.e ** (-delta / temp)
                if calc > test:
                    accepted += 1
                    use_new = True

            if use_new:
                use_new = False
                current = working
                energy_current = energy_working
                if energy_current < best_energy:
                    best_solution = current
                    best_energy = energy_current
            else:
                working = current

        temp *= alpha

    print("\nResult solution:")
    print("Temperature: ", temp)
    print("Best energy: ", best_energy)
    print("Amount of accepted solutions: ", accepted)
    print("Best solution: ", best_solution, '\n')
    print_board(best_solution, dimensions)


def print_board(board, n):
    board_to_print = [['O' for j in range(n)] for i in range(n)]

    for i in range(n):
        board_to_print[board[i] - 1][i] = 'Q'

    print("Board:")

    for row in board_to_print:
        print(row)
