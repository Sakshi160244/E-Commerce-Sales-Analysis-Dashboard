import matplotlib.pyplot as plt


def monthly_revenue_chart(delivered_df):

    monthly_revenue = (
        delivered_df
        .groupby(delivered_df["order_date"].dt.month)["total_amount"]
        .sum()
    )

    plt.figure(figsize=(10, 5))

    plt.plot(
        monthly_revenue.index,
        monthly_revenue.values,
        marker="o"
    )

    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")

    plt.xticks(
        range(1, 13),
        [
            "Jan", "Feb", "Mar", "Apr",
            "May", "Jun", "Jul", "Aug",
            "Sep", "Oct", "Nov", "Dec"
        ]
    )

    plt.tight_layout()
    plt.show()

def category_revenue_chart(category_performance):

    plt.figure(figsize=(10, 5))

    plt.bar(
        category_performance.index,
        category_performance["total_revenue"]
    )

    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()

def top_products_chart(top_products_quantity):

    plt.figure(figsize=(10, 5))

    plt.bar(
        top_products_quantity.index,
        top_products_quantity.values
    )

    plt.title("Top 10 Best-Selling Products")
    plt.xlabel("Product")
    plt.ylabel("Quantity Sold")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()

def category_quantity_chart(category_performance):

    plt.figure(figsize=(10, 5))

    plt.bar(
        category_performance.index,
        category_performance["total_quantity"]
    )

    plt.title("Category-wise Quantity Sold")
    plt.xlabel("Category")
    plt.ylabel("Total Quantity")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()


def payment_method_chart(payment_df):

    plt.figure(figsize=(8, 5))

    plt.bar(
        payment_df["payment_method"],
        payment_df["total_payments"]
    )

    plt.title("Payment Method Distribution")
    plt.xlabel("Payment Method")
    plt.ylabel("Number of Payments")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()

def top_customers_chart(customer_spending_df):

    top_customers = (
        customer_spending_df
        .sort_values(
            "total_amount",
            ascending=False
        )
        .head(5)
    )

    plt.figure(figsize=(10, 5))

    plt.bar(
        top_customers["customer_name"],
        top_customers["total_amount"]
    )

    plt.title("Top 5 Customers by Spending")
    plt.xlabel("Customer")
    plt.ylabel("Total Spending")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()

def order_status_chart(df):

    status_counts = df["order_status"].value_counts()

    plt.figure(figsize=(8, 5))

    plt.bar(
        status_counts.index,
        status_counts.values
    )

    plt.title("Order Status Distribution")
    plt.xlabel("Order Status")
    plt.ylabel("Number of Orders")

    plt.tight_layout()
    plt.show()

def customer_segment_chart(customer_spending_df):

    segment_counts = (
        customer_spending_df["customer_segment"]
        .value_counts()
    )

    plt.figure(figsize=(8, 5))

    plt.bar(
        segment_counts.index,
        segment_counts.values
    )

    plt.title("Customer Segment Distribution")
    plt.xlabel("Customer Segment")
    plt.ylabel("Number of Customers")

    plt.tight_layout()
    plt.show()

def gender_revenue_chart(gender_revenue):

    plt.figure(figsize=(8, 5))

    plt.bar(
        gender_revenue.index,
        gender_revenue.values
    )

    plt.title("Gender-wise Revenue")
    plt.xlabel("Gender")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.show()

def gender_avg_spending_chart(gender_avg_spending):

    plt.figure(figsize=(8, 5))

    plt.bar(
        gender_avg_spending.index,
        gender_avg_spending.values
    )

    plt.title("Gender-wise Average Spending")
    plt.xlabel("Gender")
    plt.ylabel("Average Spending")

    plt.tight_layout()
    plt.show()


def age_revenue_chart(age_revenue):

    plt.figure(figsize=(8, 5))

    plt.bar(
        age_revenue.index.astype(str),
        age_revenue.values
    )

    plt.title("Age Group-wise Revenue")
    plt.xlabel("Age Group")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.show()

def age_avg_spending_chart(age_avg_spending):

    plt.figure(figsize=(8, 5))

    plt.bar(
        age_avg_spending.index.astype(str),
        age_avg_spending.values
    )

    plt.title("Age Group-wise Average Spending")
    plt.xlabel("Age Group")
    plt.ylabel("Average Spending")

    plt.tight_layout()
    plt.show()

def state_revenue_chart(state_revenue):

    plt.figure(figsize=(10, 5))

    plt.bar(
        state_revenue.index,
        state_revenue.values
    )

    plt.title("State-wise Revenue")
    plt.xlabel("State")
    plt.ylabel("Revenue")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()

def discount_revenue_chart(delivered_df):

    plt.figure(figsize=(8, 5))

    plt.scatter(
        delivered_df["discount"],
        delivered_df["total_amount"]
    )

    plt.title("Discount vs Revenue")
    plt.xlabel("Discount (%)")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.show()