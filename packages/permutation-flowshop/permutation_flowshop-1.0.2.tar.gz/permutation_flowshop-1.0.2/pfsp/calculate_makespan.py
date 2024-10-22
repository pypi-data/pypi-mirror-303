import numpy as np
from pfsp.validations import validation_time_matrix, validation_nonexists_jobs, validation_duplicated_jobs

def calculate_makespan(partial_sequence, number_jobs, number_machines, time_matrix):
    validation_time_matrix(time_matrix, number_jobs, number_machines)
    validation_nonexists_jobs(partial_sequence, number_jobs)
    validation_duplicated_jobs(partial_sequence)

    partial_makespan = np.zeros((number_machines, len(partial_sequence)))

    for job in range(len(partial_sequence)):
        for machine in range(number_machines):
            if machine == 0 and job == 0:
                partial_makespan[machine][job] = time_matrix[machine][partial_sequence[job]]

            elif machine == 0 and job != 0:
                partial_makespan[machine][job] = partial_makespan[machine][job-1] + time_matrix[machine][partial_sequence[job]]

            elif machine != 0 and job == 0:
                    partial_makespan[machine][job] = partial_makespan[machine-1][job] + time_matrix[machine][partial_sequence[job]]

            else:
                partial_makespan[machine][job] = max(partial_makespan[machine][job-1], partial_makespan[machine-1][job]) + time_matrix[machine][partial_sequence[job]]

    partial_makespan = partial_makespan[number_machines - 1][len(partial_sequence) - 1]

    return partial_makespan
