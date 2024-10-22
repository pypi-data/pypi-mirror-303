import numpy as np
from pfsp.validations import validation_time_matrix, validation_nonexists_jobs, validation_duplicated_jobs


def earliest_time(sequence, time_matrix, number_machines, number_jobs):
    validation_time_matrix(time_matrix, number_jobs, number_machines)
    validation_nonexists_jobs(sequence, number_jobs)
    validation_duplicated_jobs(sequence)
    earliest_completion_time = np.zeros((number_machines, number_jobs))

    for job in range(number_jobs):
        for machine in range(number_machines):
            if machine == 0 and job == 0:
                earliest_completion_time[machine][job] = 0  # Na primeira máquina e primeira tarefa, o tempo de início é sempre 0

            elif (machine == 0 and job != 0):
                earliest_completion_time[machine][job] = earliest_completion_time[machine][job-1] + time_matrix[machine][sequence[job-1]]

            elif machine !=0 and job == 0:
                earliest_completion_time[machine][job] = earliest_completion_time[machine-1][job] + time_matrix[machine-1][sequence[job]]
            else:
                earliest_completion_time[machine][job] = max(earliest_completion_time[machine][job-1] + time_matrix[machine][sequence[job-1]], earliest_completion_time[machine-1][job] + time_matrix[machine-1][sequence[job]])

    return earliest_completion_time

def earliest_time_makespan_calculate(sequence, time_matrix, number_machines, number_jobs):

    # Calcula os tempos de início das tarefas
    earliest_completion_time = earliest_time(sequence, time_matrix, number_machines, number_jobs)

    makespan = earliest_completion_time[number_machines - 1][number_jobs-1] + time_matrix[number_machines - 1][sequence[number_jobs -1]]

    return earliest_completion_time, makespan
