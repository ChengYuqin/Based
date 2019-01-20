names=['wangshan','zhangyanxia','zhouyiyuan','chengyuqin','zhuyin']
"""#print(names)
print("I want to have a dinner with "+names[0]+", "+names[1]+" and "+names[2])
print("But "+names[1]+" can't attend the dinner!")
names[1]="zhuyin"
names.append('wanglicui')
print("Due to I find a big desk. I want to have a dinner with "+names[0]+", "+names[1]+", "+names[2]+"and "+names[3])
#print("So I want to have a dinner with "+names[0]+", "+names[1]+" and "+names[2])"""
#names.sort()#姓名按照首字母排序了，永久性排序
#names.sort(reverse=True)#反向排序
print("Here is the original list:")
print(names)
print("Here is the sorted list:")
print(sorted(names,reverse=True))#临时排序,也可反排序
print("Here is the reversed list:")
names.reverse()#反向姓名列表。未排序
print(names)
print(len(names))#输出列表长度
