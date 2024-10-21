import streamlit as st

st.title('Review', anchor=False)

st.divider()

st.subheader('Database environment to answer the business questions below.', anchor=False)

code = '''
-- Create table Sales
CREATE TABLE Sales
  (
     id          INT IDENTITY PRIMARY KEY,
     salesdate   DATE,
     product     VARCHAR(50),
     quantity    INT,
     unitvalue   DECIMAL(10, 2),
     salesperson VARCHAR(50)
  );

-- Insert data
INSERT INTO Sales
            (salesdate,product,quantity,unitvalue,salesperson)
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

st.divider()

st.subheader('Business Questions:', anchor=False)

st.write('###')

st.write(':blue[1. What is the total sales by product?]')

with st.expander("View suggested solution"):
    code = '''
    SELECT
        product,
        SUM(quantity * unitvalue) AS TotalSales
    FROM
        Sales
    GROUP BY
        product
    '''
    st.code(code, language="sql")

st.write('###')


st.write(':blue[2. What is the total sales by salesperson?]')

with st.expander("View suggested solution"):
    code = '''
    SELECT
        salesperson,
        SUM(quantity * unitvalue) AS TotalSales
    FROM
        Sales
    GROUP BY
        salesperson
    '''
    st.code(code, language="sql")

st.write('###')


st.write(":blue[3. What is the total sales by day?]")

with st.expander("View suggested solution"):
    code = '''
    SELECT
        salesdate,
        SUM(quantity * unitvalue) AS TotalSales
    FROM
        Sales
    GROUP BY
        salesdate
    '''
    st.code(code, language="sql")

st.write('###')


st.write(":blue[4. How do sales accumulate by day and by product (including daily subtotals)?]")

with st.expander("View suggested solution"):
    code = '''

    '''
    st.code(code, language="sql")

st.write('###')


st.write(":blue[5. Which salesperson and product combination generated the most sales (including all possible subtotals)?]")

with st.expander("View suggested solution"):
    code = '''

    '''
    st.code(code, language="sql")

