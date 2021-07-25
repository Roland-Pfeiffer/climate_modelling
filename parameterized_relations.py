#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

"""Parameterized relationship between T, ice latitude, and albedo"""

mean_temp = [265, 255, 245, 235, 225, 215]
ice_lat = [75, 60, 45, 30, 15, 0]
planet_albedo = [0.15, 0.25, 0.35, 0.45, 0.55, 0.65]

# Linear regression using sklearn
mean_temp_2D = np.array(mean_temp).reshape(-1, 1)  # Reshape to fit sklearns reqs
ice_lat_2D = np.array(ice_lat).reshape(-1, 1)
planet_albedo_2D = np.array(planet_albedo). reshape(-1, 1)

lin_reg = LinearRegression()
ice_lat_model = lin_reg.fit(X=mean_temp_2D, y=ice_lat_2D)
albedo_model = lin_reg.fit(X=mean_temp_2D, y=planet_albedo_2D)

print(f'Ice latitude model slope: {ice_lat_model.coef_}')
print(f'Ice latitude model intercept: {ice_lat_model.intercept_}')

print(f'Albedo latitude model slope: {albedo_model.coef_}')
print(f'Albedo model intercept: {albedo_model.intercept_}')

y = ice_lat_model.predict(mean_temp_2D)

fig, [ax1, ax2] = plt.subplots(1, 2)
ax1.scatter(mean_temp, ice_lat, label='Ice latitude', c='blue')
ax1.set_title('Ice latitude')
ax1.set_xlabel('Planetary temperature (K)')
ax1.set_ylabel('Latitude of ice occurrence (deg)')
ax2.scatter(mean_temp, planet_albedo, label='Albedo', c='grey')
ax2.set_title('Albedo')
ax2.set_xlabel('Planetary temperature (K)')
ax2.set_ylabel('Albedo')
plt.show()