import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
data=pd.read_csv("hour.csv",index_col=0)
#X=data.iloc[:,[5,8,9,10,11]]
X = data.iloc[:,5:13]
Y =data.cnt
#--------------


    
#huan luyen mo hinh
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=100)

lm = linear_model.LinearRegression()
lm.fit(X_train,y_train)

y_pred = lm.predict(X_test) #du bao
y_test

#
err = mean_squared_error(y_test,y_pred)
rmse_err = np.sqrt(err)
print(round(rmse_err,3))

print(lm.coef_)
print(lm.intercept_)
# theta0 = np.round(lm.intercept_,2)
# print("theta0",theta0)
# theta1 = np.round(lm.coef_[0],2)
# print("theta1 : ",theta1)
# theta2 = np.round(lm.coef_[1],2)
# print("theta2 : ",theta2)
# theta3 = np.round(lm.coef_[2],2)
# print("theta3 : ",theta3)
# theta4 = np.round(lm.coef_[3],2)
# print("theta4 : ",theta4)
# theta5 = np.round(lm.coef_[4],2)
# print("theta5 : ",theta5)
# -------------giai thuat sgd----------------
x= X_test.iloc[0:5,:]
x1=x.atemp;
y=y_test.iloc[0:5]
x1=np.array(x1)
y1=np.array(y)

plt.scatter(x1,y1)
plt.xlabel("Gia tri thuoc tinh X")
plt.ylabel("Gia tri thuoc tinh Y")    
plt.show()


def LR1(X,Y,eta,lanlap,theta0,theta1):
    m = len(x)
   
    for i in range(0,lanlap):
        print("- Lan lap ",i)
        for j in range(0,m):
            h = theta0 + theta1*X[j]
            theta0 = theta0 + eta*(Y[j]-h)*1
            print("Phan tu ",j, " Y=",Y[j], " h=",h," gia tri theta0= ",theta0)
            theta1 =  theta1 + eta*(Y[j]-h)*X[j]
            print("Phan tu ", j, " Y=",Y[j], " h=",h,"gia tri theta1 = ",theta1)
    return [theta0,theta1]

theta=LR1(x1,y1,0.5,4,200,500)
theta1=LR1(x1,y1,0.2,3,0.2,0.1)
# print(theta[0])
# print(theta[1])
X1 = np.array([0,1])
Y1 = theta[0]+theta[1]*X1
# X2 = np.array([0.4,600])
# Y2= theta1[0]+theta1[1]*X2
print("Y1 la :",Y1)
plt.axis([0,1,0,600])
# plt.scatter(x1,y1)
plt.plot(x1,y1,"ro",color="blue")
plt.plot(X1,Y1,color="violet")
# plt.plot(X2,Y2,color="green")
plt.xlabel("Gia tri thuoc tinh X")
plt.ylabel("Gia tri thuoc tinh Y")
plt.show()