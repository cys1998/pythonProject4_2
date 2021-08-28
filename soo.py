import matplotlib
from flask import Flask, render_template,send_file
import io
import os
import base64
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

fig,ax = plt.subplots(figsize=(8,6)) #하나의 axes를 가지는 figure를 만듦
ax = sns.set_style(style="darkgrid")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", title = '월별 꽃 판매 현황')

@app.route('/visualize')
def visualize():
    path = 'C:/Users/최윤수/Desktop/monthly_soo'
    file_list = os.listdir(path)
    print(file_list)
    soo_all = pd.DataFrame()

    for file_name in file_list:
        file_name = path + '/' + file_name
        i = pd.read_excel(file_name)
        i = i.drop(columns=['품종', '품목', '등급'], axis=0)

        a = i['속수량'].sum().astype(int)
        b = int(i['최고단가'].mean())
        c = int(i['최저단가'].mean())
        d = int(i['평균단가'].mean())
        data = {'Date': [file_name.replace(path + '/', '').split('.')[0]],
                '속수량': a,
                '최고단가': b,
                '최저단가': c,
                '평균단가': d}
        i = pd.DataFrame(data)
        soo_all = pd.concat((soo_all, i), axis=0, ignore_index=True)
    print(soo_all)

    font_location = 'C:/Windows/Fonts/malgun.ttf'
    font_name = fm.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    sns.lineplot(data=soo_all, x='Date', y='최고단가', label='최고단가', marker='s')
    sns.lineplot(data=soo_all, x='Date', y='평균단가', label='평균단가', marker='s')
    sns.lineplot(data=soo_all, x='Date', y='최저단가', label='최저단가', marker='s')
    #sns.set(font=font_name)

    plt.ylabel("PRICE")
    plt.xlabel("DATE")
    plt.title('Monthly_Sooguk', fontsize=10)

    canvas = FigureCanvas(fig) #사진이나 다양한 형태의 그림 명시하기 위한 부분.
    img = io.BytesIO() #파일로 저장 안하고 binary object에 저장해서 그대로 file에 넘겨준다고 생각하면 됨..-> 객체 내에 저장된 bytes정보를 불러와 이미지로 읽어줌.
    fig.savefig(img)  #절대경로, 상대경로...(plt.savefig('fig1.png',dpi=300) -> pyplot을 figure 파일로 저장하는 방법 // 이미지를 이미지 파일로 저장
    img.seek(0) #object읽었기 때문에 처음으로 돌아가줌..
    return send_file(img, mimetype='img/png') #url요청 오면 그에 상응하는 파일을 내부에서 생성해서 보내주는 함수


if __name__ == '__main__':
    app.run(debug=True)