import pandas as pd
import numpy as np
import time
from datetime import datetime as dt
import os
from datetime import date, timedelta
import glob


end_date = date.today() - timedelta(1)
start_date = date.today() - timedelta(3)


files_path = os.path.join('D:\\MAPS\\', '3G*')
files = sorted(
    glob.iglob(files_path), key=os.path.getctime, reverse=True)
fileList = files[0:3]
dfList = []
for filename in fileList:
    df = pd.read_excel(filename, 'Site Level')
    df = df[['Time', 'Province', 'City', '3G NODEB', 'Vendor', 'HS Frame Loss Ratio(MAX)_IR(%)']]
    df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
    df['Time'] = df['Time'].dt.date
    dfList.append(df)
df1 = pd.concat(dfList, axis=0)
df1 = df1.dropna(how='any')


df1 = df1[df1['HS Frame Loss Ratio(MAX)_IR(%)'].astype(float) >= 0.5]

dfList2 = []
for site in list(set(df1['3G NODEB'])):
    df_temp = df1[df1['3G NODEB'] == site]
    if len(df_temp['3G NODEB']) == 3:
        dfList2.append(df_temp)

df2 = pd.concat(dfList2, axis=0)
