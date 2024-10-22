import random as rd
import numpy as np
import plotly.graph_objects as go

from pfsp.earliest_time_makespan_calculate import earliest_time_makespan_calculate, earliest_time
from pfsp.validations import validation_time_matrix, validation_nonexists_jobs, validation_duplicated_jobs, validation_missing_job

def colors_generator():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)

    return f"#{r:02x}{g:02x}{b:02x}"

def gantt_chart(number_jobs, number_machines, time_matrix, sequence):
    fig = go.Figure()
    validation_time_matrix(time_matrix, number_jobs, number_machines)
    validation_nonexists_jobs(sequence, number_jobs)
    validation_missing_job(sequence, number_jobs)
    validation_duplicated_jobs(sequence)

    colors = [colors_generator() for _ in range(number_jobs)]

    earliest_completion_time, makespan = earliest_time_makespan_calculate(sequence, time_matrix, number_machines, number_jobs)

    bars= []

    for j in range(number_machines):
        for index, job in enumerate(sequence):
            machine = j + 1
            end_time = earliest_completion_time[j][index] + time_matrix[j][job]
            start_time_job = earliest_completion_time[j][index]

            if index +1 < len(sequence):
                start_time_next_job = earliest_completion_time[j][index+1]
                idle_time = start_time_next_job - end_time

            else:
                idle_time = 0

            bar = go.Bar(
                y=[f'M{machine}'],
                x=[(end_time - start_time_job)],
                base=[start_time_job],
                orientation='h',
                name=f'Job {job}',
                marker=dict(color=colors[index % len(colors)], line=dict(color='rgba(58, 71, 80, 1.0)', width=2)),
                hovertemplate=(f'Job: {job}<br>'
                              f'Processing Time: {round((end_time - start_time_job), 4)}<br>'
                              f'Start Time: {start_time_job}<br>'
                              f'Completion Time: {round(end_time, 4)}<br>'
                              '<extra></extra>')
            )
            bars.append(bar)

            if idle_time > 0:
                idle_bar = go.Bar(
                    y=[f'M{machine}'],
                    x=[idle_time],
                    base=[end_time],
                    orientation='h',
                    name='Idle Time',
                    marker=dict(color='rgba(240, 240, 240, .1)', line=dict(color='rgba(58, 71, 80, 1.0)', width=0)),
                    hovertemplate=f'Idle Time: {idle_time}<br><extra></extra>'
                )
                bars.append(idle_bar)

        max_items_per_line = 60
        lines = []
        for i in range(0, len(sequence), max_items_per_line):
            line = sequence[i:i+max_items_per_line]
            lines.append(', '.join(map(str, line)))

        title_text = '<br>'.join(lines)

        layout = go.Layout(
        title=f'Sequence: [{title_text}]',
        title_font=dict(size=12,
                    color='blue',
                    family='Arial'),
        title_y=0.98,
        xaxis=dict(title='<b>Completion Time</b>',  color="black"),
        yaxis=dict(title='<b>Machines</b>', autorange='reversed', color="black"),
        margin=dict(t=150),
        barmode='stack',
        # width=1600,
        # height=800,
        autosize=True,
        showlegend=False
    )

    fig = go.Figure(data=bars, layout=layout)
    fig.update_layout(paper_bgcolor="white")
    fig.update_layout(legend_traceorder="normal")
    fig.show()
