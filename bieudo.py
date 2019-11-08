import pandas as pd
import numpy as np
dt_hour = pd.read_csv("hour.csv")
#print(dt_hour)
dt_hour.info()
#nhan=np.unique(dt_hour.cnt)
#X=dt_hour.iloc[:,[8,9,10,11,12,13,14]]
X = dt_hour.iloc[:,10:16]#16
Y = dt_hour.cnt
#in cnt month =1 https://kipalog.com/posts/Huong-dan-su-dung-thu-vien-pandas-trong-python
nodk1 = sum(dt_hour[dt_hour['mnth']==1][['mnth','casual']].casual)#người thuê xe tháng 1 chưa đăng kí
nodk2 = sum(dt_hour[dt_hour['mnth']==2][['mnth','casual']].casual)#người thuê xe tháng 2 chưa đăng kí
nodk3 = sum(dt_hour[dt_hour['mnth']==3][['mnth','casual']].casual)#người thuê xe tháng 3 chưa đăng kí
nodk4 = sum(dt_hour[dt_hour['mnth']==4][['mnth','casual']].casual)#người thuê xe tháng 4 chưa đăng kí
nodk5 = sum(dt_hour[dt_hour['mnth']==5][['mnth','casual']].casual)#người thuê xe tháng 5 chưa đăng kí
nodk6 = sum(dt_hour[dt_hour['mnth']==6][['mnth','casual']].casual)#người thuê xe tháng 6 chưa đăng kí
nodk7 = sum(dt_hour[dt_hour['mnth']==7][['mnth','casual']].casual)#người thuê xe tháng 7 chưa đăng kí
nodk8 = sum(dt_hour[dt_hour['mnth']==8][['mnth','casual']].casual)#người thuê xe tháng 8 chưa đăng kí
nodk9 = sum(dt_hour[dt_hour['mnth']==9][['mnth','casual']].casual)#người thuê xe tháng 9 chưa đăng kí
nodk10 = sum(dt_hour[dt_hour['mnth']==10][['mnth','casual']].casual)#người thuê xe tháng 10 chưa đăng kí
nodk11 = sum(dt_hour[dt_hour['mnth']==11][['mnth','casual']].casual)#người thuê xe tháng 11 chưa đăng kí
nodk12 = sum(dt_hour[dt_hour['mnth']==12][['mnth','casual']].casual)#người thuê xe tháng 12 chưa đăng kí

dk1 = sum(dt_hour[dt_hour['mnth']==1][['mnth','registered']].registered)#người thuê xe tháng 1 đã đăng kí
dk2 = sum(dt_hour[dt_hour['mnth']==2][['mnth','registered']].registered)#người thuê xe tháng 2 đã đăng kí
dk3 = sum(dt_hour[dt_hour['mnth']==3][['mnth','registered']].registered)#người thuê xe tháng 3 đã đăng kí
dk4 = sum(dt_hour[dt_hour['mnth']==4][['mnth','registered']].registered)#người thuê xe tháng 4 đã đăng kí
dk5 = sum(dt_hour[dt_hour['mnth']==5][['mnth','registered']].registered)#người thuê xe tháng 5 đã đăng kí
dk6 = sum(dt_hour[dt_hour['mnth']==6][['mnth','registered']].registered)#người thuê xe tháng 6 đã đăng kí
dk7 = sum(dt_hour[dt_hour['mnth']==7][['mnth','registered']].registered)#người thuê xe tháng 7 đã đăng kí
dk8 = sum(dt_hour[dt_hour['mnth']==8][['mnth','registered']].registered)#người thuê xe tháng 8 đã đăng kí
dk9 = sum(dt_hour[dt_hour['mnth']==9][['mnth','registered']].registered)#người thuê xe tháng 9 đã đăng kí
dk10 = sum(dt_hour[dt_hour['mnth']==10][['mnth','registered']].registered)#người thuê xe tháng 10 đã đăng kí
dk11 = sum(dt_hour[dt_hour['mnth']==11][['mnth','registered']].registered)#người thuê xe tháng 11 đã đăng kí
dk12 = sum(dt_hour[dt_hour['mnth']==12][['mnth','registered']].registered)#người thuê xe tháng 12 đã đăng kí


mon1 =sum(dt_hour[dt_hour['mnth']==1][['mnth','cnt']].cnt) #liet ke thang 1 va cnt
mon2 =sum(dt_hour[dt_hour['mnth']==2][['mnth','cnt']].cnt) #liet ke thang 2 va cnt
mon3 =sum(dt_hour[dt_hour['mnth']==3][['mnth','cnt']].cnt) #liet ke thang 3 va cnt
mon4 =sum(dt_hour[dt_hour['mnth']==4][['mnth','cnt']].cnt) #liet ke thang 4 va cnt
mon5 =sum(dt_hour[dt_hour['mnth']==5][['mnth','cnt']].cnt) #liet ke thang 5 va cnt
mon6 =sum(dt_hour[dt_hour['mnth']==6][['mnth','cnt']].cnt) #liet ke thang 6 va cnt
mon7 =sum(dt_hour[dt_hour['mnth']==7][['mnth','cnt']].cnt) #liet ke thang 7 va cnt
mon8 =sum(dt_hour[dt_hour['mnth']==8][['mnth','cnt']].cnt) #liet ke thang 8 va cnt
mon9 =sum(dt_hour[dt_hour['mnth']==9][['mnth','cnt']].cnt) #liet ke thang 9 va cnt
mon10 =sum(dt_hour[dt_hour['mnth']==10][['mnth','cnt']].cnt) #liet ke thang 10 va cnt
mon11 =sum(dt_hour[dt_hour['mnth']==11][['mnth','cnt']].cnt) #liet ke thang 11 va cnt
mon12 =sum(dt_hour[dt_hour['mnth']==12][['mnth','cnt']].cnt) #liet ke thang 12 va cnt

#A = A[['mnth','cnt']]
#print(sum(A.cnt))
print(mon1)
print(mon2)
print(mon3)
print(mon4)
print(mon5)
print(mon6)
print(mon7)
print(mon8)
print(mon9)
print(mon10)
print(mon11)
print(mon12)
#https://viblo.asia/p/gioi-thieu-ve-matplotlib-mot-thu-vien-rat-huu-ich-cua-python-dung-de-ve-do-thi-yMnKMN6gZ7P
import matplotlib.pyplot as plt
#bieu do trong tung thang
thang = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
soxe = [mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12]
nodk = [nodk1,nodk2,nodk3,nodk4,nodk5,nodk6,nodk7,nodk8,nodk9,nodk10,nodk11,nodk12]
dk = [dk1,dk2,dk3,dk4,dk5,dk6,dk7,dk8,dk9,dk10,dk11,dk12]
index = np.arange(12)
width = 0.30
plt.bar(index,soxe, width, color='green', label = "Tổng xe")
plt.bar(index+width,nodk, width, color='red', label = "Xe chưa dk")
plt.bar(index+width+0.30,nodk, width, color='yellow', label = "Xe đã dk")
plt.title("Số xe đạp được thuê trong từng tháng") #noi dung bieu do
plt.xlabel("Tháng")#hang ngang qua
plt.ylabel("So xe dap") #tong so xe dep trong thang
plt.xticks(index+ width/3, thang)
plt.legend(loc='best')
plt.show()

#bieu do ngay trong tuan
t2 =sum(dt_hour[dt_hour['weekday']==1][['weekday','cnt']].cnt)
t3 =sum(dt_hour[dt_hour['weekday']==2][['weekday','cnt']].cnt)
t4 =sum(dt_hour[dt_hour['weekday']==3][['weekday','cnt']].cnt)
t5 =sum(dt_hour[dt_hour['weekday']==4][['weekday','cnt']].cnt)
t6 =sum(dt_hour[dt_hour['weekday']==5][['weekday','cnt']].cnt)
t7 =sum(dt_hour[dt_hour['weekday']==6][['weekday','cnt']].cnt)
t8 =sum(dt_hour[dt_hour['weekday']==0][['weekday','cnt']].cnt)
thu=np.unique(dt_hour.weekday)#[0 1 2 3 4 5 6] cn hai ba tu ...

thang = ["2", "3", "4", "5", "6", "7", "CN"]
soxe = [t2,t3,t4,t5,t6,t7,t8]
plt.bar(thang, soxe, color='green')
plt.title("Số xe đạp thuộc ngày trong tuần") #noi dung bieu do
plt.xlabel("Thứ")#hang ngang qua
plt.ylabel("Số xe đạp") #tong so xe dep trong thang
plt.show()

#bieu do theo mua xuan ha thu dong
