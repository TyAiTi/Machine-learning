import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
data=pd.read_csv("day.csv",index_col=0)

# X = data.iloc[:,[9,10,11,12]] #danh cho file hour
X = data.iloc[:,[8,9,10,11]] #danh cho file day
print(X)
Y =data.cnt 
  
#-----huan luyen mo hinh-----
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=100)

lm = linear_model.LinearRegression()
lm.fit(X_train,y_train)

y_pred = lm.predict(X_test) #du bao
y_test

# ----sai so du doan----
err = mean_squared_error(y_test,y_pred)
rmse_err = np.sqrt(err)
print(round(rmse_err,3))
# ----cac gia tri theta-----
print(lm.coef_)
print(lm.intercept_)
theta0 = np.round(lm.intercept_,2)
print("theta0",theta0)
theta1 = np.round(lm.coef_[0],2)
print("theta1 : ",theta1)
theta2 = np.round(lm.coef_[1],2)
print("theta2 : ",theta2)
theta3 = np.round(lm.coef_[2],2) 
print("theta3 : ",theta3)
theta4 = np.round(lm.coef_[3],2)
print("theta4 : ",theta4)
# ===========================================================

# x= X_test
# x1=x.hum
# y= y_test
#---workingday,weathersit,temp,atemp,windspeed,hum------
# ## vi du lay cot hum 3 phan tu dau de lm vd tren lop->x= X.iloc[0:3,:],
x= X
x1=x.hum;
y=Y

x1=np.array(x1)
y1=np.array(y)

plt.scatter(x1,y1)
plt.xlabel("Gia tri thuoc tinh X")
plt.ylabel("Gia tri thuoc tinh Y")    
plt.show()

# --------CONG THUC SGD->cap nhật trọng số theta khi duyệt qua mỗi phần tử----------
def LR1(X,Y,eta,lanlap,theta0,theta1):
    m = len(x)
   
    for i in range(0,lanlap):
        print("- Lan lap ",i)
        for j in range(0,m):
            h = theta0 + theta1*X[j]
            h = np.round(h,2)
            theta0 = theta0 + eta*(Y[j]-h)*1
            theta0 = np.round(theta0,2)
            print("Phan tu ",j, " Y=",Y[j], " h=",h," gia tri theta0= ",theta0)
            theta1 =  theta1 + eta*(Y[j]-h)*X[j]
            theta1 = np.round(theta1,2)
            print("Phan tu ", j, " Y=",Y[j], " h=",h,"gia tri theta1 = ",theta1)
    return [theta0,theta1]

# ----CONG THUC GD->khi duyệt qua tất cả các phần tử mới cập nhật trọng số theta-----
def LR2(X,Y,eta,lanlap,theta0,theta1):
    m= len(X)
    total_0=0
    total_1=0
    for i in range(0,lanlap):
        print("- Lan lap ",i)
        for j in range(0,m):
            h = theta0 + theta1*X[j]

            h = np.round(h,2)
            total_0 += (Y[j]-h)*1
            total_1 += (Y[j]-h)*X[j]
        theta0 = theta0 + eta/m*(total_0)# chia m là trung bình
        theta1 = theta1 + eta/m*(total_1)
        theta0 = np.round(theta0,2)
        theta1 = np.round(theta1,2)
        print("Total_0",total_0,"\nTotal_1",total_1)
        print("Theta0= ",theta0,"\nTheta1= ",theta1) 
    return [theta0,theta1]
# ------------------
theta=LR1(x1,y1,0.2,1,0,1)
theta1=LR2(x1,y1,0.2,1,0,1)

X1 = np.array([0.0,2.0])
Y1 = theta[0]+theta[1]*X1

X2 = np.array([0.0,2.0])
Y2= theta1[0]+theta1[1]*X2

plt.plot(x1,y1,"ro",color="blue")
plt.axis([0.0,2.0,0,8000])

plt.plot(X1,Y1,color="red")
plt.plot(X2,Y2,color="black")
plt.xlabel("Gia tri thuoc tinh X")
plt.ylabel("Gia tri thuoc tinh Y")
plt.title('Bieu do voi thuoc tinh Hum')
plt.show()


# ========DU DOAN PHAN TU MOI TOI=====
print("Sai so du doan la: ",rmse_err)
print("- Du doan ket qua phan tu moi toi:")
XX= [0.8,0.6]
for i in range(0,2):
    YY1 = theta1[0] + theta1[1]*XX[i]
    YY = theta[0] + theta[1]*XX[i]
    print("Ket qua du doan SGD : X=",XX[i]," Y =",YY)
    print("Ket qua du doan  GD : X=",XX[i]," Y =",YY1)
# ========DANH  CHO HUM===
# x= X.iloc[0:10,:]
# x1=x.hum;
# y=Y.iloc[0:10]
# theta=LR1(x1,y1,0.2,3,0,1)
# theta1=LR2(x1,y1,0.2,3,0,1)
# X1 = np.array([0.0,2.0])
# Y1 = theta[0]+theta[1]*X1

# X2 = np.array([0.0,2.0])
# Y2= theta1[0]+theta1[1]*X2

# plt.plot(x1,y1,"ro",color="blue")
# plt.axis([0.0,2.0,500,2000])
# ========DANH CHO ATEMP======
# X1 = np.array([0.0,0.50])
# Y1 = theta[0]+theta[1]*X1

# X2 = np.array([0.0,0.50])
# Y2= theta1[0]+theta1[1]*X2

# plt.plot(x1,y1,"ro",color="blue")
# plt.axis([0.0,0.50,800,1700])
# plt.title('Bieu do voi thuoc tinh atemp')
# ======DANH CHO WINDSPEED=====
# plt.title('Bieu do voi thuoc tinh windspeed')