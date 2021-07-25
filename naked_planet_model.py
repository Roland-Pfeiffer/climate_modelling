#!/usr/bin/env python3

import logging
import matplotlib.pyplot as plt
from matplotlib import text
import numpy as np

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s]\t%(message)s')
logging.disable()


def npm(resolution_yrs, steps, water_depth_m, albedo=0.3, L=1350, sigma=5.67E-8, epsilon=1) -> (list, list, list):
    """ Calculates the temperature (K) and emitted energy (J m⁻² s⁻¹) for each time step.

    :param resolution_yrs: time step value of the model.
    :param steps: number of steps calculate.
    :param water_depth_m: Water depth in meters.
    :param L: Incoming radiation from the sun in Watts per m2
    :param albedo:
    :param sigma: Stefan Boltzman constant (5.67E-8) (W/m² K⁴)
    :param epsilon: Blackbody property of the planet
    :return: time steps, temperature (K), emission (J m⁻² s⁻¹)
    """

    heat_capacity = water_depth_m * 4.0E6          # J/K m²: Joules it takes to warm 1 m² by 1 K.
    energy_in = L * (1 - albedo) / 4     # in (W / m2)
    seconds_per_year = 3600 * 24 * 365
    seconds_per_step = seconds_per_year * resolution_yrs
    time_steps_x = [0]

    # Initial values
    temp_K = [0]
    energy_out = [0]
    _heat_content = [0]

    for step in range(steps):
        _heat_difference = (energy_in - energy_out[-1]) * seconds_per_step
        _heat_content.append(_heat_content[-1] + _heat_difference)
        _temp_new = _heat_content[-1] / heat_capacity
        logging.debug(f'New temp.: {_temp_new:.3f} K.')
        temp_K.append(_temp_new)
        energy_out.append(sigma * epsilon * temp_K[-1]**4)
        time_steps_x.append(resolution_yrs * (step + 1))

    return time_steps_x, temp_K, energy_out


if __name__ == '__main__':
    model_params = {
        'resolution_yrs': 5,
        'steps': 125,
        'water_depth_m': 1000
    }

    x, y, energy_out = npm(**model_params)

    parameter_printout = 'MODEL PARAMETERS:\n'
    for i, (key, value) in enumerate(model_params.items()):
        parameter_printout = parameter_printout + str(f'{key}: {value}\n')

    fig, ax = plt.subplots()
    ax.plot(x, y, label='Temperature (K)')
    ax.plot(x, energy_out, label='Energy out (J m⁻² s⁻¹)')
    ax.set_title('Temperature and energy output over time')
    ax.set_xlabel('Years')
    ax.set_ylabel('Energy output (J m⁻² s⁻¹)\nTemperature (K.)')
    ax.grid()
    ax.text(x=0.6, y=0.6, s=parameter_printout, transform=ax.transAxes)  # transAxes uses coords as % of axes
    ax.legend()
    plt.show()
