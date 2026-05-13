# =========================
# Assignment 3: Grouping & Pivot Tables
# =========================

import pandas as pd

# Dataset
employee_data = {
    'Dept': ['IT', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'Sales'],
    'Status': ['FT', 'FT', 'Contract', 'FT', 'Contract', 'FT', 'Contract', 'FT'],
    'Salary': [95000, 60000, 70000, 80000, 55000, 98000, 72000, 85000]
}

emp_df = pd.DataFrame(employee_data)

print("Employee Data:\n")
print(emp_df)

# 1. Group by Dept and calculate average and maximum salary
grouped_data = emp_df.groupby('Dept')['Salary'].agg(['mean', 'max'])

print("\nAverage and Maximum Salary by Department:\n")
print(grouped_data)

# 2. Create Pivot Table
pivot_table = pd.pivot_table(
    emp_df,
    index='Dept',
    columns='Status',
    values='Salary',
    aggfunc='count',
    fill_value=0
)

print("\nPivot Table:\n")
print(pivot_table)

# 3. Sort pivot table by Contract workers
sorted_pivot = pivot_table.sort_values(by='Contract', ascending=False)

print("\nDepartments Sorted by Contract Workers:\n")
print(sorted_pivot)