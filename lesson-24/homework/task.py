import pandas as pd
sales = pd.read_csv('sales_data.csv')
sales

category_summary = (
    sales
    .groupby('Category')
    .agg(
    Total_Quantity=('Quantity', 'sum'),
    Average_Price=('Price', 'mean'),
    Max_Quantity=('Quantity', 'max')
).reset_index()
)
print(category_summary)

sales['Total_Sales'] = (
    sales['Quantity'] * sales['Price']
)

daily_sales = (
     sales
    .groupby('Date')
    .agg(Total_Sales=('Total_Sales', 'sum'))
    .reset_index()
)

best_sales_date = (
    daily_sales
    .loc[daily_sales['Total_Sales'].idxmax()]
)

print("Highest Sales Date:")
print(best_sales_date)


customer = pd.read_csv('customer_orders.csv')
customer

customer_orders = (
    customer
    .groupby('CustomerID')
    .agg(Order_Count=('CustomerID', 'size'))
    .reset_index()
)

filtered_customers = (
    customer_orders
    .query('Order_Count >= 20')
    .reset_index(drop=True)
)

print(filtered_customers)


customer_avg_price = (
    customer
    .groupby('CustomerID')
    .agg(Average_Price=('Price', 'mean'))
    .reset_index()
)

high_spending_customers = (
    customer_avg_price
    .query('Average_Price > 120')
    .reset_index(drop=True)
)

print(high_spending_customers)


product_summary = (
    customer
    .groupby('Product')
    .agg(
        Total_Quantity=('Quantity', 'sum'),
    )
    .reset_index()
)

filtered_products = (
    product_summary
    .query('Total_Quantity >= 5')
    .reset_index(drop=True)
)

print(filtered_products)
