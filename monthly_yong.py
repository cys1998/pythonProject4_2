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

aug = pd.read_excel('C:/Users/최윤수/Desktop/monthly_yong/용담8월.xls', sheet_name=0)
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

sep = pd.read_excel('C:/Users/최윤수/Desktop/monthly_yong/용담9월.xls', sheet_name=0)
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

oct = pd.read_excel('C:/Users/최윤수/Desktop/monthly_yong/용담10월.xls', sheet_name=0)
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

yong_all = pd.concat((aug, sep, oct), axis=0, ignore_index=True)
print(yong_all)

plt.figure(figsize=(12,8))

yong_all_max_gph = sns.lineplot(data=yong_all, x='Date', y='최고단가', label='최고단가', marker='s')
yong_all_avg_gph = sns.lineplot(data=yong_all, x='Date', y='평균단가',label='평균단가', marker='s')
yong_all_min_gph = sns.lineplot(data=yong_all, x='Date', y='최저단가',label='최저단가',marker='s')

plt.ylabel("가격")
plt.xlabel("날짜")

plt.title('용담-용담의 일년치 경매정보', fontsize=20)
plt.show()

plt.figure(figsize=(12,8))
yong_all_cnt = sns.barplot(data=yong_all, x='Date', y='속수량', color='pink', alpha = 0.5, label='속수량')
plt.show()