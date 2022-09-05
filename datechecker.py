import os
from datetime import datetime
from logger import info_log
from tkinter import messagebox as mbox
from download_viewer import DownloadView


def last_downloading() -> str or None:  # Today's date
    """Validation feature for 1st request per day"""
    all_xlsx = []
    for _, _, filenames in os.walk("."):
        for filename in filenames:
            if filename.endswith('.xlsx'):
                all_xlsx.append(filename.replace('.xlsx', '').replace('~$', ''))
    try:
        return sorted(all_xlsx, reverse=True)
    except IndexError:
        info_log('Data folder is empty')
        return None


class DateCheck:
    def __init__(self, root):
        self.root = root
        self.date = str(datetime.now().date())
        self.question()

    def question(self):
        if self.date in last_downloading():
            mbox.showinfo('Информация', f'Данные на {self.date} загружены!')
        else:
            answer = mbox.askquestion('Уведомление', f'Данные на {self.date} устарели!\n'
                                                     f'Обновить цены?')
            if answer == 'yes':
                DownloadView(self.root)
            else:
                pass
