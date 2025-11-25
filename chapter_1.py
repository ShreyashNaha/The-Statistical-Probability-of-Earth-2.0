import pandas as pd
import numpy as np

# --- UPDATED LOADING SECTION ---
# We now look for the file on your computer to avoid HTTP 404 errors.
try:
    print("Loading data from local file...")
    # skip_footer is needed because NASA CSVs sometimes have citation text at the bottom
    df = pd.read_csv('kepler_data.csv', comment='#') 
    print("Success! Local file loaded.")
except FileNotFoundError:
    print("ERROR: Could not find 'kepler_data.csv'.")
    print("Make sure you downloaded the file and renamed it correctly.")
    print("And make sure it is in the SAME folder as this python script.")
    exit()

# --- DATA CLEANING ---
# NASA column names can be tricky. Let's ensure we have the right ones.
# We filter for CONFIRMED planets and FALSE POSITIVES
df = df[df['koi_disposition'].isin(['CONFIRMED', 'FALSE POSITIVE'])]
df = df.dropna(subset=['koi_model_snr', 'koi_disposition'])

N = len(df)
print(f"Total Sample Size (N): {N}")

# --- THE MATH (Same as before) ---

# Partitioning Signal-to-Noise Ratio (SNR)
df['SNR_Bin'] = pd.cut(df['koi_model_snr'], 
                       bins=[0, 10, 100, 1000000], 
                       labels=['Low', 'Medium', 'High'])

conf = df[df['koi_disposition'] == 'CONFIRMED']
P_C = len(conf) / N

# Calculating Probabilities of partitions
probs_E = df['SNR_Bin'].value_counts(normalize=True)
P_Low = probs_E['Low']
P_Med = probs_E['Medium']
P_High = probs_E['High']

# Conditional Probabilities
def get_cond_prob(bin_label):
    subset = df[df['SNR_Bin'] == bin_label]
    confirmed = subset[subset['koi_disposition'] == 'CONFIRMED']
    return len(confirmed) / len(subset)

P_C_given_Low = get_cond_prob('Low')
P_C_given_Med = get_cond_prob('Medium')
P_C_given_High = get_cond_prob('High')

print("\n--- CONDITIONAL PROBABILITIES ---")
print(f"P(Confirmed | Low SNR):    {P_C_given_Low:.4f}")
print(f"P(Confirmed | Medium SNR): {P_C_given_Med:.4f}")
print(f"P(Confirmed | High SNR):   {P_C_given_High:.4f}")

# Total Probability Theorem
P_Total = (P_C_given_Low * P_Low) + (P_C_given_Med * P_Med) + (P_C_given_High * P_High)

print("\n--- TOTAL PROBABILITY THEOREM ---")
print(f"Calculated P(Confirmed): {P_Total:.4f}")
print(f"Actual P(Confirmed):     {P_C:.4f}")

# Bayes Theorem
bayes_num = P_C_given_Low * P_Low
P_Low_given_C = bayes_num / P_C

actual_bayes = len(conf[conf['SNR_Bin'] == 'Low']) / len(conf)

print("\n--- BAYES THEOREM ---")
print(f"P(Low SNR | Confirmed) Calculated: {P_Low_given_C:.4f}")
print(f"P(Low SNR | Confirmed) Actual:     {actual_bayes:.4f}")