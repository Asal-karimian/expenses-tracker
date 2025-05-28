import streamlit as st
from db.database import upsert_user
st.set_page_config(
    page_title="Expense Tracker",
    layout="wide"
)

st.title("Welcome to Personal Expense Tracker")
st.markdown("""
Welcome to your personal expense tracker.  
Use the sidebar to:
- Add new expenses
- View statistics and charts
- Download reports

Let's manage your money better!
""")

with st.form("user_info"):
    st.subheader("Please enter your personal information:")
    name = st.text_input("First Name", max_chars=22)
    family_name = st.text_input("Family Name", max_chars=30)
    age = st.number_input("Age", min_value=15)
    user_id = st.text_input("User ID")

    submitted = st.form_submit_button("Continue")

    if submitted:
        st.session_state["user"] = {
            "name": name,
            "family_name": family_name,
            "user_id": user_id
        }
        st.session_state["age"] = age

        upsert_user(user_id, name, family_name, age)

        st.success("Information saved!")
        st.switch_page("pages/add_expenses.py")

