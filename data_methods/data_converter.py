import copy
from logs.logger import info_log, debug_log
import data_methods.writer_and_reader as wr


class DataConvertor:
    """Data converter for checking new and deleted positions in files"""

    def __init__(self, filename_old: str, filename_new: str):
        info_log('Data validation class initialized', 'data_converter.py', 'DataConvertor', '__init__')

        self.filename_old = filename_old
        self.filename_new = filename_new

    def __file_reader(self) -> (dict, dict, str):
        info_log('Started function initialization function to read data',
                 'data_converter.py', 'DataConvertor', '__file_reader')

        old_data, first_sector_name = wr.reader(filename=self.filename_old)
        new_data, _ = wr.reader(filename=self.filename_new)
        return old_data, new_data, first_sector_name

    def unpacker(self) -> (dict, str):
        debug_log('Unpacking data from Excel file reading function',
                  'data_converter.py', 'DataConvertor', 'unpacker')

        old_data, new_data, first_sector_name = self.__file_reader()
        if old_data == new_data:
            for old in old_data:
                old_data[old] = old_data.get(old, []) + [new_data.get(old, [])[2]]
            debug_log('Returning Valid Data', 'data_converter.py', 'DataConvertor', 'unpacker')
            return old_data, first_sector_name
        else:
            old_data_copy: dict = copy.deepcopy(old_data)
            new_data_copy: dict = copy.deepcopy(new_data)
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
            debug_log('Returning Valid Data', 'data_converter.py', 'DataConvertor', 'unpacker')
            return old_data, first_sector_name
