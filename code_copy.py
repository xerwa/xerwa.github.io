import streamlit as st
st.write('北大附中初二Python-代码粘贴')

st.code("""
import turtle as t

t.hideturtle()
t.penup()
t.speed(0)
t.tracer(False)

for i in range(600, -601, -30):
    t.goto(-600, i)
    t.fillcolor('black')
    t.begin_fill()
    t.pendown()
    t.goto(600, i)
    t.goto(600, i-15)
    t.goto(-600, i-15)
    t.end_fill()
    t.penup()

p1 = t.Pen()
p2 = t.Pen()
p3 = t.Pen()
p4 = t.Pen()

down = 0
while True:
    p1.shape('square')
    p1.shapesize(3)
    p1.color('yellow')
    p1.goto(-150, 200-down)
    p1.clear()

    p2.shape('square')
    p2.shapesize(3)
    p2.color('blue')
    p2.goto(-50, 200-down)
    p2.clear()

    p3.shape('square')
    p3.shapesize(3)
    p3.color('yellow')
    p3.goto(50, 200-down)
    p3.clear()

    p4.shape('square')
    p4.shapesize(3)
    p4.color('blue')
    p4.goto(150, 200-down)
    p4.clear()

    t.update()
    down += 0.1

        """)