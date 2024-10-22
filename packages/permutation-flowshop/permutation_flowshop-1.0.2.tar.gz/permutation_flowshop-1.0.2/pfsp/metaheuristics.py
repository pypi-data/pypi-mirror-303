import numpy as np
import random as rd
import time
import sys

from pfsp.local_search import local_search_swap_best_improvement, local_search_swap_first_improvement
from pfsp.earliest_time_makespan_calculate import earliest_time_makespan_calculate, earliest_time
from pfsp.calculate_makespan import calculate_makespan
from pfsp.validations import validation_time_matrix

def multistart(number_jobs, number_machines, time_matrix, starts, ls, logs):
    best_makespan = np.inf
    best_sequence = []
    elapsed_time = 0
    iterations = 0
    local_search = None
    completion_time_matrix = np.zeros((number_machines, number_jobs), dtype=np.float64)

    validation_time_matrix(time_matrix, number_jobs, number_machines)

    if ls == 'swapbi':
        local_search = local_search_swap_best_improvement

    elif ls == 'swapfi':
        local_search = local_search_swap_first_improvement

    else:
        print("Choose a valid neighborhood operator in ls = ")
        sys.exit()

    if ls == 'swapbi' and logs == True:
        print("\nUsing Swap operator with Best Improvent Strategy...\n")

    elif ls == 'swapfi' and logs == True:
        print("\nUsing Swap operator with First Improvent Strategy...\n")

    initial_time = time.time()

    while iterations < starts:

        initial_solution = np.random.permutation(number_jobs).tolist()

        # calculating constructive makespan
        constructive_makespan = calculate_makespan(initial_solution, number_jobs, number_machines, time_matrix)
        # Executing local search
        local_search_sequence, local_search_makespan  = local_search(number_jobs, number_machines, time_matrix, initial_solution, constructive_makespan)

        # Updating best solution found
        if local_search_makespan < best_makespan:
            best_makespan = local_search_makespan
            best_sequence = local_search_sequence
            if logs == True:
                # print("Contructive Solution: ", initial_solution)
                print(f"Iteration: {iterations}. \nContructive Makespan = {constructive_makespan}; Local Search Makespan = {local_search_makespan};")
                print("Current Best Sequence: ", best_sequence)
            else:
                pass

        iterations += 1

    end_time = time.time()
    elapsed_time = round(end_time - initial_time, 4)
    if logs == True:
        print("\nBest Sequence (multi-start): ", best_sequence)
        print("Best Makespan (multi-start): ", best_makespan)
        print("Number of stars performed: ", iterations)
        print(f"Best solution (multi-start) found in {elapsed_time} (seconds)")

    earliest_completion_time, makespan = earliest_time_makespan_calculate(best_sequence, time_matrix, number_machines, number_jobs)

    # Collect completion times in the matrix
    for j in range(number_machines):
        for index, job in enumerate(best_sequence):
            machine = j
            end_time = earliest_completion_time[j][index] + time_matrix[j][job]
            completion_time_matrix[machine][index] = end_time

    if logs == True:
        print("\n===== Completion Time matrix ======")
        print(completion_time_matrix)
        print()

    return best_sequence, best_makespan, iterations, elapsed_time, completion_time_matrix

# constructive Grasp metaheuristic
def constructive_grasp(number_jobs, number_machines, time_matrix, alpha):
    sol = []
    restrict_candidate_list = []
    C = [i for i in range(number_jobs)]

    while C:
        jobs_makespans_list = []

        for i in C:
            incremental_makespan = calculate_makespan([i], number_jobs, number_machines, time_matrix)
            jobs_makespans_list.append(incremental_makespan)

            g_min = min(jobs_makespans_list)
            g_max = max(jobs_makespans_list)

            if incremental_makespan <= (g_min + alpha * (g_max - g_min)):
                restrict_candidate_list.append(i)

        if restrict_candidate_list:
            selected_job = rd.choice(restrict_candidate_list)
            sol.append(selected_job)
            C.remove(selected_job)
            restrict_candidate_list = []

    return sol

#Grasp metaheuristic
def grasp(number_jobs, number_machines, time_matrix, alpha, max_iterations, ls, logs):
    best_makespan = np.inf
    best_sequence = []
    elapsed_time = 0
    iterations = 0
    local_search = None
    completion_time_matrix = np.zeros((number_machines, number_jobs), dtype=np.float64)

    validation_time_matrix(time_matrix, number_jobs, number_machines)

    if ls == 'swapbi':
        local_search = local_search_swap_best_improvement

    elif ls == 'swapfi':
        local_search = local_search_swap_first_improvement

    else:
        print("Choose a valid neighborhood operator in ls = ")
        sys.exit()

    if ls == 'swapbi' and logs == True:
        print("\nUsing Swap operator with Best Improvent Strategy...\n")

    elif ls == 'swapfi' and logs == True:
        print("\nUsing Swap operator with First Improvent Strategy...\n")

    initial_time = time.time()

    while iterations < max_iterations:

        initial_solution = constructive_grasp(number_jobs, number_machines, time_matrix, alpha)

        # calculating constructive makespan
        constructive_makespan = calculate_makespan(initial_solution, number_jobs, number_machines, time_matrix)

        # Executing local search
        local_search_sequence, local_search_makespan = local_search(number_jobs, number_machines, time_matrix, initial_solution, constructive_makespan)

        # Updating best solution found
        if local_search_makespan < best_makespan:
            best_makespan = local_search_makespan
            best_sequence = local_search_sequence
            if logs == True:
                # print("Contructive Solution: ", initial_solution)
                print(f"Iteration: {iterations}. \nContructive Makespan = {constructive_makespan}; Local Search Makespan = {local_search_makespan};")
                print("Current Best Sequence: ", best_sequence)
            else:
                pass

        iterations += 1

    end_time = time.time()
    elapsed_time = round(end_time - initial_time, 4)
    if logs == True:
        print("\nBest Sequence (GRASP): ", best_sequence)
        print("Best Makespan (GRASP): ", best_makespan)
        print("Number of iterations performed: ", iterations)
        print(f"Best solution (GRASP) found in {elapsed_time} (seconds)")

    earliest_completion_time, makespan = earliest_time_makespan_calculate(best_sequence, time_matrix, number_machines, number_jobs)

    # Collect completion times in the matrix
    for j in range(number_machines):
        for index, job in enumerate(best_sequence):
            machine = j
            end_time = earliest_completion_time[j][index] + time_matrix[j][job]
            completion_time_matrix[machine][index] = end_time

    if logs == True:
        print("\n===== Completion Time matrix ======")
        print(completion_time_matrix)
        print()

    return best_sequence, best_makespan, iterations, elapsed_time, completion_time_matrix
