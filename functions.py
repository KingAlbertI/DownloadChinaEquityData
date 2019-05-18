import pandas as pd
import numpy as np
import os
import datetime as dt
import time
import pandas_datareader
import pandas_datareader.data as web

source_id = 'yahoo'
def get_single_stock_data(folder, stock_ticker, start_date, end_date):
    try:
        try:
            stock_data = web.DataReader(stock_ticker, source_id, start_date, end_date)
            # sh_stock_list.append(stock_ticker)
            return stock_data
        except pandas_datareader._utils.RemoteDataError:
            print('Ticker error, no such stock')
            return 1
    except KeyError:
        print('Not enough data for this stock')
        return 2