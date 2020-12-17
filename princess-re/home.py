from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
import pygame
from character import *
import character_data

class home(object):
    '''創建首頁'''
    def __init__(self,master=None):
        '''設定視窗'''
        self.root = master
        self.root.resizable(False,False)
        self.root.iconbitmap("app_icon.ico")
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        w = 1200
        h = 680
        x = int((screenWidth - w) / 2)
        y = int((screenHeight - h ) / 4)
        self.root.geometry("%dx%d+%d+%d" % (w,h,x,y))

        '''背景音樂'''
        pygame.mixer.init()
        pygame.mixer.music.load("./music/starter_BGM.mp3")
        pygame.mixer.music.play()

        '''建立工具列'''
        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='爬蟲', menu=self.filemenu)
        self.filemenu.add_command(label='日版', command=character_data.jp)

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
