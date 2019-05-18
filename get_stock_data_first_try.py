import pandas as pd
import numpy as np
import  os
import datetime as dt
import time
import pandas_datareader

import pandas_datareader.data as web

start_date = dt.date(1989,12,29)
end_date = dt.date.today()

sh_list = [str(i) for i in range(600000, 604050)]
sh_stock_list = []
keyerror_list = []
for i in sh_list:
    time.sleep(1)
    stock_ticker = i + '.SS'
    try:
        try:
            stock_data = web.DataReader(stock_ticker, 'yahoo', start_date,end_date)
            sh_stock_list.append(stock_ticker)
            try:
                stock_data.to_csv('SH_stock_data/'+stock_ticker.replace('SS', 'csv'))
                print('SH Stock %s is processed'%i)
            except FileNotFoundError:
                os.mkdir('SH_stock_data/')
                stock_data.to_csv('SH_stock_data/' + stock_ticker.replace('SS', 'csv'))
        except pandas_datareader._utils.RemoteDataError:
            print('Ticker error, no such stock')
    except KeyError:
        print('Not enough data for this stock')
        keyerror_list.append(stock_ticker)


sh_list = [str(i) for i in range(600000, 603000)]
sz_list = ['0' + x[1:] for x in sh_list]
sz_stock_list = []
keyerror_list = []
for i in sz_list:
    time.sleep(1)
    stock_ticker = i + '.SZ'
    try:
        try:
            stock_data = web.DataReader(stock_ticker, 'yahoo', start_date,end_date)
            print('SZ Stock %s is processed' % i)
            sz_stock_list.append(stock_ticker)
            try:
                stock_data.to_csv('SZ_stock_data/'+stock_ticker.replace('SZ', 'csv'))
            except FileNotFoundError:
                os.mkdir('SZ_stock_data/')
                stock_data.to_csv('SZ_stock_data/' + stock_ticker.replace('SZ', 'csv'))
        except pandas_datareader._utils.RemoteDataError:
            print('Ticker error, no such stock')
    except KeyError:
        print('Not enough data for this stock')
        keyerror_list.append(stock_ticker)


sh_list = [str(i) for i in range(600000, 600800)]
cy_list = ['3' + x[1:] for x in sh_list]
cy_stock_list = []
keyerror_list = []
for i in cy_list:
    time.sleep(1)
    stock_ticker = i + '.SZ'
    try:
        try:
            stock_data = web.DataReader(stock_ticker, 'yahoo', start_date,end_date)
            print('CYB Stock %s is processed' % i)
            cy_stock_list.append(stock_ticker)
            try:
                stock_data.to_csv('CY_stock_data/'+stock_ticker.replace('SZ', 'csv'))
            except FileNotFoundError:
                os.mkdir('CY_stock_data/')
                stock_data.to_csv('CY_stock_data/' + stock_ticker.replace('SZ', 'csv'))
        except pandas_datareader._utils.RemoteDataError:
            print('Ticker error, no such stock')
    except KeyError:
        print('Not enough data for this stock')
        keyerror_list.append(stock_ticker)


