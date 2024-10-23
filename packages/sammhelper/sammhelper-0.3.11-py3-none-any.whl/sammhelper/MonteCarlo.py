import numpy as np
import tqdm as tq
from .sol_ode import sol_ode
from .len_check import len_check
from .fill_array import fill_array

def MonteCarlo(
    model, var0, t, param=None, param_var0=None, x_ind = -1
):
    
    """
    Runs your model multiple times while varying the specified parameters.

    Args:
        model (callable(y,t,...)): The function computes the derivative of y at t.
        var0 (array): Initial condition of y.
        t (array):  A sequence of time points for which to solve for y.
        param (array, optional): Parameters used in the ODE model function.
        param_var0 (array, optional): Parameters used in the initial condition function.
        
    Returns:
        avg, std (float): Mean and standard deviation value of the all results.
        results (list): This list contains all results.
    """

    print("Start Monte Carlo simulation...")
    
    # check whether the input values for p_func, p_y0 are used for one parameter or multiple parameters
    if np.any(
        isinstance(param, (list, tuple, np.ndarray))
    ):
        var2 = np.array(param, dtype=object)  # input is a 2d array
    else:
        var2 = np.array([param], dtype=object).reshape(1, -1)  # input is a 1d array

    runs = len_check(var2)
    results = list(range(runs))

    if param_var0 != None:
        if np.any(
            isinstance(param_var0, (list, tuple, np.ndarray))
        ):
            var1 = np.array(param_var0, dtype=object)
        else:
            var1 = np.array([param_var0], dtype=object).reshape(1, -1)

        # get the numbers of runs
        runs = max(len_check(var1), len_check(var2))

        # fill the array using the runs number
        var1 = fill_array(var1, runs)

    var2 = fill_array(var2, runs)

    # different tqdm bars

    for i in tq.tqdm(range(runs)):
        var_func = [item[i] for item in var2]
        if param_var0 != None:
            var_y0 = [item[i] for item in var1]
            ydata = sol_ode(model, var0(var_y0), t, var_func)
        else:
            ydata = sol_ode(model, var0, t, var_func)
        # Workarounds for different TYPES and SIZES for ydata
        # Example 1: Exercise 08 --> TYPE list SIZE 2 --> second condition
        # Example 2: Book example 12.18 --> TYPE array SIZE (m, n) --> fourth condition
        # Example 3: Book example 12.22 --> TYPE list SIZE 1 --> first condition
        if isinstance(ydata, list) and ydata[x_ind].ndim == 1:
            results[i] = ydata[x_ind][:]
        elif isinstance(ydata, list) and ydata[x_ind].ndim > 1:
            results[i] = ydata[x_ind][:,-1]
        elif isinstance(ydata, np.ndarray) and ydata.ndim == 1:
            results[i] = ydata[:]
        else:
            results[i] = ydata[:,-1]
            
    mean = np.mean(results,0)
    stddev = np.std(results,0,ddof=1)

    return results, mean, stddev