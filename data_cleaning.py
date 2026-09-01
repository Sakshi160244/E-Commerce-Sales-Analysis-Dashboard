import pandas as pd


def clean_data(df):

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nData Types:")
    print(df.dtypes)

    df["order_date"] = pd.to_datetime(df["order_date"])

    delivered_df = df[
        df["order_status"] == "Delivered"].copy()

    print("\nUpdated Data Types:")
    print(df.dtypes)

    print("\nDelivered Orders:", len(delivered_df))

    return df, delivered_df