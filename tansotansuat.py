
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def createTablerain(): 

    df = pd.read_csv("forestfires1.csv")

    height = df["rain"]
    n1 = [i / 100 for i in height if i <= 0.64]
    n2 = [i / 100 for i in height if i > 0.64 and i <= 1.92]
    n3 = [i / 100 for i in height if i > 1.92 and i <= 2.56]
    n4 = [i / 100 for i in height if i > 2.56 and i <= 3.2]
    n5 = [i / 100 for i in height if i > 3.2 and i <= 3.84]
    n6 = [i / 100 for i in height if i > 3.84 and i <= 4.48]
    n7 = [i / 100 for i in height if i > 4.48 and i <= 5.12]
    n8 = [i / 100 for i in height if i > 5.12 and i <= 5.76]
    n9 = [i / 100 for i in height if i > 5.76 and i <= 6.4]
    n10 = [i / 100 for i in height if i > 6.4]


    #Tính tần số của
    tanso = round(pd.Series([len(n1), len(n2), len(n3), len(n4), len(n5), len(n6), len(n7), len(n8), len(n9), len(n10)]), 2)

    #Tần số tích lũy của Pos
    tansotichluy = round(tanso.cumsum(), 2)

    #Tần suất của Pos
    tansuat = round(tanso / tanso.sum() * 100, 2)

    #Tần suất tích lũy của Pos
    tansuattichluy = round(tansuat.cumsum(), 2)

    result = pd.DataFrame([np.array(tanso), np.array(tansotichluy), np.array(tansuat), np.array(tansuattichluy)], columns=["nhóm 1", "nhóm 2", "nhóm 3", "nhóm 4", "nhóm 5", "nhóm 6", "nhóm 7", "nhóm 8", "nhóm 9", "nhóm 10"], index=["Tần số", "Tần số tích lũy ", "Tần suất", "Tần suất tích lũy"]).T

    indexs = result.index.tolist()

    return indexs, result


createTablerain()

def createTable(): 

    df = pd.read_csv("forestfires1.csv")

    tanso= df['month'].value_counts()
    tansotichluy = tanso.cumsum()
    tansuat= tanso/tanso.sum()*100
    

    tansuattichluy=(tansuat.cumsum())
  

    result = pd.DataFrame([np.array(tanso), np.array(tansotichluy), np.array(tansuat), np.array(tansuattichluy)], columns=["tháng 1", "tháng 2", "tháng 3", "tháng 4", "tháng 5", "tháng 6", "tháng 7", "tháng 8", "tháng 9", "tháng 10", "tháng 11", "tháng 12"], index=["Tần số", "Tần số tích lũy", "Tần suất", "Tần suất tích lũy"]).T

    indexs = result.index.tolist()

    return indexs, result

createTable()

def createTablearea():
    # Chia 4 khoảng < 1.7, < 1.8, < 1.9, > 1.9
    df = pd.read_csv("forestfires1.csv")
    area = df["area"]

    n1 = [i / 100 for i in area if i <= 100]
    n2 = [i / 100 for i in area if i > 100 and i <= 200]
    n3 = [i / 100 for i in area if i > 200 and i <= 300]
    n4 = [i / 100 for i in area if i > 300 and i <= 400]
    n5 = [i / 100 for i in area if i > 400 and i <= 500]
    n6 = [i / 100 for i in area if i > 500 and i <= 600]
    n7 = [i / 100 for i in area if i > 600 and i <= 700]
    n8 = [i / 100 for i in area if i > 700 and i <= 800]
    n9 = [i / 100 for i in area if i > 800 and i <= 900]
    n10 = [i / 100 for i in area if i > 1000 and i <= 1100]
    n11 = [i / 100 for i in area if i > 1100]

    #Tính tần số của
    ts = round(pd.Series([len(n1), len(n2), len(n3), len(n4), len(n5), len(n6), len(n7), len(n8), len(n9), len(n10), len(n11)]), 2)

    #Tần số tích lũy của Pos
    tstl = round(ts.cumsum(), 2)

    #Tần suất của Pos
    tsuat = round(ts / ts.sum() * 100, 2)

    #Tần suất tích lũy của Pos
    tsuatTL = round(tsuat.cumsum(), 2)

    result = pd.DataFrame([np.array(ts), np.array(tstl), np.array(tsuat), np.array(tsuatTL)], columns=["Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4", "Nhóm 4", "Nhóm 4", "Nhóm 4", "Nhóm 4", "Nhóm 4", "Nhóm 4", "Nhóm 4"], index=["Tần số", "Tần số tích lũy", "Tần suất", "Tần suất tích lũy"]).T

    indexs = result.index.tolist()

    return indexs, result

createTablearea()

def createTablewind():
    # Chia 4 khoảng < 1.7, < 1.8, < 1.9, > 1.9
    df = pd.read_csv("forestfires1.csv")
    wind = df["wind"]

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


    #Tính tần số của
    ts = round(pd.Series([len(n1), len(n2), len(n3), len(n4), len(n5), len(n6), len(n7), len(n8), len(n9), len(n10)]), 2)

    #Tần số tích lũy của Pos
    tstl = round(ts.cumsum(), 2)

    #Tần suất của Pos
    tsuat = round(ts / ts.sum() * 100, 2)

    #Tần suất tích lũy của Pos
    tsuatTL = round(tsuat.cumsum(), 2)

    result = pd.DataFrame([np.array(ts), np.array(tstl), np.array(tsuat), np.array(tsuatTL)], columns=["Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4", "Nhóm 4", "Nhóm 4", "Nhóm 4", "Nhóm 4", "Nhóm 4", "Nhóm 4"], index=["Tần số", "Tần số tích lũy", "Tần suất", "Tần suất tích lũy"]).T

    indexs = result.index.tolist()

    return indexs, result

createTablewind()
# df=pd.read_csv('forestfires1.csv', index_col=0) 
# df['f_area'] = ""
# df.to_csv("forestfire1.csv", index=False)

# df.loc[(df['area']<50),'f_area']=1
# df.loc[(df['area']>=50) & (df['area']<100),'f_area']=2 
# df.loc[(df['area']>=100) & (df['area']<150),'f_area']=3 
# df.loc[(df['area']>=150) & (df['area']<200),'f_area']=4 
# df.loc[(df['area']>=200) & (df['area']<400),'f_area']=5
# df.loc[(df['area']>=400) & (df['area']<600),'f_area']=6 
# df.loc[(df['area']>=600) & (df['area']>800),'f_area']=7 
# df.loc[(df['area']>=800) & (df['area']<1000),'f_area']=8
# df.loc[(df['area']>=1000),'f_area']=9 

# ## Area
# #Tần số diện tích cháy rừng
# # tanso= df['f_area'].value_counts()
# # print(tanso)
# # tansuat= tanso/tanso.sum()*100
# # print(tansuat)
# # tansuattichluy=(tansuat.cumsum())
# # print(tansuattichluy)
# # d={'tanso':tanso,'tanxuat':tansuat,'tansuattichluy':tansuattichluy}
# # df1=pd.DataFrame(data=d)
# # print(df1)
# # x_index=['Aug','Sep','Mar','Jul','Feb','Jun']
# # print('=================')
# # plt.bar(x_index,tanso)
# # plt.show()
# # plt.pie(tanso,labels=x_index,autopct='%1.2f%%')
# # plt.show()
# # plt.plot(x_index,tansuattichluy)

# # for i, val in enumerate(tansuattichluy):
# #   plt.text(df.index[i],
# #            val,
# #            '%1.1f%%' %val,) 
# # plt.show()


# ##
# tanso= df['month'].value_counts()
# print(tanso)
# tansuat= tanso/tanso.sum()*100
# print(tansuat)

# tansuattichluy=(tansuat.cumsum())
# print(tansuattichluy)
# d={'tanso':tanso,'tanxuat':tansuat,'tansuattichluy':tansuattichluy}
# df1=pd.DataFrame(data=d)
# df1

# x_index=['Aug','Sep','Mar','Jul','Feb','Jun','Oct','Apr','Dec','May','Jan','Nov']
# #fig, (ax1,ax2,ax3) =plt.subplots(1,3,figsize=(30,10))
# print('=================')
# plt.bar(x_index,tanso)
# plt.show()
# plt.pie(tanso,labels=x_index,autopct='%1.2f%%')
# plt.show()
# plt.plot(x_index,tansuattichluy)

# for i, val in enumerate(tansuattichluy):
#   plt.text(df.index[i],
#            val,
#            '%1.1f%%' %val,) 
# plt.show()
# #fig.show()

