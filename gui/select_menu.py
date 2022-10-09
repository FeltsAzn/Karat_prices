import os
import tkinter as tk
from tkinter import Toplevel, messagebox as mbox
from logs.logger import debug_log, info_log, warning_log
from data_methods import writer_and_reader as wr
from gui.table import Table


class SelectionWindow:
    """Menu for selecting the displayed data"""
    info_log('Selection window created')

    def __init__(self, master):
        info_log('Selection window initialized', 'select_menu.py', 'SelectionWindow', '__init__')

        self.__master = master
        self.__window = Toplevel(self.__master)
        self.__menu_for_select()
        self.__elements()
        self.__data_for_select()

    def __menu_for_select(self) -> None:
        self.__window['background'] = self.__master['background']
        self.__window.title('Выборка файла')
        self.__window.geometry('350x250+500+200')
        self.__window.minsize(350, 250)
        self.__window.maxsize(350, 250)
        self.__window.grab_set()

    def __elements(self) -> None:
        info = tk.Label(self.__window,
                        text='Выберите 2 файла:',
                        font="Arial 12 bold",
                        background=self.__window['background'])
        self.__filenames = tk.Listbox(self.__window,
                                      selectmode=tk.MULTIPLE,
                                      font="Arial 12 bold",
                                      background='white',
                                      justify='left')
        info.place(x=10, y=10)
        self.__filenames.place(x=5, y=40, width=222, height=200)
        scrollbar = tk.Scrollbar(self.__window, background='#36fc45')
        scrollbar.configure(command=self.__filenames.yview)
        scrollbar.place(x=225, y=40, height=200)
        self.__filenames["yscrollcommand"] = scrollbar.set
        self.__buttons()

    def __data_for_select(self) -> None:
        debug_log("The search function for Excel files in the directory has been launched",
                  'select_menu.py', 'SelectionWindow', '__data_for_select')
        excel_files = wr.excel_finder()
        for excel_file in reversed(excel_files):
            self.__filenames.insert(tk.END, excel_file)

    def __buttons(self):
        choose_button = tk.Button(self.__window, text="Выбрать",
                                  background="#caffd3", foreground="black",
                                  padx="3", pady="3",
                                  font="Arial 12", height=1, width=8,
                                  command=self.__open_files)
        delete_button = tk.Button(self.__window, text="Удалить",
                                  background="#ff8c8f",
                                  foreground="black",
                                  padx="3", pady="3",
                                  font="Arial 12", height=1, width=8,
                                  command=self.__delete_file)
        cancel_button = tk.Button(self.__window, text="Отмена",
                                  background="#F0FFFF",
                                  foreground="black",
                                  padx="3", pady="3",
                                  font="Arial 12", height=1, width=8,
                                  command=self.__window.destroy)
        choose_button.place(x=250, y=40)
        delete_button.place(x=250, y=90)
        cancel_button.place(x=250, y=140)

    def __open_files(self) -> None:
        debug_log("The function to initialize the table with data has been launched",
                  'select_menu.py', 'SelectionWindow', '__check_button')
        select = list(self.__filenames.curselection())
        try:
            filename_old, filename_new = self.__filenames.get(select[1]), self.__filenames.get(select[0])
        except IndexError:
            f = mbox.showerror('Ошибка', "Нужно выбрать 2 файла для отображения!")
            print(f)
        else:
            self.__window.destroy()
            info_log("Selection window destroyed", 'select_menu.py', 'SelectionWindow', '__check_button')
            Table(self.__master, filename_old, filename_new)

    def __delete_file(self):
        first_answer = mbox.askquestion('Удаление файла', 'Вы действительно хотите удалить данные с ценами?')
        if first_answer == 'yes':
            second_answer = mbox.askquestion('Внимание!', 'Если файл скачан позже нынешней даты,\n'
                                                          'то его нельзя cнова скачать!\n'
                                                          'Продолжить?')
            if second_answer == 'yes':
                delete_names = []
                try:
                    filenames = list(self.__filenames.curselection())
                    for filename in filenames:
                        delete_names.append(self.__filenames.get(filename))
                        file = f'xlsx_files/{self.__filenames.get(filename)}'
                        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file)
                        os.remove(path)
                except Exception as ex:
                    self.__window.destroy()
                    mbox.showerror('Ошибка', "Нужно выбрать файл для удаления!")
                    warning_log(f'{ex}', 'select_menu.py', 'SelectWindow', '__delete_file')
                    SelectionWindow(self.__master)
                else:
                    self.__window.destroy()
                    if len(delete_names) == 1:
                        mbox.showinfo('Уведомление', f'Файл {delete_names[0]} удален!')
                    else:
                        mbox.showinfo('Уведомление', f'Файлы {", ".join(delete_names)} удалены!')
                    SelectionWindow(self.__master)


