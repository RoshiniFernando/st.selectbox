# Import Streamlit
import streamlit as st

# Header text
st.header('st.selectbox')

# selection box
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

# Print selected option
st.write('Your favorite color is ', option)