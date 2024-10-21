import streamlit as st

st.set_page_config(
    page_title="Data Analysis With SQL",
    page_icon="🔢", #📜📄
)

home = st.Page("pages/home.py", title="Home", icon="🏡")
getting_started = st.Page("pages/getting-started.py", title="Getting Started", icon="🚀")
sql_fundamentals = st.Page("pages/sql-fundamentals.py", title="SQL Fundamentals", icon="🧱")
joins = st.Page("pages/joins.py", title="Table Join", icon="🤝")

# Aggregation
#aggregation = st.Page("pages/aggregation.py", title="➕ Aggregation", icon="➕")

count  = st.Page("pages/aggregation/count.py", title="COUNT", icon="")
max  = st.Page("pages/aggregation/max.py", title="MAX", icon="")
min  = st.Page("pages/aggregation/min.py", title="MIN", icon="")
avg  = st.Page("pages/aggregation/avg.py", title="AVG", icon="")
sum  = st.Page("pages/aggregation/sum.py", title="SUM", icon="")
rollup  = st.Page("pages/aggregation/rollup.py", title="ROLLUP", icon="")
cube  = st.Page("pages/aggregation/cube.py", title="CUBE", icon="")
aggregation_review  = st.Page("pages/aggregation/aggregation-review.py", title="Review", icon="")


pg = st.navigation(
    {
        "": [home],
        "🚀 Getting Started": [],
        "🧱 SQL Fundamentals": [],
        "🤝 Table Join": [],
        "➕ Aggregation": [count, max, min, avg, sum, rollup, cube, aggregation_review],
    }
)

pg.run()
