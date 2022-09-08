import tkinter as tk
from logger import info_log, debug_log
from tkinter import Menu, messagebox as mbox
from select_menu import SelectionWindow
from date_checker import DateCheck


class GUI(tk.Tk):
    """Main window"""

    def __init__(self):
        super().__init__()
        info_log("Main window initialized", 'app.py', 'GUI', '__init__')
        self.configs()
        self.protocol('<WM_DELETE_WINDOW>', self.exiting)

    def configs(self):
        self.option_add("*Font", "TkTextFont")
        self.title('Отслеживание цен Карат-Маркет')
        self.geometry('1600x850')
        self['background'] = '#FFFFE0'
        self.minsize(900, 100)
        self.maxsize(1920, 1080)
        self.config(menu=Menubar(self))

    def refresh_data(self):
        info_log('The main window has been updated', 'app.py', 'GUI', '__init__')

        all_widgets = [w for w in self.children]
        for widget in all_widgets:
            if widget == '!menubar':
                pass
            else:
                self.nametowidget(widget).destroy()

    def exiting(self):
        answer = mbox.askquestion('Выход', 'Вы действительно хотите выйти?')
        if answer == 'yes':
            self.destroy()


class Menubar(Menu):  # Меню для управления
    """Menu for selecting actions"""

    def __init__(self, master):
        super().__init__(master)
        info_log("Menu for main window initialized", 'app.py', 'Menubar', '__init__')

        self.master = master
        self.master['background'] = master['background']
        self.configure(background=master['background'])
        self.option_add('*Font', "Arial 12 bold")
        self.menubar_filling()

    def menubar_filling(self):
        self.add_cascade(label="Выбрать цены", command=self.child_init)
        self.add_cascade(label="Загрузить новые цены", command=self.data_update)
        self.add_cascade(label="Отображение", command='')

    def data_update(self):
        DateCheck(self.master)

    def child_init(self):
        debug_log("Select box initialization function started", 'app.py', 'Menubar', '__init__')

        SelectionWindow(self.master)


if __name__ == '__main__':
    info_log("Application start", 'app.py')
    run = GUI()
    run.mainloop()
