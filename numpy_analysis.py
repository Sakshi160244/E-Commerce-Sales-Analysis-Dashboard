import numpy as np


def perform_numpy_analysis(delivered_df):

    revenue = delivered_df["total_amount"].to_numpy()

    mean_revenue = np.mean(revenue)
    max_revenue = np.max(revenue)
    min_revenue = np.min(revenue)
    revenue_std = np.std(revenue)

    correlation = np.corrcoef(
        delivered_df["quantity"],
        delivered_df["total_amount"]
    )[0, 1]

    print("\n========== NUMPY ANALYSIS ==========")

    print("Mean Revenue:", round(mean_revenue, 2))
    print("Maximum Revenue:", round(max_revenue, 2))
    print("Minimum Revenue:", round(min_revenue, 2))
    print("Revenue Standard Deviation:", round(revenue_std, 2))
    print(
        "Quantity vs Revenue Correlation:",
        round(correlation, 2)
    )