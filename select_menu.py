from tkinter import Toplevel
import tkinter as tk
import writer_and_reader as wr
from table import Table


class SelectionMenu:
    def __init__(self, master):
        self.__master = master
        self.__root = Toplevel(self.__master)
        self.__menu_for_select()
        self.__elements()
        self.__data_for_select()
        self.__root.mainloop()

    def __menu_for_select(self):
        self.__root['background'] = self.__master['background']
        self.__root.title('Выборка файла')
        self.__root.geometry('350x250+500+200')
        self.__root.minsize(350, 250)
        self.__root.maxsize(350, 250)

    def __elements(self):
        info = tk.Label(self.__root,
                        text='Выберите 2 файла',
                        font="Arial 12 bold",
                        background=self.__root['background'])
        self.filenames = tk.Listbox(self.__root,
                                    selectmode=tk.MULTIPLE,
                                    font="Arial 12 bold",
                                    background='white',
                                    justify='center')
        info.pack(side=tk.TOP)
        self.filenames.pack(side=tk.LEFT, padx=10)

        scrollbar = tk.Scrollbar(self.__root, background='#36fc45')
        self.filenames["yscrollcommand"] = scrollbar.set
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def __data_for_select(self):
        excel_files = wr.excel_finder()
        for excel_file in excel_files:
            self.filenames.insert(tk.END, excel_file)
        button = tk.Button(self.__root, text="Выбрать",
                           background="#36fc45",
                           foreground="black",
                           padx="5",
                           pady="5",
                           font="12",
                           command=self.__check_button)
        button.pack(side=tk.BOTTOM, pady=12)

    def __check_button(self):
        select = list(self.filenames.curselection())
        filename_old, filename_new = self.filenames.get(select[0]), self.filenames.get(select[1])
        __table = Table(self.__master, filename_old, filename_new)
        self.__root.destroy()
        __table.table_view()





