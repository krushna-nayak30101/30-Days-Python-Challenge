# Topic


** Challenge - Build Your Mini Project in Python **

🧠 What I Learned (Day 1 to Day 28 Concepts in Action):
-  ✅ Variables, Loops, Functions
-  ✅ File handling with CSV
-  ✅ Pandas for data cleaning, grouping, aggregation
-  ✅ Matplotlib for visualization
-  ✅ Modular, clean coding structure
-  ✅ Streamlit for building an interactive web dashboard


💡 Key Features:
-  📥 Upload sales CSV files
-  📊 Calculate total revenue and quantity sold
-  📦 Identify top-performing and low-performing products
-  📈 Visualize monthly revenue trends
-  🏷️ Track revenue by product category
-  📉 Spot sales drop periods or slumps

```

# Mini - Retail Dashboard using Streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------ 1. Load and Clean Data ------------------
def load_sales_data(filepath):
    try:
        df = pd.read_csv(filepath)
        df.dropna(inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Revenue'] = df['Quantity'] * df['Price']
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# ------------------ 2. Generate Summary ------------------
def generate_summary(df):
    total_revenue = df['Revenue'].sum()
    total_quantity = df['Quantity'].sum()
    average_order_value = total_revenue / df.shape[0]
    units_per_transaction = df['Quantity'].mean()
    return total_revenue, total_quantity, average_order_value, units_per_transaction

# ------------------ 3. Visualize Data ------------------
def visualize_monthly_sales(df):
    monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Revenue'].sum()
    fig, ax = plt.subplots()
    monthly_sales.plot(kind='line', title='Monthly Revenue', ax=ax)
    ax.set_xlabel('Month')
    ax.set_ylabel('Revenue')
    ax.grid(True)
    st.pyplot(fig)

# ------------------ 4. Additional KPIs ------------------
def show_category_revenue(df):
    category_revenue = df.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
    st.subheader("🏷️ Revenue by Category")
    st.bar_chart(category_revenue)

def show_low_performing_products(df):
    low_performers = df.groupby('Product')['Quantity'].sum()
    low_performers = low_performers[low_performers < 30]
    st.subheader("⚠️ Low Performing Products (Under 30 Units Sold)")
    st.dataframe(low_performers.reset_index().rename(columns={'Quantity': 'Units Sold'}))

# ------------------ 5. Streamlit App ------------------
def main():
    st.title("🛍️ Enhanced Retail Sales Dashboard")
    st.write("Analyze your retail sales data interactively with enhanced KPIs.")

    uploaded_file = st.file_uploader("Upload sales CSV file", type=["csv"])
    if uploaded_file is not None:
        df = load_sales_data(uploaded_file)
        if df is not None:
            st.subheader("📊 Sales Summary")
            total_revenue, total_quantity, aov, upt = generate_summary(df)
            st.metric(label="Total Revenue", value=f"₹{total_revenue:,.2f}")
            st.metric(label="Total Quantity Sold", value=total_quantity)
            st.metric(label="Average Order Value", value=f"₹{aov:,.2f}")
            st.metric(label="Units per Transaction", value=f"{upt:.2f}")

            st.subheader("📈 Monthly Revenue Trend")
            visualize_monthly_sales(df)

            show_category_revenue(df)
            show_low_performing_products(df)

if __name__ == '__main__':
    main()
```

🧩 This project helped me understand how Python ties together in a real business use case.


#Python #DataAnalysis #RetailAnalytics #Streamlit #MiniProject #LearnByDoing #CleanCode #PythonProjects #DataVisualization
