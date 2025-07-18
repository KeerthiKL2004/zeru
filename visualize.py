import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your credit score data
score_df = pd.read_csv("output/credit_scores.csv")

# Set up the plotting style
sns.set(style="whitegrid")
plt.figure(figsize=(14, 6))

# Plot 1: Histogram
plt.subplot(1, 2, 1)
sns.histplot(score_df["creditScore"], bins=50, kde=True, color="skyblue")
plt.title("Distribution of Credit Scores")
plt.xlabel("Credit Score")
plt.ylabel("Frequency")

# Plot 2: Boxplot
plt.subplot(1, 2, 2)
sns.boxplot(x=score_df["creditScore"], color="lightgreen")
plt.title("Boxplot of Credit Scores")
plt.xlabel("Credit Score")

# Display both plots
plt.tight_layout()
plt.show()
