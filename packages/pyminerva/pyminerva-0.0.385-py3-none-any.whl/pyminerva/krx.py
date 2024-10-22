# Copyright 2023-2025 Jeongmin Kang, jarvisNim @ GitHub
# See LICENSE for details.
'''
Prgram 명: pyminerva.krx.py
Author: jeongmin Kang
Mail: jarvisNim@gmail.com
목적: krx interface
History
- 20240605 create
'''
import sys, os, time
import pandas as pd
import requests
import json

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
# kospi/lospi200/kosdaq/kosdaq150/all 구분별 지표인덱스 히스토리
def get_krx_index_analyse(index_type, from_ym, to_ym):

    url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
    from_y = from_ym[:4]
    from_m = from_ym[4:]
    to_y = to_ym[:4]
    to_m = to_ym[4:]
    
    if index_type == 'KOSPI':
        data = {'bld':'dbms/MDC/EASY/visual/MDCEASY20002',
        'inqObjYn2': 'Y',
        'strtYy': from_y,
        'strtMm': from_m,
        'endYy': to_y,
        'endMm': to_m}
    elif index_type == 'KOSPI 200':
        data = {'bld':'dbms/MDC/EASY/visual/MDCEASY20002',
        'inqObjYn3': 'Y',
        'strtYy': from_y,
        'strtMm': from_m,
        'endYy': to_y,
        'endMm': to_m}
    elif index_type == 'KOSDAQ':
        data = {'bld':'dbms/MDC/EASY/visual/MDCEASY20002',
        'inqObjYn4': 'Y',
        'strtYy': from_y,
        'strtMm': from_m,
        'endYy': to_y,
        'endMm': to_m}
    elif index_type == 'KOSDAQ 150':
        data = {'bld':'dbms/MDC/EASY/visual/MDCEASY20002',
        'inqObjYn5': 'Y',
        'strtYy': from_y,
        'strtMm': from_m,
        'endYy': to_y,
        'endMm': to_m}
    elif index_type == 'ALL': # KOSPI200, KOSDAQ150 두 인덱스 같이 보여줌
        data = {'bld':'dbms/MDC/EASY/visual/MDCEASY20002',
        'inqObjYn3': 'Y',
        'inqObjYn5': 'Y',
        'strtYy': from_y,
        'strtMm': from_m,
        'endYy': to_y,
        'endMm': to_m,
        'itmTpCd1': '3'}
    else:
        print(f"get_krx_index_analyse.index_type is not good!: {index_type}")
        
    
    response = requests.post(url, data=data) ### get이 아님에 유의
#     print(response.json())
    data = response.json()['block1'] ### 불러온 정보를 json으로 추출하면 dict()구조인데 원하는 정보는 key:'block1'에 있다.
    df = pd.DataFrame(data)
    df.columns = ['마켓 구분','년월','종가','PER','PBR','배당률']
    
    return df

# kospi/lospi200/kosdaq/kosdaq150별 각 섹터별 히스토리
def get_krx_sector_analyse(index_type, from_ym, to_ym):

    url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
    from_y = from_ym[:4]
    from_m = from_ym[4:]
    to_y = to_ym[:4]
    to_m = to_ym[4:]
    
    if index_type == 'KOSPI':
        data = {'bld':'dbms/MDC/EASY/visual/MDCEASY20003',
        'inqObjYn5': 'Y',
        'strtYy': from_y,
        'strtMm': from_m,
        'endYy': to_y,
        'endMm': to_m}
    elif index_type == 'KOSPI 200':
        data = {'bld':'dbms/MDC/EASY/visual/MDCEASY20003',
        'inqObjYn3': 'Y',
        'strtYy': from_y,
        'strtMm': from_m,
        'endYy': to_y,
        'endMm': to_m}
    elif index_type == 'KOSDAQ':
        data = {'bld':'dbms/MDC/EASY/visual/MDCEASY20003',
        'inqObjYn4': 'Y',
        'strtYy': from_y,
        'strtMm': from_m,
        'endYy': to_y,
        'endMm': to_m}
    elif index_type == 'KOSDAQ 150':
        data = {'bld':'dbms/MDC/EASY/visual/MDCEASY20003',
        'inqObjYn5': 'Y',
        'strtYy': from_y,
        'strtMm': from_m,
        'endYy': to_y,
        'endMm': to_m}
    elif index_type == 'ALL': # KOSPI200, KOSDAQ150 두 인덱스 같이 보여줌
        data = {'bld':'dbms/MDC/EASY/visual/MDCEASY20003',
        'inqObjYn3': 'Y',
        'inqObjYn5': 'Y',
        'strtYy': from_y,
        'strtMm': from_m,
        'endYy': to_y,
        'endMm': to_m,
        'itmTpCd1': '3'}
    else:
        print(f"get_krx_sector_analyse.index_type is not good!: {index_type}")
        
    
    response = requests.post(url, data=data) ### get이 아님에 유의
#     print(response.json())
    data = response.json()['block1'] ### 불러온 정보를 json으로 추출하면 dict()구조인데 원하는 정보는 key:'block1'에 있다.
    df = pd.DataFrame(data)
    df.columns = ['마켓 구분','단위 구분','순번','년월','섹터명','종가','PER','PBR','배당률']  # 구분: 산업별, 시총규모별
    
    return df


# kospi/lospi200/kosdaq/kosdaq150별 투자자별 공매도 거래량
def get_krx_shorting_investor_volume_by_date(index_type, from_date, to_date):

    url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'

    if index_type == 'KOSPI':
        data = {
            'bld': 'dbms/MDC/STAT/srt/MDCSTAT30301',
            'locale': 'ko_KR',
            'inqCondTpCd': '1',
            'trdVolVal': '1',
            'mktTpCd': '1',
            'strtDd': from_date,  # 20240513
            'endDd': to_date,  # 20240613
            'share': '1',
            'csvxls_isNo': 'false'
            }
    elif index_type == 'KOSDAQ':
        data = {            
            'bld': 'dbms/MDC/STAT/srt/MDCSTAT30301',
            'locale': 'ko_KR',
            'inqCondTpCd': '1',
            'trdVolVal': '1',
            'mktTpCd': '2',
            'strtDd': from_date,  # 20240513
            'endDd': to_date,  # 20240613
            'share': '1',
            'csvxls_isNo': 'false'
            }
    else:
        print(f"get_krx_shorting_investor_volume_by_date.index_type is not good!: {index_type}")
        
    
    response = requests.post(url, data=data) ### get이 아님에 유의
    # print(response.json())
    data = response.json()['OutBlock_1'] ### 불러온 정보를 json으로 추출하면 dict()구조인데 원하는 정보는 key:'OutBlock_1'에 있다.
    df = pd.DataFrame(data)
    df.columns = ['일자','기관','개인','외국인','기타','전체']  # 구분: 산업별, 시총규모별
    
    return df


# kospi/lospi200/kosdaq/kosdaq150별 투자자별 공매도 거래금액
def get_krx_get_shorting_investor_value_by_date(index_type, from_date, to_date):

    url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
    data = 'dbms/MDC/STAT/srt/MDCSTAT30301'

    if index_type == 'KOSPI':
        data = {
            'bld': 'dbms/MDC/STAT/srt/MDCSTAT30301',
            'locale': 'ko_KR',
            'inqCondTpCd': '2',
            'trdVolVal': '2',
            'mktTpCd': '2',
            'strtDd': from_date,  # 20240513
            'endDd': to_date,  # 20240613
            'money': '1',
            'csvxls_isNo': 'false'
            }
    elif index_type == 'KOSDAQ':
        data = {            
            'bld': 'dbms/MDC/STAT/srt/MDCSTAT30301',
            'locale': 'ko_KR',
            'inqCondTpCd': '1',
            'trdVolVal': '1',
            'mktTpCd': '2',
            'strtDd': from_date,  # 20240513
            'endDd': to_date,  # 20240613
            'share': '1',
            'csvxls_isNo': 'false'
            }
    else:
        print(f"get_krx_shorting_investor_volume_by_date.index_type is not good!: {index_type}")
        
    
    response = requests.post(url, data=data) ### get이 아님에 유의
#     print(response.json())
    data = response.json()['OutBlock_1'] ### 불러온 정보를 json으로 추출하면 dict()구조인데 원하는 정보는 key:'OutBlock_1'에 있다.
    df = pd.DataFrame(data)
    df.columns = ['일자','기관','개인','외국인','기타','전체']  # 구분: 산업별, 시총규모별
    
    return df