import os
from datetime import datetime
from logs.logger import info_log, debug_log
from tkinter import messagebox as mbox
from gui.download_viewer import DownloadView


def last_downloading() -> str or None:  # Today's date
    """Validation feature for 1st request per day"""
    debug_log("Started searching for downloaded Excel file", 'date_checker.py', '', 'last_downloading')

    all_xlsx = []
    for _, _, filenames in os.walk(".."):
        for filename in filenames:
            if filename.endswith('.xlsx'):
                all_xlsx.append(filename.replace('.xlsx', '').replace('~$', ''))
    if all_xlsx:
        debug_log('List with downloaded files returned', 'date_checker.py', '', 'last_downloading')
        return sorted(all_xlsx, reverse=True)
    else:
        info_log('Data folder is empty', 'date_checker.py', '', 'last_downloading')


class DateCheck:
    """Checking the date a file was last uploaded"""
    def __init__(self, root):
        info_log('Last download date check initialized', 'date_checker.py', 'DateCheck', '__init__')
        self.root = root
        self.date = str(datetime.now().date())
        self.__question()

    def __question(self) -> None:
        if self.date in last_downloading():
            info_log("New file uploaded today", 'date_checker.py', 'DateCheck', '__question')

            mbox.showinfo('Информация', f'Данные на {self.date} загружены!')

        else:
            answer = mbox.askquestion('Уведомление', f'Данные на {self.date} устарели!\n'
                                                     f'Обновить цены?')
            if answer == 'yes':
                debug_log('File upload consent', 'date_checker.py', 'DateCheck', '__question')
                info_log('Started initialization of the file upload window',
                         'date_checker.py', 'DateCheck', 'last_downloading')
                DownloadView(self.root)
            else:
                debug_log("New file upload failure", 'date_checker.py', 'DateCheck', '__question')
