import numpy as np
import matplotlib.pyplot as plt


# Given Data
time = np.array([0, 2, 4, 6, 8, 10])
volume = np.array([0, 40, 110, 210, 340, 500])
h = 2


# 1. Numerical Differentiation (Central Difference)
# We only calculate for interior points: t=2, 4, 6, 8
flow_rate = []
for i in range(1, len(time)-1):
   rate = (volume[i+1] - volume[i-1]) / (2 * h)
   flow_rate.append(rate)


time_interior = time[1:-1] # Times corresponding to flow rates (2, 4, 6, 8)


print("--- Step 1: Flow Rate (L/min) ---")
for t, rate in zip(time_interior, flow_rate):
   print(f"Time t={t} min: {rate} L/min")


# 2. Numerical Integration (Trapezoidal Rule for Integral of V(t))
# Updated to use np.trapezoid for NumPy 2.0+ compatibility
integral_volume = np.trapezoid(volume, time)
print(f"\n--- Step 2: Integrated Volume Area ---")
print(f"Area under V(t) curve: {integral_volume}")
# 3. Visualization
plt.figure(figsize=(12, 5))


# Plot 1: Volume vs Time
plt.subplot(1, 2, 1)
plt.plot(time, volume, marker='o', color='b', linestyle='-', linewidth=2)
plt.title("Volume vs Time")
plt.xlabel("Time (min)")
plt.ylabel("Volume (L)")
plt.grid(True)


# Plot 2: Flow Rate vs Time
plt.subplot(1, 2, 2)
plt.plot(time_interior, flow_rate, marker='s', color='r', linestyle='--', linewidth=2)
plt.title("Flow Rate vs Time")
plt.xlabel("Time (min)")
plt.ylabel("Flow Rate (L/min)")
plt.grid(True)


plt.tight_layout()
plt.show()
