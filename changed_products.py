from tkinter import ttk, Scrollbar, Toplevel
import tkinter as tk


class ChangedData:
    def __init__(self, master, data):
        self.master = master
        self.changed_data = data
        self.__root = Toplevel(self.master)
        self.__menu_for_select()
        self.__elements()
        self.__root.mainloop()

    def __menu_for_select(self):
        self.__root['background'] = self.master['background']
        self.__root.title('Выборка файла')
        self.__root.geometry('1000x600+500+200')
        self.__root.minsize(1000, 250)
        self.__root.maxsize(1000, 600)

    def __elements(self):
        ChangedTable(self.__root, self.changed_data)


class MyTree(ttk.Treeview):
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
        '''Назначение тега при добавлении элемента в дерево'''

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
    def __init__(self, root, data, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.__window = root
        self.__style = ttk.Style()
        self.__data = data
        self.__columns = ("№", "Наименование товара", "Старая цена", "Новая цена")
        self.__changed_table = MyTree(self.__window, columns=self.__columns[1:])
        self.__style_tree()
        self.__table_view()
        self.__scroll_view()
        self.__filling_fields(self.__data)

    def __style_tree(self):
        self.__style.map('Treeview', foreground=self.fixed_style('foreground'), background=self.fixed_style('background'))
        self.__style.configure('Treeview', rowheight=20, font="Arial 10 bold")

    # Устранение ошибки с отображением цветов
    def fixed_style(self, option):
        return [elm for elm in self.__style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

    def __scroll_view(self):
        scroller = Scrollbar(self.__changed_table)
        scroller.pack(side=tk.RIGHT, fill=tk.Y)
        scroller.configure(command=self.__changed_table.yview)
        self.__changed_table["yscrollcommand"] = scroller.set

    def __table_view(self):
        self.__changed_table.pack(expand=tk.YES, side=tk.LEFT, fill=tk.BOTH)
        for i, heading in enumerate(self.__columns):
            self.__changed_table.heading('#' + str(i), text=heading)
            if i == 0:
                self.__changed_table.column('#' + str(i), anchor='w', width=50, stretch=False)
            elif i == 1:
                self.__changed_table.column('#' + str(i), anchor='w', width=632, stretch=False, minwidth=200)
            else:
                self.__changed_table.column('#' + str(i), anchor='center', width=50, stretch=True, minwidth=30)

    def __filling_fields(self, all_data):
        for num, _, name, old_price, new_price in all_data:
            self.__changed_table.insert('', tk.END, text=num, values=(name, old_price, new_price))
