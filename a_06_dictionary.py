"""alien_0={'color':'green','points':5}
print(alien_0)
del alien_0['points']
#alien_0['x_position']=0
#alien_0['y_position']=25
print(alien_0)"""
#print(alien_0['color'])
#print(alien_0['points'])
"""alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x_position:"+str(alien_0['x_position']))
alien_0['speed']='fast'
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x_position:"+str(alien_0['x_position']))


friend_information={
    'first_name':'wang',
    'last_name':'shan',
    'age':24,
    'city':'wuhu',
    'height':155,
    'weight':90,
}
for key,value in friend_information.items():
    print("\nkey:"+key)
    print("value:"+str(value))
#print(friend_information)"""

"""favorite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'java',
    'phil':'java',
}
friends=['jen','phil']
for name in set(favorite_language.values()):#key()可有可无
    print(name.title())
    if name in friends:
        print("Hi "+name.title()+",I see your favorite language is "
              +favorite_language[name].title()+"!")
if 'c++' not in  favorite_language.values():
        print("\nNobady like c++!")
river={
    'nile':'egypt',
    'yellowriver':'china',
    'changjiang':'china',
}
for keys,values in river.items():
    print("The "+keys.title()+" runs through "+values.title()+" .")
    print(keys.title())
    print(values.title())
"""

names=['jen','sarah','pite','phil','edward','chang']
favorite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'java',
    'phil':'c++',
}
for name in names:
    if name in favorite_language:
        print("Hi "+name.title()+".Thank you join us!")
    else:
        print("Hi "+name.title()+".Welcome to join us!")


