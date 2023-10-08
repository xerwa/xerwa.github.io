import streamlit as st

st.write("随便写点什么...")

st.title("这是一个title")

st.header("这是一个header")

st.subheader("这是一个子header")

st.caption("这是一个小写字体的标题")

st.text("这是一段正常的文本内容")

f = open('myfriends.txt', 'r', encoding='utf-8')
msg = f.read()
f.close()
st.text(msg)