import numpy as np
import scipy as sp
import pandas as pd

def fft(data):

    """
    Computes the 1-D discrete Fourier Transformation. 
    
    Args:
        data (dataframe or list): The dataframe or list with two columns, first: time, second: value.
    
    Returns:
        frq (array): x-axis (= frequency) of the descrete frequency spectrum. 
        amp (array): y-axis (= amplitude) of the descrete frequency spectrum. 
    """

    # acess data frame or list. Raise error if neither is given.
    if isinstance(data,pd.DataFrame):
        x = data.iloc[:, 0]
        y = data.iloc[:, 1]
    elif isinstance(data, list):
        x = data[0]
        y = data[1]
    else: raise Exception('Possible input: pd.DataFrame or list')
    
    # sampling interval
    si = np.median(np.diff(x))
    
    # sampling frequency
    sf = 1/si
    
    # frequencies (x-axis)
    N = len(y)
    k = np.arange(int(N/2))
    p  = N/sf
    frq = k/p
    
    # amplitude (y-axis)
    amp = sp.fft.fft(np.array(y))
    
    # normalize amplitude
    amp = abs(amp/len(y)*2)
    amp[0] = amp[0]/2
    
    # exclude sampling frequency from amplitude
    amp = amp[range(int(len(y)/2))]
    
    # output
    return frq, amp