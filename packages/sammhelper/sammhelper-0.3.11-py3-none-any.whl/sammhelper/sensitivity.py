import matplotlib.pyplot as plt
import numpy as np
from .sol_ode import sol_ode
from .get_index import get_index
from matplotlib.ticker import MaxNLocator

def sensitivity(var, xlabel="time", model=None, var0=None, t =None, param=None, param_var0=None, x_ind = -1, linestyle='solid'):
    
    """
    Computes the absolute-relative sensitivity of the results of the model 
    to a changing parameter. Runs the model with all parameters at their 
    specified value and gets the results R1(t). Adjusts the parameter slightly 
    by adding an amount ∆ equal to 0.0001*specified value. Runs the model again, 
    calling the results R2(t). Computes the absolute-relative sensitivity S(t) 
    by the following formula: S(t) = (R2(t) - R1(t)) / ∆

    Args:
        par (float): Specified value of the parameter.
        xlabel (str): Identify the xlabel of results. 
                      There are two options: time or length. 
                      Time means results changing with time. 
                      Length means results changing along the series of reactors.
        model (callable(y,t,...)): The function computes the derivative of y at t.
        var0 (array): Initial condition of y.
        t (array): A sequence of time points for which to solve for y.
        param (array, optional): Parameters used in the model.
        param_var0 (array, optional): Parameters used in the initial condition function.
        x_ind (integer, optional): Index of the model output for the case of several outputs (e.g. X,S). Default is -1.

    Returns:
        array: Absolute-relative sensitivity of the results of the model to a changing parameter.
    """
    
    # Set up the line style based on plot count
    line_styles = ['solid', 'dashed', 'dashdot', 'dotted']
    
    if isinstance(param, int) | isinstance(param, float):
        param = [param]
    if isinstance(param_var0, int) | isinstance(param_var0, float):
        param_var0 = [param_var0]
    
    if param_var0 != None:

        # solve the ode function using the initial input parameter
        C = sol_ode(model, var0(param_var0), t, param)

        # times the parameter with 1.0001
        param_var0_new = param_var0
        param_new = param
        if var in param_var0:
            index = get_index(var, param_var0)
            param_var0_new[index[0]] = 1.0001 * var
        if var in param:
            index = get_index(var, param)
            param_new[index[0]] = 1.0001 * var

        # solve the ode function using the changed parameter
        C_sens = sol_ode(model, var0(param_var0_new), t, param_new)
    else:
        # solve the ode function using the initial input parameter
        C = sol_ode(model, var0, t, param)

        # times the parameter with 1.0001
        param_new = param

        if var in param:
            index = get_index(var, param)
            param_new[index[0]] = 1.0001 * var

        # solve the ode function using the changed parameter
        C_sens = sol_ode(model, var0, t, param_new)
    # calculate the sensitivity of the parameter along the time or length
    if xlabel == "time":
        if var == 0:
            try:
                result = var*(C_sens - C) / (0.0001)
            except:
                result = var*(C_sens[x_ind]- C[x_ind])/(0.0001)
        else:
            try:
                result = var*(C_sens - C) / (0.0001 * var)
            except:
                result = var*(C_sens[x_ind]- C[x_ind])/(0.0001 * var)        
        # plot the results
        plt.figure('sensitivity')
        plt.grid()
        try:
            plt.plot(t,result[:,-1], linestyle = linestyle)
        except:
            plt.plot(t,result, linestyle = linestyle)
        
        return result
    
    elif xlabel == "length":
        if var == 0: 
            result = var * (np.array([arr[-1] for arr in C_sens]) - np.array([arr[-1] for arr in C])) / 0.0001
        else:
            result = var * (np.array([arr[-1] for arr in C_sens]) - np.array([arr[-1] for arr in C])) / (0.0001 * var)
        
        # plot the results
        plt.figure('sensitivity')
        plt.plot(range(1,len(result)+1), result, linestyle = linestyle)
        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.xlim(xmin=1, xmax=len(result)+1)
          
        return result