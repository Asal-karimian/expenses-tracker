import time
import streamlit as st
from db.database import insert_expenses

if "user" not in st.session_state or "age" not in st.session_state:
    st.warning("Please enter your info first.")
    st.toast("Redirecting to home page in 5 seconds...")
    time.sleep(5)
    st.switch_page("app.py")

st.title("Add New Expense")

with st.form("add_expense"):
    category = st.selectbox("Category", ["Food", "Transport", "Rent", "Health", "Entertainment", "Other"])
    amount = st.number_input("Amount ($)", min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Add")

if submitted:
    user_id = st.session_state["user"]["user_id"]

    insert_expenses(
        user_id=user_id,
        category=category,
        amount=amount
    )

    st.success("Expense added successfully!")


if st.button("Go to overall"):
    st.switch_page("pages/overall.py")

if st.button("Go to Report"):
    st.switch_page("pages/report.py")
