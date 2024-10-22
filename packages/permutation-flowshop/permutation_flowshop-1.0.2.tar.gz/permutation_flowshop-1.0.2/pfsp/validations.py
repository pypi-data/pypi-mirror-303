import numpy as np
import collections
import sys

def validation_time_matrix(time_matrix, number_jobs, number_machines):
    for row in time_matrix:
        for element in row:
            if element < 0:
                print("Error! Your time array has one or more negative elements!")
                sys.exit()

            elif number_jobs != len(row) or number_machines != len(time_matrix):
                print(f"Error! Dimension mismatch! A matrix with ({number_machines} machines, {number_jobs} jobs) was expected, but a matrix with ({len(time_matrix)} machines, {len(row)} jobs) was received.")
                sys.exit()

            else:
                pass

def validation_nonexists_jobs(sequence, number_jobs):
    for i in sequence:
        if i > number_jobs-1:
            print("Error! Your sequence has one or more jobs non-existent!")
            sys.exit()
        elif i < 0:
            print("Error! Negative jobs do not exist!")
            sys.exit()

def validation_duplicated_jobs(sequence):
    if len(sequence) != len(set(sequence)):
        print("Error! Your sequence has one or more duplicated jobs!")
        sys.exit()

def validation_missing_job(sequence, number_jobs):
    if len(sequence)<number_jobs:
        print("Error! Your sequence has one or more missing jobs!")
        sys.exit()
