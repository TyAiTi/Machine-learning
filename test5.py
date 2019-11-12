import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
data=pd.read_csv("day.csv",index_col=0)
X=data.iloc[:,[5,8,9,10,11]]
Y =data.cnt
#--------------
data1=data.iloc[0:3,:]
x=np.array([data1.weekday,data1.temp,data1.atemp,data1.hum,data1.windspeed])
#x=np.array(data1.temp)

y=np.array(data1.cnt)
x=np.round(x,2)
y=np.round(y,2)
labels=['weekday', 'temp', 'atemp','hum','windspeed']
colors=['r','g','b','g','y']
for i in range(len(x)):
    plt.scatter(x[i],y)
    plt.plot(x[i],y,"ro",color=colors[i],label=labels[i])


plt.xlabel("Gia tri thuoc tinh X")
plt.ylabel("Gia tri thuoc tinh Y")    
plt.show()

    
#huan luyen mo hinh
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=100)

lm = linear_model.LinearRegression()
lm.fit(X_train,y_train)

y_pred = lm.predict(X_test) #du bao
y_test
#----in hinh dung dc su sai khac giua gt thuc te va du bao=------
plt.scatter(y_test,y_pred)
plt.xlabel("Gia tri thuoc tinh X")
plt.ylabel("Gia tri thuoc tinh Y")    
plt.show()
#
err = mean_squared_error(y_test,y_pred)
rmse_err = np.sqrt(err)
print(round(rmse_err,3))

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
theta5 = np.round(lm.coef_[4],2)
print("theta5 : ",theta5)

def LR1(x,y,eta,lanlap,theta0,theta1,theta2,theta3,theta4,theta5):
    m = len(x[0])
    n=len(x)
   #(--  h=theta0 + theta1X1 +theta2X2 +.. +theta5X5 --)
    for i in range(0,lanlap):
        print("- Lan lap ",i)
        for j in range(0,m):
            
            h = theta0 + theta1*x[0][j]+theta2*x[1][j]+theta3*x[2][j]+theta4*x[3][j]+theta5*x[4][j]
            h=np.round(h,2)
            print("theta0: ",theta0)
            theta0 = theta0 + eta*(y[j]-h)*1
            print("Phan tu ",j, " Y=",y[j], " h=",h," gia tri theta0= ",theta0)
            theta1 =  theta1 + eta*(y[j]-h)*x[0][j]
            print("Phan tu ", j, " Y=",y[j], " h=",h,"gia tri theta1 = ",theta1)
            theta2= theta2+eta*(y[j]-h)*x[1][j]
            print("Phan tu ", j, " Y=",y[j], " h=",h,"gia tri theta2 = ",theta2)
            theta3= theta3+eta*(y[j]-h)*x[2][j]
            print("Phan tu ", j, " Y=",y[j], " h=",h,"gia tri theta3 = ",theta3)
            theta4= theta4+eta*(y[j]-h)*x[3][j]
            print("Phan tu ", j, " Y=",y[j], " h=",h,"gia tri theta4 = ",theta4)
            theta5= theta5+eta*(y[j]-h)*x[4][j]
            print("Phan tu ", j, " Y=",y[j], " h=",h,"gia tri theta5 = ",theta5)
            print("--------------------------------------")
    return [theta0,theta1,theta2,theta3,theta4,theta5]

LR1(x,y,0.2,1,theta0,theta1,theta2,theta3,theta4,theta5)



#array([[6.      , 0.      , 1.      ],
#       [0.344167, 0.363478, 0.196364],
#       [0.363625, 0.353739, 0.189405],
#       [0.805833, 0.696087, 0.437273],
#       [0.160446, 0.248539, 0.248309]])

#array([ 985,  801, 1349], dtype=int64)
#----------GIAI THUAT GD-----------
def LR2(x,y,eta,lanlap,theta0,theta1,theta2,theta3,theta4,theta5):
    m=len(x[0])
    #(--  h=theta0 + theta1X1 +theta2X2 +.. +theta5X5 --)
    for i in range(0,lanlap):
        print ("Lan lap thu ",i)
        total_0 = 0
        total_1 = 0
        total_2 = 0
        total_3 = 0
        total_4 = 0
        total_5 = 0
        total_6 = 0
        for j in range(0,m):
            h = theta0 + theta1*x[0][j] + theta2*x[1][j] + theta3*x[2][j] + theta4*x[3][j] + theta5*x[4][j]
            total_0 += total_0 +(y[j]-h)*1
            total_1 += total_1 +(y[j]-h)*x[0][j]
            total_2 += total_2 +(y[j]-h)*x[1][j]
            total_3 += total_3 +(y[j]-h)*x[2][j]
            total_4 += total_4 +(y[j]-h)*x[3][j]
            total_5 += total_5 +(y[j]-h)*x[4][j]
        theta0 = theta0 + eta/m*(total_0)
        theta1 = theta1 + eta/m*(total_1)
        theta2 = theta2 + eta/m*(total_2)
        theta3 = theta3 + eta/m*(total_3)
        theta4 = theta4 + eta/m*(total_4)
        theta5 = theta5 + eta/m*(total_5)
        print("->Theta0",theta0)
        print("->Theta1",theta1)
        print("->Theta2",theta2)
        print("->Theta3",theta3)
        print("->Theta4",theta4)
        print("->Theta5",theta5)
    return [theta0,theta1,theta2,theta3,theta4,theta5]     

#   
print("Cac gia tri theta voi cong thuc SGD")
LR1(x,y,0.2,1,theta0,theta1,theta2,theta3,theta4,theta5)
print("Cac gia tri theta voi cong thuc GD")
LR2(x,y,0.2,1,theta0,theta1,theta2,theta3,theta4,theta5)

        
        
        
        
        
        
        