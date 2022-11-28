# Assume you have weather data: Temp

import numpy as np
import matplotlib.pyplot as plt

# Genrate my own weather data 

def f(t, params):
    A = params[0]
    B = params[1]
    C = params[2]
    omega = params[3]
    phi = params[4]
    
    return A + B*t + C*np.sin(omega*t + phi)


N = 365*3
sim_data = np.zeros(N)


A = 5.0
B = 0.2
C = 10.0
omega = 2*np.pi
phi = np.pi/2

params = [A, B, C, omega, phi]
s_d = 3


for i in range(N):
    sim_data[i] = f(i/365, params) + s_d*np.random.randn()

time_set = np.arange(start = 0, stop = 3, step = 1/365)

X = np.zeros((N, len(params)-1 ))
X[:,0] = np.ones(N)
X[:,1] = time_set
X[:,2] = np.sin(omega*time_set)
X[:,3] = np.cos(omega*time_set)

regress_coeffs = np.linalg.solve(X.T @ X , X.T @ sim_data)

A_est = regress_coeffs[0]
B_est = regress_coeffs[1]
C_est = np.sqrt(regress_coeffs[2]**2 +regress_coeffs[3]**2)
omega_est = omega
phi_est  =np.pi - np.arctan(regress_coeffs[3]/regress_coeffs[2])

parameters = [A_est, B_est, C_est, omega_est, phi_est]

fitted = f(time_set, parameters)

sd_est = np.sqrt(np.dot( fitted - sim_data , fitted - sim_data) / (N - len(parameters)-1))

plt.plot(sim_data)
plt.plot(fitted)