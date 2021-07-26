#!/usr/bin/env python3

def energy_IN_Wm2(L=1350, albedo=0.3, sphere=True) -> float:
    """Calculates the average incoming energy (W m⁻²), by default for a sphere that receives light from one side.
    :param L: Solar constant (in W/m²)
    :param albedo: Albedo
    :return: incoming energy (W m⁻²")
    """
    emission_sphere = (L * (1 - albedo)) / 4
    if sphere:
        return emission_sphere
    else:
        return emission_sphere * 4


def calc_equilibrium_temp(L, albedo, sigma=5.670374419E-8, epsilon=1):
    """
    Gives the equilibrium temperature (K) base don the incoming radiation, the albedo, sigma and the BB properties.
    :param L: Solar constant (or incoming light in W m⁻²)
    :type L: int
    :param albedo: Amount of incoming light reflected (0-1)
    :type albedo: float
    :param sigma: Stefan Boltzmann constant 5.670374419e-8
    :type sigma:
    :param epsilon: Emissive term (0-1). 1 for perfect black bodies.
    :type epsilon: Union(float, int)
    :return: Returns the emission temperature in K.
    :rtype:
    """
    t_K = ((L * (1 - albedo)) / (4 * epsilon * sigma)) ** 0.25
    return t_K


def energy_OUT_Wm2(T, epsilon=1, sigma=5.670374419E-8) -> float:
    """
    Returns the emission of a sphere of temperature T (K) in Watts per m² surface.
    :param T: Temperature (K)
    :param epsilon: emissive termn (1 for perfect blackbodies)
    :param sigma: Stefan Boltzmann constant (W / (m² K⁴))
    :return: Emission (W m⁻²)
    """
    return sigma * epsilon * (T ** 4)


def calc_temp_K(energy_Wm2, epsilon=1, sigma=5.670374419E-8) -> float:
    """
    Calculates the equilibrium temperature (K) based on the energy flow.
    :param energy_Wm2:
    :type energy_Wm2:
    :param epsilon:
    :type epsilon:
    :param sigma:
    :type sigma:
    :return:
    :rtype:
    """
    T = (energy_Wm2 / (sigma * epsilon)) ** 0.25
    return T


def multilayer_model(L, albedo, layers, epsilon=1, sigma=5.670374419E-8):
    T_skin = 0
    T_middle_layers = []
    T_ground = 0
    T_current = 0
    T_previous = 0

    T_skin = calc_temp_K(energy_IN_Wm2(L, albedo), epsilon=epsilon, sigma=sigma)
    if layers == 0:
        T_ground = T_skin
    else:
        T_previous = T_skin
        for i in range(layers):
            # Intermediate layers
            if i < (layers - 1):
                T_current = calc_temp_K(2 * energy_OUT_Wm2(T_previous))
                T_middle_layers.append(T_current)
                T_previous = T_current
            # Ground layer:
            else:
                T_current = calc_temp_K(energy_IN_Wm2(L, albedo=albedo) + energy_OUT_Wm2(T_previous))
                T_ground = T_current

    return T_skin, T_middle_layers, T_ground



if __name__ == '__main__':
    planets = {'Venus': {'L': 2600, 'albedo': 0.7},
               'Earth': {'L': 1350, 'albedo': 0.3},
               'Mars': {'L': 600, 'albedo': 0.15}}
    sigma = 5.670374419E-8

    for planet, values in planets.items():
        L = values['L']
        albedo = values['albedo']
        print(f'{planet}:\t T: {calc_temp_K(energy_IN_Wm2(L, albedo))}')

    T_L2 = calc_temp_K(energy_IN_Wm2())
    T_L1 = (2 * T_L2 ** 4) ** 0.25
    print(f'L2: {T_L2}')
    print(f'L1: {T_L1}')
    TG = (energy_IN_Wm2() / sigma + T_L1 ** 4) ** 0.25
    print(f'Ground: {TG}')
    print(f'Diff. L2/L1: {T_L2 - T_L1}')


    L2 = calc_equilibrium_temp(1350, 0.3)
    L1 = calc_temp_K(energy_IN_Wm2())
    print(L1)

    skin, intermediate, ground = multilayer_model(1350, 0.3, 2)
    print(skin, intermediate, ground)