import streamlit as st

st.title('Aggregation', anchor=False)

st.divider()

st.subheader('Database environment to answer the business questions below.', anchor=False)

# c0 = st.container(border=True)

#with st.expander("Database Objects and Data"):
code = '''
-- Create table
CREATE TABLE Sales
  (
     Id          INT IDENTITY PRIMARY KEY,
     Salesdate   DATE,
     Product     VARCHAR(50),
     Quantity    INT,
     Unitvalue   DECIMAL(10, 2),
     Salesperson VARCHAR(50)
  ); 


-- Insert Data
INSERT INTO Sales (SalesDate, Product, Quantity, UnitValue, SalesPerson)
VALUES ('2023-11-01', 'Produto A', 10, 100.00, 'Zico'),
    ('2023-11-01', 'Produto B', 5, 200.00, 'Romário'),
    ('2023-11-02', 'Produto A', 7, 100.00, 'Ronaldo'),
    ('2023-11-02', 'Produto C', 3, 150.00, 'Bebeto'),
    ('2023-11-03', 'Produto B', 8, 200.00, 'Romário'),
    ('2023-11-03', 'Produto A', 5, 100.00, 'Zico'),
    ('2023-11-04', 'Produto C', 10, 150.00, 'Bebeto'),
    ('2023-11-04', 'Produto A', 2, 100.00, 'Ronaldo'),
    ('2023-11-05', 'Produto B', 6, 200.00, 'Romário'),
    ('2023-11-05', 'Produto C', 4, 150.00, 'Bebeto');
'''
st.code(code, language="sql")

# st.write('_Create the study environment to answer the questions below._')

st.divider()

st.subheader('Business Questions:', anchor=False)

st.write('###')

st.markdown(":green[**1. What is the total sales per product?**]")

with st.expander("View suggested solution"):
    code = '''
    SELECT
        produto,
        SUM(quantidade * valorunitario)
    FROM
        cap10.vendas
    GROUP BY
        produto
    ORDER BY
        produto
    '''
    st.code(code, language="sql")




st.write('###')

st.markdown(":green[**2. What is the total sales per product?**]")

with st.expander("View suggested solution"):
    code = '''
    SELECT
        produto,
        SUM(quantidade * valorunitario)
    FROM
        cap10.vendas
    GROUP BY
        produto
    ORDER BY
        produto
    '''
    st.code(code, language="sql")