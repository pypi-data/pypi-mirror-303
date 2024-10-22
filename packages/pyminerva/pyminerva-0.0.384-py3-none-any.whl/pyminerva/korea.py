# Copyright 2023-2025 Jeongmin Kang, jarvisNim @ GitHub
# See LICENSE for details.
'''
Prgram 명: pyminerva.krx.py
Author: jeongmin Kang
Mail: jarvisNim@gmail.com
목적: krx interface
History
- 20240605 krx 연결 (한국증권시장)
- 20240627 korfia 연결 (한국금융투자)
'''
import sys, os, time
import pandas as pd
import requests
import json
import urllib

from datetime import date, datetime, timedelta
from bs4 import BeautifulSoup
from .utils import constant as cst
from . import base

'''
0. 공통영역 설정
'''
_krx_headers = {'User-Agent': 'Chrome/78.0.3904.87 Safari/537.36',
               'Referer': 'http://data.krx.co.kr/', }



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

    print(f"url: {url}")
    print(f"data: {data}")
    response = requests.post(url, data=data, headers=_krx_headers) ### get이 아님에 유의
    # print(response.json())
    print(f"response: {response}")
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
        
    
    response = requests.post(url, data=data, headers=_krx_headers) ### get이 아님에 유의
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
        
    
    response = requests.post(url, data=data, headers=_krx_headers) ### get이 아님에 유의
    # print(response.json())
    data = response.json()['OutBlock_1'] ### 불러온 정보를 json으로 추출하면 dict()구조인데 원하는 정보는 key:'OutBlock_1'에 있다.
    df = pd.DataFrame(data)
    df.columns = ['일자','기관','개인','외국인','기타','전체']  # 구분: 산업별, 시총규모별
    
    return df


# kospi/lospi200/kosdaq/kosdaq150별 투자자별 공매도 거래금액
def get_krx_shorting_investor_value_by_date(index_type, from_date, to_date):
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
        
    
    response = requests.post(url, data=data, headers=_krx_headers) ### get이 아님에 유의
#     print(response.json())
    data = response.json()['OutBlock_1'] ### 불러온 정보를 json으로 추출하면 dict()구조인데 원하는 정보는 key:'OutBlock_1'에 있다.
    df = pd.DataFrame(data)
    df.columns = ['일자','기관','개인','외국인','기타','전체']  # 구분: 산업별, 시총규모별
    
    return df



# 증시자금>증시자금추이
# 
# 추세변화 공식: -5 ~ +5점
# 투자 예탹금 / 위탁매매 미수금 / 반대매매 금액
# - 1달전, 2달전, 3달전 투자예탁금 증가/감소 추세이면 각 +- 1점
# - 3개월 평균 투자예탁금 대비 전일 금액 비율:  (변화비중 / 평균비중) * 100 (단, 전일비중이 평균비중보다 작으면 * -1)
# 이벤트: 절대값 포인트가 1점보다 크면 리포트
def get_korfia_capital_trends(from_date, to_date):
    url = 'https://freesis.kofia.or.kr/meta/getMetaDataList.do'
    body = json.dumps({"dmSearch":{
        'OBJ_NM': "STATSCU0100000060BO",
        'tmpV1': "D",
        'tmpV40': "1000000",
        'tmpV41': "1",
        'tmpV45': from_date, # "20240324",
        'tmpV46': to_date,  # "20240624"
        }
    }, ensure_ascii=False)
    # Response
    request = urllib.request.Request(url)
    request.add_header("Content-Type","application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))

    rescode = response.getcode()
    if(rescode==200):
        result = json.loads(response.read())
    #     print(result)
        data = result['ds1'] ### 불러온 정보를 json으로 추출하면 dict()구조인데 원하는 정보는 key:'block1'에 있다.
        df = pd.DataFrame(data)
        df.columns = ['일자','예탁금','파생상품 예수금','RP','미수금','반대매매금액','미수금대비 반대매매 비중(%)']
        # print(df)
    else:
        print("Error Code:" + rescode)

    return df


# 주식>신용공여현황>신용공여 잔고 추이
# 
# 추세변화 공식: -5 ~ +5점
# 신용거래융자 유가증권/코스닥, 신용거래대주 유가증권/코스닥, 예탁증권 담보융자
# - 3거래일 연속 금액 증가하면 +1, 1일 추가시마다 +1
# - 3개월 평균 금액 대비 전일비중이 비율:  (변화비중 / 평균비중) * 100 (단, 전일비중이 평균비중보다 작으면 * -1)
# 이벤트: 절대값 포인트가 1점보다 크면 리포트
def get_korfia_credit_remain(from_date, to_date):
    url = 'https://freesis.kofia.or.kr/meta/getMetaDataList.do'
    body = json.dumps({"dmSearch":{
            'OBJ_NM': "STATSCU0100000070BO",
            'tmpV1': "D",
            'tmpV40': "1000000",
            'tmpV41': "1",
            'tmpV45': from_date, # "20240324",
            'tmpV46': to_date,  # "20240624"
            }
        }, ensure_ascii=False)
    # Response
    request = urllib.request.Request(url)
    request.add_header("Content-Type","application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))

    rescode = response.getcode()
    if(rescode==200):
        result = json.loads(response.read())
    #     print(result)
        data = result['ds1'] ### 불러온 정보를 json으로 추출하면 dict()구조인데 원하는 정보는 key:'block1'에 있다.
        df = pd.DataFrame(data)
        df.columns = ['일자','신용거래융자/전체','신용거래융자/유가증권','시용거래융자/코스닥','신용거래대주/전체','신용거래대주/유가증권','신용거래대주/코스닥','청약자금대출','예탁증권담보융자']
        print(df)
    else:
        print("Error Code:" + rescode)

    return df


# 주식
# 증시자금/신용공여 증감율
# 
# 추세변화 공식: 전일/전월/전년 대비율 + 리스트상의 날짜기간 3주 워킹데이 의 증감이 지속적으로 나타나고 있으면 -5 ~ +5점
# - 투자예탁금이 추세적으로 늘어나고 있는가? 줄어들고 있는가?
# - 장내파생상품 거래예수금이 추세적으로 늘어나고 있는가? 줄어들고 있는가?
# - 신용거래융자금액이 추세적으로 늘어나고 있는가? 줄어들고 있는가?
# - 예탁증권담보융자금액이 추세적으로 늘어나고 있는가? 줄어들고 있는가?
# 이벤트: 절대값 점수가 1보다 크면 리포트
def get_korfia_stock_market_summary():
    url = 'https://freesis.kofia.or.kr/stockSubMain/STATSCUSUBMAIN01BO.do'
    body = json.dumps({"data":{
            'ipAddress': "",
            'searchLog': "",
            'serviceId': "STATSCUSUBMAIN01",
            'tmpV87': "2",
            'userId': "GUEST"
            }
        }, ensure_ascii=False)
    # Response
    request = urllib.request.Request(url)
    request.add_header("Content-Type","application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))

    rescode = response.getcode()
    if(rescode==200):
        result = json.loads(response.read())
        # print(result)
        columns = [value for key, value in result['dmTitle'].items()]  ### 테이블상의 칼럼명 리스트
        data = result['dsResultList']
        # dsResultList를 데이터프레임으로 변환
        df = pd.DataFrame(data=data)
        # dmTitle 값을 컬럼 이름으로 변경
        df.columns = columns[:len(df.columns)]
        print(df)
    else:
        print("Error Code:" + rescode)

    return df


# 주식>증시동향>유가증권시장
# 
# 추세변화 공식: -5 ~ +5점
# - 3거래일 연속 외국인 비중 증가하면 +1, 1일 추가시마다 +1
# - 3개월 평균 외국인 비중 대비 전일비중이 비율:  (변화비중 / 평균비중) * 100 (단, 전일비중이 평균비중보다 작으면 * -1)
# 이벤트: 절대값 포인트가 1점보다 크면 리포트
def get_korfia_kospi_foregin(from_date, to_date):
    url = 'https://freesis.kofia.or.kr/meta/getMetaDataList.do'
    body = json.dumps({"dmSearch":{
            'OBJ_NM': "STATSCU0100000020BO",
            'tmpV1': "D",
            'tmpV40': "100000000",
            'tmpV41': "10000",
            'tmpV45': from_date, # "20240324",
            'tmpV46': to_date,  # "20240624"
            }
        }, ensure_ascii=False)
    # Response
    request = urllib.request.Request(url)
    request.add_header("Content-Type","application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))

    rescode = response.getcode()
    if(rescode==200):
        result = json.loads(response.read())
    #     print(result)
        data = result['ds1'] ### 불러온 정보를 json으로 추출하면 dict()구조인데 원하는 정보는 key:'block1'에 있다.
        df = pd.DataFrame(data)
        df.columns = ['일자','KOSPI지수','거래량','거래대금','시가총액','외국인 시가총액','외국인 비중']
        print(df)
    else:
        print("Error Code:" + rescode)

    return df


# 주식>증시동향>코스닥시장
# 
# 추세변화 공식: -5 ~ +5점
# - 3거래일 연속 외국인 비중 증가하면 +1, 1일 추가시마다 +1
# - 3개월 평균 외국인 비중 대비 전일비중이 비율:  (변화비중 / 평균비중) * 100 (단, 전일비중이 평균비중보다 작으면 * -1)
# - 이벤트: 절대값 포인트가 1점보다 크면 리포트
def get_korfia_kosdaq_foregin(from_date, to_date):
    url = 'https://freesis.kofia.or.kr/meta/getMetaDataList.do'
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
    # Response
    request = urllib.request.Request(url)
    request.add_header("Content-Type","application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))

    rescode = response.getcode()
    if(rescode==200):
        result = json.loads(response.read())
    #     print(result)
        data = result['ds1'] ### 불러온 정보를 json으로 추출하면 dict()구조인데 원하는 정보는 key:'block1'에 있다.
        df = pd.DataFrame(data)
        df.columns = ['일자','KOSDAQ지수','거래량','거래대금','시가총액','외국인 시가총액','외국인 비중']
        print(df)
    else:
        print("Error Code:" + rescode)

    return df


# ticker 로 한글명 가져오기
def get_korfia_ticker_name(ticker):
    url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
    data = {
        'locale': 'ko_KR',
        'mktsel': 'ALL',   
        'searchText': ticker,
        'bld': 'dbms/comm/finder/finder_srtisu',
        }
    # Response
    response = requests.post(url, data=data, headers=_krx_headers) ### get이 아님에 유의
    # print(response.json())
    data = response.json()['block1'] ### 불러온 정보를 json으로 추출하면 dict()구조인데 원하는 정보는 key:'block1'에 있다.
    df = pd.DataFrame(data)
    df.columns = ['full_code','short_code','codeName','marketCode','marketName',]
    
    return df


# 통계>공매도통계>공매도종합정보>개별종목공매도종합정보
def get_korfia_ticker_shortselling(ticker, ticker_full, ticker_name, from_date, to_date):
    url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
    buf = ticker + '/' + ticker_name

    data = {
        'bld': 'dbms/MDC/STAT/srt/MDCSTAT30001',
        'locale': 'ko_KR',
        'tboxisuCd_finder_srtisu0_0': buf,
        'isuCd': ticker_full,
        'isuCd2': '',
        'codeNmisuCd_finder_srtisu0_0': ticker_name,
        'param1isuCd_finder_srtisu0_0': '',
        'strtDd': from_date,  # 20240513
        'endDd': to_date,  # 20240613
        'share': '1',
        'money': '1',
        'csvxls_isNo': 'false'
        }
    # Response
    response = requests.post(url, data=data, headers=_krx_headers) ### get이 아님에 유의
    # print(response.json())
    data = response.json()['OutBlock_1'] ### 불러온 정보를 json으로 추출하면 dict()구조인데 원하는 정보는 key:'OutBlock_1'에 있다.
    df = pd.DataFrame(data)
    df.columns = ['일자','전체','업틱룰적용','업틱룰예외','순보유잔고수량','전체','업틱룰적용','업틱룰예외','순보유잔고금액']  # 구분: 산업별, 시총규모별
    
    return df



# 통계>기본통계>파생상품>거래실적>투자자별거래실적
    # dict_holders = {
    #     '코스피200선물':['KRDRVFUXAT','KRDRVFUK2I',''],
    #     '미니코스피200선물':['KRDRVFUXAT','KRDRVFUMKI',''],
    #     '코스피200옵션':['KRDRVFUXAT','KRDRVOPK2I',''],
    #     '코스피200위클리옵션(목)':['KRDRVFUXAT','KRDRVOPWKI',''],
    #     '코스피200위클리옵션(월)':['KRDRVFUXAT','KRDRVOPWKM',''],
    #     '미니코스피200옵션':['KRDRVFUXAT','KRDRVOPMKI',''],
    #     '코스닥150선물':['KRDRVFUXAT','KRDRVFUKQI',''],
    #     '코스닥글로벌선물':['KRDRVFUXAT','KRDRVFUQGI',''],
    #     '코스닥150옵션':['KRDRVFUXAT','KRDRVOPKQI',''],
    #     '변동성지수선물':['KRDRVFUXAT','KRDRVFUVKI',''],
    #     '3년국채선물':['KRDRVFUXAT','KRDRVFUBM3',''],
    #     '5년국채선물':['KRDRVFUXAT','KRDRVFUBM5',''],
    #     '10년국채선물':['KRDRVFUXAT','KRDRVFUBMA',''],
    #     '30년국채선물':['KRDRVFUXAT','KRDRVFUBML',''],
    #     '미국달러선물':['KRDRVFUXAT','KRDRVFUUSD',''],
    #     '엔선물':['KRDRVFUXAT','KRDRVFUJPY',''],
    #     '주식선물':['KRDRVFUEQU','KRDRVFUEQU','KRDRVFUEQU'],
    #     '주식옵션':['KRDRVOPEQU','KRDRVOPEQU','KRDRVOPEQU'],
    #     '선물합계':['KRDRVOPEQU','KRDRVFUTTT',''],
    #     '옵션합계':['KRDRVOPEQU','KRDRVOPTTT',''],
    # }
def get_korfia_derivates(product_type, proId, isuCd, isuCd2, from_date, to_date):
    url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
    data = {
        'bld': 'dbms/MDC/STAT/standard/MDCSTAT13101',
        'locale': 'ko_KR',
        'prodId': proId,
        'strtDd': from_date,  # 20240513
        'endDd': to_date,  # 20240613
        'inqTpCd': '1',
        'prtType': 'AMT',
        'prtCheck': 'SUN',
        'isuCd': isuCd,
        'isuCd2': isuCd2,
        'juya': 'ALL',
        'strtDdBox1': from_date,
        'endDdBox1': to_date,
        'strtDdBox2': from_date,
        'endDdBox2': to_date,
        'share': '1',
        'money': '3',
        'csvxls_isNo': 'false'
        }
    # Response
    response = requests.post(url, data=data, headers=_krx_headers) ### get이 아님에 유의
    # print(response.json())
    data = response.json()['output'] ### 불러온 정보를 json으로 추출하면 dict()구조인데 원하는 정보는 key:'OutBlock_1'에 있다.
    df = pd.DataFrame(data)
    df.columns = ['투자자구분','매도','매수','순매수','매도','매수','순매수']  # 1레벨 : 거래량, 거래대금
    
    return df
