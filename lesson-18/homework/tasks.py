import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)
print(df1[['Student_ID', 'Average']])

top_student = df1.loc[df1['Average'].idxmax()]
print(top_student)


df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
print(df1[['Student_ID', 'Total']])

import matplotlib.pyplot as plt

subject_averages = df1[['Math', 'English', 'Science']].mean()
subject_averages.plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Average Grades by Subject')
plt.xlabel('Subject')
plt.ylabel('Average Grade')
plt.xticks(rotation=0)
plt.show()


import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)


df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=0)
print(df2[['Product_A', 'Product_B', 'Product_C', 'Total_Sales']])

df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
max_sales_date = df2.loc[df2['Total_Sales'].idxmax()]
print(max_sales_date)

df2[['Product_A_pct_change', 'Product_B_pct_change', 'Product_C_pct_change']] = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
print(df2[['Date', 'Product_A_pct_change', 'Product_B_pct_change', 'Product_C_pct_change']])


import matplotlib.pyplot as plt

df2.set_index('Date')[['Product_A', 'Product_B', 'Product_C']].plot(kind='line', figsize=(10, 6))
plt.title('Sales Trends for Each Product Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.legend(title='Products')
plt.tight_layout()
plt.show()


import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

average_salary = df3.groupby('Department')['Salary'].mean()
print(average_salary)


most_experienced_employee = df3.loc[df3['Experience (Years)'].idxmax()]
print(most_experienced_employee)

min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100
print(df3[['Name', 'Salary', 'Salary Increase']])

mport matplotlib.pyplot as plt

department_counts = df3['Department'].value_counts()
department_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Employees in Each Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

total_revenue = df4['Total_Price'].sum()
print(f"Total Revenue: ${total_revenue}")

most_ordered_product = df4['Product'].mode()[0]
print(f"Most Ordered Product: {most_ordered_product}")

average_quantity = df4['Quantity'].mean()
print(f"Average Quantity Ordered: {average_quantity}")


import matplotlib.pyplot as plt

sales_per_product = df4.groupby('Product')['Total_Price'].sum()

sales_per_product.plot(kind='pie', autopct='%1.1f%%', figsize=(7, 7))
plt.title('Sales Distribution Across Products')
plt.ylabel('')  
plt.show()
