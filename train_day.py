import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dt_date = pd.read_csv("day.csv") #đọc file .csv
#print(dt_date.head(5))
dt_date = dt_date.drop(columns=['dteday','instant'])# bỏ cột ngày và thứ tự không cần thiết
#print(dt_date.head(5))


from sklearn import preprocessing #sử dụng sklearn
x=dt_date.drop(['cnt',],axis=1) # x là phải bỏ cột nhãn ra
print(x.head(5))
y=dt_date['cnt'] #là nhãn
x = preprocessing.normalize(x)# tiền xử lý để chuẩn hóa
print("------------ ---------------- --------------- \n")
#for i in range(0,13): #max chỉ có 13 cột thôi (bỏ dteday, instant, cnt)
#    print(x[0][i])

#print(type(x))


from sklearn.model_selection import train_test_split  #dùng hold-out phân tách dữ liệu làm thành bộ training mô hình
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)# 2 tập độc lập 1/3 là test


from sklearn.linear_model import LinearRegression #Hoi quy tuyen tinh Linear Regression
from sklearn.metrics import mean_squared_error #binh phuong sai so loi erro

from sklearn.metrics import r2_score #diem
linearRegressor = LinearRegression()
linearRegressor.fit(x_train, y_train) #bat dau train
y_predicted = linearRegressor.predict(x_test) #du doan
mse = mean_squared_error(y_test, y_predicted) # binh phuong sai so
r = r2_score(y_test, y_predicted) #so diem chua nhan voi 100
from math import sqrt
#from sklearn.metrics import accuracy_score
#print("Accuracy is", accuracy_score(y_test,y_pred)*100)
print("Giai thuat hoi quy tuyen tinh Linear Regression: ")
print("Binh phuong sai so MSE (Mean Squared Error): ",mse," RMSE",sqrt(mse))
print("Do chinh xac la: ",r)
print("---------------- ----------------- ----------------- \n \n")
plt.title("Hồi quy tuyến tính")
plt.scatter(y_test,y_predicted)
plt.xlabel("Test")
plt.ylabel("Predict")
plt.grid(True)
plt.show()

from sklearn.tree import DecisionTreeRegressor #Cay quyet dinh decision tree
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(x_train, y_train)
y_predicted_2 = regressor.predict(x_test)
mse2 = mean_squared_error(y_test, y_predicted_2)
r2 = r2_score(y_test, y_predicted_2)
print("Giai thuat cay quyet dinh Decision Tree: ")
print("Binh phuong sai so MSE (Mean Squared Error): ",mse2," RMSE",sqrt(mse2))
print("Do chinh xac la: ",r2)
plt.title("Cây quyết định ")
plt.scatter(y_test,y_predicted_2)
plt.xlabel("Test")
plt.ylabel("Predict")
plt.grid(True)
plt.show()

from prettytable import PrettyTable#tao bang
table = PrettyTable()
table.field_names = ["Giai Thuat", "MSE","RMSE" ,"Do chinh xac"]

models = [
    LinearRegression(),
    DecisionTreeRegressor(random_state = 100)
]

for model in models:
    model.fit(x_train, y_train)
    y_res = model.predict(x_test)
    mse_b = mean_squared_error(y_test, y_res)
    score_b = model.score(x_test, y_test)*100
    rmse_b = np.sqrt(mse)
    table.add_row([type(model).__name__, format(mse_b, '.2f'),format(rmse_b, '.2f'),format(score_b, '.2f')])
print(table)
