import numpy as np
import tqdm as tq

from .sol_ode import sol_ode
from .delay import delay

def PID_controller(model, var0, t, param, ylimit, w, y0 = 0, PID = [0,0,0], Tt = 0, x_ind = -1, y_ind = -1, n = 1, n_meas = 0):

    """
    Creates a PID controller to adjust the control member y of the input ODE function,
    calculates the controlled variable x using the adjusted parameters.

    Args:
        model (callable(y,t,...)): The function computes the derivative of y at t.
        var0 (array): Initial condition of var.
        t (array): A sequence of time points for which to solve for y.
        param (array, optional): Input parameters to model function.           
        ylimit (array, optional): Lower and upper setpoint for controlled member y (actuator).               
        w (float or int, optional): The setpoint w of the controlled variable x.
        y0 (int, optional): First value of the controlled member y (actuator). Default is 0.
        PID (array, optional): Parameter of the PID controller [KP,KI,KD]. Default is 0.
        Tt (float, optional): Specified dead time.

        x_ind (int, optional): Index of the controlled element x in var0. Default is -1.
        y_ind (int, optional): Index of control member y in param. Default is -1.
        
        n (int, optional): For a cascade of CSTRS, number of total CSTRs n. Default is 1.
        n_meas (int,optional): The reactor in which the controlled variable x measured. Default is the last reactor.

    Returns:
        results: The solved differential equation using the controller.
        y_final: The log of the adjusted control member y.
        e_final: The log of the offset.
    """

#    warnings.filterwarnings("ignore")


    # create the y value list with initial value.
    y = y0
    y_final = np.zeros(len(t))
    x = np.zeros(len(t)-1)
    e_final = np.zeros(len(t))
    e = w
    KP, KI, KD = PID
    Int_e = 0
    
    # empty dataframe for saving results
    results = list(range(len(t)))

    #  store the value calculated from last time.
    for i in tq.tqdm(range(len(t)-1),position=0,leave=True):
        
        y_final[i] = y
        param[y_ind] = y

        #   get the solved results and get the new kla
        df = sol_ode(model, var0, t[i:i+2], param)

        #  from curve_fit_ode: how to handle if there is only one model output?          
        if isinstance(df,list):
            C = df[x_ind]
            if isinstance(C,np.ndarray):
                if C.ndim > 1:
                    C = C[:,-1]
        elif isinstance(df,np.ndarray):
            if df.ndim > 1:
                C = df[:,-1]
            else: 
                C = df
        else: 
            raise('Output of the model must be list or array.')

        # save the solved results, drop the duplicated value with the same time index,
        # only keeping the last one.
        
        if n == 1:
            results[i] = np.transpose(df)[-1]
            var0 = np.transpose(df)[-1]
            x[i] = df[x_ind][-1]
        else:
            results[i] =np.array(df)[:,-1]
            var0 = np.array(df)[:,-1]
            x[i] = df[x_ind][-1,n_meas-1]
            
        
        if Tt != 0:
            x_delay = delay(t, x, Tt, value = 0)

        else:
            x_delay = x

        e_temp = w - x_delay[i]
        # D component
        D = KD * (e - e_temp) / (t[i+1]-t[i])
        # P component
        e = e_temp
        e_final[i] = e_temp
        P = KP * e
        if y<ylimit[1] and y>ylimit[0]:
            Int_e = Int_e + e *(t[i+1]-t[i])
        else: Int_e = Int_e + 0

        # I component
        I = KI*Int_e

        y = y0 + P + I - D
        y = max(min(y, ylimit[1]), ylimit[0])
        
    results[len(t)-1] = results[len(t)-2]
    e_final[len(t)-1] = e_final[len(t)-2]
    y_final[len(t)-1] = y_final[len(t)-2]
    
    if n != 1: 
        r = np.array(results)
        results = r.transpose(1,0,2)
    else: results = np.transpose(results)
    return results, y_final, e_final