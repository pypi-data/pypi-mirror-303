import csv
import sys

def read_txt(file):
    with open(file, 'r') as file:
        first_line = file.readline().split()
        number_jobs, number_machines = map(int, first_line[:2])
        time_matrix = [list(map(float, linha.split())) for linha in file]

    return number_jobs, number_machines, time_matrix

def read_csv(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        time_matrix = []
        for row in reader:
            time_matrix.append([float(x) for x in row if x])

        if len(time_matrix) == 0 or len(time_matrix) < 0 or len(time_matrix[0]) == 0 or len(time_matrix[0]) < 0:
            print("Erro!You array is incorrect!")
            sys.exit()
        else:
            number_jobs = len(time_matrix[0])
            number_machines = len(time_matrix)

    return number_jobs, number_machines, time_matrix
