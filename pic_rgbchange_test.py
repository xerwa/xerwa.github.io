import streamlit as st
from PIL import Image

st.write(":sunglasses:图片换色小程序:sunglasses:")
# 创建一个file_uploader组件，设置label为"上传图片"，type为['png','jpeg','jpg']
uploaded_file = st.file_uploader("上传图片", type=['png','jpeg','jpg'])

if uploaded_file:
    # 获取图片文件的名称、类型和大小
    file_name = uploaded_file.name
    file_type = uploaded_file.type
    file_size = uploaded_file.size

    # 在控制台中打印图片文件的信息
    print(f"文件名称：{file_name}")
    print(f"文件类型：{file_type}")
    print(f"文件大小：{file_size}")

    # 用PIL库打开图片文件
    img = Image.open(uploaded_file)
    
    # 在streamlit中显示图片
    st.write('原图：')
    st.image(img, caption=file_name)
    # 获取图片尺寸
    width, height = img.size
    # 加载图片像素点内容
    img_array = img.load()
    # 循环处理像素点
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            # 将处理后的点覆盖原数据
            img_array[x, y] = (b, r, g)
    st.write('换色：')
    st.image(img, caption=file_name)