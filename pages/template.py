import streamlit as st

st.title('Review', anchor=False)

st.divider()

st.subheader('Database environment to answer the business questions below.', anchor=False)

code = '''
-- Create table

-- Insert data

'''
st.code(code, language="sql")

st.divider()

st.subheader('Business Questions:', anchor=False)

st.write('###')

st.write(':blue[1. Question?]')

with st.expander("View suggested solution"):
    code = '''

    '''
    st.code(code, language="sql")

st.write('###')
