import streamlit as st
from db.database import get_expenses_by_user
from utils.services import *

st.set_page_config(page_title="Overview", layout="wide")
st.header("Expense Overview")

if "user" not in st.session_state:
    st.warning("Please enter your info first.")
    st.stop()


user_id = st.session_state["user"]["user_id"]
df = get_expenses_by_user(user_id)

if df.empty:
    st.info("No expenses have been added.")
else:
    st.subheader("Your Expenses")
    st.dataframe(df)

    st.subheader("Expense Distribution")
    st.plotly_chart(plot_pie_chart(df), use_container_width=True)

    st.subheader("Spending Over Time")
    st.plotly_chart(plot_line_chart(df), use_container_width=True)

    st.subheader("Maximum Expense by Category")
    max_per_category = df.groupby("category")["amount"].max().reset_index().sort_values(by="amount", ascending=False)
    max_per_category.columns = ["Category", "Max Amount Spent"]
    st.table(max_per_category)

if st.button("⬅ Back to Add Expenses"):
    st.switch_page("pages/add_expenses.py")

if st.button("Download the Report"):
    st.switch_page("pages/report.py")
