Below is the code used to apply the plot style used for a bunch of plots in these notes:

``` python
import plotly.graph_objects as go

def apply_obsidian_style_square(fig, size=500):
    """
    Applies dark-mode transparency and a square aspect ratio.
    """
    fig.update_layout(
        template="plotly_dark",
        # Force square dimensions
        width=size,
        height=size,
        autosize=False,
        
        # Transparency
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        
        # Font & Style
        font=dict(family="Inter, sans-serif", color="#e0e0e0"),
        
        # Symmetrical margins for the square look
        margin=dict(l=40, r=40, t=60, b=40),
        
        # Grid lines
        xaxis=dict(gridcolor='#333333', zerolinecolor='#444444'),
        yaxis=dict(gridcolor='#333333', zerolinecolor='#444444'),
    )
    return fig
    
# --- Example Usage ---
fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[1, 3, 2]))
fig.add_trace(go.Scatter(x=[4, 6, 7], y=[3, 3, 5]))
fig = apply_obsidian_style_square(fig, size=500)
fig.write_image("stats_plot.svg")
```