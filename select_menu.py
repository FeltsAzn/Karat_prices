from tkinter import Toplevel
import tkinter as tk
from logger import debug_log, info_log
import writer_and_reader as wr
from table import Table


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

    def __elements(self) -> None:
        info = tk.Label(self.__window,
                        text='Выберите 2 файла',
                        font="Arial 12 bold",
                        background=self.__window['background'])
        self.__filenames = tk.Listbox(self.__window,
                                      selectmode=tk.MULTIPLE,
                                      font="Arial 12 bold",
                                      background='white',
                                      justify='center')
        info.pack(side=tk.TOP)
        self.__filenames.pack(side=tk.LEFT, padx=10)

        scrollbar = tk.Scrollbar(self.__window, background='#36fc45')
        self.__filenames["yscrollcommand"] = scrollbar.set
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def __data_for_select(self) -> None:
        debug_log("The search function for Excel files in the directory has been launched",
                  'select_menu.py', 'SelectionWindow', '__data_for_select')
        excel_files = wr.excel_finder()
        for excel_file in excel_files:
            self.__filenames.insert(tk.END, excel_file)
        button = tk.Button(self.__window, text="Выбрать",
                           background="#36fc45",
                           foreground="black",
                           padx="5",
                           pady="5",
                           font="12",
                           command=self.__check_button)
        button.pack(side=tk.BOTTOM, pady=12)

    def __check_button(self) -> None:
        debug_log("The function to initialize the table with data has been launched",
                  'select_menu.py', 'SelectionWindow', '__check_button')
        select = list(self.__filenames.curselection())
        filename_old, filename_new = self.__filenames.get(select[0]), self.__filenames.get(select[1])
        self.__window.destroy()
        info_log("Selection window destroyed", 'select_menu.py', 'SelectionWindow', '__check_button')
        Table(self.__master, filename_old, filename_new)
