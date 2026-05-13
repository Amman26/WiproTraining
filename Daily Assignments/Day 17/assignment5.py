# Import matplotlib
import matplotlib.pyplot as plt

# Dataset
cities = ['Chennai', 'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad']
sales_values = [450, 600, 520, 780, 410]

categories = ['Electronics', 'Fashion', 'Groceries', 'Home Decor']
market_share = [35, 25, 30, 10]

# Create figure with 2 subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# =================================
# 1. Bar Chart
# =================================

axes[0].bar(cities, sales_values, color='teal')

axes[0].set_title("City Sales")
axes[0].set_xlabel("Cities")
axes[0].set_ylabel("Sales Values")

# Add grid on Y-axis
axes[0].grid(axis='y')

# =================================
# 2. Pie Chart
# =================================

explode = (0.1, 0, 0, 0)

axes[1].pie(
    market_share,
    labels=categories,
    explode=explode,
    autopct='%1.1f%%'
)

axes[1].set_title("Market Share")

# =================================
# Main Title
# =================================

fig.suptitle("Regional Sales & Category Analysis")

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()
