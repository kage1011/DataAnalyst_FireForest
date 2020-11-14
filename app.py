from flask import Flask, render_template, request
import mpld3, numpy as np
from matplotlib import pyplot as plt
from mpld3 import plugins
import matplotlib.patches as mpatches
import pandas as pd
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials, firestore
import tansotansuat


cred = credentials.Certificate('admin.json')
d = pd.read_csv('forestfires1.csv')
firebase_admin.initialize_app(cred,
                              {
                                  'databaseURL': 'https://forestfire1-d16e4.firebaseio.com'
                              }
                              )
db = firestore.client()
col = db.collection('forestfire1').get()
data = {
    'X': [],
    'Y': [],
    'month': [],
    'day': [],
    'FFMC': [],
    'DMC': [],
    'DC': [],
    'ISI': [],
    'temp': [],
    'RH': [],
    'wind': [],
    'rain': [],
    'area': []
}
for i in col:
    j = i.to_dict()
    for k, v in j.items():
        data[k].append(v)



#storage = app.storage()

df = pd.read_csv('forestfires1.csv').values

x1,y1,month1, day1, ffmc1, dmc1, dc1, isi1, temp1, rh1, wind1, rain1, area1 = df[:,0], df[:,1], df[:,2], df[:,3], df[:,4,], df[:,5], df[:,6], df[:,7], df[:,8], df[:,9], df[:,10], df[:,11], df[:,12]

#tính dữ liệu tổng diện tích cháy từng tháng
month=data['month']
area=data['area']
ffmc=data['FFMC']
dmc=data['DMC']
dc=data['DC']
isi=data['ISI']
temp=data['temp']
rh=data['RH']
wind=data['wind']
rain=data['rain']

def convertTo12Month(arr , m): # m la month chua xu ly, arr la tap du lieu can xu ly theo month

    j = 0
    k , a, convertValue, monthOfYear = 0, m[j], [], []
    monthOfYear.append(a)


    while j < len(m):
        if m[j] == a:
            k = k + arr[j]
            j += 1
            if j == len(m):
                convertValue.append(k)
        else:
            convertValue.append(k)
            k = 0
            a = m[j]
            monthOfYear.append(a)
    return convertValue



areaWthoutConvert = area1
windWthoutConvert = wind1


ffmc1 = convertTo12Month(ffmc1, month1)
dmc1 = convertTo12Month(dmc1, month1)
dc1 = convertTo12Month(dc1, month1)
isi1 = convertTo12Month(isi1, month1)
temp1 = convertTo12Month(temp1, month1)
rh1 = convertTo12Month(rh1, month1)
wind1 = convertTo12Month(wind1, month1)
rain1 = convertTo12Month(rain1, month1)
area1 = convertTo12Month(area1, month1)
month1 = list( dict.fromkeys(month1) )


app = Flask(__name__)\

@app.route('/home/')
def index():
    return render_template('index.html')


@app.route('/')
def simplechart():
    return render_template('simplechart.html')
    
@app.route('/line/')
def line():
  
    fig,ax2 = plt.subplots(figsize=(6, 5))
   

        
    # # Tốc độ lan truyền lữa dự kiến và diện tích cháy thực tế
    lineISI = mpatches.Patch(color='red', label='Chỉ số ISI')
    barArea = mpatches.Patch(color='blue', label='Diện tích rừng cháy')
    plt.title("Tốc độ lan truyền lữa dự kiến (ISI) và diện tích cháy thực tế")

    ax2.bar(month1, area1)
    ax2.set_ylabel("ISI")
    ax2.set_xlabel("Tháng")

    #ax2=ax.twinx()
    ax2.plot(month1, isi1, "red")
    ax2.set_ylabel("Diện tích rừng cháy")

    plt.legend(handles=[lineISI, barArea])
    
    chart_html = mpld3.fig_to_html(fig)

    return render_template('line.html',chart=chart_html)


@app.route('/dinhnghia/')
def dinhnghia():
    return render_template("dinhnghiadl.html")

@app.route('/tinh tap trung/')
def tinhtaptrung():
    return render_template("tinhtaptrung.html")

@app.route('/dulieuthieu/')
def dulieuthieu():
    return render_template("dulieuthieu.html")

@app.route('/t1/')
def t1():
    return render_template("t1.html")

@app.route('/t2/')
def t2():
    return render_template("t2.html")

@app.route('/t3/')
def t3():
    return render_template("t3.html")

@app.route('/t4/')
def t4():
    return render_template("t4.html")

@app.route('/line1/')
def line1():
  
    fig,ax1 = plt.subplots(figsize=(6, 5))
    #Tốc độ gió và diện tích cháy thực tế
    ax1.bar(month1, area1)
    ax1.set_ylabel("Diện tích")
    plt.title("Biểu đồ liên hệ giữa gió và diện tích cháy rừng")
    ax1.set_xlabel("Tháng")
    bar = mpatches.Patch(color='blue', label='Diện tích rừng cháy')
    line= mpatches.Patch(color='red', label='Gió')
   
    ax1.plot(month1, wind1, "red")
    ax1.set_ylabel("Tốc độ gió")
    plt.legend(handles=[line, bar]) 
    
    chart_html = mpld3.fig_to_html(fig)

    return render_template('line.html',chart=chart_html)
@app.route("/lineF_area")
def lineF_area():
    fig, ax = plt.subplots()
    divisions, data = tansotansuat.createTable()
    index = np.arange(len(divisions))
    width = 0.3
    ax.set_title("Tần suất tích lũy số vụ cháy rừng ")
    ax.plot(index,data["Tần suất tích lũy"])

    for i, val in enumerate(data["Tần suất tích lũy"]):
        plt.text(index[i],
           val,
           '%1.1f%%' %val,) 
    ax.legend(loc="best")
    listData = []
    columns = data.columns

    for item in columns:
        listData.append(list(data[item]))

    plt.savefig("static/arealine1.png")
    
    return render_template("lineF_area.html",labels=data.columns, index=divisions, data=listData)

@app.route("/lineF_area1")
def lineF_area1():
    fig, ax = plt.subplots()
    divisions, data = tansotansuat.createTablearea()
    index = np.arange(len(divisions))
    width = 0.3
    ax.set_title("Tần suất tích lũy diện tích cháy rừng ")
    ax.plot(index,data["Tần suất tích lũy"])

    for i, val in enumerate(data["Tần suất tích lũy"]):
        plt.text(index[i],
           val,
           '%1.1f%%' %val,) 
    ax.legend(loc="best")
    listData = []
    columns = data.columns

    for item in columns:
        listData.append(list(data[item]))

    plt.savefig("static/arealineF.png")
    
    return render_template("lineF_area1.html",labels=data.columns, index=divisions, data=listData)

@app.route("/lineF_rain")
def lineF_rain():
    fig, ax = plt.subplots()
    divisions, data = tansotansuat.createTablerain()
    index = ['0 -0.64',
'0.64 - 1.28',
'1.28 - 1.92',
'1.92 - 2.56',
'2.56 - 3.2',
'3.2 - 3.84',
'3.84 - 4.48',
'4.48 - 5.12',
'5.12 - 5.76',
'5.76 - 6.4'
]
    width = 0.3
    ax.set_title("Tần suất tích lũy lượng mưa")
    ax.plot(index,data["Tần suất tích lũy"])

    for i, val in enumerate(data["Tần suất tích lũy"]):
        plt.text(index[i],
           val,
           '%1.1f%%' %val,) 
    ax.legend(loc="best")
    listData = []
    columns = data.columns

    for item in columns:
        listData.append(list(data[item]))

    plt.savefig("static/lineraina.png")
    
    return render_template("lineF_rain.html",labels=data.columns, index=divisions, data=listData)

@app.route("/lineF_wind")
def lineF_wind():
    fig, ax = plt.subplots()
    divisions, data = tansotansuat.createTablewind()
    index = ['0 -0.94',
'0.94 - 1.88',
'1.88 - 2.82',
'2.82 - 3.76',
'3.76 - 4.7',
'4.7 - 5.64',
'5.64 - 6.58',
'6.58 - 7.52',
'7.52 - 8.46',
'8.46 - 9.4'
]
    width = 0.3
    ax.set_title("Tần suất tích lũy tốc độ gió ")
    ax.plot(index,data["Tần suất tích lũy"])

    for i, val in enumerate(data["Tần suất tích lũy"]):
        plt.text(index[i],
           val,
           '%1.1f%%' %val,) 
    ax.legend(loc="best")
    listData = []
    columns = data.columns

    for item in columns:
        listData.append(list(data[item]))

    plt.savefig("static/windlineabc.png")
    
    return render_template("lineF_wind.html",labels=data.columns, index=divisions, data=listData)
@app.route('/scatter/')
def scatter():
   fig,ax = plt.subplots(figsize=(6, 5))
   
   
   tempmean=d.groupby('month')['temp'].mean()
   windmean=d.groupby('month')['wind'].mean()
   areamean=d.groupby('month')['area'].mean()
   x_index= windmean.index

   ax.scatter(x_index, tempmean,s=(areamean+1)*30, c=windmean)

   ax.set_title('Tương quan nhiệt độ, gió và diện tích cháy rừng')
   ax.set_xlabel('Tháng')
   ax.set_ylabel('Nhiệt độ')
   
   chart_html = mpld3.fig_to_html(fig)
   return render_template("scatter.html", chart=chart_html)

@app.route('/bar/')
def bar():
   
    # bieu do chỉ số độ ẩm của rác và nhiên liệu cháy, thể hiện mức độ dễ cháy của chúng (ffmc)
    #  ta thấy chỉ số ffmc càng lớn thì diện tích cháy rừng càng cao.


    ind = np.arange(12)
    width = 0.35
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.set_title('biểu đồ chỉ số độ ẩm của rác dễ cháy và diện tích rừng bị cháy')
   
    rects1 = ax.bar(ind - width / 2, ffmc,
                width, color='#1f77b4', alpha=0.5)
    rects2 = ax.bar(ind + width / 2, area,width, color='#1f77b4')
    plt.legend((rects1[0], rects2[0]), ('FFMC', 'Diện tích rừng cháy'))

    chart_html = mpld3.fig_to_html(fig)
    return render_template("bar.html", chart=chart_html)
@app.route('/bar1/')
def bar1():
   
    # bieu do chỉ số độ ẩm của rác và nhiên liệu cháy, thể hiện mức độ dễ cháy của chúng (ffmc)
    #  ta thấy chỉ số dmc càng lớn thì diện tích cháy rừng càng cao.


    ind = np.arange(12)
    width = 0.35
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.set_title('biểu đồ chỉ số độ ẩm của nhiên liệu hỏng  và diện tích rừng bị cháy')
   
    rects1 = ax.bar(ind - width / 2, dmc,
                width, color='#1f77b4', alpha=0.5)
    rects2 = ax.bar(ind + width / 2, area,width, color='#1f77b4')
    plt.legend((rects1[0], rects2[0]), ('DMC', 'Diện tích rừng cháy'))

    chart_html = mpld3.fig_to_html(fig)
    return render_template("bar1.html", chart=chart_html)

@app.route('/bar2/')
def bar2():
   
    

  fig, ax = plt.subplots(figsize=(7, 6))
  
  ax.set_title('biểu đồ chỉ số FFMC ,DMC và DC giữa các tháng')
  rect1 = plt.bar(np.arange(12), ffmc, width=0.5, color='orangered')
  rect2 = plt.bar(np.arange(12), dmc, bottom=ffmc, width=0.5, color='#1f77b4')
  rect2 = plt.bar(np.arange(12), dc, bottom=dmc, width=0.5, color='green')

  chart_html = mpld3.fig_to_html(fig)
  return render_template("bar1.html", chart=chart_html)


def change(arr):
    a = arr[6:]
    a.reverse()
    b = arr[:6]
    c = []
    for i,j in zip(a,b):
        c.append(i)
        c.append(j)
    return c

@app.route("/pie")
def pie():
    fig, ax = plt.subplots()
    divisions, data = tansotansuat.createTable()
    index = index=['Aug','Sep','Mar','Jul','Feb','Jun','Oct','Apr','Dec','May','Jan','Nov']
    width = 0.3
    ax.set_title("Tần suất số lần cháy rừng ")
    ax.pie(data["Tần suất"],labels=index,autopct='%1.2f%%')
    ax.legend(loc="best")
    listData = []
    columns = data.columns

    for item in columns:
        listData.append(list(data[item]))
    plt.savefig("static/areapie1.png")
    
    return render_template("pie.html",labels=data.columns, index=divisions, data=listData)
@app.route("/piearea")
def piearea():
    fig, ax = plt.subplots()
    divisions, data = tansotansuat.createTablearea()
    index = ['0 - 100',
'100 - 200',
'200 - 300',
'300 - 400',
'400 - 500',
'500 - 600',
'600 - 700',
'700 - 800',
'800 - 900',
'900 - 1000',
'>=1000'
]
    width = 0.3
    ax.set_title("Tần suất diện tích cháy rừng ")
    ax.pie(data["Tần suất"],labels=index,autopct='%1.2f%%')
    ax.legend(loc="best")
    listData = []
    columns = data.columns

    for item in columns:
        listData.append(list(data[item]))
    plt.savefig("static/pieareaF.PNG")
    
    return render_template("piearea.html",labels=data.columns, index=divisions, data=listData)
@app.route("/pierain")
def pierain():
    fig, ax = plt.subplots()
    divisions, data = tansotansuat.createTablerain()
    index = ['0 -0.64',
'0.64 - 1.28',
'1.28 - 1.92',
'1.92 - 2.56',
'2.56 - 3.2',
'3.2 - 3.84',
'3.84 - 4.48',
'4.48 - 5.12',
'5.12 - 5.76',
'5.76 - 6.4'
]
    width = 0.3
    ax.set_title("Tần suất lượng mưa trong năm ")
    ax.pie(data["Tần suất"],labels=index,autopct='%1.2f%%')
    ax.legend(loc="best")
    listData = []
    columns = data.columns

    for item in columns:
        listData.append(list(data[item]))

    plt.savefig("static/piearainf.PNG")
    
    return render_template("pierain.html",labels=data.columns, index=divisions, data=listData)
@app.route("/piewind")
def piewind():
    fig, ax = plt.subplots()
    divisions, data = tansotansuat.createTablewind()
    index = ['0 -0.94',
'0.94 - 1.88',
'1.88 - 2.82',
'2.82 - 3.76',
'3.76 - 4.7',
'4.7 - 5.64',
'5.64 - 6.58',
'6.58 - 7.52',
'7.52 - 8.46',
'8.46 - 9.4'
]
    width = 0.3
    ax.set_title("Tần suất tốc độ gió trong năm ")
    ax.pie(data["Tần suất"],labels=index,autopct='%1.2f%%')
    ax.legend(loc="best")
    listData = []
    columns = data.columns

    for item in columns:
        listData.append(list(data[item]))

    plt.savefig("static/piewind.PNG")
    
    return render_template("piewind.html",labels=data.columns, index=divisions, data=listData)

@app.route('/barchart')
def barchart():
    fig, ax = plt.subplots()
    divisions, data = tansotansuat.createTable()
    index = np.arange(1,13)
    width = 0.3
    ax.set_title("Tần số số lần cháy rừng ")
    ax.bar(index, data["Tần số"], width, color="blue", label="số lần cháy rừng")
    ax.legend(loc="best")
    listData = []
    columns = data.columns

    for item in columns:
        listData.append(list(data[item]))

    plt.savefig("static/areabar1.png")
    
    return render_template("barchart.html",labels=data.columns, index=divisions, data=listData)

@app.route('/barchartarea')
def barchartarea():
    fig, ax = plt.subplots()
    divisions, data = tansotansuat.createTablearea()
    index = np.arange(1,12)
    width = 0.3
    ax.set_title("Tần số diện tích cháy rừng ")
    ax.bar(index, data["Tần số"], width, color="blue", label="diện tích cháy rừng")
    ax.legend(loc="best")
    listData = []
    columns = data.columns

    for item in columns:
        listData.append(list(data[item]))

    plt.savefig("static/areabar2.png")
    
    return render_template("barchartarea.html",labels=data.columns, index=divisions, data=listData)
@app.route('/barchartrain')
def barchartrain():
    fig, ax = plt.subplots()
    divisions, data = tansotansuat.createTablerain()
    index = np.arange(1,11)
    width = 0.3
    ax.set_title("Tần số lượng mưa")
    ax.bar(index, data["Tần số"], width, color="red", label="lượng mưa")
    ax.legend(loc="best")
    listData = []
    columns = data.columns

    for item in columns:
        listData.append(list(data[item]))

    plt.savefig("static/rainbarf.png")
    
    return render_template("barchartrain.html",labels=data.columns, index=divisions, data=listData)

@app.route('/barchartwind')
def barchartwind():
    fig, ax = plt.subplots()
    divisions, data = tansotansuat.createTablewind()
    index = index = ['0 -0.94',
'0.94 - 1.88',
'1.88 - 2.82',
'2.82 - 3.76',
'3.76 - 4.7',
'4.7 - 5.64',
'5.64 - 6.58',
'6.58 - 7.52',
'7.52 - 8.46',
'8.46 - 9.4'
]
    width = 0.3
    ax.set_title("Tần số tốc độ gió")
    ax.bar(index, data["Tần số"], width, color="red", label="tốc độ gió")
    ax.legend(loc="best")
    listData = []
    columns = data.columns

    for item in columns:
        listData.append(list(data[item]))

    plt.savefig("static/windbarF.png")
    
    return render_template("barchartwind.html",labels=data.columns, index=divisions, data=listData)
@app.route('/analyst')
def analyst():
    
    
    return render_template("analyst.html")
@app.route('/area/')
def areac():
   fig, ax = plt.subplots(figsize=(7, 6))

   ax.set_title('biểu đồ area tương quang giữa tổng diện tích cháy rừng,tốc độ gió,nhiệt độ ')
   ax.set_xlabel('tháng')
   plt.fill_between(np.arange(len(area1)), area1, color="lightpink",alpha=0.5, label='tổng diện Tích cháy rừng')
   plt.fill_between(np.arange(len(temp1)), temp1, color="green",alpha=0.5, label='tổng nhiệt độ')
   plt.fill_between(np.arange(len(wind1)), wind1, color="black",alpha=0.5, label='tổng tốc độ gió')
   plt.legend()
   
   chart_html = mpld3.fig_to_html(fig)

   return render_template("area.html", chart=chart_html)

@app.route('/box1/')
def box1():
   fig, ax = plt.subplots(figsize=(7, 6))
   
   divisions, data = tansotansuat.createTable()
   data['Tần số'].describe()
   ax.boxplot(data["Tần số"], boxprops=dict(),vert=False)
   ax.set_title('Box plot số vụ cháy rừng trong năm 2007')
 
#plt.ylim(min_price*1.2, max_price*1.2)
#plt.xticks(ticks=range(1, len(group_list)+1), labels=name_list)

   chart_html = mpld3.fig_to_html(fig)

   return render_template("box1.html", chart=chart_html)

@app.route('/box2/')
def box2():
   divisions, data = tansotansuat.createTablewind()
   fig, ax = plt.subplots(figsize=(7, 6))
   ax.boxplot(data["Tần số"], boxprops=dict(),vert=False)
   ax.set_title('Box plot tốc độ gió')
  
   chart_html = mpld3.fig_to_html(fig)

   return render_template("box2.html", chart=chart_html)
@app.route('/box3/')
def box3():
   fig, ax = plt.subplots(figsize=(7, 6))
   
   divisions, data = tansotansuat.createTablerain()
   data['Tần số'].describe()
   ax.boxplot(rain, boxprops=dict(),vert=False)
   #ax.boxplot(data["Tần số"],month)
   ax.set_title('Box plot Lượng mưa trong năm')
  
   chart_html = mpld3.fig_to_html(fig)

   return render_template("box3.html", chart=chart_html)

@app.route('/hist1/')
def hist1():
   fig, ax = plt.subplots(figsize=(7, 6))
   ax.set_title('biểu đồ histogram diện tích cháy rừng')
   ax = fig.add_subplot(1,1,1)
   ax.hist(area, bins=5, density=True)

   ax.grid(alpha=0.2)


   chart_html = mpld3.fig_to_html(fig)

   return render_template("hist1.html", chart=chart_html)

@app.route('/hist2/')
def hist2():
   fig, ax = plt.subplots(figsize=(7, 6))
   wind = data["wind"]

   n1 = [i / 100 for i in wind if i <= 0.94]
   n2 = [i / 100 for i in wind if i > 0.94 and i <= 1.88]
   n3 = [i / 100 for i in wind if i > 1.88 and i <= 2.82]
   n4 = [i / 100 for i in wind if i > 2.82 and i <= 3.76]
   n5 = [i / 100 for i in wind if i > 3.76 and i <= 4.7]
   n6 = [i / 100 for i in wind if i > 4.7 and i <= 5.64]
   n7 = [i / 100 for i in wind if i > 5.64 and i <= 6.58]
   n8 = [i / 100 for i in wind if i > 6.58 and i <= 7.52]
   n9 = [i / 100 for i in wind if i > 7.52 and i <= 8.46]
   n10 = [i / 100 for i in wind if i > 8.46 and i <= 9.4]
   n11 = [i / 100 for i in wind if i > 9.4]

    #Tính tần số của toc do gio
   ts = round(pd.Series([len(n1), len(n2), len(n3), len(n4), len(n5), len(n6), len(n7), len(n8), len(n9), len(n10), len(n11)]), 2)

   #divisions, data = tansotansuat.createTablewind()
   #ax = fig.add_subplot(1,1,1)
   ax.hist(ts, bins=15)
   #ax.xlim(left=0, right=21)
   #ax.xticks(np.arange(12))
   ax.set_title('biểu đồ histogram tốc độ gió')
   ax.grid(alpha=0.2)


   chart_html = mpld3.fig_to_html(fig)

   return render_template("hist2.html", chart=chart_html)
@app.route('/hist3/')
def hist3():
   fig, ax = plt.subplots(figsize=(7, 6))
#    divisions, data = tansotansuat.createTablerain()
#    ax = fig.add_subplot(1,1,1)
   ax.set_title('biểu đồ histogram lượng mưa trong năm')
   ax.hist(rain, bins=5)
   #ax.xlim(left=0, right=21)
   #ax.xticks(np.arange(12))

   ax.grid(alpha=0.2)


   chart_html = mpld3.fig_to_html(fig)

   return render_template("hist3.html", chart=chart_html)



#SIMPLE CHART


@app.route("/linechartdemo")
def linechartdemo():
    data = 15 * np.random.random_sample(10)

    fig, ax = plt.subplots()
    ax.plot(data)
    ax.set_title("Line chart")
    ax.set_xlabel("x value")
    ax.set_ylabel("y value")

    chart_html = mpld3.fig_to_html(fig)

    return render_template("linechart.html", chart=chart_html)

@app.route("/barchartdemo")
def barchartdemo():
    fig, ax = plt.subplots()

    divisions = ["Div A", "Div B", "Div C", "Div D", "Div E"]
    division_average_marks = np.random.randint(5, 25, size=5)
    boys_average_marks = np.random.randint(5, 25, size=5)

    index = np.arange(len(divisions))
    width = 0.3

    ax.set_title("Bar chart")
    ax.bar(index, division_average_marks, width, color="green", label="Division Mark")
    ax.bar(index + width, boys_average_marks, width, color="blue", label="Boy Mark")
    ax.set_xticks(index + width/2, divisions)
    ax.legend(loc="best")

    chart_html = mpld3.fig_to_html(fig)

    return render_template("barchartdemo.html", chart=chart_html)

@app.route("/piechartdemo")
def piechartdemo():
    data = 15 * np.random.random_sample(5)
    names = ["Product A", "Product B", "Product C", "Product D", "Product E"]

    explode = np.zeros(len(data))

    for i in range(len(data)):
        if data[i] == max(data):
            explode[i] = 0.1

    fig, ax = plt.subplots()
    ax.pie(data,explode=explode, labels=names)
    ax.set_title("Pie chart")

    chart_html = mpld3.fig_to_html(fig)

    return render_template("piechart.html", chart=chart_html)

@app.route("/scatterchartdemo")
def scatterchartdemo():
    data = 15 * np.random.random_sample(15)
    labels = [i for i in range(len(data))]
    fig, ax = plt.subplots()
    ax.scatter(x=labels, y=data, color="green")
    ax.set_title("Scatter chart")

    chart_html = mpld3.fig_to_html(fig)

    return render_template("scatterchart.html", chart=chart_html)

@app.route("/histdemo")
def histdemo():
    data = 15 * np.random.random_sample(15)
    fig, ax = plt.subplots()
    ax.hist(data, bins=6, density=True)
    

    ax.grid(alpha=0.2)

    chart_html = mpld3.fig_to_html(fig)

    return render_template("histdemo.html", chart=chart_html)



if __name__ == '__main__':
    app.run(debug=True)