'''代码'''
import streamlit as st

st.write('第3天预制代码')
st.write('————————————————————————————————————————')
st.write('与石墨文档不同的是，这里的代码是可以复制粘贴的，格式不会错乱')

st.code("""
from pynput import mouse, keyboard
import time

def on_move(x, y):
    '''监测的鼠标移动'''
    print('坐标:', x, y)

def on_click(x, y, button, pressed):
    '''监测到鼠标按键'''
    if pressed:
        print('按下')
    else:
        print('抬起')

def on_scroll(x, y, dx, dy):
    '''监测到鼠标滚轮'''
    if dy < 0:
        print('滚轮下')
    elif dy > 0:
        print('滚轮上')

listen_mouse = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
listen_mouse.start()

while True:
    time.sleep(10)
""")
