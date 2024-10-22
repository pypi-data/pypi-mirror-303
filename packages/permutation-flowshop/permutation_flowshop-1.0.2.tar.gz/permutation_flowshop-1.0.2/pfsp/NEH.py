import numpy as np

from pfsp.validations import validation_time_matrix
from pfsp.calculate_makespan import calculate_makespan

def NEH(number_jobs, number_machines, time_matrix, show=False):
    validation_time_matrix(time_matrix, number_jobs, number_machines) #validation of time matrix
    best_makespan = np.inf
    minimal_makespan = np.inf
    best_sequence = None

    p = np.zeros(number_jobs)

    for i in range(number_jobs):
        p[i] = sum(time_matrix[j][i] for j in range(number_machines))

    sorted_jobs = np.argsort(p)[::-1].tolist()

    best_sequence = sorted_jobs[:2]

    makespan_sequence_2_jobs = calculate_makespan(best_sequence, number_jobs, number_machines, time_matrix)

    best_inverted_sequence = best_sequence[::-1]

    makespan_sequence_2_jobs_inverted = calculate_makespan(best_inverted_sequence, number_jobs, number_machines, time_matrix)

    if makespan_sequence_2_jobs_inverted < makespan_sequence_2_jobs:
        best_sequence = best_inverted_sequence

    for i in range(2, number_jobs):
        current_job = sorted_jobs[i]
        best_local_makespan = np.inf
        best_local_position = 0

        for position in range(i + 1):
            candidate_list = best_sequence[:position] + [current_job] + best_sequence[position:]
            current_makespan = calculate_makespan(candidate_list, number_jobs, number_machines, time_matrix)

            if current_makespan < best_local_makespan:
                best_local_makespan = current_makespan
                best_local_position = position

        best_sequence = best_sequence[:best_local_position] + [current_job] + best_sequence[best_local_position:]
        best_makespan = best_local_makespan

    if show == True:
        print("Sequence Obtained by the NEH Heuristic: ", best_sequence)
        print("Makespan Obtained by the NEH Heuristic = ", best_makespan)
    else:
        pass
    return best_sequence, best_makespan
