import copy
import writer_and_reader as wr


class DataConvertor:
    def __init__(self, filename_old, filename_new):
        self.filename_old = filename_old
        self.filename_new = filename_new

    def __file_reader(self):
        old_data, first_sector_name = wr.reader(filename=self.filename_old)
        new_data, _ = wr.reader(filename=self.filename_new)
        return old_data, new_data, first_sector_name

    def unpacker(self):
        old_data, new_data, first_sector_name = self.__file_reader()
        if old_data == new_data:
            return old_data, first_sector_name
        else:
            old_data_copy = copy.deepcopy(old_data)
            new_data_copy = copy.deepcopy(new_data)
            for old in old_data_copy:
                if old in new_data_copy:
                    old_data[old] = old_data.get(old, []) + [new_data.get(old, [])[2]]
            for name in old_data_copy:
                if name not in new_data_copy:
                    old_data[name] = old_data.get(name, []) + ['Товар удален']
            for name in new_data_copy:
                if name not in old_data:
                    data_list = new_data.get(name, [])
                    price_product = data_list.pop(2)
                    old_data[name] = data_list + ['Новый товар', price_product]
            return old_data, first_sector_name
