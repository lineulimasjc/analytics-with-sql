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

-- Insert data
INSERT INTO Sales
            (Salesdate,Product,Quantity,Unitvalue,Salesperson)
VALUES      ('2024-11-01','Product A',10,100.00,'John'),
            ('2024-10-01','Product B',6,200.00,'Susan'),
            ('2024-10-02','Product A',8,100.00,'David'),
            ('2024-10-02','Product C',4,150.00,'Jennifer'),
            ('2024-10-03','Product B',9,200.00,'Susan'),
            ('2024-10-03','Product A',6,100.00,'John'),
            ('2024-10-04','Product C',11,150.00,'Jennifer'),
            ('2024-10-04','Product A',3,100.00,'David'),
            ('2024-10-05','Product B',7,200.00,'Susan'),
            ('2024-10-05','Product C',3,150.00,'Jennifer'); 
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