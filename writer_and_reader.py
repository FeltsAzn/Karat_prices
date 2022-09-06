import pandas
import os
from datetime import datetime
from logger import exception_log, debug_log, info_log


def sorter(data):
    """The function of sorting a tuple in alphabetical order:
    first the section name, then the dictionary key
    """
    d, name = data
    key = d.keys()
    return name, *key


def writer(list_tuples: [tuple]) -> None:
    """The function of writing received data to xlsx file"""
    info_log('Entered the function to write data Excel file', 'writer_and_reader.py', '', 'writer')

    names = []
    prices = []
    names_sections = []
    backup_list = []
    counter = 0
    for d, names_section in sorted(list_tuples, key=sorter):
        for name, price in d.items():
            counter += 1
            names_sections.append(names_section)
            names.append(name)
            prices.append(price)
            backup_list.append((str(counter), str(names_section), str(name), str(price)))
    data = pandas.DataFrame(
        {
            'Number_id': [i for i in range(1, counter+1)],
            'Section_name': names_sections,
            'Product_name': names,
            'Price': prices
         }
    )
    date = datetime.now().date()
    try:
        data.to_excel(f'xlsx_files/{date}.xlsx', encoding='utf-8')
    except Exception as ex:
        exception_log('Data has not been recorded', 'writer_and_reader.py', '', 'writer', ex)
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Backup_data.txt')
        os.remove(path)
        with open('Backup_data.txt', 'a', encoding='utf-8') as file:
            for line in backup_list:
                for el in line:
                    file.write(el)
                file.write('\n')

        debug_log('Information was been save to Backup_data.txt', 'writer_and_reader.py', '', 'writer')
    else:

        debug_log(f'Information was been save to {date}.xlsx', 'writer_and_reader.py', '', 'writer')
        debug_log('Registration completed successfully!', 'writer_and_reader.py', '', 'writer')


def excel_finder() -> list:
    """Searching for files in the program directory"""
    info_log('Entered the function to display Excel files in a directory',
             'writer_and_reader.py', '', 'excel_finder')

    filenames = []
    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename.endswith('.xlsx') and filename.startswith('20'):
                filenames.append(filename)

    debug_log('Return a list of excel files in a directory',
              'writer_and_reader.py', '', 'excel_finder')

    return filenames


def reader(filename: str) -> (dict, str):
    """Excel file reading function"""
    info_log('The function was entered to read the excel file in the directory',
             'writer_and_reader.py', '', 'reader')

    excel_data = pandas.read_excel(filename, sheet_name='Sheet1')
    numbers_id = [num for num in excel_data['Number_id']]
    sector_names = [data for data in excel_data['Section_name']]
    product_names = [data for data in excel_data['Product_name']]
    prices = [data for data in excel_data['Price']]
    all_data = {}
    first_sector_name = sector_names[0]
    for number_id, sector_name, product_name, price in zip(numbers_id, sector_names, product_names, prices):
        all_data[product_name] = [number_id, sector_name, price]

    debug_log("Returning a dictionary with data from an excel\n"
              " file and the name of the first section with data",
              'writer_and_reader.py', '', 'reader')

    return all_data, first_sector_name
