import numpy as np
import matplotlib.pyplot as plt


time = np.array([0, 1, 2, 3, 4, 5])
position = np.array([0, 5, 15, 30, 50, 75])
h = 1

velocity = []
for i in range(1, len(time)-1):
   v = (position[i+1] - position[i-1]) / (2 * h)
   velocity.append(v)

time_interior = time[1:-1]

print("--- Step 1: Velocity (m/s) ---")
for t, v in zip(time_interior, velocity):
   print(f"Time t={t} s: {v} m/s")

integral_position = np.trapezoid(position, time)
print(f"\n--- Step 2: Integrated Position Area ---")
print(f"Area under x(t) curve: {integral_position}")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(time, position, marker='o', color='b', linestyle='-', linewidth=2)
plt.title("Position vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(time_interior, velocity, marker='s', color='r', linestyle='--', linewidth=2)
plt.title("Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)

plt.tight_layout()
plt.show()