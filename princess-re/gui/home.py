from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
from character import *

class home(object):
    '''創建首頁'''
    def __init__(self,master=None):
        self.root = master
        # 鎖定頁面
        self.root.resizable(False,False)
        # icon設定
        self.root.iconbitmap("mainpage/app_icon.ico")
        # 螢幕寬度
        screenWidth = self.root.winfo_screenwidth()
        # 螢幕高度
        screenHeight = self.root.winfo_screenheight()
        # 視窗寬
        w = 1200
        # 視窗高
        h = 680
        # 視窗左上角x軸位置
        x = int((screenWidth - w) / 2)
        # 視窗左上角Y軸位置
        y = int((screenHeight - h ) / 4)
        self.root.geometry("%dx%d+%d+%d" % (w,h,x,y))

        '''建立工具列'''
        self.menubar = Menu(self.root)
        # 第6步，建立一個File選單項（預設不下拉，下拉內容包括New，Open，Save，Exit功能項）
        filemenu = Menu(self.menubar, tearoff=0)
        # 將上面定義的空選單命名為File，放在選單欄中，就是裝入那個容器中
        self.menubar.add_cascade(label='工具', menu=filemenu)

        # 在File中加入New、Open、Save等小選單，即我們平時看到的下拉選單，每一個小選單對應命令操作。
        # filemenu.add_separator()    # 新增一條分隔線
        filemenu.add_command(label='爬蟲', command=lambda:self.root.destroy())
        filemenu.add_command(label='離開', command=lambda:self.root.destroy()) # 用tkinter裡面自帶的quit()函式

        self.root.config(menu=self.menubar)

        self.createPage()
        self.root.mainloop()
    
    def createPage(self):
        '''首頁內容'''
        self.page = Frame(self.root)
        self.page.pack()
        '''背景圖片'''
        self.yellowstone = ImageTk.PhotoImage(file="mainpage/background.gif")
        Label(self.page,image=self.yellowstone).pack()
        self.main_button_font= tkFont.Font(size=36, weight="bold")
        self.main_button＿pic = PhotoImage(file="mainpage/main_button.gif")
        '''跳轉'''
        Button(self.page,text="前衛",image= self.main_button＿pic,compound=CENTER,font= self.main_button_font,command=self.goto_frontPage).place(x=150,y=300,width=260,height=90)
        Button(self.page,text="中衛",image= self.main_button＿pic,compound=CENTER,font= self.main_button_font,command=self.goto_middlePage).place(x=450,y=300,width=260,height=90)
        Button(self.page,text="後衛",image= self.main_button＿pic,compound=CENTER,font= self.main_button_font,command=self.goto_lastPage).place(x=750,y=300,width=260,height=90)
    
    def goto_frontPage(self):
        '''跳轉至前衛角色資料'''
        self.page.destroy()
        character(self.root,'front')

    def goto_middlePage(self):
        '''跳轉至中衛角色資料'''
        self.page.destroy()
        character(self.root,'middle')

    def goto_lastPage(self):
        '''跳轉至後衛角色資料'''
        self.page.destroy()
        character(self.root,'last')
