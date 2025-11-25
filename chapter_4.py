import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv('kepler_data.csv', comment='#')
except FileNotFoundError:
    print("Error: kepler_data.csv not found.")
    exit()

df = df[df['koi_disposition'] == 'CONFIRMED']
df = df.dropna(subset=['koi_srad', 'koi_period', 'koi_prad'])

star_radius = df['koi_srad']
orbital_period = df['koi_period']

corr_coef, p_value = stats.pearsonr(star_radius, orbital_period)

print("--- CORRELATION ANALYSIS ---")
print(f"Variables: Star Radius vs. Orbital Period")
print(f"Pearson Correlation (r): {corr_coef:.4f}")
print(f"P-value:                 {p_value:.4e}")

if p_value < 0.05:
    print("Result: Statistically Significant Correlation.")
else:
    print("Result: No Significant Correlation.")

plt.figure(figsize=(10, 6))
sns.scatterplot(x=star_radius, y=orbital_period, alpha=0.5)
plt.title(f'Correlation: Star Size vs. Orbit (r={corr_coef:.2f})')
plt.xlabel('Star Radius (Solar Radii)')
plt.ylabel('Orbital Period (Days)')
plt.xscale('log')
plt.yscale('log')
plt.show()

population = df['koi_prad'].values
population = population[population < 20]
true_mean = np.mean(population)
true_std = np.std(population)

sample_size = 50
num_samples = 1000
sample_means = []

for _ in range(num_samples):
    sample = np.random.choice(population, sample_size)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)
mean_of_means = np.mean(sample_means)
std_error_calc = np.std(sample_means)
std_error_theory = true_std / np.sqrt(sample_size)

print("\n--- CENTRAL LIMIT THEOREM VERIFICATION ---")
print(f"True Population Mean:       {true_mean:.4f}")
print(f"Mean of Sample Means:       {mean_of_means:.4f}")
print(f"Theoretical Standard Error: {std_error_theory:.4f}")
print(f"Calculated Standard Error:  {std_error_calc:.4f}")

plt.figure(figsize=(10, 6))
sns.histplot(sample_means, kde=True, color='green', stat="density", label='Sampling Dist')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, true_mean, std_error_theory)
plt.plot(x, p, 'r--', linewidth=2, label='Theoretical Normal Curve')

plt.title(f'Central Limit Theorem (n={sample_size})')
plt.xlabel('Mean Planet Radius (Earth Radii)')
plt.legend()
plt.show()