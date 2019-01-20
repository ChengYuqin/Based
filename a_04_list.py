"""pizzas=['tianpizze','xianpizze','lapizze']
for pizza in pizzas:
    print("I like "+pizza+" pizza!")
print("I really like pizza!")"""
"""for value in range(1,5):
    print(value)
numbers=list(range(2,11,3))
print(numbers)"""
squares=[]#输出1~10整数的平方
"""for value in range(1,11):
    #square=value**2
    #squares.append(square)
    squares.append(value**2)#简洁些
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))"""
squares=[value**2 for value in range(1,11)]#列表解析,没有冒号
print(squares)

