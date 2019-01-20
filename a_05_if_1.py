"""car='subaru'
print("Is car == 'subaru'? I predict True.")
print(car=='subaru')#输出结果为True
print("\nIs car == 'audi'? I predict False.")
print(car== 'audi')#输出结果为False

age=12
if age<4:
    price=0
    #print("Your admission cost $0")
elif age<18:
    price=5
    #print("Your admission cost $5")
else:
    price=10
    #print("Your admission cost $10")
print("Your admission cost $"+str(price))#转换price的类型

alien_color=['green','yellow','red']
color= 'red'
if color=='green':
    print("Player win 5 score")
elif color=="yellow":
    print("Player win 10 score")
else:
    print("Player win 15 score")

age=20
if age<2:
    print("He is a baby")
elif age<13:
    print("He is a child")
elif age <20:
    print("He is a young")
elif age<65:
    print("He is a adult")
else:
    print("He is a old people")"""
favorite_fruits=['apples','bananas','peach']
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'peach' in favorite_fruits:
    print("You really like peach!")
if 'pear' not in favorite_fruits:
    print("You don't like peach!")
if 'orange' not in favorite_fruits:
    print("You don't like peach!")



