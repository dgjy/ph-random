#!/usr/bin/python3
# -*- coding: utf-8 -*-
from mastodon import Mastodon
import time
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os


# 구글시트 세팅


scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("vernal-byway-400717-7ffe1d5a3490.json", scope)
gc = gspread.authorize(creds)
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1l3Zc0-L4yyQ4lCXKTerwA7nnjWwtFOPy-3VSVeEJADE/edit?usp=sharing')
sheet = sh.worksheet("시트1")

# 구글시트 세팅 끝

# 마스토돈 계정 세팅

BASE = 'https://phantasm-enigma.live'

m = Mastodon(
    client_id= os.environ.get("client_id"),
    client_secret= os.environ.get("client_secret"),
    access_token= os.environ.get("access_token"),
    api_base_url=BASE
)

# print('성공적으로 로그인 되었습니다.')

# 마스토동 계정 세팅 끝

celldata2 = sheet.get_all_values()

while True:
    print('루프시작')
    celldata = sheet.get_all_values()
    data_temp = celldata2.copy()
    celldata2 = sheet.get_all_values()

    data_result = celldata.copy()

    idx=0
    for i in celldata:
        if idx >= (len(data_temp)):
            if celldata:
                def main():
                    m.status_post(f"{i[0]}의 랜덤박스 결과: {i[1]}", visibility='unlisted')

            if __name__ == '__main__':
                main()
        idx = idx+1

    time.sleep(10)
