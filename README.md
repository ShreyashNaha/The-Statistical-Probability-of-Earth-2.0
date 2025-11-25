# The Statistical Probability of Earth 2.0 🌍

### A Rigorous Statistical Audit of Exoplanetary Populations

This project applies advanced mathematical statistics to the NASA Kepler Mission dataset ($N > 7,000$ objects) to answer a fundamental astronomical question: **"How statistically unique is the Earth?"** By combining Probability Theory with Astrophysics, we characterize the population of exoplanets and mathematically test the likelihood of finding another Earth-sized planet in the Habitable Zone.

## 📊 Mathematical Framework

This analysis covers five core statistical concepts implemented in Python:

1. **Bayesian Reliability:** Calculating the False Positive Probability (FPP) of faint signals using Bayes' Theorem ($P(C|L)$).
2. **Distributions:** Modeling planetary radii using **Normal (Gaussian)** distributions and predicting mission success rates using **Binomial** distributions.
3. **Moments:** Using **Skewness** and **Kurtosis** to infer the physical mass function of the galaxy and validate the Core Accretion theory.
4. **Sampling:** Verifying the **Central Limit Theorem (CLT)** to justify the use of parametric tests on non-normal data.
5. **Hypothesis Testing:** Performing a **One-Sample Z-Test** at 1% and 5% significance levels to scientifically prove the dominance of "Super-Earths" over Earth-sized planets.

## 🛠️ Prerequisites

You need **Python 3.x** and the following scientific libraries. You can install them via pip:

```bash
pip install pandas numpy scipy matplotlib seaborn
```

## 📂 Data Setup (Crucial Step)

The scripts rely on the Kepler Cumulative Object of Interest (KOI) table. Due to file size limits and API stability, you must download this manually:

Go to the NASA Exoplanet Archive.

In the top-left corner, click the Download Table button.

Select CSV Format.

Rename the downloaded file to exactly: kepler_data.csv

Move this file into the root folder of this project (the same folder where the python scripts are located).

## 🚀 How to Run the Analysis

The project is divided into 5 chapters, corresponding to the statistical progression of the research. Run them in order to generate the analysis and graphs:

### 1. Reliability Analysis
   
Calculates Bayesian probabilities for signal detection based on Signal-to-Noise Ratios.

```bash
python chapter_1.py
```

### 2. Distributions & Modeling
   
Fits the Normal distribution to planetary radii and calculates Binomial probabilities for future mission planning.

```bash
python chapter_2.py
```

### 3. Population Characterization
   
Calculates the 3rd and 4th Moments (Skewness/Kurtosis) to infer planet formation physics.

```bash
python chapter_3.py
```

### 4. Correlation & Sampling
   
Tests the Central Limit Theorem (CLT) and analyzes correlations between star size and planetary orbital periods.

```bash
python chapter_4.py
```

### 5. Hypothesis Testing
 
The final statistical proof. Performs a Z-Test to determine if the average habitable planet is Earth-sized.

```bash
python chapter_5.py
```

## 📜 License & Data Source

This project uses public data from the NASA Exoplanet Archive, which is operated by the California Institute of Technology, under contract with the National Aeronautics and Space Administration under the Exoplanet Exploration Program.
