import numpy as np

def delay(time, var, delay, value = 0):

    """
    This function returns a sequence of values shifted by the delay value.

    Args:
        time (array): A sequence of time points.
        var (array): A sequence of values.
        delay (float): Specified delay time.
        value (float, optional): Specified value for var for the time before the delay time. 
        
    Returns:
        var_delayed (array): Returns a sequence of values delayed by the delay time with the same length as the time vector.
    """
    
    DT = time[1]-time[0]
    i_delay = int(round(delay/DT))
    if np.ndim(var)!= 1: var = var[:,-1]
    else: pass
    
    var_delayed = np.zeros(len(var))
    var_delayed[0:i_delay] = value
    var_delayed[i_delay:] = var[0:-i_delay]
    
    return var_delayed