import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
from statsmodels.graphics.gofplots import ProbPlot

def plot_cook(model, threshold=0.5, subplot=None):
    """
    Plots Cook's Distance for each observation in a fitted statsmodels regression model to identify influential points.

    Args:
        model (statsmodels.regression.linear_model.RegressionResultsWrapper): A fitted statsmodels regression model.
        threshold (float, optional): The threshold for Cook's Distance to highlight influential points. Default is 0.5.

    Returns:
        None. Displays a plot of Cook's Distance for each observation.
    """
    # Calculate Cook's Distance
    influence = model.get_influence()
    cooks_d = influence.cooks_distance[0]

    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 6)) if subplot is None else subplot
    ax.stem(np.arange(len(cooks_d)), cooks_d, markerfmt=",")
    ax.set_xlabel('Observation Index')
    ax.set_ylabel("Cook's Distance")
    ax.set_title("Cook's Distance Plot")

    # Adding a reference line for the specified threshold
    ax.axhline(y=threshold, linestyle='--', color='red', label=f'Influence threshold ({threshold})')
    ax.legend()

    # Show the plot if subplot is not specified
    if subplot is None:
        plt.show()
        plt.clf()
        plt.close()

