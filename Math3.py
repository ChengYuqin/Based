import matplotlib.pyplot as plt
import math
import numpy as np

plt.title("D/H",fontsize=24)
plt.xlabel("time")
plt.ylabel("D/H")

t=[]#把时间设为一个列表，开始为空
D=[]#把电位移通量设为一个列表，开始为空
H=[]#把感生磁动势设为一个列表，开始为空
plt.plot(t,D,color="blue",linestyle="-",label="D",alpha=0.5)#这只左上角的线的说明。红色对应H，蓝色对应D
plt.plot(t,H,color="red",linestyle="-",label="H",alpha=0.5)

ax=plt.gca()#gca()函数表示获得当前图表
ax.spines["right"].set_color("none")#把图表右边设成无色
ax.spines["top"].set_color("none")#把图表上边设成无色
ax.spines["left"].set_position(("data",0))#左边从0位置开始
ax.spines["bottom"].set_position(("data",0))#下边从0位置开始
ax.xaxis.set_ticks_position("bottom")#把x轴设在下方
ax.yaxis.set_ticks_position("left")#把y轴设在左方
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor="white",edgecolor="None",alpha=0.2))#设置表面颜色白，边框颜色无，透明度0.2
#图例显示
plt.legend(loc="upper left")
#显示网格
plt.grid()

ε0=input("输入介质常量ε0：")#输入的值为字符型
ε0=int(ε0)#强制类型转换，转换为整型，下面同理
b=input("输入矩形平面的宽度：")
b=int(b)
d=input("输入矩形平面的长度：")
d=int(d)
E0=input("输入时变电场E0：")
E0=int(E0)
ω=input("输入角速度ω：")
ω=int(ω)
a=np.arange(1,20)
for i in a:
    t.append(i)
    D.append((ε0*b*b*d*E0* math.sin(math.radians(ω * i)))/2)
    H.append((ε0*b*b*d*E0* math.cos(math.radians(ω * i))*ω)/2)
print("电位移通量D：\n" + str(D) + "(A)" + "\n" + "感生磁动势H：\n" + str(H) + "(V)\n")

plt.plot(t,D)
plt.plot(t,H)
plt.show()

