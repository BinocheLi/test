def decorator_passing_arbitrary_arguments(func):
    def wrapper_accepting_arbitrary_arguments(*args):
            return str('The positional arguments are', args)
    return wrapper_accepting_arbitrary_arguments      

@ decorator_passing_arbitrary_arguments
def function_with_arguments(arg1, arg2, arg3):
    return (arg1, arg2, arg3)

ans13 = function_with_arguments(1,2,3)
print(ans13)

def plus_one(i):
    def add_one():
        result=1+i
        return result
    return add_one


print(plus_one(7))

def add(*args, **kwargs):
    result=0
    for i in args:
        result +=i
    for k,v in kwargs.items():
        result +=v
    return result

## decoration and wrapping functions
def mydeco2(func):
    def wrapper(*args, **kwargs):
        result=func(*args, **kwargs)
        return f'my decorated result: {result}!!!'
    return wrapper

# kwargs={"arg1":29, "arg2":35}
# args=(30,40)
# myadd=mydeco2(add)
# print(myadd(*args, **kwargs))

## In python, "@" is followed by the decorator fucntion name.
@ mydeco2
def mysum(*args,**kwargs):
    '''Sum any numbers together, the long way This is a really long comment that can make 
    the code look ugly and uncomfortable to read on  small screen so it needs to be broken into
    multi-line strings using double triple-quotes'''
    total=0
    for i in args:
        total+=i
    for k,v in kwargs.items():
        total+=v
    return total

print(mysum(20,30,40,60,arg1=29, arg2=35))  

from functools import wraps
def mydeco3(func):
    @ wraps(func)
    def wrapper2(*args, **kwargs):
        result=func(*args, **kwargs)
        return f'{result}!!!'
    return wrapper2

@ mydeco3
def mysum2(*args):
    total=0
    for i in args:
        total+= i
    return total

print(mysum2(6,-9,8,1))



def hello():
    return "hello world"

def wrapper(func):
    greeting="wrapper says "
    return f"{greeting}{func()} !!!"


def mydeco(func):
    def wrapper():
        greeting="wrapper says "
        return f"{greeting}{func()} !!!"
    return wrapper

myhello=mydeco(hello)
print(myhello())

def display_user_total_assets(FirstName, LastName, **kwargs):
    result=0
    for k,v in kwargs.items():
        result += v
    print(FirstName +' ' + LastName + ': ' + str(result))
ans8a = display_user_total_assets("John", "Smith", Car=30000, House=450000, Savings=1000000)
ans8b = display_user_total_assets("Joe", "Clark", Car=15000, House=250000)

def hello_user(**kwargs):
    for k,v in kwargs.items():
        if k=="First_Name":
            result = 'Hello'+" "+ v
    return result

ans7a = hello_user(First_Name="Elon", Last_Name="Musk", Email="Elon.Musk@yy.com")
ans7b = None

def subtract_from_highest(*args):
    highest=max(args)
    result=highest
    for i in args:
        if i<highest:
            result -=i
    return result
ans3a = subtract_from_highest(1,2,3)

