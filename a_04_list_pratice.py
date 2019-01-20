"""numbers=[]
for value in range(1,1000001):
    number=value
    numbers.append(number)
    #print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))"""
#numbers=list(range(1,20,2))#list直接将数转换成列表
#print(numbers)
"""numbers=range(1,11)
for value in numbers:
    number=value**3
    print(number)"""
#numbers=[value**3 for value in range(1,11)]#列表解析
#print(numbers)
players=['cheng','wan','zhang','zhou','zhu']
#print(player[-3:])#包括前一个数，不包括后一个数 
for player in players[0:3]:
    print(player.title())