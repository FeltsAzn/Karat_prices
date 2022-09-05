import tkinter as tk
from threading import Thread
from tkinter import Toplevel, messagebox as mbox
from logger import debug_log
from async_parser_class_xlsx import Parser


def run_download():
    data_downloader = Parser()
    data_downloader.start_collecting()
    debug_log('Start parsing')


class DownloadView:
    def __init__(self, master):
        self.master = master
        self.__window = Toplevel(self.master)
        self.__points_counter = 0
        self.__view()
        self.__configuration()
        self.__window.after_idle(self.__loading_points, 0)
        self.__downloader_thread = Thread(target=run_download)
        self.__downloader_thread.start()
        self.__window.mainloop()

    def __configuration(self):
        self.infobox = tk.Text(self.__window, height=15, font="Arial 8", width=70, background='white')
        self.__window['background'] = '#caffd3'
        self.__window.title('Загрузка данных')
        self.__window.geometry('675x300+450+200')
        self.__window.minsize(675, 300)
        self.__window.maxsize(675, 300)

    def __view(self):
        text1 = tk.Label(self.__window,
                         text='Идёт загрузка данных,',
                         font="Arial 12 bold",
                         bg='#caffd3')
        text2 = tk.Label(self.__window,
                         text='Пожалуйста подождите завершения',
                         font="Arial 12 bold",
                         bg='#caffd3')
        self.points = tk.Label(self.__window, text='.', font="Arial 12 bold", bg='#caffd3')
        text1.place(x=250, y=10)
        text2.place(x=195, y=30)
        self.points.place(x=492, y=30)
        self.__info_box_view()

    def __info_box_view(self):
        with open('logs.txt', 'r', encoding='utf-8') as file:
            data = file.read()
        self.infobox = tk.Text(self.__window, height=15, font="Arial 8", width=110, background='white', pady=5)
        self.infobox.insert('end', data)
        self.infobox.configure(state='disabled')
        self.infobox.place(x=5, y=70)
        self.infobox.yview(tk.END)

    def __loading_points(self, n):
        self.infobox.destroy()
        if self.__downloader_thread.is_alive() is True:
            if self.__points_counter % 4 == 0:
                self.__points_counter = 0
            points = '.' * self.__points_counter
            self.points['text'] = f'{points}'
            self.__points_counter += 1
            self.__info_box_view()
            self.__window.after(500, self.__loading_points, n + 1)
        else:
            self.__stop()

    def __stop(self):
        self.__window.destroy()
        mbox.showinfo('Уведомление', 'Новая цена загружена!')
