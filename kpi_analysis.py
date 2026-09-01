def perform_kpi_analysis(df, delivered_df):

    print("\n========== KPI ANALYSIS ==========")

    # Overall KPIs
    total_orders = df["order_id"].nunique()
    total_customers = df["customer_id"].nunique()
    total_products = df["product_id"].nunique()

    total_revenue = delivered_df["total_amount"].sum()

    # Average Order Value
    aov = delivered_df["total_amount"].mean()

    # Cancellation Rate
    cancelled_orders = (
        df["order_status"] == "Cancelled"
    ).sum()

    cancellation_rate = (
        cancelled_orders / total_orders
    ) * 100

    # Return Rate
    returned_orders = (
        df["order_status"] == "Returned"
    ).sum()

    return_rate = (
        returned_orders / total_orders
    ) * 100

    # Average Quantity
    average_quantity = df["quantity"].mean()

    print("Total Orders:", total_orders)
    print("Total Customers:", total_customers)
    print("Total Products:", total_products)
    print("Total Revenue: ₹", round(total_revenue, 2))
    print("Average Order Value: ₹", round(aov, 2))
    print(
        "Average Quantity per Order:",
        round(average_quantity, 2)
    )
    print(
        "Cancellation Rate:",
        round(cancellation_rate, 2),
        "%"
    )
    print(
        "Return Rate:",
        round(return_rate, 2),
        "%"
    )

    return {
        "total_orders": total_orders,
        "total_customers": total_customers,
        "total_products": total_products,
        "total_revenue": total_revenue,
        "aov": aov,
        "average_quantity": average_quantity,
        "cancellation_rate": cancellation_rate,
        "return_rate": return_rate
    }


