import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. LOAD AND CLEAN DATA ---
try:
    df = pd.read_csv('kepler_data.csv', comment='#')
except FileNotFoundError:
    print("Error: kepler_data.csv not found. Please download it.")
    exit()

# Filter for Confirmed Planets only
df = df[df['koi_disposition'] == 'CONFIRMED']

# Filter for Habitable Zone: Equilibrium Temp (Kelvin) between 200K and 320K
# We also filter for 'Potentially Rocky' radii (< 2.5 Earth Radii)
habitable_zone = df[(df['koi_teq'] >= 200) & (df['koi_teq'] <= 320)]
sample_data = habitable_zone[habitable_zone['koi_prad'] < 2.5]['koi_prad']

# --- 2. CALCULATE STATISTICS ---
n = len(sample_data)
sample_mean = np.mean(sample_data)
sample_std = np.std(sample_data, ddof=1) # Sample Standard Deviation
mu_0 = 1.0  # Null Hypothesis Mean (Earth Radius)

# Calculate Standard Error
std_error = sample_std / np.sqrt(n)

# Calculate Z-Statistic
# Formula: Z = (X_bar - mu_0) / (sigma / sqrt(n))
z_stat = (sample_mean - mu_0) / std_error

# Calculate P-Value (Two-Tailed)
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

print(f"--- HYPOTHESIS TESTING DATA ---")
print(f"Sample Size (n):       {n}")
print(f"Sample Mean:           {sample_mean:.4f} Earth Radii")
print(f"Sample Std Dev:        {sample_std:.4f}")
print(f"Hypothesized Mean:     {mu_0:.4f}")
print(f"Calculated Z-Score:    {z_stat:.4f}")
print(f"P-Value:               {p_value:.4e}")
print("-" * 40)

# --- 3. DECISION LOGIC ---
def evaluate_hypothesis(alpha, z_stat):
    # Two-tailed critical value
    z_crit = stats.norm.ppf(1 - alpha/2)
    print(f"--- TEST AT {alpha*100:.0f}% SIGNIFICANCE LEVEL (alpha={alpha}) ---")
    print(f"Critical Z-Score:      +/- {z_crit:.4f}")
    
    if abs(z_stat) > z_crit:
        print("Result: REJECT Null Hypothesis.")
        print("Conclusion: The average radius is statistically DIFFERENT from Earth.")
    else:
        print("Result: FAIL TO REJECT Null Hypothesis.")
        print("Conclusion: The average radius is statistically SIMILAR to Earth.")
    print("-" * 40)
    return z_crit

# Evaluate at 5% (0.05)
z_crit_5 = evaluate_hypothesis(0.05, z_stat)

# Evaluate at 1% (0.01)
z_crit_1 = evaluate_hypothesis(0.01, z_stat)

# --- 4. PLOTTING FUNCTIONS ---
def plot_hypothesis_test(z_stat, z_crit, alpha, title_suffix):
    plt.figure(figsize=(12, 7))
    
    # Create range for x-axis
    # We ensure the plot is wide enough to show both the critical region (near 0)
    # AND the calculated Z-statistic (which is far out at ~12.45)
    limit = max(4, abs(z_stat) + 2)
    x = np.linspace(-limit, limit, 1000)
    y = stats.norm.pdf(x, 0, 1)
    
    # Plot the Bell Curve
    plt.plot(x, y, label='Standard Normal Distribution', color='blue')
    
    # Shade Rejection Regions (Two-Tailed)
    plt.fill_between(x, y, where=(x >= z_crit), color='red', alpha=0.3, label=f'Rejection Region (Z > {z_crit:.2f})')
    plt.fill_between(x, y, where=(x <= -z_crit), color='red', alpha=0.3, label=f'Rejection Region (Z < -{z_crit:.2f})')
    
    # Shade Acceptance Region
    plt.fill_between(x, y, where=((x > -z_crit) & (x < z_crit)), color='green', alpha=0.1, label='Acceptance Region (Fail to Reject)')
    
    # Plot Critical Values (Vertical Lines)
    plt.axvline(z_crit, color='red', linestyle=':', linewidth=2)
    plt.axvline(-z_crit, color='red', linestyle=':', linewidth=2)
    
    # Plot Calculated Z-Statistic
    plt.axvline(z_stat, color='black', linestyle='--', linewidth=3, label=f'Calculated Z ({z_stat:.2f})')
    
    # Formatting
    plt.title(f'Hypothesis Test: {title_suffix}\nComparing Calculated Z ({z_stat:.2f}) vs Critical Z (+/- {z_crit:.2f})')
    plt.xlabel('Z-Score (Standard Deviations)')
    plt.ylabel('Probability Density')
    plt.legend(loc='upper left')
    plt.grid(True, alpha=0.3)
    
    # Show Plot (User will screenshot)
    plt.show()

# --- 5. GENERATE PLOTS ---

# Plot A: 5% Significance Level
plot_hypothesis_test(z_stat, z_crit_5, 0.05, '5% Significance Level (95% Confidence)')

# Plot B: 1% Significance Level
plot_hypothesis_test(z_stat, z_crit_1, 0.01, '1% Significance Level (99% Confidence)')