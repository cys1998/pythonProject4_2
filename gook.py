import matplotlib
from flask import Flask, render_template,send_file
import io
import base64
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

fig,ax = plt.subplots(figsize=(6,4))
ax = sns.set_style(style="darkgrid")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", title = '월별 꽃 판매 현황')

@app.route('/visualize')
def visualize():
    aug = pd.read_excel('C:/Users/최윤수/Desktop/monthly_gook/국화8월.xls', sheet_name=0)
    aug = aug.drop(columns=['등급', '품목', '품종'], axis=0)

    a = aug['속수량'].sum().astype(int)
    b = int(aug['최고단가'].mean())
    c = int(aug['최저단가'].mean())
    d = int(aug['평균단가'].mean())
    data = {'Date': ['20/08'],
            '속수량': a,
            '최고단가': b,
            '최저단가': c,
            '평균단가': d}

    aug = pd.DataFrame(data)
    aug

    sep = pd.read_excel('C:/Users/최윤수/Desktop/monthly_gook/국화9월.xls', sheet_name=0)
    sep = sep.drop(columns=['등급', '품목', '품종'], axis=0)

    a = sep['속수량'].sum().astype(int)
    b = int(sep['최고단가'].mean())
    c = int(sep['최저단가'].mean())
    d = int(sep['평균단가'].mean())
    data = {'Date': ['20/09'],
            '속수량': a,
            '최고단가': b,
            '최저단가': c,
            '평균단가': d}

    sep = pd.DataFrame(data)
    sep

    oct = pd.read_excel('C:/Users/최윤수/Desktop/monthly_gook/국화10월.xls', sheet_name=0)
    oct = oct.drop(columns=['등급', '품목', '품종'], axis=0)

    a = oct['속수량'].sum().astype(int)
    b = int(oct['최고단가'].mean())
    c = int(oct['최저단가'].mean())
    d = int(oct['평균단가'].mean())
    data = {'Date': ['20/10'],
            '속수량': a,
            '최고단가': b,
            '최저단가': c,
            '평균단가': d}

    oct = pd.DataFrame(data)
    oct

    nov = pd.read_excel('C:/Users/최윤수/Desktop/monthly_gook/국화11월.xls', sheet_name=0)
    nov = nov.drop(columns=['등급', '품목', '품종'], axis=0)

    a = nov['속수량'].sum().astype(int)
    b = int(nov['최고단가'].mean())
    c = int(nov['최저단가'].mean())
    d = int(nov['평균단가'].mean())
    data = {'Date': ['20/11'],
            '속수량': a,
            '최고단가': b,
            '최저단가': c,
            '평균단가': d}

    nov = pd.DataFrame(data)
    nov

    dec = pd.read_excel('C:/Users/최윤수/Desktop/monthly_gook/국화12월.xls', sheet_name=0)
    dec = dec.drop(columns=['등급', '품목', '품종'], axis=0)

    a = dec['속수량'].sum().astype(int)
    b = int(dec['최고단가'].mean())
    c = int(dec['최저단가'].mean())
    d = int(dec['평균단가'].mean())
    data = {'Date': ['20/12'],
            '속수량': a,
            '최고단가': b,
            '최저단가': c,
            '평균단가': d}

    dec = pd.DataFrame(data)
    dec

    mar = pd.read_excel('C:/Users/최윤수/Desktop/monthly_gook/국화3월.xls', sheet_name=0)
    mar = mar.drop(columns=['등급', '품목', '품종'], axis=0)

    a = mar['속수량'].sum().astype(int)
    b = int(mar['최고단가'].mean())
    c = int(mar['최저단가'].mean())
    d = int(mar['평균단가'].mean())
    data = {'Date': ['21/03'],
            '속수량': a,
            '최고단가': b,
            '최저단가': c,
            '평균단가': d}

    mar = pd.DataFrame(data)
    mar

    apr = pd.read_excel('C:/Users/최윤수/Desktop/monthly_gook/국화4월.xls', sheet_name=0)
    apr = apr.drop(columns=['등급', '품목', '품종'], axis=0)

    a = apr['속수량'].sum().astype(int)
    b = int(apr['최고단가'].mean())
    c = int(apr['최저단가'].mean())
    d = int(apr['평균단가'].mean())
    data = {'Date': ['21/04'],
            '속수량': a,
            '최고단가': b,
            '최저단가': c,
            '평균단가': d}

    apr = pd.DataFrame(data)
    apr

    may = pd.read_excel('C:/Users/최윤수/Desktop/monthly_gook/국화5월.xls', sheet_name=0)
    may = may.drop(columns=['등급', '품목', '품종'], axis=0)

    a = may['속수량'].sum().astype(int)
    b = int(may['최고단가'].mean())
    c = int(may['최저단가'].mean())
    d = int(may['평균단가'].mean())
    data = {'Date': ['21/05'],
            '속수량': a,
            '최고단가': b,
            '최저단가': c,
            '평균단가': d}

    may = pd.DataFrame(data)
    may

    jun = pd.read_excel('C:/Users/최윤수/Desktop/monthly_gook/국화6월.xls', sheet_name=0)
    jun = jun.drop(columns=['등급', '품목', '품종'], axis=0)

    a = jun['속수량'].sum().astype(int)
    b = int(jun['최고단가'].mean())
    c = int(jun['최저단가'].mean())
    d = int(jun['평균단가'].mean())
    data = {'Date': ['21/06'],
            '속수량': a,
            '최고단가': b,
            '최저단가': c,
            '평균단가': d}

    jun = pd.DataFrame(data)
    jun

    jul = pd.read_excel('C:/Users/최윤수/Desktop/monthly_gook/국화7월.xls', sheet_name=0)
    jul = jul.drop(columns=['등급', '품목', '품종'], axis=0)

    a = jul['속수량'].sum().astype(int)
    b = int(jul['최고단가'].mean())
    c = int(jul['최저단가'].mean())
    d = int(jul['평균단가'].mean())
    data = {'Date': ['21/07'],
            '속수량': a,
            '최고단가': b,
            '최저단가': c,
            '평균단가': d}

    jul = pd.DataFrame(data)
    jul

    aug_21 = pd.read_excel('C:/Users/최윤수/Desktop/monthly_gook/국화21년8월.xls', sheet_name=0)
    aug_21 = aug_21.drop(columns=['등급', '품목', '품종'], axis=0)

    a = aug_21['속수량'].sum().astype(int)
    b = int(aug_21['최고단가'].mean())
    c = int(aug_21['최저단가'].mean())
    d = int(aug_21['평균단가'].mean())
    data = {'Date': ['21/08'],
            '속수량': a,
            '최고단가': b,
            '최저단가': c,
            '평균단가': d}

    aug_21 = pd.DataFrame(data)
    aug_21

    gook_all = pd.concat((aug, sep, oct, nov, dec, mar, apr, may, jun, jul, aug_21), ignore_index=True)
    print(gook_all)

    font_location = 'C:/Windows/Fonts/malgun.ttf'
    font_name = fm.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    sns.lineplot(data=gook_all, x='Date', y='최고단가', label='최고단가', marker='s')
    sns.lineplot(data=gook_all, x='Date', y='평균단가', label='평균단가', marker='s')
    sns.lineplot(data=gook_all, x='Date', y='최저단가', label='최저단가', marker='s')

    plt.ylabel("PRICE")
    plt.xlabel("DATE")
    plt.title('Monthly Gookhwa', fontsize=10)

    canvas = FigureCanvas(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='img/png')

if __name__ == '__main__':
    app.run(debug=True)