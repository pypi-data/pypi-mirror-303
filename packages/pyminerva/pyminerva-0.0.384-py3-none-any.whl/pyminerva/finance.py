# Copyright 2023-2025 Jeongmin Kang, jarvisNim @ GitHub
# See LICENSE for details.
'''
Prgram 명: pyminerva.finance.py
Author: jeongmin Kang
Mail: jarvisNim@gmail.com
목적: 금융관련 함수들 정의
History
- 20240522 create
'''

import sys, os, time
import numpy as np
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import yfinance as yf
import requests

from scipy import signal
from datetime import date, datetime, timedelta
from bs4 import BeautifulSoup
from .utils import constant as cst
from . import base

'''
0. 공통영역 설정
'''

#####################################
# funtions
#####################################

def make_margin_debt_____():

    table_name = 'WorldBank'

    url = 'https://www.finra.org/sites/default/files/2021-03/margin-statistics.xlsx'

    response = requests.get(url, timeout=10, verify=False)
    
    if response.status_code == 200:
        with open(data_dir+'/WorldBank.xlsx', 'wb') as file:
            file.write(response.content)
        sleep(10)            
    else:
        log_batch.error(f" >>> WorldBank.xlsx 다운로드 실패. 응답 코드: {response.status_code}")

    df = pd.read_excel('./batch/reports/data/WorldBank.xlsx', skiprows=range(0, 3),)
    df = df.reset_index(drop=True)
    df.columns = ['Category_1', 'Category_2', 'Category_3', 'Category_4', 'Category_5', '_2021', '_2022', '_2023e',\
                  '_2024f', '_2025f', 'filler' ,'_2023e_d', '_2024f_d', '_2025f_d']
    write_dump_table(table_name, df)
    
