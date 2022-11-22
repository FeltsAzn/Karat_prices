# Scraping site
These are applications for tracking prices on a building materials website. Graphic cover - Tkinter.
An asynchronous data parser from the site has been implemented.
Also displaying changed items for easy tracking.


To implement the tasks set, the following were used libraries:

***Beatifulsoup4***, ***aiohttp***, ***fake-useragent***, ***lxml*** - to implement data scraping,

***pandas*** - to save data in excel format, as well as to read them (data is saved in excel, because it is easier to edit and view for the customer),

and another built-in libraries such as: ***asyncio***, ***multiprocessing***, ***logging***, ***tkinter***, ***datetime***.

The auto-pu-to-exe library is used to deploy the application on the customer's computer

The application is divided into different files (blocks), which are easier to manage and implement new features.
(In addition to the presented pictures, a logger and separate settings for scraping are also implemented)


App Visual Style:                                                                                                        
# Main application window                                                            
![Alt text](https://github.com/FeltsAzn/Karat_prices/blob/master/ScreenShots/main_menu.png)

To select the data to display, use the "Выбрать цены" menu item.
A window for selecting Excel files will open to display prices for different time periods. 

# File selection menu                                                            
![Alt text](https://github.com/FeltsAzn/Karat_prices/blob/master/ScreenShots/select_menu_view.png)

You can also cancel the selection of prices, or delete old irrelevant files with prices to clean up the program space

# Tables with master data and changed data                                                            
![Alt text](https://github.com/FeltsAzn/Karat_prices/blob/master/ScreenShots/table_view.png)

After selecting two excel files with prices, a table will automatically load. This is a table with sections of the online store. sections are closed by default to make it easier to navigate. An additional window will also be displayed that will show which positions have changed.

Changed positions have their own color:
White color - the product has not changed prices and is in the new data
Green color - the product has reduced the price compared to the previous day
Yellow color - the product increased in price compared to the previous day
Lightblue color - new product
Red color - the product has been removed from the database

To download fresh prices, you need to click on the menu item "Download new prices". This will start checking for the last download of current prices, after which the download window will open.

# Loading new data output window                                                            
![Alt text](https://github.com/FeltsAzn/Karat_prices/blob/master/ScreenShots/download_view.png)

This window displays the usual logs of the parser. It does not carry a semantic load, but it shows visually that the program is doing something. If desired, you can cancel the download of new data

It is worth noting that the output of the download data and the download itself are in different processes so that you can run these tasks in parallel.



