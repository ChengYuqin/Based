"""alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'blue','points':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

aliens=[]
for alien_number in range(30):
    new_alien={'speed':'slow','color':'green','points':5}
    aliens.append(new_alien)
for alien in aliens[:3]:#对前三个外星人信息进行修改
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens:"+str(len(aliens)))

pizza={
    'crust':'thick',
    'topping':['mushrooms','extra cheese'],
}

print("You ordered a"+pizza['crust']+"-crust pizza"+" with the following toppings:")
for topping in pizza['topping']:
    print("\t"+topping)

favorite_language={
    'jen':['python','java'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','c++'],
}

for name,language in favorite_language.items():
    print("\n"+name.title()+"'s favorite language are:")
    for language in favorite_language[name]:
        print("\t"+language.title())"""

users={
    'chengyuqin':{
        'first':'cheng',
        'last':'yuqin',
        'city':'hefei',
    },
    'wangshan':{
        'first':'wang',
        'last':'shan',
        'city':'wuhu',
    },
}
for name,information in users.items():
    print("username:"+name)
    print("Full name:"+information['first'].title()+" "+information['last'].title())
    print("City:"+information['city'].title()+"\n")

