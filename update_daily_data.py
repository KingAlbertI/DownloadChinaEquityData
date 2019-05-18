import pandas as pd
import numpy as np
import os
import datetime as dt
import time
from functions import get_single_stock_data
from configs import data_folder_dict, ticker_postfix_dict

start_date = dt.date(2019, 3, 25)
end_date = dt.date.today()

for market_symbol in  ['SH', 'SZ','CY']: #'SH', 'SZ',
    data_folder = data_folder_dict[market_symbol]
    stock_list = os.listdir(data_folder)
    stock_postfix = ticker_postfix_dict[market_symbol]
    keyerror_list = []
    start_number = 1
    for i in stock_list:
        if int(i[:6]) >= start_number:
            time.sleep(1)
            old_data = pd.read_csv(data_folder + i, index_col='Date')
            old_data.index = pd.to_datetime(old_data.index)
            stock_ticker = i.replace('csv',stock_postfix)
            new_data = get_single_stock_data(data_folder, stock_ticker, start_date, end_date)
            if not isinstance(new_data, int):
                data = pd.concat([old_data[old_data.index < new_data.index[0]], new_data], axis=0)
                data.to_csv(data_folder + stock_ticker.replace(stock_postfix, 'csv'))
                print('stock %s is updated' % stock_ticker[:6])