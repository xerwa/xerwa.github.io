'''代码'''
import streamlit as st

st.write('第10天代码')
st.write('————————————————————————————————————————')
st.write('与石墨文档不同的是，这里的代码是可以复制粘贴的，格式不会错乱')

st.code("""
'''手速测试小游戏'''
from pgzrun import *
import time

# 常量区
WIDTH = 600
HEIGHT = 400

# 变量区
player_button = Actor('button.png', (300, 200))
start_time = 0 # 游戏计时器
point = 0

# 函数区
def on_mouse_down(pos, button):
    '''鼠标按下'''
    global start_time, point
    # 开始游戏
    if player_button.collidepoint(pos) and start_time == 0:
        if (player_button.x, player_button.y) != (300, 200):
            start_time = time.time()
    # 增加点数
    if player_button.collidepoint(pos) and start_time != 0:
        point += 1

def on_mouse_up(pos, button):
    '''鼠标抬起'''
    pass

def on_key_down(key):
    '''键盘按键按下'''
    pass

def on_key_up(key):
    '''键盘按键抬起'''
    pass

def update():
    '''循环判断函数'''
    # 上下左右移动
    if keyboard.left:
        player_button.x -= 10
    if keyboard.right:
        player_button.x += 10
    if keyboard.up:
        player_button.y -= 10
    if keyboard.down:
        player_button.y += 10
    # 移动限制
    if player_button.x <= 0:
        player_button.x = 0
    if player_button.x >= WIDTH:
        player_button.x = WIDTH
    if player_button.y <= 0:
        player_button.y = 0
    if player_button.y >= HEIGHT:
        player_button.y = HEIGHT
    # 游戏结束-按钮移开
    if start_time != 0 and time.time() - start_time >= 10:
        player_button.x = 100000
        player_button.y = 100000

def draw():
    '''循环显示函数'''
    screen.fill((180, 255, 180))
    player_button.draw()
    # 游戏结束-显示结果
    if start_time != 0 and time.time() - start_time >= 10:
        screen.draw.text('points:'+str(point), (200, 170), color="gray", fontsize=60)

go()
""")
