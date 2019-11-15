#https://www.youtube.com/watch?v=ic3XgjY2VDY
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dt_date = pd.read_csv("day.csv") #đọc file .csv
print(dt_date.head(10))
#dt_date = dt_date.drop(columns=['dteday','instant','yr','holiday','workingday'])# bỏ cột ngày và thứ tự không cần thiết
#print(dt_date.head(5))
dt_date = dt_date.drop(columns=['instant','dteday','season','yr','mnth','holiday','weekday','workingday','weathersit','casual','registered'])

print("Thuoc tinh va nhan can thiet la: ")
print(dt_date.head(10))
#print(dt_date)
from sklearn import preprocessing #sử dụng sklearn
x=dt_date.drop(['cnt',],axis=1) # x là phải bỏ cột nhãn ra
#print(x.head(5))
y=dt_date['cnt'] #là nhãn
x= np.array(x)
y = np.array(y)
#x = preprocessing.normalize(x)# tiền xử lý để chuẩn hóa
print("------------ ---------------- --------------- \n")

from sklearn.model_selection import train_test_split  #dùng hold-out phân tách dữ liệu làm thành bộ training mô hình
# 2 tập độc lập 1/3 là test
from sklearn.linear_model import LinearRegression #Hoi quy tuyen tinh Linear Regression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from math import sqrt
cong = 0;
tongL = 0 #tong 10 lan lap hoi quy
tongD = 0 #tong 10 lan lap cay quyet dinh

rmse1 = 0
rmse2 = 0
print("Lan lap thu: " ,"LinearRegressor: ","DecisionTreeRegressor: ")
for i in range(1,11):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = cong)
    cong = cong +5
    #Hoi quy
    linearRegressor = LinearRegression()
    linearRegressor.fit(x_train, y_train)
    y_predicted = linearRegressor.predict(x_test)
    mseL = mean_squared_error(y_test, y_predicted)
    rmseL = sqrt(mseL) #rmse
    r = r2_score(y_test, y_predicted) #do chinh xac
    #print(" ",mse," ",sqrt(mse), " ",r*100)
    #cay quyet dinh
    regressor = DecisionTreeRegressor(max_depth=10,min_samples_leaf=5)
    regressor.fit(x_train, y_train)
    y_predicted_2 = regressor.predict(x_test)
    mseD = mean_squared_error(y_test, y_predicted_2)
    rmseD = sqrt(mseD)#rmse
    r2 = r2_score(y_test, y_predicted_2)

    rmse1 = rmse1 + rmseD
    rmse2 = rmse2 + rmseL
    tongL = tongL + r*100
    tongD = tongD + r2*100
    print("        ",i,"",r*100," ",r2*100)
    #print("Kiem tra RMSE_L ",rmseL," RMSE_D ",rmseD)
print("\n-------------------------------------------")
print("Trung binh 10 lan lap")
print("LinearRegressor       ",tongL/10, "RMSE: ",rmse1/10)
print("DecisionTreeRegressor ",tongD/10, "RMSE: ",rmse2/10)
