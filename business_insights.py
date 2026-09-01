def generate_business_insights(
    delivered_df,
    kpis,
    top_category,
    top_product,
    top_revenue_product,
    top_customer,
    repeat_customers,
    repeat_customer_rate
):

    state_revenue = (
        delivered_df.groupby("state")["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== FINAL BUSINESS INSIGHTS ==========")

    print(
        "Total Revenue: ₹",
        round(kpis["total_revenue"], 2)
    )

    print(
        "Average Order Value: ₹",
        round(kpis["aov"], 2)
    )

    print("Top Category:", top_category)

    print("Top Selling Product:", top_product)

    print(
        "Top Revenue Product:",
        top_revenue_product
    )

    print(
        "Top Customer:",
        top_customer["customer_name"]
    )

    print(
        "Top State:",
        state_revenue.idxmax()
    )

    print(
        "Repeat Customers:",
        repeat_customers
    )

    print(
        "Repeat Customer Rate:",
        round(repeat_customer_rate, 2),
        "%"
    )

    print(
        "Cancellation Rate:",
        round(kpis["cancellation_rate"], 2),
        "%"
    )

    print(
        "Return Rate:",
        round(kpis["return_rate"], 2),
        "%"
    )