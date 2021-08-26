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
    aug = pd.read_excel('C:/Users/최윤수/Desktop/monthly_yong/용담8월.xls', sheet_name=0)
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

    sep = pd.read_excel('C:/Users/최윤수/Desktop/monthly_yong/용담9월.xls', sheet_name=0)
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

    oct = pd.read_excel('C:/Users/최윤수/Desktop/monthly_yong/용담10월.xls', sheet_name=0)
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

    yong_all = pd.concat((aug, sep, oct), axis=0, ignore_index=True)
    print(yong_all)

    font_location = 'C:/Windows/Fonts/malgun.ttf'
    font_name = fm.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    sns.lineplot(data=yong_all, x='Date', y='최고단가', label='최고단가', marker='s')
    sns.lineplot(data=yong_all, x='Date', y='평균단가', label='평균단가', marker='s')
    sns.lineplot(data=yong_all, x='Date', y='최저단가', label='최저단가', marker='s')

    plt.ylabel("PRICE")
    plt.xlabel("DATE")
    plt.title('Monthly_Yongdam', fontsize=10)

    canvas = FigureCanvas(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='img/png')



if __name__ == '__main__':
    app.run(debug=True)