import numpy as np
import plotly.graph_objs as go
from obsidian_format import apply_obsidian_style


def sigmoid(x):
    return 1 / (1+np.exp(-3*x))


sigmoid_x = np.linspace(-3, 3, 1000)
sigmoid_y = sigmoid(sigmoid_x)

x = [-2.5, -2.3, -2.2, -1.8, -1.5, -0.9, -0.8, -0.55, -0.2, 0.5, 0.75, 0.95, 1.1, 1.2, 1.55, 1.6, 2.0, 2.1, 2.23, 2.5, 2.7, -0.75, 0.5]
y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

fig = go.Figure()
fig.add_trace(go.Scattergl(x=sigmoid_x, y=sigmoid_y, line=dict(color='white')))
fig.add_trace(go.Scattergl(x=x, y=y, mode='markers', marker=dict(color='blue')))
fig.update_xaxes(title_text="$\eta$")
fig.update_yaxes(title_text="$P(y=1)$")
fig.update_layout(showlegend=False)

fig = apply_obsidian_style(fig)
fig.write_image(f"./output/power_example_plot.svg")