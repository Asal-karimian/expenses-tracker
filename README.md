
## This is a simple Streamlit web app for tracking your personal expenses. You can add, view, and analyze your expenses using charts and summaries.
![image](https://github.com/user-attachments/assets/858e17e6-51c3-4e64-9938-f68dd611d2be)

---

## 🎯 Goal of the Project

Managing personal finances can be overwhelming, especially when tracking multiple categories manually or across scattered tools. The goal of this app is to provide:

- ✅ A **simple, user-friendly interface** to log and manage expenses
- 📊 Clear **visual insights** (pie and line charts) to understand spending behavior
- 🧾 A quick way to **generate reports** and view maximum spending per category
- 📁 A lightweight and local **SQLite** database backend for offline usage

---

##  Project Structure

expenses_tracker/
expenses_tracker/
│
├── .streamlit/              # Streamlit settings (theme, layout)
│   └── config.toml
│
├── db/                      # Database layer
│   └── database.py
│
├── pages/                   # Additional Streamlit pages
│   ├── add_expenses.py
│   ├── overall.py
│   └── report.py
│
├── utils/                   # Utility services (plotting, calculations)
│   └── services.py
│
├── app.py                   # Main Streamlit entry point
├── expenses.db              # SQLite database file
├── requirements.txt         # List of Python dependencies

---
## Why I Designed It
This project was developed as part of a university assignment where the goal was to create a website with a well-designed UI and UX, connected to a database.

As a Data Science student, I saw this as an opportunity to merge the project requirements with my own learning path. Instead of building just a static website, I wanted to:

📊 Apply data science concepts like data handling, aggregation, and visualization

🔄 Build a dynamic app that provides real-time feedback through visual charts

🧠 Practice Python-based tools relevant to my career, like Streamlit, SQLite, and Plotly
