# E-Commerce Sales Analysis Dashboard

## Project Overview

This project is an interactive **E-Commerce Sales Analysis Dashboard** built using **Python, Pandas, NumPy, Matplotlib, and Streamlit**.

The dashboard analyzes e-commerce sales data from CSV files and provides insights into customers, products, orders, payments, KPIs, and overall business performance.

The project was initially developed using MySQL, and the final dashboard version uses CSV files so it can be easily deployed on Streamlit Cloud.

## Features

- Interactive Streamlit Dashboard
- Exploratory Data Analysis (EDA)
- Customer Analysis
- Gender-wise Analysis
- Age Group Analysis
- State-wise Analysis
- Product Analysis
- Category Analysis
- Order Status Analysis
- Discount Analysis
- Payment Method Analysis
- KPI Analysis
- Business Insights
- Interactive Charts and Visualizations

## Key KPIs

- Total Orders: 100
- Total Customers: 30
- Total Products: 19
- Total Revenue: ₹1,098,049.90
- Average Order Value: ₹22,876.04
- Cancellation Rate: 15%
- Return Rate: 15%

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- CSV

## Project Structure

```text
E-Commerce-Sales-Analysis-Dashboard/
│
├── Sales_data_app.py
├── sales_data.csv
├── payments_summary.csv
├── data_cleaning.py
├── eda.py
├── numpy_analysis.py
├── customer_analysis.py
├── product_analysis.py
├── order_analysis.py
├── kpi_analysis.py
├── visualization.py
├── business_insights.py
├── requirements.txt
└── README.md
```

## Dashboard Sections

### Dashboard

Displays important business KPIs including:

- Total Revenue
- Total Orders
- Total Customers
- Total Products
- Average Order Value
- Cancellation Rate
- Return Rate

### Exploratory Data Analysis

Provides:

- Dataset Shape
- Dataset Preview
- Statistical Summary
- Missing Values
- Order Status Distribution

### Customer Analysis

Analyzes:

- Customer Spending
- Repeat Customers
- Repeat Customer Rate
- Gender-wise Revenue
- Age Group Revenue
- State-wise Revenue

### Product Analysis

Analyzes:

- Category Performance
- Top Category
- Top Selling Product
- Top Revenue Product
- Product Quantity

### Order Analysis

Analyzes:

- Order Status Revenue
- Average Discount
- Maximum Discount
- Minimum Discount

### Payment Analysis

Displays payment method distribution using payment data stored in CSV format.

### KPI Analysis

Displays important business KPIs in an easy-to-understand dashboard format.

### Visualizations

Provides interactive visualizations for:

- Monthly Revenue
- Category Revenue
- Category Quantity
- Top Products
- Top Customers
- Order Status
- Customer Segments
- Gender Revenue
- Gender Average Spending
- Age Revenue
- Age Average Spending
- State Revenue
- Discount vs Revenue

### Business Insights

Summarizes important findings from the e-commerce sales data.

## Data Files

The dashboard uses the following CSV files:

```text
sales_data.csv
payments_summary.csv
```

These files contain sales, customer, product, order, and payment-related data used for analysis.

## How to Run the Project

### 1. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit App

```bash
streamlit run Sales_data_app.py
```

The dashboard will open automatically in your browser.

## Project Objective

The objective of this project is to analyze e-commerce sales data and identify useful business insights such as:

- Revenue Performance
- Customer Purchasing Behavior
- Top Performing Products
- Best Performing Categories
- Repeat Customer Behavior
- Order Cancellation Trends
- Order Return Trends
- Payment Preferences
- State-wise Sales Performance

## Author

**Sakshi Panchal**

Aspiring Data Analyst
