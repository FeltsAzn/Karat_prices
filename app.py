import tkinter as tk
from logger import info_log, debug_log
from tkinter import Menu, messagebox as mbox
from select_menu import SelectionMenu
from datechecker import DateCheck


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configs()
        self.protocol('<WM_DELETE_WINDOW>', self.exiting)
        DateCheck(self)

    def configs(self):
        self.option_add("*Font", "TkTextFont")
        self.title('Отслеживание цен Карат-Маркет')
        self.geometry('1600x850')
        self['background'] = '#caffd3'
        self.minsize(900, 100)
        self.maxsize(1920, 1080)
        self.config(menu=Menubar(self))

    def exiting(self):
        answer = mbox.askquestion('Выход', 'Вы действительно хотите выйти?')
        if answer is True:
            self.destroy()


class Menubar(Menu):  # Меню для управления
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master['background'] = master['background']
        self.configure(background=master['background'])
        self.option_add('*Font', "Arial 12 bold")
        self.show_changed = tk.BooleanVar()
        self.show_changed.set(False)
        self.file_menu = Menu(self, tearoff=0, background=master['background'])
        self.help_menu = Menu(self, tearoff=0, background=master['background'])
        self.menubar_filling()

    def menubar_filling(self):
        self.file_menu.add_command(label="Выбрать цены...", command=self.child_init)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Обновить таблицу", command='')

        self.help_menu.add_checkbutton(label="Вывести только изменившиеся позиции",
                                       onvalue=1,
                                       offvalue=0,
                                       variable=self.show_changed,
                                       command='self.filtered_data')

        self.add_cascade(label="Цены", menu=self.file_menu)
        self.add_cascade(label="Отображение", menu=self.help_menu)

    def child_init(self):
        SelectionMenu(self.master)


if __name__ == '__main__':
    run = GUI()
    run.mainloop()

'''Подумать, как очищать таблицу, 
реализовать фильтрацию по изменённым значениям, 
разобраться с проверкой цен и наимнований'''
