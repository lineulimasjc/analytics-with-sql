import streamlit as st

st.set_page_config(
    page_title="Analytics With SQL",
    page_icon="🗄️",
)

getting_started = st.Page("pages/getting-started.py", title="Getting Started", icon=":material/search:")
sql_fundamentals = st.Page("pages/sql-fundamentals.py", title="SQL Fundamentals", icon=":material/history:")

pg = st.navigation(
    {
        "Data Analysis with SQL": [getting_started, sql_fundamentals],
    }
)

pg.run()
