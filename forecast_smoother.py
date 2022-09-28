import numpy as np
import matplotlib.pyplot as plt


forecast = -np.random.randn(48)
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

