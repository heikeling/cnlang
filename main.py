import threading
import subprocess
import easygui as g
import requests
import json
import tkinter as tk
import logging
import tkinter.ttk as ttk
import os
import codecs
from tkinter.filedialog import askdirectory
import tkinter.filedialog as filedialog
from tkinter import *

class main:
    def __init__(self):
        self.win = tk.Tk()
        self.win.iconbitmap('cn.ico')
        self.win.title('Cn语言-打造全中文编程')
        self.win.geometry("900x600")
        self.lb1 = tk.Label(self.win,text="欢迎使用Cn语言",font=("微软雅黑", 20),bg="grey")
        self.lb1.place(x=0,y=0)
        self.lb2 = tk.Label(self.win, text="请选择对应选项", font=("微软雅黑", 14), bg="grey")
        self.lb2.place(x=0, y=50)
        self.win.config(bg="grey")
        self.btncreatebz=tk.Button(self.win,text="标准界面",height=3,width=10,font=("微软雅黑", 20),bg="grey")
        self.cv = tk.Canvas(self.win, bg='white')
        self.cv.create_rectangle(10, 10, 300, 200)
        self.cv.create_text(200, 50, text="项目",font=("微软雅黑", 20))
        self.cv.place(x=400,y=100)
        self.btncreatebz = tk.Button(self.win, text="标准界面", height=3, width=10, font=("微软雅黑", 20), bg="grey",command=self.ide)
        self.btncreatebz.place(x=0, y=100)
        self.btncreatedh = tk.Button(self.win, text="对话框", height=3, width=10, font=("微软雅黑", 20), bg="grey")
        self.btncreatedh.place(x=190, y=100)
        self.btnopen = tk.Button(self.win, text="打开项目", height=3, width=10, font=("微软雅黑", 20), bg="grey")
        self.btnopen.place(x=0, y=250)
        self.et = tk.Entry(self.win,font=("微软雅黑", 20))
        self.et.place(x=0,y=500,height=30,width=400)
        self.et.insert(tk.END,"D:\Project1")
        self.xz = tk.Button(self.win,text="选择文件夹",command=self.xzf,font=("微软雅黑", 10), bg="grey")
        self.xz.place(x=500,y=500)
        self.win.mainloop()
    def xzf(self):
        self.path_xz = askdirectory()
        self.et.delete(0,tk.END)
        self.et.insert(tk.END,self.path_xz)
    def ide(self):
        self.paths = self.et.get()
        self.win.destroy()
        self.root = tk.Tk()
        self.root.iconbitmap('cn.ico')
        self.root.title(self.paths+"\main.cn")
        with open(self.paths+"\main.cn","w")as f:
            f.write("打印('hello')")
        self.root.geometry("1000x800")
        self.root.config(bg="grey")
        self.code = tk.Text(self.root,height=30,width=90,font=("微软雅黑", 10))
        self.code.place(x=230,y=0)
        self.code.bind('<Key>', self.rcolor)
        self.put = tk.Text(self.root, height=10, width=90, font=("微软雅黑", 10))
        self.put.place(x=230, y=500)
        with open(self.paths+"main.cn","w")as f:
            self.code.insert(tk.END,"打印('hello')")
        self.files = os.listdir(self.paths)
        print(self.files)
        self.file = ttk.Treeview(self.root,columns=('id'), show="headings", displaycolumns="#all")
        print(len(self.files))
        self.file.heading('id', text="file", anchor=W)
        for itm in self.files:
            self.file.insert("", END, values=itm)
        self.file.bind("<<TreeviewSelect>>", self.onSelect)
        self.file.place(x=0,y=0)
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='文件', menu=filemenu)
        filemenu.add_command(label='打开', command=self.opens)
        filemenu.add_command(label='保存', command=self.file1)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='编译', menu=filemenu)
        filemenu.add_command(label='运行', command=self.run)
        filemenu.add_command(label='打包exe(需python环境+pyinstaller)', command=self.exe)
        self.root.config(menu=menubar)
        self.rcolor()
        self.root.mainloop()
    def exe(self):
        self.bd = tk.Tk()
        self.bd.title("打包exe")
        self.bd.geometry("300x500")
        self.bd.iconbitmap("cn.ico")
        cde = '''
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
'''+self.code.get('1.0','end')+'''
win.mainloop()'''
        f = codecs.open('code.py', 'w', "UTF-8")
        f.write(cde)
        f.close()
        def dab():
            process = subprocess.Popen("pyinstaller -F -w code.py", shell=True, bufsize=0, stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT,
                                       stdin=subprocess.PIPE)
            run.delete('0.0', tk.END)
            output = process.stdout.readline()
            while output:
                run.insert(tk.END, output)
                run.see('end')
                output = process.stdout.readline()
            process.stdout.close()
            os.system("xcopy .\dist\code.exe " + xz)
        def td():
            run_t = threading.Thread(target=dab)
            run_t.start()
        def openlj():
            s = askdirectory()
            if s == None:
                pass
            else:
                ps.delete('0',tk.END)
                ps.insert(tk.INSERT,s)
        btn = tk.Button(self.bd,text="开始打包",command=td)
        btn.pack()
        btn0 = tk.Button(self.bd, text="路径", command=openlj)
        btn0.place(x=0,y=0)
        ps = tk.Entry(self.bd)
        ps.pack()
        xz=ps.get()
        run = tk.Text(self.bd)
        run.pack()
        self.bd.config(bg='grey')
        btn.config(bg='grey')
        btn0.config(bg='grey')
        run.config(bg='grey')
        self.bd.mainloop()

    def onSelect(self,e):
        self.itm = self.file.set(self.file.focus())
        with open(self.paths+"/"+self.itm["id"],"r")as s:
            self.codeccs = s.read()
            print(self.codeccs)
        print(self.itm)
        self.code.delete("1.0","end")
        self.code.insert(tk.END, self.codeccs)
        pass
    def file1(self):
        filename = filedialog.asksaveasfilename(filetypes=[("CN", ".cn")])
        with open(filename + '.cn', 'w') as f:
            f.write(self.code.get('1.0', 'end'))
    def opens(self):
        filename = filedialog.askopenfilename()
        if filename == None:
            pass
        else:
            f = open(filename, 'r')
            f2 = f.read()
            f.close()
            self.code.insert(INSERT, f2)
    def run(self):
        codes = self.code.get('1.0','end')
        self.codes = codes
        def 打印(txt, color='black'):
            global textMess
            if self.put != None:
                if self.put != 'black':
                    self.put.tag_config(color, foreground=color)
                self.put.insert(tk.END, txt, color)
                self.put.see(tk.END)

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

        logging.debug("[INFO]函数加载完成")
        logging.debug("[INFO]开始编译...")
        self.put.insert(END, '[INFO]开始编译...\n')
        try:
            if "否则如果 " in codes:
                codes = codes.replace("否则如果", "elif")
            if "列表(" in codes:
                codes = codes.replace("列表", "list")
            if "否则:" in codes:
                codes = codes.replace("否则", "else")
            if "标题(" in codes:
                codes = codes.replace("标题", "title")
            if "大小(" in codes:
                codes = codes.replace("大小", "geometry")
            if "如果 " in codes:
                codes = codes.replace("如果", "if")
            if "导入 " in codes:
                codes = codes.replace("导入库 ", "import ")
            if "条件循环 " in codes:
                codes = codes.replace("弹出", "while")
            if "遍历循环 " in codes:
                codes = codes.replace("变量循环", "for")
            if "于 " in codes:
                codes = codes.replace("于", "in")
            if "画布(" in codes:
                codes = codes.replace("画布", "Canvas")
            if "和 " in codes:
                codes = codes.replace("和", "and")
            if "定义 " in codes:
                codes = codes.replace("定义", "def")
            if "打破循环" in codes:
                codes = codes.replace("打破循环", "break")
            if "类 " in codes:
                codes = codes.replace("类", "class")
            if "同 " in codes:
                codes = codes.replace("同 ", "with")
            if "打开 " in codes:
                codes = codes.replace("打开", "open")
            if "退出(" in codes:
                codes = codes.replace("退出", "quit")
            if "监听(" in codes:
                codes = codes.replace("监听", "bind")
            if "从 " in codes:
                codes = codes.replace("从", "from")
            if "看作 " in codes:
                codes = codes.replace("看作", "as")
            if "返回 " in codes:
                codes = codes.replace("返回", "return")
            if "写入(" in codes:
                codes = codes.replace("写入", "write")
            if "尝试 " in codes:
                codes = codes.replace("尝试", "try")
            if "异常 " in codes:
                codes = codes.replace("异常", "except")
            if "（" in codes:
                codes = codes.replace("（", "(")
            if "）" in codes:
                codes = codes.replace("）", ")")
            if "，" in codes:
                codes = codes.replace("，", ",")
            if "：" in codes:
                codes = codes.replace("：", ":")
            if "获取(" in codes:
                codes = codes.replace("获取", 'get')
            if "窗口插入文本" in codes:
                codes = codes.replace("窗口插入文本", 'insert')
            if "多行文本框(" in codes:
                codes = codes.replace("多行文本框", 'tk.Text')
            if "主菜单" in codes:
                codes = codes.replace("主菜单", 'add_cascade')
            if "创建菜单" in codes:
                codes = codes.replace("创建菜单", 'Menu')
            if "菜单内容" in codes:
                codes = codes.replace("菜单内容", 'add_command')
            if "设置操作" in codes:
                codes = codes.replace("设置操作", 'config')
            exec(codes)
        except (Exception, BaseException) as e:
            e = str(e)
            baoc = self.translator(e)
            self.colorprint("代码报错，终止运行\n" + baoc + "\n", 'red')
            logging.error(e)

    def translator(self,str):
        """
        input : str 需要翻译的字符串
        output：translation 翻译后的字符串
        """
        # API
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
        # 传输的参数， i为要翻译的内容
        key = {
            'type': "AUTO",
            'i': str,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "ue": "UTF-8",
            "action": "FY_BY_CLICKBUTTON",
            "typoResult": "true"
        }
        # key 这个字典为发送给有道词典服务器的内容
        response = requests.post(url, data=key)
        # 判断服务器是否相应成功
        if response.status_code == 200:
            # 通过 json.loads 把返回的结果加载成 json 格式
            result = json.loads(response.text)
            #         print ("输入的词为：%s" % result['translateResult'][0][0]['src'])
            #         print ("翻译结果为：%s" % result['translateResult'][0][0]['tgt'])
            translation = result['translateResult'][0][0]['tgt']
            return translation
        else:
            print("有道词典调用失败")
            # 相应失败就返回空
            return None

    def colorprint(self,txt, color='black'):
        global textMess
        if self.put != None:
            if self.put != 'black':
                self.put.tag_config(color, foreground=color)
            self.put.insert(tk.END, txt, color)
            self.put.see(tk.END)
    def rcolor(self,event=None):
        def search(text_widget, keyword, tag):
            pos = '1.0'
            while True:
                idx = text_widget.search(keyword, pos, END)
                if not idx:
                    break
                pos = '{}+{}c'.format(idx, len(keyword))
                text_widget.tag_add(tag, idx, pos)

        self.code.tag_config('failed', foreground='red')
        self.code.tag_config('passed', foreground='blue')
        self.code.tag_config('t', foreground='green')
        search(self.code, '导入', 'failed')
        search(self.code, '遍历循环', 'failed')
        search(self.code, '条件循环', 'failed')
        search(self.code, '从', 'passed')
        search(self.code, '如果', 'passed')
        search(self.code, '打印', 'failed')
        search(self.code, '否则如果', 'passed')
        search(self.code, '否则', 'passed')
        search(self.code, '整数型', 't')
        search(self.code, '字符型', 't')
        search(self.code, '浮点型', 't')
        search(self.code, '弹出', 'failed')
        search(self.code, '询问', 'failed')
        search(self.code, 'True', 't')
        search(self.code, 'False', 't')
        search(self.code, '创建界面', 'failed')
        search(self.code, '类', 'failed')
        search(self.code, '定义', 'failed')
        search(self.code, '看作', 't')
        search(self.code, '尝试', 't')
        search(self.code, '写入', 't')
        search(self.code, '返回', 't')
        search(self.code, '异常', 't')
        search(self.code, '同', 't')
        search(self.code, '打开', 't')
        search(self.code, '退出', 't')
        search(self.code, '显示按钮', 'passed')
        search(self.code, '显示文字', 'passed')
        search(self.code, '标题', 'passed')
        search(self.code, '大小', 'passed')
        search(self.code, '输入框', 't')
        search(self.code, '放置', 't')
        search(self.code, 'place', 't')
        search(self.code, '和', 't')
        search(self.code, '里面', 't')
        search(self.code, '编译代码', 'failed')
        search(self.code, '多行文本框', 'failed')
        search(self.code, '获取值', 'failed')
        search(self.code, '设置操作', 'failed')
        search(self.code, '窗口插入文本', 't')
        search(self.code, '主菜单', 't')
        search(self.code, '菜单内容', 't')
        search(self.code, '创建菜单', 't')
if __name__ == "__main__":
    main=main
    main()