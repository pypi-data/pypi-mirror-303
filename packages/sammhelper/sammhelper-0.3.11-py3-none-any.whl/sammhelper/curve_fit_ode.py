import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from .sol_ode import sol_ode
from .get_index import get_index

def curve_fit_ode(model,
    var0,
    t,
    xdata,
    ydata,
    param=None,
    param_var0=None,
    guess0=None,
    bounds=None,
    x_ind=-1,
    n_opt = 0
    ):

    """
    Uses non-linear least squares to fit results of ODE (model) to data.

    Args:
        model (callable(y,t,...)): The function computes the derivative of y at t.
        var0 (callable or array): Initial condition of var.
        t (array): A sequence of time points for which to solve for y.
        xdata (array):  The independent variable where the data is measured.
                        Should usually be an M-length sequence or an
                        (k,M)-shaped array for functions with k predictors,
                        but can actually be any object.
        ydata (array): The dependent data, a length M array - nominally f(xdata, ...).                    
        param (array, optional): Parameters used in the ODE model function.
        param_var0 (array, optional): Parameters used in the initial condition function.
        guess0 (array, optional): Initial guess for the parameters (length N). If None,
                                  then the initial values will all be 1 (if the number of
                                  parameters for the function can be determined using
                                  introspection, otherwise a ValueError is raised).
        bounds (2-tuple of array_like, optional): Lower and upper bounds of parameters.
                                                  Defaults to [0.1*guess0, 1.5*guess0].
        x_ind (int, optional): The index of fitted results in the solved list
                               of the model. The default is the last column of
                               the list.
        n_opt (int, optional): For a model of n CSTRs, this defines which CSTR is used for the fitting. Default is the last CSTR.

    Returns:
        avg: Optimal values for the parameters so that the sum of the squared residuals
                of f(xdata, *popt) - ydata is minimized.
        cov: The estimated covariance of avg. The diagonals provide the variance of the
                parameter estimate.
    """
    
    if isinstance(param, int) | isinstance(param, float):
        param = [param]
    if isinstance(param_var0, int) | isinstance(param_var0, float):
        param_var0 = [param_var0]
    
    if isinstance(ydata, int) | isinstance(ydata, float):
        ydata = np.array([ydata] * len(xdata))
    
    if xdata[0] != 0:
        xdata.loc[-1] = 0
        xdata.index = xdata.index + 1
        xdata = xdata.sort_index()
        ydata.loc[-1] = np.nan
        ydata.index = ydata.index + 1
        ydata = ydata.sort_index()
                         
    if callable(var0):
        df = sol_ode(model, var0(param_var0), t, param)
    else: df = sol_ode(model, var0, t, param)
        
    if isinstance(df,list):
        C = df[x_ind]
        if isinstance(C,np.ndarray):
            if C.ndim > 1:
                C = df[x_ind][:,n_opt-1]
            else: pass
        else: pass
    elif isinstance(df,np.ndarray):
        if df.ndim > 1:
            C = df[:,n_opt-1]
        else: C = df
    else: raise('Output of the model must be list or array.')

    plt.figure('curve fit')
    plt.grid()
    plt.plot(xdata, ydata, 'o', markersize = 3)
    plt.plot(t,C,color='black')
    
    # set the default bounds
    if (bounds == None) & (guess0 != None):
        bounds = np.empty([2, len(guess0)])
        for i in range(len(guess0)):
            if guess0[i] > 0:
                bounds[0][i] = -3 * guess0[i]
                bounds[1][i] = 3 * guess0[i]
            elif guess0[i] == 0:
                bounds[0][i] = -np.inf
                bounds[1][i] = np.inf
            else:
                bounds[0][i] = 3 * guess0[i]
                bounds[1][i] = -3 * guess0[i]

    # identify the index of initial condition's parameters in input guess0
    try:
        p0, p0_converse = get_index(param_var0, guess0)
    except:
        pass

    # identify the index of ode function's parameters in input guess0
    try:
        p1, p1_converse = get_index(param, guess0)
    except:
        pass

    # create the fitted function, changing the parameter to making the ode
    # function solved results fitting the input data
    def func(xdata, *args):

        # change the parameter in the ode function
        param_new = param
        for i in range(len(p1)):
            param_new[p1_converse[i]] = args[p1[i]]

        if callable(var0):
            # change the parameter in the initial condition
            param_var0_new = param_var0
            for i in range(len(p0)):
                param_var0_new[p0_converse[i]] = args[p0[i]]
            # solve the ode function
            results = sol_ode(model, var0(param_var0_new), xdata, param_new)
        else:
            results = sol_ode(model, var0, xdata, param_new)

        # return the solved result
        if isinstance(results,list):
            ar = results[x_ind]
            if isinstance(ar,np.ndarray):
                if ar.ndim > 1:
                    return ar[:,n_opt-1][~np.isnan(ydata)]
                else: return ar[~np.isnan(ydata)]
            else: return ar[~np.isnan(ydata)]
        elif isinstance(results,np.ndarray):
            if results.ndim > 1:
                return results[:,n_opt-1][~np.isnan(ydata)]
            else: return results[~np.isnan(ydata)]
        else: raise('Output of the model must be list or array.')
        
        
    avg, cov = sp.optimize.curve_fit(func, xdata, ydata[~np.isnan(ydata)], p0=guess0, bounds=bounds)
    if callable(var0):
         df = sol_ode(model, var0(param_var0), t, param)
    else:
         df = sol_ode(model, var0, t, param)
    
        
    if isinstance(df,list):
        Cnew = df[x_ind]
        if isinstance(Cnew,np.ndarray):
            if Cnew.ndim > 1:
                Cnew = df[x_ind][:,n_opt-1]
            else: pass
        else: pass
    elif isinstance(df,np.ndarray):
        if df.ndim > 1:
            Cnew = df[:,n_opt-1]
        else: Cnew = df
    else: raise('Output of the model must be list or array.')
        
    plt.figure('curve fit')
    plt.plot(t,Cnew,color='red',linestyle='dashed')
    plt.legend(["measured data","model","fitted model"])
    
    print("Original vs fitted average values:", guess0, avg)
    std = np.sqrt(np.diag(cov))
    print("Standard deviation of estimated parameters:", std)
    
    return avg, cov