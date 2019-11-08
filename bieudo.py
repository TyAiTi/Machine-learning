import pandas as pd
import numpy as np
dt_hour = pd.read_csv("hour.csv")
#print(dt_hour)
dt_hour.info()
#nhan=np.unique(dt_hour.cnt)
#X=dt_hour.iloc[:,[8,9,10,11,12,13,14]]
X = dt_hour.iloc[:,10:16]#16
Y = dt_hour.cnt

#bieu do hinh tron
import matplotlib.pyplot as plt
tongsoxe = sum(dt_hour.cnt)
xedk = sum(dt_hour.registered)
xenodk = sum(dt_hour.casual)
label = ["Xe đã dk", "Xe chưa dk"]
market = [xedk,xenodk]
colors = ['yellow','red']
Explode = [0.1,0]#khoang cach
plt.pie(market,explode=Explode, labels=label,shadow=True,startangle=45,autopct='%1.1f%%', colors=colors)
plt.axis('equal')
plt.legend(title="Biểu đồ xe")
plt.show()

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


print("mon1 = ",mon1," tong= ",nodk1,"+ ",nodk1," = ", nodk1+dk1)
print("mon1 = ",mon2," tong= ",dk2,"+ ",nodk2," = ", nodk2+dk2)
print("mon1 = ",mon3," tong= ",dk3,"+ ",nodk3," = ", nodk3+dk3)
print("mon1 = ",mon4," tong= ",dk4,"+ ",nodk4," = ", nodk4+dk4)
print("mon1 = ",mon5," tong= ",dk5,"+ ",nodk5," = ", nodk5+dk5)
print("mon1 = ",mon6," tong= ",dk6,"+ ",nodk6," = ", nodk6+dk6)
print("mon1 = ",mon7," tong= ",dk7,"+ ",nodk7," = ", nodk7+dk7)
print("mon1 = ",mon8," tong= ",dk8,"+ ",nodk8," = ", nodk8+dk8)
print("mon1 = ",mon9," tong= ",dk9,"+ ",nodk9," = ", nodk9+dk9)
print("mon1 = ",mon10," tong= ",dk10,"+ ",nodk10," = ", nodk10+dk10)
print("mon1 = ",mon11," tong= ",dk11,"+ ",nodk11," = ", nodk11+dk11)
print("mon1 = ",mon12," tong= ",dk12,"+ ",nodk12," = ", nodk12+dk12)
#https://viblo.asia/p/gioi-thieu-ve-matplotlib-mot-thu-vien-rat-huu-ich-cua-python-dung-de-ve-do-thi-yMnKMN6gZ7P

#bieu do trong tung thang
thang = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
soxe = [mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12]
dk = [dk1,dk2,dk3,dk4,dk5,dk6,dk7,dk8,dk9,dk10,dk11,dk12]
nodk = [nodk1,nodk2,nodk3,nodk4,nodk5,nodk6,nodk7,nodk8,nodk9,nodk10,nodk11,nodk12]

index = np.arange(12)
width = 0.30
plt.bar(index,      soxe, width, color='green', label = "Tổng xe")
plt.bar(index+width,dk, width, color='yellow', label = "Xe đã dk")
plt.bar(index+width+0.3,nodk, width, color='red', label = "Xe chưa dk")
plt.title("Số xe đạp được thuê trong từng tháng") #noi dung bieu do
plt.xlabel("Tháng")#hang ngang qua
plt.ylabel("So xe dap") #tong so xe dep trong thang
plt.xticks(index+ width/3, thang)
plt.legend(loc='best')
plt.show()


#bieu do ngay trong tuan
t2nodk = sum(dt_hour[dt_hour['weekday']==1][['weekday','casual']].casual)
t3nodk = sum(dt_hour[dt_hour['weekday']==2][['weekday','casual']].casual)
t4nodk = sum(dt_hour[dt_hour['weekday']==3][['weekday','casual']].casual)
t5nodk = sum(dt_hour[dt_hour['weekday']==4][['weekday','casual']].casual)
t6nodk = sum(dt_hour[dt_hour['weekday']==5][['weekday','casual']].casual)
t7nodk = sum(dt_hour[dt_hour['weekday']==6][['weekday','casual']].casual)
t8nodk = sum(dt_hour[dt_hour['weekday']==0][['weekday','casual']].casual)

t2dk = sum(dt_hour[dt_hour['weekday']==1][['weekday','registered']].registered)
t3dk = sum(dt_hour[dt_hour['weekday']==2][['weekday','registered']].registered)
t4dk = sum(dt_hour[dt_hour['weekday']==3][['weekday','registered']].registered)
t5dk = sum(dt_hour[dt_hour['weekday']==4][['weekday','registered']].registered)
t6dk = sum(dt_hour[dt_hour['weekday']==5][['weekday','registered']].registered)
t7dk = sum(dt_hour[dt_hour['weekday']==6][['weekday','registered']].registered)
t8dk = sum(dt_hour[dt_hour['weekday']==0][['weekday','registered']].registered)

print(t2nodk)
print(t2dk)
t2 =sum(dt_hour[dt_hour['weekday']==1][['weekday','cnt']].cnt)
print(t2)

t3 =sum(dt_hour[dt_hour['weekday']==2][['weekday','cnt']].cnt)
t4 =sum(dt_hour[dt_hour['weekday']==3][['weekday','cnt']].cnt)
t5 =sum(dt_hour[dt_hour['weekday']==4][['weekday','cnt']].cnt)
t6 =sum(dt_hour[dt_hour['weekday']==5][['weekday','cnt']].cnt)
t7 =sum(dt_hour[dt_hour['weekday']==6][['weekday','cnt']].cnt)
t8 =sum(dt_hour[dt_hour['weekday']==0][['weekday','cnt']].cnt)
thu=np.unique(dt_hour.weekday)#[0 1 2 3 4 5 6] cn hai ba tu ...

print("Thu 2 = ",t2," la tong cua ",t2nodk," + ",t2dk," la: ", t2nodk+t2dk)


thu = ["2", "3", "4", "5", "6", "7", "CN"]
soxet = [t2,t3,t4,t5,t6,t7,t8]
tnodk = [t2nodk,t3nodk,t4nodk,t5nodk,t6nodk,t7nodk,t8nodk]
tdk = [t2dk,t3dk,t4dk,t5dk,t6dk,t7dk,t8dk]
index = np.arange(7)
width = 0.30
plt.bar(index,      soxet, width, color='green', label = "Tổng xe")
plt.bar(index+width,tdk, width, color='yellow', label = "Xe đã dk")
plt.bar(index+width+0.3,tnodk, width, color='red', label = "Xe chưa dk")
plt.xticks(index+ width/3, thu)
plt.title("Số xe đạp thuộc ngày trong tuần") #noi dung bieu do
plt.xlabel("Thứ")#hang ngang qua
plt.ylabel("Số xe đạp") #tong so xe dep trong thang
plt.legend(loc='best')
plt.show()

#bieu do theo mua xuan ha thu dong
xuan =sum(dt_hour[dt_hour['season']==1][['season','cnt']].cnt)
ha =sum(dt_hour[dt_hour['season']==2][['season','cnt']].cnt)
thu =sum(dt_hour[dt_hour['season']==3][['season','cnt']].cnt)
dong =sum(dt_hour[dt_hour['season']==4][['season','cnt']].cnt)
#print(np.unique(dt_hour.season))

mnodk1 =  sum(dt_hour[dt_hour['season']==1][['season','casual']].casual)
mnodk2 =  sum(dt_hour[dt_hour['season']==2][['season','casual']].casual)
mnodk3 =  sum(dt_hour[dt_hour['season']==3][['season','casual']].casual)
mnodk4 =  sum(dt_hour[dt_hour['season']==4][['season','casual']].casual)

mdk1 = sum(dt_hour[dt_hour['season']==1][['season','registered']].registered)
mdk2 = sum(dt_hour[dt_hour['season']==2][['season','registered']].registered)
mdk3 = sum(dt_hour[dt_hour['season']==3][['season','registered']].registered)
mdk4 = sum(dt_hour[dt_hour['season']==4][['season','registered']].registered)
print(xuan," ", mnodk1," ",mdk1)
print(ha," ", mnodk2," ",mdk2)
print(thu," ", mnodk3," ",mdk3)
print(dong," ", mnodk4," ",mdk4)

mua = ["Xuân", "Hạ", "Thu", "Đông"]
soxem = [xuan,ha,thu,dong]
mnodk = [mnodk1,mnodk2,mnodk3,mnodk4]
mdk = [mdk1,mdk2,mdk3,mdk4]
index = np.arange(4)
width = 0.30
plt.bar(index,      soxem, width, color='green', label = "Tổng xe")
plt.bar(index+width,mdk, width, color='yellow', label = "Xe đã dk")
plt.bar(index+width+0.3,mnodk, width, color='red', label = "Xe chưa dk")
plt.xticks(index+ width/3, mua)
plt.title("Tổng số xe đạp theo mùa") #noi dung bieu do
plt.xlabel("Mùa")#hang ngang qua
plt.ylabel("Số xe đạp") #tong so xe dep trong thang
plt.legend(loc='best')
plt.show()
