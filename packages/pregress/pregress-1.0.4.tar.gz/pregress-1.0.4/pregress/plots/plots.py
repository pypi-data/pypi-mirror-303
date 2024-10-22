from pregress.modeling.parse_formula import parse_formula
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plots(formula, data=None, xcolor="blue", ycolor="red", lines=False, linescolor = "black", subplot=None):
    """
    Generates and prints a plot of each scatter plot corresponding to all X and Y values.

    Args:
        formula (str): Formula to define the model (dependent ~ independent).
        data (DataFrame, optional): Data frame containing the data.
        xcolor (str, optional): Color of the points in the scatter plot among both x variables.
        ycolor (str, optional): Color of the points in the scatter plot including the y variable.
        lines (bool, optional): Whether or not to include the regression line in each plot.

    Returns:
        None. The function creates and shows a plot.
    """
    # Clear any existing plots
    plt.clf()
    plt.close()

    formula = formula + "+0"
    Y_name, X_names, Y_out, X_out = parse_formula(formula, data)

    # Convert Y_out to a Series if it isn't already
    if isinstance(Y_out, pd.DataFrame):
        Y_out = Y_out.squeeze()

    # Check the number of predictor variables in the model
    if len(X_names) == 1:
        print("The plots function is for multiple predictor variables.")
    else:
        # Combine Y and X data for pairplot
        plot_data = pd.concat([pd.Series(Y_out, name=Y_name), X_out], axis=1)

        # Create the pairplot
        pair_plot = sns.pairplot(plot_data, diag_kind="kde")

        # Customizing scatter plot colors
        for i in range(len(plot_data.columns)):
            for j in range(len(plot_data.columns)):
                if plot_data.columns[i] == Y_name or plot_data.columns[j] == Y_name:
                    for collection in pair_plot.axes[i, j].collections:
                        collection.set_color(ycolor)
                else:
                    for collection in pair_plot.axes[i, j].collections:
                        collection.set_color(xcolor)

        # Customizing the color of the diagonal plots
        for i, ax in enumerate(pair_plot.diag_axes):
            if plot_data.columns[i] == Y_name:
                for collection in ax.collections:
                    collection.set_color(ycolor)
            else:
                for collection in ax.collections:
                    collection.set_color(xcolor)

        # Optionally add regression lines to the scatter plots
        if lines:
            for i in range(len(plot_data.columns)):
                for j in range(len(plot_data.columns)):
                    if i != j:
                        if plot_data.columns[i] == Y_name or plot_data.columns[j] == Y_name:
                            sns.regplot(x=plot_data.columns[j], y=plot_data.columns[i], data=plot_data,
                                        ax=pair_plot.axes[i, j], scatter_kws={'color': ycolor},
                                        line_kws={'color': linescolor}, ci=None, truncate=False)
                        else:
                            sns.regplot(x=plot_data.columns[j], y=plot_data.columns[i], data=plot_data,
                                        ax=pair_plot.axes[i, j], scatter_kws={'color': xcolor},
                                        line_kws={'color': linescolor}, ci=None, truncate=False)

        # Show the plot if subplot is not specified
        if subplot is None:
            plt.show()
            plt.clf()
            plt.close()






