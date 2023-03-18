
import easygui as g
import tkinter as tk
win = tk.Tk()
win.title("Cn-for-windows")
put = tk.Text()
put.pack()
def 打印(txt, color='black'):
    global textMess
    if put != None:
        if put != 'black':
            put.tag_config(color, foreground=color)
        put.insert(tk.END, txt, color)
        put.see(tk.END)

def 询问(put):
    a = g.enterbox(put)
    return a

def 创建界面():
    return tk.Tk()

def 弹出(msg):
    return g.msgbox(msg)

def 显示按钮(对象, 文本, 函数=None):
    return tk.Button(对象, text=文本, command=函数)

def 显示文字(对象, 文本, 样式=None):
    return tk.Label(对象, text=文本, font=样式)

def 字符型(bl):
    return str(bl)

def 浮点型(参数):
    return float(参数)

def 整数型(参数):
    return int(参数)

def 再次编译(execs):
    return exec(execs)

def 输入框(对象):
    return tk.Entry(对象)
打印('hello')

win.mainloop()