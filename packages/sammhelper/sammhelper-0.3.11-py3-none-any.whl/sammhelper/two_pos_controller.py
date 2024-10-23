import numpy as np
import tqdm as tq

from .sol_ode import sol_ode
from .delay import delay
from .two_position import two_position

def two_pos_controller(model, var0, t, param, Tt, xlimit, ylimit, x_ind=-1, y_ind=-1, n=1, n_meas=0):
    """
    Creates a two position controller to adjust the parameters of the input ODE function,
    calculates the controlled variable x with the adjusted parameters.

    Args:
        model (callable(y,t,...)): The function computes the derivative of y at t.
        time (array): A sequence of time points for which to solve for y.
        xlimit (list): Setpoints for controlled variable x.
        ylimit (list): Setpoints for control member y (actuator).
        Tt (float): Specified dead time.
        
        x_ind (int, optional): Index of the controlled element x in var0. Default is -1.
        y_ind (int, optional): Index of control member y in param. Default is -1.
        
        n (int, optional): For a cascade of CSTRS, number of total CSTRs n. Default is 1.
        n_meas (int, optional): The reactor in which the controlled variable x is measured. Default is the last reactor.
    
    Returns:
        results: The solved differential equation using the controller.
        y_final: The log of the adjusted control member y.
    """
    
    # Initialize y value and other variables
    y = ylimit[0]
    y_final = np.zeros(len(t))
    x = np.zeros(len(t))

    # Empty list for saving results
    results = []

    for i in tq.tqdm(range(len(t)-1), position=0, leave=True):
        y_final[i] = y
        param[y_ind] = y

        # Solve ODE for the current time step
        df = sol_ode(model, var0, t[i:i+2], param)
        
        # Handle multiple outputs or single output from the ODE model
        if isinstance(df, list) or isinstance(df, tuple):
            # Multiple outputs
            results.append(np.array(df)[:,-1])
            var0 = np.array(df)[:,-1]
            x[i] = df[x_ind][-1, n_meas-1] if n != 1 else df[x_ind][-1]
        else:
            # Single output
            results.append(df[-1])
            var0 = df[-1]
            x[i] = df[-1]

        # Apply delay if necessary
        if Tt != 0:
            x_delay = delay(t, x, Tt, value=0)
        else:
            x_delay = x

        # Apply two-position controller
        y = two_position(x_delay[i], y, xlimit, ylimit)
    
    y_final[-1] = y_final[-2]
    results.append(results[-1])
    
    if n != 1:
        r = np.array(results)
        results = r.transpose(1, 0, 2)
    else:
        results = np.array(results)

    # Get the number of columns
    n_cols = results.shape[1]

    # Transforming to a list with n entries, each being a list of a column
    if n_cols > 1: 
        results = [results[:, i].tolist() for i in range(n_cols)]

    return results, y_final


