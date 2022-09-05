from tkinter import ttk, Scrollbar
import tkinter as tk
from changed_products import ChangedData, MyTree
from data_converter import DataConvertor


def sorter(data):
    """
        The function of sorting a tuple in alphabetical order:
        first the section name, then the dictionary key
    """
    key, list_values = data
    return list_values[1], key


class Table(MyTree):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Table, cls).__new__(cls)
        return cls.__instance

    def __init__(self, master, old_filename, new_filename, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.old_filename = old_filename
        self.new_filename = new_filename
        self.data_changed = list()
        self.style = ttk.Style()
        self.table = MyTree(self.master)

    def __style_tree(self):
        self.style.map('Treeview',
                       foreground=self.__fixed_style('foreground'),
                       background=self.__fixed_style('background'))
        self.style.configure('Treeview', rowheight=20, font="Arial 10 bold")

    # Устранение ошибки с отображением цветов
    def __fixed_style(self, option):
        return [elm for elm in self.style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

    def __scroll_view(self):
        scroll = Scrollbar()
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        scroll.configure(command=self.table.yview)
        self.table["yscrollcommand"] = scroll.set

    def table_view(self):
        columns = ("№", "Наименование товара", f"Цена на {self.old_filename}", f"Цена на {self.new_filename}")
        filename_old = f'xlsx_files/{self.old_filename}'
        filename_new = f'xlsx_files/{self.new_filename}'
        self.table.configure(columns=columns[1:])
        self.table.pack(expand=tk.YES, side=tk.LEFT, fill=tk.BOTH)
        for i, heading in enumerate(columns):
            self.table.heading('#' + str(i), text=heading)
            if i == 0:
                continue
            elif i == 1:
                self.table.column('#' + str(i), anchor='w', width=632, stretch=False, minwidth=200)
            else:
                self.table.column('#' + str(i), anchor='center', width=50, stretch=True, minwidth=80)
        self.__style_tree()
        self.__scroll_view()
        self.__filling_fields(filename_old, filename_new)

    def __filling_fields(self, filename_old, filename_new):
        self.clear()
        data_package = DataConvertor(filename_old, filename_new)
        all_data, first_sector_name = data_package.unpacker()
        root_item = self.table.insert('', tk.END, text=first_sector_name, open=False)

        for key, value in sorted(all_data.items(), key=sorter):
            name = key
            num = value[0]
            sector_name = value[1]
            old_price = value[2]
            new_price = value[3]
            try:
                if (int(old_price[:-3].replace(' ', '')) > int(new_price[:-3].replace(' ', '')) or
                        int(old_price[:-3].replace(' ', '')) < int(new_price[:-3].replace(' ', ''))):
                    changed = [num, sector_name, name, old_price, new_price]
                    self.data_changed.append(changed)
            except ValueError:
                if old_price == 'Новый товар' or new_price == 'Товар удален':
                    changed = [num, sector_name, name, old_price, new_price]
                    self.data_changed.append(changed)
            if sector_name == first_sector_name:
                self.table.insert(root_item, tk.END, text=num, values=(name, old_price, new_price))
            else:
                root_item = self.table.insert('', tk.END, text=sector_name, open=False)
                self.table.insert(root_item, tk.END, text=num, values=(name, old_price, new_price))
                first_sector_name = sector_name
        ChangedData(self.master, self.data_changed)

    def clear(self):
        for children in self.table.get_children():
            self.table.delete(children)