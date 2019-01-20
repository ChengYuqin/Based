"""message=input("Tell me something, and I will repeat it back to you:")
print(message)

prompt="If you tell us who you are,we can personalize the messages you see."
prompt+="\nWhat is your first name?"
name=input(prompt)
print("\nHello,"+name.title()+"!")

height=input("How tall are you,in inches?")
height=int(height)
if height>36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

number=input("Enter a number, and I'll tell you if it's even or odd:")
number=int(number)
if number%2==0:
    print("\nThe number "+str(number)+" is even!")
else:
    print("\nThe number "+str(number)+" is odd!")

#订餐
people=input("Hello,how many people are coming for dinner?")
people=int(people)
if people>8:
    print("Sorry,there is no empty table!")
else:
    print("Ok,there have empty table!")

number=input("Enter a number and decide if this number is a multiple of 10!")
number=int(number)
if number%10==0:
    print("The number is a multiple of 10.")
else:
    print("The number is not a multiple of 10.")

number=1
while number <=5:
    print(number)
    number+=1

prompt="\nTell me something,and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."
#active=True
#while active:
while True:
    message=input(prompt)
    if message =='quit':
        #active=False
        break
    else:
        print(message)

pizza="\nEnter the pizza toppings you want to add:"
pizza+="\nEnter 'quit' to end the program."
active=True
while active:
    message=input(pizza)
    if message=='quit':
        active=False
    else:
        print("We will add "+message+" in the pizza！")


age=input("\nPlease enter your age:")
#age+="\nEnter 'quit' to end the program."
age=int(age)
while True:
    #message=input(age)
    if age<3:
        print("You need to pay $0.")
        break
    elif age <12:
        print("You need to pay $10.")
        break
    else:
        print("You need to pay $15.")
        break


unconfirmed_users=['alice','brian','candace']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print("Verifying user:"+current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


pets=['dog','duck','fish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses={}
active=True
while active:
    name=input("\nWhat is your name?")
    response=input("Which mountain would you like to climb someday?")
    responses[name]=response
    repeat=input("Would you like to let another person respond?(yes/no)")
    if repeat=='no':
        active=False
print("\n---Poll Results---")
for name,response in responses.items():
    print(name+" Would like to climb "+response+".")

#7-8,7-9
sandwich_orders=['ham sandwich','pastrami sandwich','tuna sandwich','pastrami sandwich','chicken sandwich',
                 'pastrami sandwich']
finished_sandwiches=[]
#for sandwich_order in sandwich_orders:
    #print("I made your "+sandwich_order)
print("Sorry, the pastrami sandwiches are sold out!")
while sandwich_orders:
    while 'pastrami sandwich' in sandwich_orders:
        sandwich_orders.remove('pastrami sandwich')
    sandwich=sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

print("The sandwiches are finished! ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

vacationland={}
active=True
while active:
    people_name=input("\nWhat is you name?")#键
    place_name=input("\nIf you could visit one place in the world,where would you go?")#值
    vacationland[people_name]=place_name#***将键和值存入字典中
    repeat=input("Would you like to let another person respond?(yes/no)")
    if repeat=='no':
        active=False
print("----Results----")
for people_name,place_name in vacationland.items():
    print(people_name+" would like to "+place_name)"""





