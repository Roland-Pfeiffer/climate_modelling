#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy
import numpy as np
from sklearn.linear_model import LinearRegression

# Set up the data and the linear regression models using sklearn
mean_temp = np.array([265, 255, 245, 235, 225, 215]).reshape(-1, 1)  # Reshape to fit sklearns reqs
ice_lat = np.array([75, 60, 45, 30, 15, 0]).reshape(-1, 1)
planet_albedo = np.array([0.15, 0.25, 0.35, 0.45, 0.55, 0.65]).reshape(-1, 1)

# Linear regression models
ice_lat_model = LinearRegression().fit(X=mean_temp, y=ice_lat)
albedo_from_temp = LinearRegression().fit(X=mean_temp, y=planet_albedo)
temp_from_albedo = LinearRegression().fit(X=planet_albedo, y=mean_temp)

LRange = (1600, 1200)
L = LRange[0]
albedo = 0.15
convergence_threshold = 0.01

results = {}
while L > LRange[1] - 1:  # -1 to include the last T value of 1200
    albedos = [albedo]
    temps = [float(albedo_from_temp.predict(np.array([[albedos[-1]]])))]

    for i in range(100):
        new_albedo = albedo_from_temp.predict(np.array([[temps[-1]]]))
        albedos.append(float(new_albedo))

        new_temp = temp_from_albedo.predict(np.array([[albedos[-1]]]))
        temps.append(float(new_temp))

    results[L] = {'T': temps,
                  'Albedos': albedos}
    L -= 10

for key, item in results.items():
    plt.plot(item['T'])
plt.show()