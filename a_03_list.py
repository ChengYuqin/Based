names=['chengyuqin', 'wangshan','zhangyanxia','zhouyiyuan','zhuyin','wanglicui']
print(names)
"""print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])"""
#names[0]="cyq"
#print("Hello "+names[0]+"!")
"""names.append('pcy')
names.insert(1,'D.O.')
del names[3]"""
#poped_names=names.pop()#弹出列表末尾元素
#poped_names=names.pop(2)#加索引弹出任意元素
#names.remove('wanglicui')#根据元素的值删除元素
unlike='wanglicui'
names.remove(unlike)
print(names)
print("\nI don't like "+unlike.title()+"!")
#print(poped_names)