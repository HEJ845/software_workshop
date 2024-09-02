import numpy as nmp

def frequency_calculation(lamda):
    """
    Calculate the frequency based on the equation
    frequency = 1/(2pi) * sqrt(x)
    """
    pi = nmp.pi
   
    # calculate the frequency using the function defined above
    frequency = 1/(pi) * nmp.sqrt(lamda)

    return frequency


