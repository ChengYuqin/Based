import math #先导入math包
import numpy as np#导入numpy包，这是一个科学计算库，后面的arange()函数是这个库里面的
mark=input("是否输入已知变量：（yes/no）")
while mark=="yes":
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
    for t in np.arange(0.1,1,0.1):
        #表示从0.1开始，每次加0.1，直到0.9，这个用整数也可以（1,10）从1到9，默认加1
        s=math.sin(math.radians(ω*t))#调用math包中的sin函数,radians把度数化成弧度
        c=math.cos(math.radians(ω*t))#调用math包中的cos函数
        D=(ε0*b*b*d*E0*s)/2
        H=(ε0*b*b*d*E0*c*ω)/2
        print("电位移通量："+str(D)+"(A)"+"    "+"感生磁动势："+str(H)+"(V)")
        #因为D为数值型，用str函数转换成字符型输出
    mark = input("是否继续输入已知变量：（yes/no）")
    if mark=="yes":
        continue
    else:
        break