import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from data_cleaning import clean_data

from customer_analysis import (
    perform_customer_analysis,
    gender_analysis,
    age_analysis,
    state_analysis,
)

from product_analysis import perform_product_analysis
from order_analysis import perform_order_analysis, discount_analysis
from kpi_analysis import perform_kpi_analysis


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0F172A 0%, #172554 100%);
}

[data-testid="stSidebar"] * {
    color: white;
}

.dashboard-header {
    padding: 1.2rem 1.4rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #1D4ED8 0%, #2563EB 55%, #3B82F6 100%);
    margin-bottom: 1.25rem;
}

.dashboard-header h1 {
    margin: 0;
    font-size: 2rem;
}

.dashboard-header p {
    margin: .35rem 0 0 0;
    opacity: .8;
}

div[data-testid="stMetric"] {
    border: 1px solid #DBEAFE;
    padding: 16px;
    border-radius: 16px;
    background: #FFFFFF;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,.16);
    padding: .65rem .75rem;
    font-weight: 600;
}

[data-testid="stSidebar"] .stButton > button {
    background: rgba(255,255,255,.08);
    color: white;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: #2563EB;
    border-color: #60A5FA;
}

body {
    background-color: #F8FAFC;
}

h1, h2, h3 {
    color: #0F172A;
}

.dashboard-header h1,
.dashboard-header p {
    color: white !important;
}

[data-testid="stMetricLabel"] {
    color: #475569;
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    color: #0F172A;
    font-weight: 700;
}

[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
}

[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,.15);
}

[data-testid="stSidebar"] .stButton > button {
    text-align: left;
    transition: all .2s ease;
}

[data-testid="stSidebar"] .stButton > button:hover {
    transform: translateX(3px);
}

.stAlert {
    border-radius: 14px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dashboard-header">
    <h1>E-Commerce Sales Analysis Dashboard</h1>
    <p>Interactive sales, customer, product, order and KPI analysis</p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# CSV DATA LOADING
# ==========================================

@st.cache_data
def get_data():
    df = pd.read_csv("sales_data.csv")
    df, delivered_df = clean_data(df)
    return df, delivered_df


@st.cache_data
def get_payment_data():
    return pd.read_csv("payments_summary.csv")


try:
    df, delivered_df = get_data()
    payment_df = get_payment_data()

except Exception as e:
    st.error("CSV data load nahi ho paya.")
    st.error(e)
    st.stop()


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.markdown("## Navigation")
st.sidebar.caption("Choose a section")

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

nav_items = [
    ("Dashboard", "Dashboard"),
    ("EDA", "EDA"),
    ("Customer Analysis", "Customer Analysis"),
    ("Product Analysis", "Product Analysis"),
    ("Order Analysis", "Order Analysis"),
    ("Payment Analysis", "Payment Analysis"),
    ("KPI Analysis", "KPI Analysis"),
    ("Visualizations", "Visualizations"),
    ("Business Insights", "Business Insights"),
]

for label, value in nav_items:
    if st.sidebar.button(label, use_container_width=True, key=f"nav_{value}"):
        st.session_state.page = value

choice = st.session_state.page

st.sidebar.divider()
st.sidebar.caption("E-Commerce Sales Data Analysis")


# ==========================================
# DASHBOARD
# ==========================================

if choice == "Dashboard":

    st.header("Dashboard Overview")

    kpis = perform_kpi_analysis(df, delivered_df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Revenue",
        f"₹{kpis['total_revenue']:,.2f}"
    )

    col2.metric(
        "Total Orders",
        kpis["total_orders"]
    )

    col3.metric(
        "Total Customers",
        kpis["total_customers"]
    )

    col4.metric(
        "Average Order Value",
        f"₹{kpis['aov']:,.2f}"
    )

    col5, col6, col7 = st.columns(3)

    col5.metric(
        "Total Products",
        kpis["total_products"]
    )

    col6.metric(
        "Cancellation Rate",
        f"{kpis['cancellation_rate']:.2f}%"
    )

    col7.metric(
        "Return Rate",
        f"{kpis['return_rate']:.2f}%"
    )

    st.subheader("Sales Data")

    st.dataframe(
        df,
        use_container_width=True
    )


# ==========================================
# EDA
# ==========================================

elif choice == "EDA":

    st.header("Exploratory Data Analysis")

    st.subheader("Dataset Shape")

    col1, col2 = st.columns(2)

    col1.metric(
        "Rows",
        df.shape[0]
    )

    col2.metric(
        "Columns",
        df.shape[1]
    )

    st.subheader("Dataset")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader("Statistical Summary")

    st.dataframe(
        df.describe(),
        use_container_width=True
    )

    st.subheader("Missing Values")

    st.dataframe(
        df.isnull().sum().to_frame("Missing Values"),
        use_container_width=True
    )

    st.subheader("Order Status Distribution")

    st.dataframe(
        df["order_status"]
        .value_counts()
        .to_frame("Orders"),
        use_container_width=True
    )


# ==========================================
# CUSTOMER ANALYSIS
# ==========================================

elif choice == "Customer Analysis":

    st.header("Customer Analysis")

    (
        customer_spending_df,
        customer_order_count,
        top_customer,
        repeat_customers,
        repeat_customer_rate,
        average_orders_per_customer,
    ) = perform_customer_analysis(delivered_df)

    gender_revenue, gender_avg_spending = gender_analysis(
        delivered_df
    )

    age_revenue, age_avg_spending = age_analysis(
        delivered_df
    )

    state_revenue = state_analysis(
        delivered_df
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Top Customer",
        top_customer["customer_name"]
    )

    col2.metric(
        "Repeat Customers",
        repeat_customers
    )

    col3.metric(
        "Repeat Customer Rate",
        f"{repeat_customer_rate:.2f}%"
    )

    st.subheader("Customer Spending")

    st.dataframe(
        customer_spending_df,
        use_container_width=True
    )

    st.subheader("Gender-wise Revenue")

    st.bar_chart(
        gender_revenue
    )

    st.subheader("Age Group Revenue")

    st.bar_chart(
        age_revenue
    )

    st.subheader("State-wise Revenue")

    st.bar_chart(
        state_revenue
    )


# ==========================================
# PRODUCT ANALYSIS
# ==========================================

elif choice == "Product Analysis":

    st.header("Product Analysis")

    (
        category_performance,
        top_category,
        top_product,
        top_revenue_product,
        top_products_quantity,
    ) = perform_product_analysis(delivered_df)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Top Category",
        top_category
    )

    col2.metric(
        "Top Selling Product",
        top_product
    )

    col3.metric(
        "Top Revenue Product",
        top_revenue_product
    )

    st.subheader("Category Performance")

    st.dataframe(
        category_performance,
        use_container_width=True
    )

    st.subheader("Category Revenue")

    st.bar_chart(
        category_performance["total_revenue"]
    )

    st.subheader("Top Products")

    st.bar_chart(
        top_products_quantity
    )


# ==========================================
# ORDER ANALYSIS
# ==========================================

elif choice == "Order Analysis":

    st.header("Order Analysis")

    status_revenue = perform_order_analysis(df)

    (
        average_discount,
        maximum_discount,
        minimum_discount,
        discount_correlation,
    ) = discount_analysis(delivered_df)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Average Discount",
        f"{average_discount:.2f}%"
    )

    col2.metric(
        "Maximum Discount",
        f"{maximum_discount:.2f}%"
    )

    col3.metric(
        "Minimum Discount",
        f"{minimum_discount:.2f}%"
    )

    st.subheader("Order Status Revenue")

    st.bar_chart(
        status_revenue
    )


# ==========================================
# PAYMENT ANALYSIS
# ==========================================

elif choice == "Payment Analysis":

    st.header("Payment Analysis")

    st.dataframe(
        payment_df,
        use_container_width=True
    )

    st.bar_chart(
        payment_df.set_index(
            "payment_method"
        )["total_payments"]
    )


# ==========================================
# KPI ANALYSIS
# ==========================================

elif choice == "KPI Analysis":

    st.header("KPI Analysis")

    kpis = perform_kpi_analysis(
        df,
        delivered_df
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Orders",
        kpis["total_orders"]
    )

    col2.metric(
        "Total Customers",
        kpis["total_customers"]
    )

    col3.metric(
        "Total Products",
        kpis["total_products"]
    )

    col4, col5 = st.columns(2)

    col4.metric(
        "Total Revenue",
        f"₹{kpis['total_revenue']:,.2f}"
    )

    col5.metric(
        "Average Order Value",
        f"₹{kpis['aov']:,.2f}"
    )

    col6, col7 = st.columns(2)

    col6.metric(
        "Cancellation Rate",
        f"{kpis['cancellation_rate']:.2f}%"
    )

    col7.metric(
        "Return Rate",
        f"{kpis['return_rate']:.2f}%"
    )


# ==========================================
# VISUALIZATIONS
# ==========================================

elif choice == "Visualizations":

    st.header("Visualizations")

    (
        customer_spending_df,
        customer_order_count,
        top_customer,
        repeat_customers,
        repeat_customer_rate,
        average_orders_per_customer,
    ) = perform_customer_analysis(delivered_df)

    (
        category_performance,
        top_category,
        top_product,
        top_revenue_product,
        top_products_quantity,
    ) = perform_product_analysis(delivered_df)

    gender_revenue, gender_avg_spending = gender_analysis(
        delivered_df
    )

    age_revenue, age_avg_spending = age_analysis(
        delivered_df
    )

    state_revenue = state_analysis(
        delivered_df
    )

    chart_choice = st.selectbox(
        "Select Chart",
        [
            "Monthly Revenue",
            "Category Revenue",
            "Category Quantity",
            "Top Products",
            "Top Customers",
            "Order Status",
            "Customer Segment",
            "Gender Revenue",
            "Gender Average Spending",
            "Age Revenue",
            "Age Average Spending",
            "State Revenue",
            "Discount vs Revenue",
        ]
    )


    if chart_choice == "Monthly Revenue":

        monthly_revenue = (
            delivered_df
            .groupby(
                delivered_df["order_date"].dt.month
            )["total_amount"]
            .sum()
        )

        st.line_chart(
            monthly_revenue
        )


    elif chart_choice == "Category Revenue":

        st.bar_chart(
            category_performance[
                "total_revenue"
            ]
        )


    elif chart_choice == "Category Quantity":

        st.bar_chart(
            category_performance[
                "total_quantity"
            ]
        )


    elif chart_choice == "Top Products":

        st.bar_chart(
            top_products_quantity
        )


    elif chart_choice == "Top Customers":

        top_customers = (
            customer_spending_df
            .sort_values(
                "total_amount",
                ascending=False
            )
            .head(5)
        )

        st.bar_chart(
            top_customers.set_index(
                "customer_name"
            )["total_amount"]
        )


    elif chart_choice == "Order Status":

        st.bar_chart(
            df["order_status"]
            .value_counts()
        )


    elif chart_choice == "Customer Segment":

        st.bar_chart(
            customer_spending_df[
                "customer_segment"
            ]
            .value_counts()
        )


    elif chart_choice == "Gender Revenue":

        st.bar_chart(
            gender_revenue
        )


    elif chart_choice == "Gender Average Spending":

        st.bar_chart(
            gender_avg_spending
        )


    elif chart_choice == "Age Revenue":

        st.bar_chart(
            age_revenue
        )


    elif chart_choice == "Age Average Spending":

        st.bar_chart(
            age_avg_spending
        )


    elif chart_choice == "State Revenue":

        st.bar_chart(
            state_revenue
        )


    elif chart_choice == "Discount vs Revenue":

        st.scatter_chart(
            delivered_df,
            x="discount",
            y="total_amount"
        )


# ==========================================
# BUSINESS INSIGHTS
# ==========================================

elif choice == "Business Insights":

    st.header("Business Insights")

    (
        customer_spending_df,
        customer_order_count,
        top_customer,
        repeat_customers,
        repeat_customer_rate,
        average_orders_per_customer,
    ) = perform_customer_analysis(delivered_df)

    (
        category_performance,
        top_category,
        top_product,
        top_revenue_product,
        top_products_quantity,
    ) = perform_product_analysis(delivered_df)

    kpis = perform_kpi_analysis(
        df,
        delivered_df
    )

    state_revenue = state_analysis(
        delivered_df
    )

    st.success(
        f"Total Revenue: ₹{kpis['total_revenue']:,.2f}"
    )

    st.info(
        f"Top Category: {top_category}"
    )

    st.info(
        f"Top Selling Product: {top_product}"
    )

    st.info(
        f"Top Revenue Product: {top_revenue_product}"
    )

    st.info(
        f"Top Customer: {top_customer['customer_name']}"
    )

    st.info(
        f"Top State: {state_revenue.idxmax()}"
    )

    st.info(
        f"Repeat Customers: {repeat_customers}"
    )

    st.info(
        f"Repeat Customer Rate: {repeat_customer_rate:.2f}%"
    )

    st.warning(
        f"Cancellation Rate: {kpis['cancellation_rate']:.2f}%"
    )

    st.warning(
        f"Return Rate: {kpis['return_rate']:.2f}%"
    )