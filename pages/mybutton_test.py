import streamlit as st

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

if st.session_state.button:
    # The message and nested widget will remain on the page
    st.write('Button is on!')
    v = st.slider('Select a value')
else:
    st.write('Button is off!')

if st.button('调用滑动条数据'):
    st.write('滑动条的数值是：'+str(v))