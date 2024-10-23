from math import log, pi
import numpy as np

def FF_to_conc(ff, volume, concentration):
    return_list = []
    for i in ff:
        if 0 < i < 1:  # Ensure that 1 - i is positive
            result = -np.log(1 - i) / (volume * concentration)  # Use np.log for logarithm
            return_list.append(result)
        else:
            return_list.append(float('nan'))  # Append NaN for invalid values
    return return_list

def FF_to_volume(ff, diameter, volume, concentration):
    return_list = []
    for i in ff:
        if 0 < i < 1:  # Ensure that 1 - i is positive
            return_list.append(-log(1 - i) / (volume * concentration * (4/3) * pi * ((diameter/2) ** 3)))
        else:
            return_list.append(float('nan'))  # Append NaN for invalid values
    return return_list

def FF_to_surface(ff, diameter, volume, concentration):
    return_list = []
    for i in ff:
        if 0 < i < 1:  # Ensure that 1 - i is positive
            return_list.append(-log(1 - i) / (volume * concentration * 4 * pi * ((diameter / 2) ** 2)))
        else:
            return_list.append(float('nan'))  # Append NaN for invalid values
    return return_list
