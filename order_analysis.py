import numpy as np
def perform_order_analysis(df):

    status_revenue = (
        df
        .groupby("order_status")["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== ORDER ANALYSIS ==========")

    print("\nOrder Status-wise Revenue:")
    print(status_revenue)

    return status_revenue

def discount_analysis(delivered_df):

    discount_array = delivered_df["discount"].to_numpy()
    revenue_array = delivered_df["total_amount"].to_numpy()

    average_discount = np.mean(discount_array)
    maximum_discount = np.max(discount_array)
    minimum_discount = np.min(discount_array)

    correlation = np.corrcoef(
        discount_array,
        revenue_array
    )[0, 1]

    print("\n========== DISCOUNT ANALYSIS ==========")

    print(
        "Average Discount:",
        round(average_discount, 2),
        "%"
    )

    print(
        "Maximum Discount:",
        round(maximum_discount, 2),
        "%"
    )

    print(
        "Minimum Discount:",
        round(minimum_discount, 2),
        "%"
    )

    print(
        "Discount vs Revenue Correlation:",
        round(correlation, 2)
    )

    return (
        average_discount,
        maximum_discount,
        minimum_discount,
        correlation
    )