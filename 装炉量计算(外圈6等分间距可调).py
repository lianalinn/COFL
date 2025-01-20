import matplotlib.pyplot as plt
import numpy as np
import math

def calculate_load(a, b, h):
    q = int(60 / (math.atan((b + d) / (175 - a - e) / 2) * 2 / math.pi * 180) + 0.5) * 6
    
    if h > 280:
        c = 1
    elif 180 <= h <= 280:
        c = 2
    elif 130 <= h < 180:
        c = 3
    elif 80 <= h < 130:
        c = 4
    elif 40 <= h < 80:
        c = 6
    elif 31 <= h < 40:
        c = 9
    elif 27 <= h < 31:
        c = 12
    else:
        c = 15


    # q是一层治具圆隔板最外圈摆放产品的数量，c是转架上下方向治具圆隔板的数量，t是转架内治具圆隔板的总数量，u是转架内摆放产品的总数
    t = 4 * c
    u = q * t
    
    if c in [1, 2, 3, 4]:
        v = t
    else:
        v = 12
    
    return q, t, u

def plot_load(a, b, h):
    q, t, u = calculate_load(a, b, h)
    
    # 画圆形治具
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), 175, color='black', fill=False)
    ax.add_artist(circle)
    
    # 均匀排列长方形产品
    angles = np.linspace(0, 2 * np.pi, q, endpoint=False)
    for angle in angles:
        x = (175 - (a + e)) * np.cos(angle)
        y = (175 - (a + e)) * np.sin(angle)
        rect = plt.Rectangle((x+b/2*np.sin(angle), y-b/2*np.cos(angle)), a, b, angle=angle*180/np.pi, edgecolor='blue', facecolor='cyan', alpha=0.5)
        ax.add_patch(rect)

    # 画直线
    plt.plot((175 - a - e, 175 - a - e), (- b / 2 -2, - b / 2 -80), linewidth=0.7, color='black')
    plt.plot((175 - e , 175 -  e), ( - b / 2 -2, - b / 2 -80), linewidth=0.7, color='black')
    plt.plot((175 - a - e ,  175 - e), ( - b / 2 -78,  - b / 2 -78), linewidth=0.7, color='black')
    plt.plot((175 - a - e ,  175 - a - e +6), ( - b / 2 -78,  - b / 2 -78+ 1), linewidth=0.7, color='black')
    plt.plot((175 - e ,  175 - e - 6), ( - b / 2 -78,  - b / 2 -78 + 1), linewidth=0.7, color='black')
    plt.text(175 - e + 17, - b / 2 -78, f"{int( a )} ", ha='center', fontsize=14)

    plt.plot((175 - e + 2 ,  175 + 45),  (b / 2,  b / 2), linewidth=0.7, color='black')
    plt.plot((175 - e + 2 ,  175 + 45), ( - b / 2,  - b / 2), linewidth=0.7, color='black')
    plt.plot((175 + 43 ,  175 + 43), ( b / 2,  - b / 2), linewidth=0.7, color='black')
    plt.plot((175 + 43 ,  175 + 43 - 1), ( b / 2,  b / 2 - 6), linewidth=0.7, color='black')
    plt.plot((175 + 43 ,  175 + 43 - 1), ( - b / 2,  - b / 2 + 6), linewidth=0.7, color='black')
    plt.text(175 + 28, - g - 5, f"{int( b )} ", ha='center', fontsize=14)

    y1=int(((175 - e - a ) * np.sin(np.pi/q*2)- b / 2 - b / 2 * np.cos(np.pi/q*2))*100+0.5)/100
    plt.plot((175 - a - e + 2 ,  175 + 45), ( b / 2 + y1,  b / 2 + y1), linewidth=0.7, color='black')
    plt.plot((175 + 43 ,  175 + 43), ( b / 2,  b / 2 + y1+12), linewidth=0.7, color='black')
    plt.plot((175 + 43 ,  175 + 43 - 1), ( b / 2+ y1,  b / 2 + y1 + 6), linewidth=0.7, color='black')     
    plt.text(175 + 25, b / 2 + y1+2, f"{y1} ", ha='center', fontsize=14)
    
    # 图形设置
    ax.set_xlim(-200, 230)
    ax.set_ylim(-200, 200)
    ax.set_aspect('equal', 'box')
    plt.axis('off')
    
    # 在图形下方标示装炉量计算结果
    c1= int(t / 4)
    plt.text(0, -210, f"{q} × {c1} × {4} = {q*t}pcs", ha='center', fontsize=14)
    
    plt.show()

# 输入产品的长宽高
a = float(input("请输入产品的长度 (mm):           "))
b = float(input("请输入产品的宽度 (mm):           "))
h = float(input("请输入产品的高度 (mm):           "))
e = float(input("请输入产品到治具圆外圈间距 (mm): "))
d = float(input("请输入产品同一圈的间距     (mm): "))
if b > 15:
     g = 0
else:
     g = 8+b / 2   

plot_load(a, b, h)