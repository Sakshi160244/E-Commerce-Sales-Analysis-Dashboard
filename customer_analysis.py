import numpy as np
import pandas as pd

def perform_customer_analysis(delivered_df):

    print("\n========== CUSTOMER ANALYSIS ==========")

    # Customer-wise spending
    customer_spending = (
        delivered_df
        .groupby(["customer_id", "customer_name"])["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )

    customer_spending_df = customer_spending.reset_index()

    # Customer segmentation
    customer_spending_df["customer_segment"] = np.select(
        [
            customer_spending_df["total_amount"] >= 50000,
            customer_spending_df["total_amount"] >= 20000
        ],
        [
            "High Spender",
            "Medium Spender"
        ],
        default="Low Spender"
    )

    # Top customer
    top_customer = customer_spending_df.iloc[0]

    # Repeat customer analysis
    customer_order_count = (
        delivered_df
        .groupby(["customer_id", "customer_name"])["order_id"]
        .nunique()
        .sort_values(ascending=False)
    )

    repeat_customers = (customer_order_count >= 2).sum()

    total_active_customers = len(customer_order_count)

    repeat_customer_rate = (
        repeat_customers / total_active_customers
    ) * 100

    average_orders_per_customer = customer_order_count.mean()
    

    # Output
    print("\nTop Customer:", top_customer["customer_name"])
    print(
        "Top Customer Spending: ₹",
        round(top_customer["total_amount"], 2)
    )

    print("Repeat Customers:", repeat_customers)

    print(
        "Repeat Customer Rate:",
        round(repeat_customer_rate, 2),
        "%"
    )

    print(
        "Average Orders per Customer:",
        round(average_orders_per_customer, 2)
    )

    print("\nCustomer Segments:")
    print(
        customer_spending_df["customer_segment"]
        .value_counts()
    )

    return (
        customer_spending_df,
        customer_order_count,
        top_customer,
        repeat_customers,
        repeat_customer_rate,
        average_orders_per_customer
    )

def gender_analysis(delivered_df):

    gender_revenue = (
        delivered_df
        .groupby("gender")["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )

    gender_avg_spending = (
        delivered_df
        .groupby("gender")["total_amount"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\n========== GENDER ANALYSIS ==========")

    print("\nGender-wise Revenue:")
    print(gender_revenue)

    print("\nGender-wise Average Spending:")
    print(gender_avg_spending)

    return gender_revenue, gender_avg_spending



def age_analysis(delivered_df):

    age_bins = [0, 25, 35, 50, 100]

    age_labels = [
        "18-25",
        "26-35",
        "36-50",
        "51+"
    ]

    delivered_df = delivered_df.copy()

    delivered_df["age_group"] = pd.cut(
        delivered_df["age"],
        bins=age_bins,
        labels=age_labels
    )

    age_revenue = (
        delivered_df
        .groupby("age_group", observed=True)["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )

    age_avg_spending = (
        delivered_df
        .groupby("age_group", observed=True)["total_amount"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\n========== AGE GROUP ANALYSIS ==========")

    print("\nAge Group-wise Revenue:")
    print(age_revenue)

    print("\nAge Group-wise Average Spending:")
    print(age_avg_spending)

    return age_revenue, age_avg_spending


def state_analysis(delivered_df):

    state_revenue = (
        delivered_df
        .groupby("state")["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== STATE ANALYSIS ==========")

    print("\nState-wise Revenue:")
    print(state_revenue)

    return state_revenue