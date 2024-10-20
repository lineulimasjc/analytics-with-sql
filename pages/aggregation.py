import streamlit as st

st.title('Aggregation')

st.divider()

st.subheader('Creating the data structure environment:')
# st.subheader('Criando o ambiente de estudo:')

code = '''
-- Create table
CREATE TABLE cap10.vendas (
    ID              INT             PRIMARY KEY,
    DataVenda       DATE,
    Produto         VARCHAR(50),
    Quantidade      INT,
    ValorUnitario   DECIMAL(10, 2),
    Vendedor        VARCHAR(50)
);


-- Insert Data
INSERT INTO cap10.vendas (ID, DataVenda, Produto, Quantidade, ValorUnitario, Vendedor)
VALUES (1, '2023-11-01', 'Produto A', 10, 100.00, 'Zico'),
       (2, '2023-11-01', 'Produto B', 5, 200.00, 'Romário'),
       (3, '2023-11-02', 'Produto A', 7, 100.00, 'Ronaldo'),
       (4, '2023-11-02', 'Produto C', 3, 150.00, 'Bebeto'),
       (5, '2023-11-03', 'Produto B', 8, 200.00, 'Romário'),
       (6, '2023-11-03', 'Produto A', 5, 100.00, 'Zico'),
       (7, '2023-11-04', 'Produto C', 10, 150.00, 'Bebeto'),
       (8, '2023-11-04', 'Produto A', 2, 100.00, 'Ronaldo'),
       (9, '2023-11-05', 'Produto B', 6, 200.00, 'Romário'),
       (10, '2023-11-05', 'Produto C', 4, 150.00, 'Bebeto');
'''
st.code(code, language="sql")

# st.image('img/mer.png')

st.divider()



c1 = st.container(border=True)

c1.write('**1. What is the total sales per product?**')
# c1.write('**1. Qual o total de vendas por produto?**')

with st.expander("Ver solução"):
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



c2 = st.container(border=True)

c2.write('**2. Qual o total de vendas por produto?**')

with st.expander("Ver solução"):
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