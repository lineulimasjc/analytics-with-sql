import streamlit as st

st.title('COUNT', anchor=False)

st.divider()

st.subheader('Database environment to answer the business questions below.', anchor=False)

code = '''
-- Create table Customer
IF Object_id(N'[Customers]', 'U') IS NOT NULL
  DROP TABLE Customers

CREATE TABLE Customers
  (
     id_cust INT IDENTITY PRIMARY KEY,
     name    CHAR(35),
     type    CHAR(15),
     city    CHAR(30),
     state   CHAR(02)
  );  

-- Create table Products
IF Object_id(N'[Produts]', 'U') IS NOT NULL
  DROP TABLE Products

CREATE TABLE Products
  (
     id_prod INT IDENTITY PRIMARY KEY,
     name    CHAR(35),
     level   CHAR(35)
  ); 

-- Create table Orders
IF Object_id(N'[Orders]', 'U') IS NOT NULL
  DROP TABLE Orders

CREATE TABLE Orders
  (
     id_ord      INT IDENTITY PRIMARY KEY,
     id_product  INT,
     date        DATE NULL,
     value       DECIMAL(10, 2) NULL,
     id_customer INT,
     FOREIGN KEY (id_product) REFERENCES Products (id_prod),
     FOREIGN KEY (id_customer) REFERENCES Customers (id_cust)
  ); 


INSERT INTO Customers
            (NAME,type,city,state)
VALUES      ('Barbara','Doctoral','Portland','ME'),
            ('Mary','Doctoral','Baton Rouge','LA'),
            ('Maria','Doctoral','Boston','MA'),
            ('David','Doctoral','Des Moines','IA'),
            ('Mary','Doctoral','Baton Rouge','LA'),
            ('Patricia','Doctoral','New Orleans','LA'),
            ('William','Doctoral','Indianapolis','IN'),
            ('Dorothy','Doctoral','Saint Paul','MN'),
            ('David','Doctoral','Des Moines','IA'),
            ('Patricia','Doctoral','New Orleans','LA'),
            ('Robert','Doctoral','Springfield','IL'),
            ('Robert','Doctoral','Springfield','IL'),
            ('John','Master','Boise','ID'),
            ('Susan','Doctoral','Lansing','MI'),
            ('Margaret','Doctoral','Detroit','MI'),
            ('David','Doctoral','Des Moines','IA'),
            ('Linda','Doctoral','Augusta','ME'),
            ('Thomas','Doctoral','Louisville','KY'),
            ('Margaret','Doctoral','Detroit','MI'),
            ('Barbara','Doctoral','Portland','ME'); 

INSERT INTO Products
            (name,level)
VALUES      ('MATLAB','Data Analysis'),
            ('Java','Web'),
            ('CSS','Web'),
            ('C++','Embedded'),
            ('Ruby','Embedded'),
            ('Java','Web'),
            ('Ruby','Embedded'),
            ('Rust','Embedded'),
            ('Go','Web'),
            ('Scala','Data Analysis'); 


INSERT INTO Orders
            (id_product,date,value,id_customer)
VALUES      (2,'2024/10/01',801.85,4),
            (3,'2024/10/02',680.09,10),
            (5,'2024/10/03',569.52,1),
            (10,'2024/10/04',1082.4,10),
            (10,'2024/10/05',1374.18,4),
            (8,'2024/10/06',281.27,7),
            (1,'2024/10/07',339.52,2),
            (6,'2024/10/08',432.26,9),
            (8,'2024/10/09',409.37,6),
            (8,'2024/10/10',248.46,1); 
'''
st.code(code, language="sql")

st.divider()

st.subheader('Business Questions:', anchor=False)

st.write('###')

st.write(':blue[1. Retrieve all customers]')

with st.expander("View suggested solution"):
    code = '''
    SELECT * 
	FROM Customers;
    '''
    st.code(code, language="sql")

st.write('###')


st.write(':blue[2. Count all customers]')

with st.expander("View suggested solution"):
    code = '''
	SELECT COUNT(*) 
	FROM Customers;
    '''
    st.code(code, language="sql")

st.write('###')


st.write(':blue[3. Count customers]')

with st.expander("View suggested solution"):
    code = '''
	SELECT COUNT(id_cust)
	FROM Customers;
    '''
    st.code(code, language="sql")

st.write('###')


st.write(':blue[4. Count customers by city (Is this query incorrect?)]')

with st.expander("View suggested solution"):
    code = '''
	SELECT city, COUNT(id_cust)
	FROM Customers;
    '''
    st.code(code, language="sql")

st.write('###')