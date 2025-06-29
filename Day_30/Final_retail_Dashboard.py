import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# --- Page Configuration ---
st.set_page_config(
    page_title="Interactive Retail Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Retail Performance Dashboard")
st.markdown("Explore key retail metrics and trends.")

# --- Custom CSS for KPI Cards (Power BI Style) ---
# Inject custom CSS to style the KPI cards
st.markdown("""
<style>
    /* Main KPI Card Container */
    .kpi-card {
        background-color: #f0f2f6; /* Light grey background for cards */
        border-radius: 8px;
        padding: 15px 20px; /* Internal padding of the card */
        margin-bottom: 15px; /* Space between cards */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05); /* Subtle shadow */
        display: flex; /* Use flex to align content inside */
        align-items: flex-start; /* Align content to the top-left */
        overflow: hidden; /* Ensures the border is contained */
        position: relative;
    }

    /* Left border styles for different KPI colors */
    .kpi-card.sales {
        border-left: 8px solid #4CAF50; /* Green for Sales */
    }
    .kpi-card.profit {
        border-left: 8px solid #2196F3; /* Blue for Profit */
    }
    .kpi-card.aov {
        border-left: 8px solid #FFC107; /* Amber for AOV */
    }
    .kpi-card.quantity {
        border-left: 8px solid #9C27B0; /* Purple for Quantity */
    }
    .kpi-card.margin {
        border-left: 8px solid #F44336; /* Red for Margin */
    }
    .kpi-card.customers {
        border-left: 8px solid #607D8B; /* Blue Grey for Customers */
    }
    .kpi-card.transactions {
        border-left: 8px solid #00BCD4; /* Cyan for Transactions */
    }
    .kpi-card.arpu {
        border-left: 8px solid #FF9800; /* Orange for ARPU */
    }

    /* --- Styling for the content INSIDE the custom KPI card --- */
    .kpi-content {
        display: flex;
        flex-direction: column; /* Stack label, value, delta vertically */
        align-items: flex-start; /* Align text to the left */
        flex-grow: 1; /* Allow content to take available space */
    }

    .kpi-label {
        font-size: 1.0em; /* Slightly smaller label */
        color: #555;
        margin-bottom: 5px; /* Space between label and value */
    }

    .kpi-value {
        font-size: 2.2em; /* Make value significantly more prominent */
        font-weight: bold;
        color: #333;
        line-height: 1.1; /* Adjust line height for better spacing */
        margin-bottom: 0px; /* No space below value if delta is present */
    }

    .kpi-delta {
        font-size: 0.9em;
        margin-top: 5px; /* Space above delta */
    }

    /* Specific delta colors */
    .kpi-delta.green { color: #4CAF50; }
    .kpi-delta.red { color: #F44336; }
    .kpi-delta.gray { color: #666; } /* Neutral color for non-positive/negative deltas */

</style>
""", unsafe_allow_html=True)

# --- 1. Data Generation (Sample Data) ---
@st.cache_data
def generate_sample_data(num_rows=50000): # Increased num_rows for more data points and better trend visibility
    """Generates a sample retail sales dataset with asymmetrical trends, seasonality,
       and variability across regions and customer segments.
    """
    start_date = datetime(2022, 1, 1) # Start earlier to show more trend
    dates = pd.to_datetime([start_date + timedelta(days=np.random.randint(0, 365 * 3)) for _ in range(num_rows)]) # 3 years of data
    
    df_temp = pd.DataFrame({'Date': dates})
    df_temp.sort_values(by='Date', inplace=True)
    df_temp['Day_of_Year'] = df_temp['Date'].dt.dayofyear
    df_temp['Month'] = df_temp['Date'].dt.month
    df_temp['Year'] = df_temp['Date'].dt.year

    categories = ['Electronics', 'Apparel', 'Home Goods', 'Books', 'Groceries', 'Beauty', 'Outdoors', 'Tools']
    regions = ['North', 'South', 'East', 'West', 'Central', 'Midwest', 'Southeast']
    segments = ['Consumer', 'Corporate', 'Home Office', 'Small Business']
    customer_ids = [f'CUST{i:05d}' for i in range(int(num_rows * 0.7))]

    # Assign categories, regions, segments first for multipliers
    df_temp['Category'] = np.random.choice(categories, num_rows)
    df_temp['Region'] = np.random.choice(regions, num_rows)
    df_temp['Customer Segment'] = np.random.choice(segments, num_rows)

    # Base sales with an upward trend over time
    base_sales = 100 + (df_temp['Year'] - df_temp['Year'].min()) * 50 + np.random.normal(0, 20, num_rows)

    # Seasonality (e.g., higher sales in Q4, lower in Q1)
    seasonal_factor = np.sin((df_temp['Month'] - 1) * (2 * np.pi / 12)) * 50 + 50 # Peaks around month 4-6, troughs around 10-12
    # Adjust seasonality to be higher in Nov/Dec (months 11, 12)
    seasonal_factor = np.where(df_temp['Month'].isin([11, 12]), seasonal_factor + 100, seasonal_factor) # Boost for holidays
    seasonal_factor = np.where(df_temp['Month'].isin([1, 2]), seasonal_factor - 30, seasonal_factor) # Dip for Jan/Feb

    # --- Introduce Region-specific and Segment-specific multipliers ---
    region_multipliers = {
        'North': 1.2,
        'South': 0.8,
        'East': 1.1,
        'West': 0.9,
        'Central': 1.0,
        'Midwest': 0.95,
        'Southeast': 1.05
    }
    segment_multipliers = {
        'Consumer': 1.0,
        'Corporate': 1.5,   # Corporate customers might have higher sales per transaction
        'Home Office': 0.7, # Home office might have lower sales
        'Small Business': 1.1
    }

    # Map multipliers to the DataFrame
    df_temp['Region_Multiplier'] = df_temp['Region'].map(region_multipliers)
    df_temp['Segment_Multiplier'] = df_temp['Customer Segment'].map(segment_multipliers)

    # Combine all factors for final sales calculation
    # Ensure multipliers are not NaN if a key is missing (though our maps cover all generated values)
    sales = np.maximum(10, base_sales * df_temp['Region_Multiplier'] * df_temp['Segment_Multiplier'] + seasonal_factor + np.random.normal(0, 30, num_rows)) # Add daily noise


    quantity = np.floor(sales / np.random.uniform(10, 100, num_rows)) # Quantity derived from sales
    quantity = np.maximum(1, quantity).astype(int) # Ensure quantity is at least 1

    profit_margin_base = np.random.uniform(0.15, 0.35, num_rows)
    # Apply segment multiplier to profit as well, corporate might have higher profit margins too
    profit_margin_adjusted = profit_margin_base * (1 + (df_temp['Segment_Multiplier'] - 1) * 0.2) # Adjust profit margin slightly based on segment
    profit = sales * profit_margin_adjusted - np.random.uniform(5, 50, num_rows) # Profit can still be negative sometimes


    data = pd.DataFrame({
        'Date': df_temp['Date'],
        'Sales': sales,
        'Quantity': quantity,
        'Profit': profit,
        'Category': df_temp['Category'],
        'Region': df_temp['Region'],
        'Customer Segment': df_temp['Customer Segment'],
        'Customer_ID': np.random.choice(customer_ids, num_rows)
    })
    
    data.sort_values(by='Date', inplace=True)
    return data

df = generate_sample_data()

# --- 2. Sidebar Filters ---
st.sidebar.header("Filter Options")

# Date Range Slider
min_date = df['Date'].min().to_pydatetime().date()
max_date = df['Date'].max().to_pydatetime().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Ensure date_range has two dates
if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = df[(df['Date'].dt.date >= start_date) & (df['Date'].dt.date <= end_date)]
elif len(date_range) == 1:
    # If only one date is selected, treat it as the start date and filter up to max_date
    start_date = date_range[0]
    filtered_df = df[(df['Date'].dt.date >= start_date) & (df['Date'].dt.date <= max_date)]
else:
    # No date selected, or invalid selection, show all data
    filtered_df = df
    st.sidebar.warning("Please select a valid date range.")

# Category Filter
selected_categories = st.sidebar.multiselect(
    "Select Category",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)
filtered_df = filtered_df[filtered_df['Category'].isin(selected_categories)]

# Region Filter
selected_regions = st.sidebar.multiselect(
    "Select Region",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)
filtered_df = filtered_df[filtered_df['Region'].isin(selected_regions)]

# Customer Segment Filter
selected_segments = st.sidebar.multiselect(
    "Select Customer Segment",
    options=df['Customer Segment'].unique(),
    default=df['Customer Segment'].unique()
)
filtered_df = filtered_df[filtered_df['Customer Segment'].isin(selected_segments)]

# Check if filtered_df is empty
if filtered_df.empty:
    st.warning("No data available for the selected filters. Please adjust your selections.")
    st.stop()

# --- 3. Key Performance Indicators (KPIs) ---
st.header("Key Performance Indicators")

# Custom function to display KPI cards with direct HTML rendering
def display_kpi_card(label, value, delta=None, delta_color_style="normal", card_class=""):
    """Displays a KPI in a custom card style with label and value inside."""
    delta_html = ""
    if delta is not None:
        delta_class = "gray" # Default neutral color
        # Determine delta color based on numerical value if possible
        if isinstance(delta, (int, float)):
            if delta_color_style == "normal": # Green for positive, Red for negative (e.g., Sales, Profit)
                if delta > 0:
                    delta_class = "green"
                elif delta < 0:
                    delta_class = "red"
            elif delta_color_style == "inverse": # Red for positive, Green for negative (e.g., Returns, Costs)
                if delta > 0:
                    delta_class = "red"
                elif delta < 0:
                    delta_class = "green"
        # If delta is a string (e.g., "+$50,000"), we rely on it being formatted with sign
        # For simple string deltas, we just assign color based on explicit text like "+" or "-"
        elif isinstance(delta, str):
            if delta.startswith('+'):
                delta_class = "green"
            elif delta.startswith('-'):
                delta_class = "red"
            else: # For string deltas like "N/A", they will be gray
                delta_class = "gray"

        delta_html = f'<div class="kpi-delta {delta_class}">{delta}</div>'

    # Construct the entire card's inner HTML
    card_inner_html = f"""
        <div class="kpi-content">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            {delta_html}
        </div>
    """
    # Now, wrap it in the outer card div
    st.markdown(
        f"""
        <div class="kpi-card {card_class}">
            {card_inner_html}
        </div>
        """,
        unsafe_allow_html=True
    )


# Split KPIs into two rows for better layout
col1, col2, col3, col4 = st.columns(4)
col5, col6, col7, col8 = st.columns(4) # New row for additional KPIs

with col1:
    total_sales = filtered_df['Sales'].sum()
    
    end_date_dt = end_date
    start_date_dt = start_date
    current_period_duration = (end_date_dt - start_date_dt).days + 1
    prev_end_date = start_date_dt - timedelta(days=1)
    prev_start_date = prev_end_date - timedelta(days=current_period_duration - 1)
    prev_period_df = df[(df['Date'].dt.date >= prev_start_date) & (df['Date'].dt.date <= prev_end_date)]
    prev_total_sales = prev_period_df['Sales'].sum()

    delta_sales_str = None # Default to None to hide if no previous data
    if prev_total_sales != 0:
        delta_sales_val = total_sales - prev_total_sales
        delta_sales_str = f"{'+' if delta_sales_val > 0 else ''}{delta_sales_val:,.2f}"
    
    display_kpi_card("Total Sales", f"${total_sales:,.2f}", delta=delta_sales_str, delta_color_style="normal", card_class="sales")

with col2:
    total_profit = filtered_df['Profit'].sum()
    prev_total_profit = prev_period_df['Profit'].sum() # Assuming prev_period_df is calculated above

    delta_profit_str = None
    if prev_total_profit != 0:
        delta_profit_val = total_profit - prev_total_profit
        delta_profit_str = f"{'+' if delta_profit_val > 0 else ''}{delta_profit_val:,.2f}"
    display_kpi_card("Total Profit", f"${total_profit:,.2f}", delta=delta_profit_str, delta_color_style="normal", card_class="profit")

with col3:
    if len(filtered_df) > 0:
        avg_order_value = filtered_df['Sales'].mean()
        prev_avg_order_value = prev_period_df['Sales'].mean() if len(prev_period_df) > 0 else 0
        
        delta_aov_str = None
        if prev_avg_order_value != 0:
            delta_aov_val = avg_order_value - prev_avg_order_value
            delta_aov_str = f"{'+' if delta_aov_val > 0 else ''}{delta_aov_val:,.2f}"
        display_kpi_card("Average Order Value", f"${avg_order_value:,.2f}", delta=delta_aov_str, delta_color_style="normal", card_class="aov")
    else:
        display_kpi_card("Average Order Value", "$0.00", card_class="aov")

with col4:
    total_quantity = filtered_df['Quantity'].sum()
    prev_total_quantity = prev_period_df['Quantity'].sum()

    delta_quantity_str = None
    if prev_total_quantity != 0:
        delta_quantity_val = total_quantity - prev_total_quantity
        delta_quantity_str = f"{'+' if delta_quantity_val > 0 else ''}{int(delta_quantity_val):,}"
    display_kpi_card("Total Quantity Sold", f"{int(total_quantity):,}", delta=delta_quantity_str, delta_color_style="normal", card_class="quantity")

# --- Additional KPIs ---
with col5:
    if total_sales > 0: # Check total_sales for profit margin calculation
        profit_margin_pct = (total_profit / total_sales) * 100
        prev_profit_margin_pct = (prev_total_profit / prev_total_sales) * 100 if prev_total_sales > 0 else 0
        
        delta_margin_str = None
        if prev_profit_margin_pct != 0:
            delta_margin_val = profit_margin_pct - prev_profit_margin_pct
            delta_margin_str = f"{'+' if delta_margin_val > 0 else ''}{delta_margin_val:,.2f}%"
        display_kpi_card("Profit Margin (%)", f"{profit_margin_pct:,.2f}%", delta=delta_margin_str, delta_color_style="normal", card_class="margin")
    else:
        display_kpi_card("Profit Margin (%)", "0.00%", card_class="margin")

with col6:
    num_unique_customers = filtered_df['Customer_ID'].nunique()
    prev_num_unique_customers = prev_period_df['Customer_ID'].nunique()

    delta_customers_str = None
    if prev_num_unique_customers != 0:
        delta_customers_val = num_unique_customers - prev_num_unique_customers
        delta_customers_str = f"{'+' if delta_customers_val > 0 else ''}{int(delta_customers_val):,}"
    display_kpi_card("Unique Customers", f"{num_unique_customers:,}", delta=delta_customers_str, delta_color_style="normal", card_class="customers")

with col7:
    num_transactions = len(filtered_df)
    prev_num_transactions = len(prev_period_df)

    delta_transactions_str = None
    if prev_num_transactions != 0:
        delta_transactions_val = num_transactions - prev_num_transactions
        delta_transactions_str = f"{'+' if delta_transactions_val > 0 else ''}{int(delta_transactions_val):,}"
    display_kpi_card("Total Transactions", f"{num_transactions:,}", delta=delta_transactions_str, delta_color_style="normal", card_class="transactions")

with col8:
    if total_quantity > 0: # Check total_quantity for ARPU calculation
        avg_revenue_per_unit = total_sales / total_quantity
        prev_avg_revenue_per_unit = prev_period_df['Sales'].sum() / prev_period_df['Quantity'].sum() if prev_period_df['Quantity'].sum() > 0 else 0
        
        delta_arpu_str = None
        if prev_avg_revenue_per_unit != 0:
            delta_arpu_val = avg_revenue_per_unit - prev_avg_revenue_per_unit
            delta_arpu_str = f"{'+' if delta_arpu_val > 0 else ''}{delta_arpu_val:,.2f}"
        display_kpi_card("Avg Revenue per Unit", f"${avg_revenue_per_unit:,.2f}", delta=delta_arpu_str, delta_color_style="normal", card_class="arpu")
    else:
        display_kpi_card("Avg Revenue per Unit", "$0.00", card_class="arpu")


# --- 4. Interactive Visualizations ---
st.header("Data Trends and Distributions")

tab1, tab2, tab3, tab4 = st.tabs(["Sales Over Time", "Sales by Category", "Sales by Region", "Profit by Segment"])

with tab1:
    st.subheader("Sales Trend Over Time")
    # Group by date for line chart
    # Use 'W' for weekly aggregation for better trend visibility with more data
    sales_over_time = filtered_df.groupby(pd.Grouper(key='Date', freq='W'))['Sales'].sum().reset_index()
    fig_sales_time = px.line(
        sales_over_time,
        x='Date',
        y='Sales',
        title='Weekly Sales Trend',
        labels={'Date': 'Date', 'Sales': 'Sales ($)'}
    )
    fig_sales_time.update_xaxes(rangeslider_visible=True)
    st.plotly_chart(fig_sales_time, use_container_width=True)

with tab2:
    st.subheader("Sales by Product Category")
    sales_by_category = filtered_df.groupby('Category')['Sales'].sum().sort_values(ascending=False).reset_index()
    fig_sales_category = px.bar(
        sales_by_category,
        x='Sales',
        y='Category',
        orientation='h',
        title='Total Sales by Product Category',
        labels={'Sales': 'Sales ($)', 'Category': 'Product Category'}
    )
    fig_sales_category.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig_sales_category, use_container_width=True)

with tab3:
    st.subheader("Sales by Region")
    sales_by_region = filtered_df.groupby('Region')['Sales'].sum().sort_values(ascending=False).reset_index()
    fig_sales_region = px.bar(
        sales_by_region,
        x='Region',
        y='Sales',
        title='Total Sales by Region',
        labels={'Sales': 'Sales ($)', 'Region': 'Region'}
    )
    st.plotly_chart(fig_sales_region, use_container_width=True)

with tab4:
    st.subheader("Profit by Customer Segment")
    profit_by_segment = filtered_df.groupby('Customer Segment')['Profit'].sum().sort_values(ascending=False).reset_index()
    fig_profit_segment = px.bar(
        profit_by_segment,
        x='Customer Segment',
        y='Profit',
        color='Customer Segment',
        title='Total Profit by Customer Segment',
        labels={'Profit': 'Profit ($)', 'Customer Segment': 'Customer Segment'}
    )
    st.plotly_chart(fig_profit_segment, use_container_width=True)

st.markdown("---")
st.info("This dashboard provides a high-level overview of retail performance. Filters on the sidebar allow for deeper analysis.")
