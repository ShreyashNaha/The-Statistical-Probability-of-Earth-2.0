import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('kepler_data.csv', comment='#')
except FileNotFoundError:
    print("Error: kepler_data.csv not found.")
    exit()

df = df[df['koi_disposition'] == 'CONFIRMED']
df = df.dropna(subset=['koi_prad', 'kepid'])

Y = df['koi_prad']
Y = Y[Y < 20]

mean_val = np.mean(Y)
var_val = np.var(Y)
skew_val = stats.skew(Y)
kurt_val = stats.kurtosis(Y)

print("--- MOMENTS OF CONTINUOUS VARIABLE Y (RADIUS) ---")
print(f"1st Moment (Mean):      {mean_val:.4f} Earth Radii")
print(f"2nd Moment (Variance):  {var_val:.4f}")
print(f"3rd Moment (Skewness):  {skew_val:.4f}")
print(f"4th Moment (Kurtosis):  {kurt_val:.4f}")

planet_counts = df['kepid'].value_counts()
X = planet_counts.values

mean_X = np.mean(X)
var_X = np.var(X)

print("\n--- MOMENTS OF DISCRETE VARIABLE X (MULTIPLICITY) ---")
print(f"Average Planets per Star: {mean_X:.4f}")
print(f"Variance of System Size:  {var_X:.4f}")
print(f"Most planets in one system: {np.max(X)}")

if skew_val > 1:
    print("\n[Analysis] Distribution is Positively Skewed.")
    print("Conclusion: Small planets are significantly more common than Gas Giants.")
elif skew_val < -1:
    print("\n[Analysis] Distribution is Negatively Skewed.")
else:
    print("\n[Analysis] Distribution is Symmetric.")

plt.figure(figsize=(10, 6))
plt.hist(Y, bins=50, color='purple', alpha=0.7, edgecolor='black')
plt.axvline(mean_val, color='yellow', linestyle='dashed', linewidth=2, label=f'Mean ({mean_val:.2f})')
plt.axvline(np.median(Y), color='lime', linestyle='dashed', linewidth=2, label=f'Median ({np.median(Y):.2f})')
plt.title('Distribution of Planet Radii (Variable Y)')
plt.xlabel('Earth Radii')
plt.ylabel('Frequency')
plt.legend()
plt.show()