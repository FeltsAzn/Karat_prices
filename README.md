# Парсинг сайта
Это приложения для отслеживания цен на сайте строительных материалов. Графическая оболочка - Tkinter.
Реализован асинхронный парсер данных с сайта.
Также отображение измененных элементов для удобства отслеживания.


## Локальное развёртывание

Скопируйте через terminal репозиторий:
```bash
git clone https://github.com/FeltsAzn/website-parser-with-gui
```

Установка виртуального окружения, если у вас нет его локально.
```bash
python3 -m pip install --user virtualenv
```

Создайте виртуальное окружение в скопированном репозитории:
```bash
python3 -m venv env
```

Активируйте виртуальное окружение:
```bash
source env/bin/activate
```

Установите файл с зависимостями в виртуальном окружении:
```bash
(venv):~<путь до проекта>$ pip install -r requirements.txt
```

Если вы разворачиваете проект на Linux, то нужно установить Tkinter для графического отображения:
```bash
sudo apt install python3-tk
```


#### Либо запускаете файл через IDE и устанавливаете ```requirements.txt```


Запускаете файл **app.py**
__________________________________________________________________________________________________________________________________________________________
 

Для реализации поставленных задач использовались следующие библиотеки:

***Beatifulsoup4***, ***aiohttp***, ***fake-useragent***, ***lxml*** - для парсинга данных,

***pandas*** - для сохранения данных в формате excel, а также для их чтения (данные сохраняются в excel, т.к. заказчику удобнее редактировать и просматривать),

и другие встроенные библиотеки, такие как: ***asyncio***, ***multiprocessing***, ***logging***, ***tkinter***, ***datetime***.

Библиотека auto-pu-to-exe используется для развертывания приложения на компьютере заказчика.

Приложение разделено на разные файлы (блоки), которыми проще управлять и внедрять новые функции.
(Помимо представленных картинок так же реализован логгер и отдельные настройки парсинга)


Визуальный стиль приложения:
### Главное окно приложения
![Главное меню](https://github.com/FeltsAzn/Karat_prices/blob/master/ScreenShots/main_menu.png)

Для выбора данных для отображения используйте пункт меню «Выбрать цены».
Откроется окно выбора файлов Excel для отображения цен за разные периоды времени.

### Меню выбора файла
![Alt text](https://github.com/FeltsAzn/Karat_prices/blob/master/ScreenShots/select_menu_view.png)

Вы также можете отменить выбор цен, или удалить старые неактуальные файлы с ценами, чтобы очистить место в программе.

### Таблицы с основными данными и измененными данными
![Таблица](https://github.com/FeltsAzn/Karat_prices/blob/master/ScreenShots/table_view.png)

После выбора двух excel-файлов с ценами автоматически загрузится таблица. Это таблица с разделами интернет-магазина. разделы закрыты по умолчанию, чтобы упростить навигацию. Также появится дополнительное окно, которое покажет, какие позиции изменились.

Измененные позиции имеют свой цвет:
- ***Белый цвет*** - товар не изменил цены и находится в новых данных
- ***Зеленый цвет*** - товар подешевел по сравнению с предыдущим днем
- ***Желтый цвет*** – товар подорожал по сравнению с предыдущим днем
- ***Голубой цвет*** - новый продукт
- ***Красный цвет*** - товар удален из базы

Чтобы скачать свежие прайсы, нужно нажать на пункт меню «Скачать новые прайсы». Начнется проверка последней загрузки текущих цен, после чего откроется окно загрузки.

### Загрузка нового окна вывода данных
![Загрузка](https://github.com/FeltsAzn/Karat_prices/blob/master/ScreenShots/download_view.png)

В этом окне отображаются обычные логи парсера. Он не несет смысловой нагрузки, но визуально показывает, что программа что-то делает. При желании можно отменить загрузку новых данных

Стоит отметить, что вывод данных загрузки и сама загрузка находятся в разных процессах, чтобы можно было запускать эти задачи параллельно.

________________________________________________________
# Scraping site
These are applications for tracking prices on a building materials website. Graphic cover - Tkinter.
An asynchronous data parser from the site has been implemented.
Also displaying changed items for easy tracking.

## Local deployment

Copy via terminal repository:
```bash
git clone https://github.com/FeltsAzn/website-parser-with-gui
```

Install virtual environment if you don't have it
```bash
python3 -m pip install --user virtualenv
```

Create a virtual environment in the copied repository:
```bash
python3 -m venv env
```

Activate the virtual environment:
```bash
source env/bin/activate
```

Install the dependency file in the virtual environment:
```bash
(venv):~<project path>$ pip install -r requirements.txt
```

If you are deploying a project on Linux, then you need to install Tkinter for graphical display:
```bash
sudo apt install python3-tk
```

#### Or run the file through the IDE and install ```requirements.txt```


Run the **app.py** file


To implement the tasks set, the following were used libraries:

***Beatifulsoup4***, ***aiohttp***, ***fake-useragent***, ***lxml*** - to implement data scraping,

***pandas*** - to save data in excel format, as well as to read them (data is saved in excel, because it is easier to edit and view for the customer),

and another built-in libraries such as: ***asyncio***, ***multiprocessing***, ***logging***, ***tkinter***, ***datetime***.

The auto-pu-to-exe library is used to deploy the application on the customer's computer

The application is divided into different files (blocks), which are easier to manage and implement new features.
(In addition to the presented pictures, a logger and separate settings for scraping are also implemented)


App Visual Style:                                                                                                        
### Main application window                                                            
![Alt text](https://github.com/FeltsAzn/Karat_prices/blob/master/ScreenShots/main_menu.png)

To select the data to display, use the "Выбрать цены" menu item.
A window for selecting Excel files will open to display prices for different time periods. 

### File selection menu                                                            
![Alt text](https://github.com/FeltsAzn/Karat_prices/blob/master/ScreenShots/select_menu_view.png)

You can also cancel the selection of prices, or delete old irrelevant files with prices to clean up the program space

### Tables with master data and changed data                                                            
![Alt text](https://github.com/FeltsAzn/Karat_prices/blob/master/ScreenShots/table_view.png)

After selecting two excel files with prices, a table will automatically load. This is a table with sections of the online store. sections are closed by default to make it easier to navigate. An additional window will also be displayed that will show which positions have changed.

Changed positions have their own color:
- ***White color*** - the product has not changed prices and is in the new data
- ***Green color*** - the product has reduced the price compared to the previous day
- ***Yellow color*** - the product increased in price compared to the previous day
- ***Lightblue color*** - new product
- ***Red color*** - the product has been removed from the database

To download fresh prices, you need to click on the menu item "Download new prices". This will start checking for the last download of current prices, after which the download window will open.

### Loading new data output window                                                            
![Alt text](https://github.com/FeltsAzn/Karat_prices/blob/master/ScreenShots/download_view.png)

This window displays the usual logs of the parser. It does not carry a semantic load, but it shows visually that the program is doing something. If desired, you can cancel the download of new data

It is worth noting that the output of the download data and the download itself are in different processes so that you can run these tasks in parallel.



