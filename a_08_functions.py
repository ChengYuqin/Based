"""def greet_user(username):
    #显示简单的问候语
    print("Hello, "+username.title()+"!")
greet_user('jesse')
greet_user('sarah')

def display_message():
    print("In this chapter I learn about functions.")
display_message()

def favorite_book(title):
    print("One of my favorite books is "+title.title()+".")
favorite_book('alice in wonderland')


#def describe_pet(animal_type,pet_name):
def describe_pet(pet_name,animal_type='dog'):#默认值：形参指定默认值,要先列出没有默认值得形参
    print("I have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
#describe_pet('dog','baibai')#位置实参：要求实参顺序与形参相同
describe_pet(animal_type='cat',pet_name='boss')#关键字实参
describe_pet(pet_name='baibai'.title())#关键字实参


def make_shirt(size,type):
    print("The shirt size is "+size+", and the type is "+type)
make_shirt('xl','Hello world!')"""

def get_formatte_name(first_name,last_name,middle_name=''):
    """if middle_name:
        print(first_name.title()+" "+middle_name.title()+" "+last_name.title())
    else:
        print(first_name.title()+" "+last_name.title())
get_formatte_name('cheng','qin','yu')#位置实参，要按顺序填写
get_formatte_name('wang','shan')"""
    if middle_name:
        full_name=first_name+' '+middle_name+' '+last_name

    else:
        full_name=first_name+' '+last_name
    return full_name.title()
musician=get_formatte_name('cheng','qin','yu')#位置实参，要按顺序填写
print(musician)
musician=get_formatte_name('wang','shan')
print(musician)