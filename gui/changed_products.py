from tkinter import ttk, Scrollbar, Toplevel
from logs.logger import info_log, debug_log
import tkinter as tk


class ChangedData:
    """Changed data output window"""

    def __init__(self, master, data: list):
        info_log('Window table with changed positions initialized',
                 'changed_products.py', 'ChangedData', '__init__')

        self.master = master
        self.changed_data = data
        self.__root = Toplevel(self.master)
        self.__menu_for_select()
        self.__elements()
        self.__root.mainloop()

    def __menu_for_select(self) -> None:
        self.__root['background'] = self.master['background']
        self.__root.title('Выборка файла')
        self.__root.geometry('1000x588+500+200')
        self.__root.minsize(1000, 250)
        self.__root.maxsize(1000, 588)

    def __elements(self) -> None:
        debug_log("The function of initializing the table with the changed "
                  "positions of the product has been launched",
                  'changed_products.py', 'ChangedData', '__elements')

        ChangedTable(self.__root, self.changed_data)


class MyTree(ttk.Treeview):
    """Editing a class method to change the background color of an individual row"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Элементам с тегом green назначить зеленый фон, элементам с тегом red назначить красный фон
        self.tag_configure('green', background='#a6ffa6')
        self.tag_configure('white', background='white')
        self.tag_configure('red', background='#ff8c8f')
        self.tag_configure('lightblue', background='#b7eaff')
        self.tag_configure('yellow', background='#f8ff71')
        self.tag_configure('white', background='white')

    def insert(self, parent_node, index, **kwargs):
        """Assigning a tag when adding an element to the tree"""

        item = super().insert(parent_node, index, **kwargs)

        values = kwargs.get('values', None)

        if values:
            try:
                if values[2] == 'Товар удален':
                    super().item(item, tag='red')
                elif values[1] == 'Новый товар':
                    super().item(item, tag='lightblue')
                elif int(values[1][:-3].replace(' ', '')) > int(values[2][:-3].replace(' ', '')):
                    super().item(item, tag='green')
                elif int(values[1][:-2].replace(' ', '')) == int(values[2][:-3].replace(' ', '')):
                    super().item(item, tag='white')
                elif int(values[1][:-2].replace(' ', '')) < int(values[2][:-3].replace(' ', '')):
                    super().item(item, tag='yellow')
            except ValueError:
                pass

        return item


class ChangedTable(MyTree):
    """Changed data table"""

    def __init__(self, root, data: list, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        info_log('Window changed table initialized', 'changed_products.py', 'ChangedTable', '__init__')

        self.__window = root
        self.__style = ttk.Style()
        self.__data = data
        self.__columns = ("№", "Наименование товара", "Старая цена", "Новая цена")
        self.__changed_table = MyTree(self.__window, columns=self.__columns[1:])
        self.__table_view()

        self.__filling_fields(self.__data)

    def __style_tree(self) -> None:
        self.__style.map('Treeview', foreground=self.fixed_style('foreground'),
                         background=self.fixed_style('background'))
        self.__style.configure('Treeview', rowheight=20, font="Arial 10 bold")

    def fixed_style(self, option: str) -> list:  # Troubleshooting color display
        return [elm for elm in self.__style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

    def __scroll_view(self) -> None:
        scroll = Scrollbar(self.__changed_table)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        scroll.configure(command=self.__changed_table.yview)
        self.__changed_table["yscrollcommand"] = scroll.set

    def __table_view(self) -> None:
        self.__scroll_view()
        self.__style_tree()
        self.__changed_table.pack(expand=tk.YES, side=tk.LEFT, fill=tk.BOTH)
        for i, heading in enumerate(self.__columns):
            self.__changed_table.heading('#' + str(i), text=heading)
            if i == 0:
                self.__changed_table.column('#' + str(i), anchor='w', width=50, stretch=False)
            elif i == 1:
                self.__changed_table.column('#' + str(i), anchor='w', width=632, stretch=False, minwidth=200)
            else:
                self.__changed_table.column('#' + str(i), anchor='center', width=50, stretch=True, minwidth=30)

    def __filling_fields(self, all_data: list) -> None:
        for num, _, name, old_price, new_price in all_data:
            self.__changed_table.insert('', tk.END, text=num, values=(name, old_price, new_price))

        debug_log('Table with changed product positions is full',
                  'changed_products.py', 'ChangedTable', '__filling_fields')
