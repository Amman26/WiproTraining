# Import required libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in dataset
tips = sns.load_dataset('tips')

# ==============================
# 1. Histogram using displot
# ==============================

sns.displot(
    data=tips,
    x='total_bill',
    kde=True,
    color='darkblue'
)

plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Count")

plt.show()


# ==============================
# 2. JointPlot with Regression Line
# ==============================

sns.jointplot(
    data=tips,
    x='total_bill',
    y='tip',
    kind='reg'
)

plt.show()


# ==============================
# 3. BoxPlot
# ==============================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='smoker'
)

plt.title("Total Bill Across Different Days")
plt.xlabel("Day")
plt.ylabel("Total Bill")

plt.show()