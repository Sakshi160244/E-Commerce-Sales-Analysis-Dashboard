def perform_product_analysis(delivered_df):

    print("\n========== PRODUCT ANALYSIS ==========")

    # Category performance
    category_performance = (
        delivered_df
        .groupby("category")
        .agg(
            total_revenue=("total_amount", "sum"),
            total_quantity=("quantity", "sum")
        )
        .sort_values(
            "total_revenue",
            ascending=False
        )
    )

    # Top category
    top_category = category_performance[
        "total_revenue"
    ].idxmax()

    # Product-wise quantity
    product_quantity = (
        delivered_df
        .groupby("product_name")["quantity"]
        .sum()
        .sort_values(ascending=False)
    )
    top_products_quantity = product_quantity.head(10)

    # Top selling product
    top_product = product_quantity.idxmax()
    top_product_quantity = product_quantity.max()

    # Product-wise revenue
    product_revenue = (
        delivered_df
        .groupby("product_name")["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )

    # Top revenue product
    top_revenue_product = product_revenue.idxmax()
    top_revenue = product_revenue.max()

    print("\nTop Category:", top_category)

    print(
        "Top Selling Product:",
        top_product
    )

    print(
        "Quantity Sold:",
        top_product_quantity
    )
    print("\nTop 10 Products by Quantity Sold:")
    print(top_products_quantity)

    print(
        "Top Revenue Product:",
        top_revenue_product
    )

    print(
        "Revenue: ₹",
        round(top_revenue, 2)
    )

    print("\nCategory Performance:")
    print(category_performance)

    return (
        category_performance,
        top_category,
        top_product,
        top_revenue_product,
        top_products_quantity
    )