import numpy as np
import matplotlib.pyplot as plt

years = np.array([2020, 2021, 2022, 2023, 2024])
population = np.array([10000, 10800, 11900, 13200, 14800])

# Step 1: umerical Di erentiation (Growth Rate for 2021-2023)
# Formula: P'(t) = (P(t+1) - P(t-1)) / 2
growth_rates = []
calc_years = years[1:-1] # slices out the 1st and last years

for i in range(1, len(years)-1):
    rate = (population[i+1] - population[i-1]) / 2
    growth_rates.append(rate)

print("--- Table of Derivatives (Growth Rate) ---")
for yr, rate in zip(calc_years, growth_rates):
    print(f"Year {yr}: {int(rate)} people/year")

# Step 2: Numerical Integration (Total Change)
# Formula: Trapezoidal Rule with step size h = 1
h = 1
total_integrated_pop = (h / 2) * (population[0] + 2 * sum(population[1:-1]) + population[-1])

print("\n--- Numerical Integration ---")
print(f"Integrated Total Population Estimate (2020-2024): {int(total_integrated_pop)}")

# Step 3: Visualization (Plotting)
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Case Study 1: Population Growth Analysis', fontsize=16, fontweight='bold')

# Population vs Time
ax1.plot(years, population, marker='o', color='cyan', linestyle='-', linewidth=2)
ax1.set_title('Population vs Time')
ax1.set_xlabel('Year')
ax1.set_ylabel('Population')
ax1.set_xticks(years)
ax1.grid(True, alpha=0.3)

# Growth Rate vs Time
ax2.plot(calc_years, growth_rates, marker='s', color='orange', linestyle='-', linewidth=2)
ax2.set_title('Growth Rate vs Time')
ax2.set_xlabel('Year')
ax2.set_ylabel('Growth Rate (People/Year)')
ax2.set_xticks(calc_years)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('case1_visualization.png')
plt.show()

print("\n--- Summary ---")
print("1. Acceleration: The central difference calculations prove the population is not just growing, but accelerating. The rate of change increased linearly, peaking at 1,450 new people/year in 2023.")
print("2. Accumulation: The numerical integration (Trapezoidal Rule) estimates a total accumulated population area of 48,300 over the 5-year block, quantifying the massive scale of the growth.")
print("3. Trend & Prediction: Because the acceleration is constant (+250 people/year), the overall population growth is exponential. Following this trend, we project the population will reach roughly 16,500 by 2025.")