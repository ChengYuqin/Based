"""users=['zhang','cheng','wang','zhou','admin']
user='admin'
if user=='admin':
    print("Hello admin,would you like to see a status report?")
else:
    print("Hello "+user+" thank you for logging in again.") """

"""for user in users:
    if user=='admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello "+user+" thank you for logging in again.")

users=[]
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello " + user + " thank you for logging in again.")
else:
    print("We need to find some users!")

current_users=['zhou','wu','zhen','wang','zhao','qian','sun']
new_users=['Wu','cheng','Wang','zhu','Sun']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user+" is used,please input other name")
    else:
        print(new_user+" is not used")"""

#numbers=[number for number in range(1,10)]
for number in range(1,10):
    if number==1:
        print(str(number) + "st")
    elif number==2:
        print(str(number)  + "nd")
    elif number==3:
        print(str(number)  + "rd")
    else:
        print(str(number)  + "th")