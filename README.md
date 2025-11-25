The Statistical Probability of Earth 2.0 🌍

A Rigorous Statistical Audit of Exoplanetary Populations

This project applies advanced mathematical statistics to the NASA Kepler Mission dataset ($N > 7,000$ objects) to answer a fundamental astronomical question: "How statistically unique is the Earth?" By combining Probability Theory with Astrophysics, we characterize the population of exoplanets and mathematically test the likelihood of finding another Earth-sized planet in the Habitable Zone.

📊 Mathematical Framework

This analysis covers five core statistical concepts implemented in Python:

Bayesian Reliability: Calculating the False Positive Probability (FPP) of faint signals using Bayes' Theorem.

Distributions: Modeling planetary radii using Normal (Gaussian) and Binomial distributions.

Moments: Using Skewness and Kurtosis to validate the Core Accretion theory of planet formation.

Sampling: Verifying the Central Limit Theorem (CLT) to justify parametric testing.

Hypothesis Testing: Performing a One-Sample Z-Test at 1% and 5% significance levels to prove the "Super-Earth" dominance.

🛠️ Prerequisites

You need Python 3.x and the following scientific libraries:

pip install pandas numpy scipy matplotlib seaborn


📂 Data Setup (Crucial Step)

The scripts rely on the Kepler Cumulative Object of Interest (KOI) table. Due to file size limits and API stability, you must download this manually:

Go to the NASA Exoplanet Archive.

In the top-left corner, click Download Table $\to$ CSV Format.

Rename the downloaded file to: kepler_data.csv

Move this file into the root folder of this project (same folder as the python scripts).

🚀 How to Run the Analysis

The project is divided into 5 chapters, corresponding to the statistical progression of the report. Run them in order:

Chapter 1: Reliability Analysis
Calculates Bayesian probabilities for signal detection.

python chapter_1.py


Chapter 2: Distributions
Fits the Normal distribution to planet radii and calculates Binomial probability for future missions.

python chapter_2.py


Chapter 3: Moments
Calculates Skewness and Kurtosis to infer planet formation physics.

python chapter_3.py


Chapter 4: Correlation & Sampling
Tests the Central Limit Theorem and correlations between star size and planetary orbit.

python chapter_4.py


Chapter 5: Hypothesis Testing
The final Z-Test proving whether the average habitable planet is Earth-sized.

python chapter_5.py


📄 Project Report

A complete academic report (report.pdf) generated via LaTeX is available in this repository, detailing the methodology, mathematical derivations, and physical interpretations of the results.

📜 License

This project uses public data from the NASA Exoplanet Archive, which is operated by the California Institute of Technology, under contract with the National Aeronautics and Space Administration under the Exoplanet Exploration Program.
