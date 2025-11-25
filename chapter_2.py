import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# --- LOAD LOCAL DATA ---
try:
    df = pd.read_csv('kepler_data.csv', comment='#')
except FileNotFoundError:
    print("Error: kepler_data.csv not found.")
    exit()

# Filter for CONFIRMED planets only
df = df[df['koi_disposition'] == 'CONFIRMED']
df = df.dropna(subset=['koi_prad', 'koi_teq'])

# --- PART 1: NORMAL DISTRIBUTION (Continuous) ---
# We filter out Gas Giants (> 10 Earth Radii) to focus on rocky/icy worlds
# otherwise the 'mean' is skewed by Jupiters.
rocky_worlds = df[df['koi_prad'] < 10]['koi_prad']

# Fit the data to a Normal Distribution to get Mean (mu) and Std Dev (sigma)
mu, sigma = stats.norm.fit(rocky_worlds)

print(f"--- NORMAL DISTRIBUTION FIT ---")
print(f"Mean Planet Radius: {mu:.4f} Earth Radii")
print(f"Standard Deviation: {sigma:.4f}")

# Calculate Z-Score for Earth (Radius = 1.0)
earth_radius = 1.0
z_score = (earth_radius - mu) / sigma

print(f"Earth Z-Score:      {z_score:.4f}")
print(f"Probability Density at Earth: {stats.norm.pdf(earth_radius, mu, sigma):.4f}")

# Visualization
plt.figure(figsize=(10, 6))
sns.histplot(rocky_worlds, bins=30, kde=False, stat="density", color='skyblue', label='Actual Data')

# Plot the Bell Curve overlay
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mu, sigma)
plt.plot(x, p, 'k', linewidth=2, label='Normal Distribution (Fit)')
plt.axvline(x=1.0, color='red', linestyle='--', label='Earth (1.0)')

plt.title('Distribution of Planetary Radii (Earth = 1.0)')
plt.xlabel('Planet Radius (Earth Radii)')
plt.legend()
plt.show()

# --- PART 2: BINOMIAL DISTRIBUTION (Discrete) ---
# Criteria for "Earth 2.0":
# 1. Radius between 0.8 and 1.2 Earth Radii
# 2. Temperature between 200K and 320K (Liquid Water)

earth_candidates = df[
    (df['koi_prad'] > 0.8) & (df['koi_prad'] < 1.2) & 
    (df['koi_teq'] > 200) & (df['koi_teq'] < 320)
]

num_success = len(earth_candidates)
num_trials_total = len(df)
prob_success = num_success / num_trials_total

print(f"\n--- BINOMIAL PROBABILITY ---")
print(f"Total Planets Analyzed: {num_trials_total}")
print(f"Earth 2.0 Candidates:   {num_success}")
print(f"Probability (p):        {prob_success:.5f}")

# PREDICTION: If we scan 100 new stars, what is probability of finding at least one?
# P(X >= 1) = 1 - P(X = 0)
n_future = 100
prob_at_least_one = 1 - stats.binom.pmf(0, n_future, prob_success)

print(f"\n[Prediction] Mission scanning {n_future} stars:")
print(f"Probability of finding ZERO Earths:       {stats.binom.pmf(0, n_future, prob_success):.4f}")
print(f"Probability of finding AT LEAST ONE Earth:{prob_at_least_one:.4f}")