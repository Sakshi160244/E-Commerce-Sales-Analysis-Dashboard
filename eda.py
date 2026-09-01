def perform_eda(df):

    print("\n========== EXPLORATORY DATA ANALYSIS ==========")

    print("\nDataset Shape:")
    print(df.shape)

    print("\nDataset Information:")
    df.info()

    print("\nStatistical Summary:")
    print(df.describe())

    print("\nOrder Status Distribution:")
    print(df["order_status"].value_counts())