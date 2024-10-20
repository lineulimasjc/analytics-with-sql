import streamlit as st

st.set_page_config(
    page_title="Analytics With SQL",
    page_icon="🔢", #📜📄
)

getting_started = st.Page("pages/getting-started.py", title="Getting Started", icon="🚀")
sql_fundamentals = st.Page("pages/sql-fundamentals.py", title="SQL Fundamentals", icon="🧱")
joins = st.Page("pages/joins.py", title="Table Join", icon="🤝")
aggregation = st.Page("pages/aggregation.py", title="Aggregation", icon="➕")

pg = st.navigation(
    {
        "Data Analysis with SQL": [getting_started,
                                   sql_fundamentals,
                                   joins,
                                   aggregation
                                   ],
    }
)

pg.run()
