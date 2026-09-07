import plotly.graph_objs as go
from plotly.subplots import make_subplots
from scipy.stats import norm
import numpy as np
from obsidian_format import apply_obsidian_style

x = np.linspace(-5, 5, 5000)
y_H0 = norm.pdf(x, loc=0, scale=1)
y_H1 = norm.pdf(x, loc=2, scale=1)

c_value = 1.5  # Critical Value

mask = x > c_value

x_alpha = x[mask]
y_alpha = y_H0[mask]

x_beta = x[~mask]
y_beta = y_H1[~mask]

x_power = x[mask]
y_power = y_H1[mask]


fig = make_subplots(rows=2, cols=1, subplot_titles=(r"Distribution of estimator under Null Hypothesis",
                                                    r"Distribution of estimator under Alternate Hypothesis"))

fig.add_trace(go.Scattergl(x=x, y=y_H0, name=r"$\hat \theta | H_0$",
                           line=dict(color='white'), showlegend=False),
              row=1, col=1)
fig.add_trace(go.Scattergl(x=x, y=y_H1, name=r"$\hat \theta | H_1$",
                           line=dict(color='white'), showlegend=False),
              row=2, col=1)

fig.add_vline(x=c_value, line_dash="dash", line_color="white", row=1, col=1)
fig.add_vline(x=c_value, line_dash="dash", line_color="white", row=2, col=1)

fig.add_trace(go.Scattergl(x=x_alpha, y=y_alpha,
                           line=dict(color='white'),
                           fill='tozeroy', fillcolor='blue',
                           name=r'$\alpha$'),
              row=1, col=1)
fig.add_trace(go.Scattergl(x=x_beta, y=y_beta,
                           line=dict(color='white'),
                           fill='tozeroy', fillcolor='orange',
                           name=r'$\beta$'),
              row=2, col=1)
fig.add_trace(go.Scattergl(x=x_power, y=y_power,
                           line=dict(color='white'),
                           fill='tozeroy', fillcolor='red',
                           name=r'Power'),
              row=2, col=1)

fig.update_xaxes(tickmode='array', tickvals=[0, c_value],
                 ticktext=[r'$\theta_0$', r'$cv$'], tickfont_size=20,
                 row=1, col=1)
fig.update_xaxes(tickmode='array', tickvals=[2, c_value],
                 ticktext=[r'$\theta$', r'$cv$'], tickfont_size=20,
                 row=2, col=1)

fig.update_yaxes(showticklabels=False, row=1, col=1)
fig.update_yaxes(showticklabels=False, row=2, col=1)

fig = apply_obsidian_style(fig, width=1000, height=500)
fig.write_image("./output/power_visualization.svg")

