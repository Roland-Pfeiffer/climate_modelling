import math

sigma = 5.67E-8
boltzmann_constant = 1.380649E-23


print("\nGW1 W3 Moon's equilibrium temperature at noon")
albedo = 0.33
moon_radius_m = 1736000
L = 1350
heat_in = (L * (1 - albedo))
temp_moon_noon = (heat_in / sigma) ** 0.25
print(f'Temp. moon at noon: {temp_moon_noon} K.')

print("\nGW1 W3 Moon's equilibrium temperature at night")
L = 0
heat_in = L * (1 - albedo)
temp_moon_night = (heat_in / sigma) ** 0.25
print(f'Moon temperature at night: {temp_moon_night} K.')

print('\nGW1 W3 A stronger GHG effect')
L = 1350
albedo = 0.3
heat_in = L * (1 - albedo) / 4
t_skin = (heat_in / sigma) ** 0.25  # same as ((L * (1 - albedo)) / (4 * sigma)) ** 0.25
print(f'Temp. skin layer:\t{t_skin} K.')
t_middle = (2 * t_skin ** 4) ** 0.25
print(f'Temp. middle layer:\t{t_middle} K.')
t_ground = ((heat_in / sigma) + (t_middle ** 4)) ** 0.25
print(f'Temp. ground layer:\t{t_ground} K.')
print(f'Middle/skin temp. ratio: {t_middle / t_skin}')
print(f'Ground/skin temp. ratio: {t_ground / t_skin}')

print('\nGW1 W3 Nuclear winter')
L = 1350
albedo = 0.3
heat_in = L * (1 - albedo) / 4
t_a = (heat_in / (2 * sigma)) ** 0.25
t_g = t_a
print(f'Ground temperature at nuclear winter: {t_g} K.')
print(f'Atmosphere temperature at nuclear winter: {t_a} K.')
print(f'Earth/atmosphere ratio under nuclear winter conditions: {t_g/t_a}')
