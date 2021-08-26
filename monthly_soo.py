import matplotlib
import pandas as pd
import xlrd
from glob import glob
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

font_location='C:/Windows/Fonts/malgun.ttf'
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

aug = pd.read_excel('C:/Users/최윤수/Desktop/monthly_soo/수국8월.xls', sheet_name=0)
aug = aug.drop(columns=['등급', '품목', '품종'], axis=0)

a = aug['속수량'].sum().astype(int)
b = int(aug['최고단가'].mean())
c = int(aug['최저단가'].mean())
d = int(aug['평균단가'].mean())
data = {'Date': ['2020-08'],
        '속수량': a,
        '최고단가': b,
        '최저단가': c,
        '평균단가': d}

aug = pd.DataFrame(data)

sep = pd.read_excel('C:/Users/최윤수/Desktop/monthly_soo/수국9월.xls', sheet_name=0)
sep = sep.drop(columns=['등급', '품목', '품종'], axis=0)

a = sep['속수량'].sum().astype(int)
b = int(sep['최고단가'].mean())
c = int(sep['최저단가'].mean())
d = int(sep['평균단가'].mean())
data = {'Date': ['2020-09'],
        '속수량': a,
        '최고단가': b,
        '최저단가': c,
        '평균단가': d}

sep = pd.DataFrame(data)

oct = pd.read_excel('C:/Users/최윤수/Desktop/monthly_soo/수국10월.xls', sheet_name=0)
oct = oct.drop(columns=['등급', '품목', '품종'], axis=0)

a = oct['속수량'].sum().astype(int)
b = int(oct['최고단가'].mean())
c = int(oct['최저단가'].mean())
d = int(oct['평균단가'].mean())
data = {'Date': ['2020-10'],
        '속수량': a,
        '최고단가': b,
        '최저단가': c,
        '평균단가': d}

oct = pd.DataFrame(data)

nov = pd.read_excel('C:/Users/최윤수/Desktop/monthly_soo/수국11월.xls', sheet_name=0)
nov = nov.drop(columns=['등급', '품목', '품종'], axis=0)

a = nov['속수량'].sum().astype(int)
b = int(nov['최고단가'].mean())
c = int(nov['최저단가'].mean())
d = int(nov['평균단가'].mean())
data = {'Date': ['2020-11'],
        '속수량': a,
        '최고단가': b,
        '최저단가': c,
        '평균단가': d}

nov = pd.DataFrame(data)

dec = pd.read_excel('C:/Users/최윤수/Desktop/monthly_soo/수국12월.xls', sheet_name=0)
dec = dec.drop(columns=['등급', '품목', '품종'], axis=0)

a = dec['속수량'].sum().astype(int)
b = int(dec['최고단가'].mean())
c = int(dec['최저단가'].mean())
d = int(dec['평균단가'].mean())
data = {'Date': ['2020-12'],
        '속수량': a,
        '최고단가': b,
        '최저단가': c,
        '평균단가': d}

dec = pd.DataFrame(data)

apr = pd.read_excel('C:/Users/최윤수/Desktop/monthly_soo/수국4월.xls', sheet_name=0)
apr = apr.drop(columns=['등급', '품목', '품종'], axis=0)

a = apr['속수량'].sum().astype(int)
b = int(apr['최고단가'].mean())
c = int(apr['최저단가'].mean())
d = int(apr['평균단가'].mean())
data = {'Date': ['2021-04'],
        '속수량': a,
        '최고단가': b,
        '최저단가': c,
        '평균단가': d}

apr = pd.DataFrame(data)

jul = pd.read_excel('C:/Users/최윤수/Desktop/monthly_soo/수국7월.xls', sheet_name=0)
jul = jul.drop(columns=['등급', '품목', '품종'], axis=0)

a = jul['속수량'].sum().astype(int)
b = int(jul['최고단가'].mean())
c = int(jul['최저단가'].mean())
d = int(jul['평균단가'].mean())
data = {'Date': ['2021-07'],
        '속수량': a,
        '최고단가': b,
        '최저단가': c,
        '평균단가': d}

jul = pd.DataFrame(data)

aug_21 = pd.read_excel('C:/Users/최윤수/Desktop/monthly_soo/수국21년8월.xls', sheet_name=0)
aug_21 = aug_21.drop(columns=['등급', '품목', '품종'], axis=0)

a = aug_21['속수량'].sum().astype(int)
b = int(aug_21['최고단가'].mean())
c = int(aug_21['최저단가'].mean())
d = int(aug_21['평균단가'].mean())
data = {'Date': ['2021-08'],
        '속수량': a,
        '최고단가': b,
        '최저단가': c,
        '평균단가': d}

aug_21 = pd.DataFrame(data)

soo_all = pd.concat((aug, sep, oct, nov, dec, apr, jul, aug_21), axis=0, ignore_index=True)
print(soo_all)

plt.figure(figsize=(12,8))

soo_all_max_gph = sns.lineplot(data=soo_all, x='Date', y='최고단가', label='최고단가', marker='s')
soo_all_avg_gph = sns.lineplot(data=soo_all, x='Date', y='평균단가',label='평균단가', marker='s')
soo_all_min_gph = sns.lineplot(data=soo_all, x='Date', y='최저단가',label='최저단가',marker='s')

plt.ylabel("가격")
plt.xlabel("날짜")
plt.title('수국-그린의 일년치 경매정보', fontsize=20)
plt.show()

plt.figure(figsize=(12,8))
soo_all_cnt = sns.barplot(data=soo_all, x='Date', y='속수량', color='pink', alpha = 0.5, label='속수량')
plt.show()