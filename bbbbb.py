import random as rnd
import tkinter as tk

height = 10
width = 20
field = [[0 for i in range(width)] for i in range(height)]
but_pushed = [[False for i in range(width)] for i in range(height)]
field_flag = [[0 for i in range(width)] for i in range(height)]
jirai = 70
for i in range(jirai):
    field[rnd.randint(0,height-1)][rnd.randint(0,width-1)] += 1
first = True
flag = False
flag_ = False

def pochi(xy):
    global first, jirai
    if flag or flag_:
        if first:
            return
        if but_pushed[xy[1]][xy[0]]:
            return
        if flag:
            field_flag[xy[1]][xy[0]] += 1
            buttons[xy[1]][xy[0]].config(text=f"🚩{field_flag[xy[1]][xy[0]]}")
            jirai -= 1
        if flag_ and field_flag[xy[1]][xy[0]]:
            field_flag[xy[1]][xy[0]] -= 1
            if field_flag[xy[1]][xy[0]] == 0:
                buttons[xy[1]][xy[0]].config(text="")
            else:
                buttons[xy[1]][xy[0]].config(text=f"🚩{field_flag[xy[1]][xy[0]]}")
            jirai += 1
        return
    if first:
        for y in range(-1,2):
            for x in range(-1,2):
                if x + xy[0] < 0 or x + xy[0] >= width or y + xy[1] < 0 or y + xy[1] >= height:
                    continue
                jirai -= field[y+xy[1]][x+xy[0]]
                field[y+xy[1]][x+xy[0]] = 0
        first = False
    but_pushed[xy[1]][xy[0]] = True
    if field[xy[1]][xy[0]]:
        buttons[xy[1]][xy[0]].config(bg="red", text=field[xy[1]][xy[0]])
        jirai -= field[xy[1]][xy[0]]
    else:
        jirai_sum = 0
        for y in range(-1,2):
            for x in range(-1,2):
                if x + xy[0] < 0 or x + xy[0] >= width or y + xy[1] < 0 or y + xy[1] >= height:
                    continue
                jirai_sum += 1 if field[y+xy[1]][x+xy[0]] else 0
        buttons[xy[1]][xy[0]].config(bg="white", text=jirai_sum)
        if jirai_sum == 0:
            for y in range(-1,2):
                for x in range(-1,2):
                    if x + xy[0] < 0 or x + xy[0] >= width or y + xy[1] < 0 or y + xy[1] >= height or but_pushed[y+xy[1]][x+xy[0]]:
                        continue
                    pochi([x+xy[0],y+xy[1]])
    label.config(text=f"残り地雷数：{jirai}")
    
def flagb_f(hata):
    global flag,flag_
    if hata == "+":
        flag = not flag
        if flag:
            flag_button.config(bg="green")
        else:
            flag_button.config(bg="white")
        flag_ = False
        flag_button_.config(bg="white")
    else:
        flag_ = not flag_
        if flag_:
            flag_button_.config(bg="green")
        else:
            flag_button_.config(bg="white")
        flag = False
        flag_button.config(bg="white")

screen_h = 1000
screen_w = 2000
font = ("",24)
root = tk.Tk()
root.geometry(f"{screen_w}x{screen_h}")
size = int(min(screen_w/width, (screen_h-200)/height))
buttons = [[0 for i in range(width)] for i in range(height)]
for y in range(height):
    for x in range(width):
        buttons[y][x] = tk.Button(root, command=lambda index=[x,y]:pochi(index), height=size//font[1]//2, width=size//font[1], font=font)
        buttons[y][x].place(x=x*size,y=y*size)

label = tk.Label(root, text="", font=font)
label.place(x=40, y=screen_h-100)
flag_button = tk.Button(root, command=lambda:flagb_f("+"), text="🚩+", font=font, bg="white")
flag_button_ = tk.Button(root, command=lambda:flagb_f("-"), text="🚩-", font=font, bg="white")
flag_button.place(x=320,y=screen_h-100)
flag_button_.place(x=400,y=screen_h-100)

root.mainloop()