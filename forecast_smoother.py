import numpy as np
import matplotlib.pyplot as plt


forecast = -np.array([-21.65,-21.5,-21.3,-21.05,-20.8,-20.8,-20.75,-20.7,-21,-21.25,-22.1,-23.7,-27.4,-30.75,-33.3,-36.2,-39.35,-42.95,-44.75,-45.85,-45.95,-47,-46.8,-46.85,-46.5,-46.5,-45.35,-45.25,-44.55,-44.55,-43.3,-43.25,-40.8,-39.9,-37,-35.7,-33.5,-33.65,-32.2,-32.3,-30.5,-30,-28.35,-27.05,-25.1,-24.35,-23.3,-21.55])

indices = [i for i in range(1,49)]

width = 6   # width can be anything in {k : 48 mod k = 0 and k>4}

if 48 % width !=0:
    print("Width must fit evenly into 48")

n_intervals = int(48/width)

forecast_matrix = np.reshape(forecast, (n_intervals,width))
hh_matrix = np.reshape(np.arange(1,49,1), forecast_matrix.shape)

    

interpolation_functions = []

for i in range(n_intervals):
    interpolation_functions.append( np.polyfit( hh_matrix[i] , forecast_matrix[i],3))
    
smoothed_matrix = np.zeros(forecast_matrix.shape)

for i in range(n_intervals):
    p = interpolation_functions[i]
    for j in range(width):
        smoothed_matrix[i,j] = np.polyval(p, hh_matrix[i,j])
        
smoothed_forecast = smoothed_matrix.flatten()


print(smoothed_forecast)
plt.plot(smoothed_forecast)
plt.plot(forecast)

plt.show()

