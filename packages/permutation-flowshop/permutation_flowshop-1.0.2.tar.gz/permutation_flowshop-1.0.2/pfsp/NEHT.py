import numpy as np
from pfsp.validations import validation_time_matrix

def makespan_taillard(partial_sequence, number_machines, time_matrix):

    current_e = np.zeros((number_machines, len(partial_sequence)))

    for j in range(number_machines):
        for i in range(len(partial_sequence)):

            if j == 0 and i == 0:
                current_e[j][i] = 0 + time_matrix[j][partial_sequence[i]]

            elif j == 0 and i != 0:
                current_e[j][i] = current_e[j][i-1] + time_matrix[j][partial_sequence[i]]

            elif i == 0 and j != 0:
                current_e[j][i] = current_e[j-1][i] + time_matrix[j][partial_sequence[i]]

            else:
                current_e[j][i]  = max(current_e[j][i-1], current_e[j-1][i]) + time_matrix[j][partial_sequence[i]]

    return current_e[number_machines-1][len(partial_sequence)-1]

def NEHT(number_jobs, number_machines, time_matrix, show=False):
    validation_time_matrix(time_matrix, number_jobs, number_machines)
    job_list = []
    for i in range(number_jobs):
        total_processing_time = 0
        for j in range(number_machines):
            total_processing_time = total_processing_time + time_matrix[j][i]
        job_list.append((i, total_processing_time))

    p = np.zeros(number_jobs)

    for i in range(number_jobs):
        p[i] = sum(time_matrix[j][i] for j in range(number_machines))

    sorted_jobs = np.argsort(p)[::-1].tolist()

    seq_1 = np.zeros(2, dtype=int).tolist()
    seq_2 = np.zeros(2, dtype=int).tolist()

    seq_1[0] = seq_2[1] = sorted_jobs[0]
    seq_1[1] = seq_2[0] = sorted_jobs[1]

    if makespan_taillard(seq_1, number_machines, time_matrix) < makespan_taillard(seq_2, number_machines, time_matrix):
        seq_2 = seq_1

    best_sequence = seq_2

    sorted_jobs.pop(0)
    sorted_jobs.pop(0)

    for k in sorted_jobs:
        insert_job = k

        e = np.zeros((number_machines, len(seq_2)))
        q = np.zeros((number_machines, len(seq_2)))
        f = np.zeros((number_machines, len(seq_2)+1))
        M = np.zeros(len(seq_2)+1)

        #calculate eij
        for j in range(number_machines):
            for i in range(len(seq_2)):
                if i == 0 and j == 0:
                    e[j][i] = 0 + time_matrix[j][seq_2[i]]

                elif j == 0 and i != 0:
    	            e[j][i] = e[j][i-1] + time_matrix[j][seq_2[i]]

                elif i == 0 and j != 0:
                     e[j][i] = e[j-1][i] + time_matrix[j][seq_2[i]]

                else:
                    e[j][i] = max(e[j][i-1], e[j-1][i]) + time_matrix[j][seq_2[i]]

        #calculate qij
        for j in range(number_machines)[::-1]:
            for i in range(len(seq_2))[::-1]:

                if j == number_machines-1 and i == len(seq_2)-1:
                    q[j][i] = 0 + time_matrix[j][seq_2[i]]

                elif j == number_machines-1:
                    q[j][i] = q[j][i+1] + time_matrix[j][seq_2[i]]

                elif i == len(seq_2)-1:
                    q[j][i] = q[j + 1][i] + time_matrix[j][seq_2[i]]

                else:
                    q[j][i] = max(q[j + 1][i], q[j][i + 1]) + time_matrix[j][seq_2[i]]

        # Calculate  fij
        for j in range(number_machines):
            for pos in range(len(f[:][0])):
                if j == 0 and pos == 0:
                    f[j][pos] = 0 + time_matrix[j][insert_job]

                elif j == 0 and pos != 0:
                    f[j][pos] = e[j][pos-1] + time_matrix[j][insert_job]

                elif pos == 0 and j != 0:
                    f[j][pos] = f[j-1][pos] + time_matrix[j][insert_job]

                else:
                    f[j][pos] = max(f[j-1][pos], e[j][pos-1]) + time_matrix[j][insert_job]

        #Calculate  Mi
        for pos in range(len(M)):
            M[pos] = -np.inf

            if pos == len(seq_2):
                for j in range(number_machines):
                    if f[j][pos] > M[pos]:
                        M[pos] = f[j][pos]
            else:
                for j in range(number_machines):
                    if f[j][pos] + q[j][pos] > M[pos]:
                        M[pos] = f[j][pos] + q[j][pos]

        best_pos = np.argmin(M)
        best_sequence.insert(best_pos, insert_job)

    best_makespan = makespan_taillard(best_sequence, number_machines, time_matrix)

    if show == True:
        print("Sequence Obtained by the NEHT Heuristic: ", best_sequence)
        print("Makespan Obtained by the NEHT Heuristic = ", best_makespan)

    else:
        pass

    return best_sequence, best_makespan
