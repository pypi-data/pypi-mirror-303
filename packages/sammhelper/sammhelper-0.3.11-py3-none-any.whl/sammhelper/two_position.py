def two_position(x, y, xlimit, ylimit):

    """
    Checks if the measured element is within its setpoints and if needed it
    adjusts the control element in order to meet this requirement. The output 
    values of the control element are in the range of its setpoints.
    
    For example: Is the oxygen concentration above xmin and below xmax?
    If no, change the aeration rate to low/OFF or high/ON in order to meet this
    requirement. 

    Args:
        x (float, optional): Measured element (for example: oxygen concentration).
        y (float, optional): Control element (for example: aeration rate).
        xmin (int, optional): Lower setpoint for measured element (for example: lower limit of oxygen concentration).
        xmax (int, optional): Upper setpoint for measured element (for example: upper limit of oxygen concentration).
        ymin (int, optional): Lower setpoint for control element (for example: low aeration rate or OFF).
        ymax (int, optional): Upper setpoint for control element (for example: high aeration rate or ON).

    Returns:
        y (float, optional): Adjusted values of the control element.
    """

    if x > xlimit[-1]:
        y = ylimit[-1]
    elif x < xlimit[0]:
        y = ylimit[0]

    return y