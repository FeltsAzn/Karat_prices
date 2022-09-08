from multiprocessing import Process
import tkinter as tk
from tkinter import Toplevel, Button, messagebox as mbox
from logger import debug_log, info_log
from parser import Parser


def run_download():
    """Thread for running in parallel in the background"""
    debug_log('The function to start a new thread has been launched', 'download_viewer.py', '', 'run_download')

    data_downloader = Parser()
    data_downloader.start_collecting()


class DownloadView:
    """Window for displaying the download of new data from the website"""

    def __init__(self, master):
        info_log('Load display window initialized', 'download_viewer.py', 'DownloadView', '__init__')
        self.master = master
        self.__window = Toplevel(self.master)
        self.__points_counter = 0
        self.__view()
        self.__configuration()
        self.__window.after_idle(self.__loading_points, 0)
        self.__downloader_process = Process(target=run_download, daemon=True)
        self.__downloader_process.start()
        self.__window.mainloop()

    def __configuration(self) -> None:
        self.__infobox = tk.Text(self.__window, height=15, font="Arial 8", width=70, background='white')
        self.__window['background'] = '#FFFFE0'
        self.__window.title('Загрузка данных')
        self.__window.geometry('675x300+450+200')
        self.__window.minsize(675, 300)
        self.__window.maxsize(675, 300)
        self.__window.grab_set()

    def __view(self) -> None:
        text1 = tk.Label(self.__window,
                         text='Идёт загрузка данных,',
                         font="Arial 12 bold",
                         bg='#FFFFE0')
        text2 = tk.Label(self.__window,
                         text='Пожалуйста подождите завершения',
                         font="Arial 12 bold",
                         bg='#FFFFE0')
        cancel_button = Button(self.__window, text="Отмена загрузки",
                               background="#ff8c8f",
                               foreground="black",
                               padx="1", pady="1",
                               font="Arial 10", height=1, width=12,
                               command=self.download_cancel)
        self.__points = tk.Label(self.__window, text='.', font="Arial 12 bold", bg='#FFFFE0')
        text1.place(x=250, y=10)
        text2.place(x=195, y=30)
        cancel_button.place(x=525, y=15)
        self.__points.place(x=492, y=30)
        self.__info_box_view()

    def __info_box_view(self) -> None:
        """Data from the logs to display loading"""
        with open('logs.txt', 'r', encoding='utf-8') as file:
            data = file.read()
        self.__infobox = tk.Text(self.__window, height=15, font="Arial 8", width=110, background='white', pady=5)
        self.__infobox.insert('end', data)
        self.__infobox.configure(state='disabled')
        self.__infobox.place(x=5, y=70)
        self.__infobox.yview(tk.END)

    def __loading_points(self, n: int) -> None:
        """Dynamic display of points to visualize data loading"""
        self.__infobox.destroy()
        if self.__downloader_process.is_alive() is True:
            if self.__points_counter % 4 == 0:
                self.__points_counter = 0
            points = '.' * self.__points_counter
            self.__points['text'] = f'{points}'
            self.__points_counter += 1
            self.__info_box_view()
            self.__window.after(500, self.__loading_points, n + 1)
        else:
            self.__end_of_download()

    def download_cancel(self):
        answer = mbox.askquestion('Отмена загрузки файла', "Вы уверены, что хотите отменить загрузку новых цен?")
        if answer == 'yes':
            self.__window.destroy()
            self.__downloader_process.terminate()
            mbox.showinfo('Уведомление', 'Загрузка отменена.')
        else:
            pass

    def __end_of_download(self) -> None:
        self.__window.destroy()
        mbox.showinfo('Уведомление', 'Новая цена загружена!')
        info_log("A new file has been uploaded to the directory", 'download_viewer.py', 'DownloadView', '__stop')
