import streamlit as st
import pandas as pd
from db.database import get_expenses_by_user

st.header("Download Reports")

if "user" not in st.session_state:
    st.warning("You are not logged in. Please go to the main page first.")
    st.stop()

user_id = st.session_state["user"]["user_id"]
df = get_expenses_by_user(user_id)

if not df.empty:
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="expense_report.csv",
        mime="text/csv"
    )

    st.dataframe(df.head(10))
else:
    st.info("No data to download.")

if st.button("⬅ Back to result"):
    st.switch_page("pages/overall.py")
