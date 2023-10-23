'''我们的地图'''
import streamlit as st
page = st.sidebar.radio('选择菜单', ['我们的地图', '我们的留言区', '伙伴个人页面'])
data = {'lat': [39.9, 22.5], 'lon': [116.4, 114.0]}

def header(url):
    st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;"> {url}</p>', unsafe_allow_html=True)

if page == '我们的地图':
    st.write(':orange[:sunglasses:深空教研小纵队:sunglasses:]')
    # st.image("logo.png", caption="Image Caption", use_column_width=True)
    st.write('这是我们的线上工作室\n8个伙伴的小纵队\n我们代表猫厂对教育的品味\n精益求精，打造标杆，致力于成为满意度和转介绍第一的少儿编程品牌')
    st.write('我们的成员分布地图：')
    st.map(data, size=100000, zoom=3)
    header("这是一个标题")
    st.write("这是一些内容")