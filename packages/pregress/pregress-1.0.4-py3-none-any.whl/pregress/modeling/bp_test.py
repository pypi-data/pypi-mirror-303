import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan

def bp_test(model, out=True):
    """
    Perform the Breusch-Pagan test for heteroscedasticity on a given statsmodels regression results object.

    Args:
        model (statsmodels.regression.linear_model.RegressionResultsWrapper): A fitted statsmodels regression model.
        out (bool): If True, prints the test details.

    Returns:
        float: The p-value of the Breusch-Pagan test.
    """
    # Perform the Breusch-Pagan test
    bp_test = het_breuschpagan(model.resid, model.model.exog)
    
    # Extract the test statistic and p-value
    bp_test_statistic, bp_test_p_value, _, _ = bp_test

    # Determine if the model is heteroscedastic or homoscedastic
    if bp_test_p_value < 0.05:
        result = 'Heteroscedastic (p < 0.05)'
    else:
        result = 'Homoscedastic (p >= 0.05)'

    # Optionally print the details
    if out:
        print("Breusch-Pagan Test for Heteroscedasticity")
        print("========================================")
        print(f"Test Statistic : {bp_test_statistic:.4f}")
        print(f"P-value        : {bp_test_p_value:.4g}")
        print(f"Result         : {result}")
        print("========================================")

    # Return the p-value
    return bp_test_p_value

