# import time
#
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #do something before run function
#         function()
#
#     return wrapper_function
#
# #wrap say hello with @ = put the function to the other function
# #equal delay_decoration(say_hello)
# @delay_decorator
# def say_hello():
#     print("Hello, World!")
#
# @delay_decorator
#     print("Bye, World!")
#
# def say_greeting():
#     print("Hello, Greeter!")
#
# say_hello()



# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
# def create_blog_post(user):
#     print(f"Creating Blog Post from {user.name}")
#
# def is_auth_decoration(function):
#     #*args to accept any number of arguments:
#     # many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function()
#     return wrapper
#
#
# @is_auth_decoration
# def created_blog_post(user):
#     print(f"Creating Blog Post from {user.name}")
#
# new_user = User("John")
# new_user.is_logged_in = True
# create_blog_post(new_user)


def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(*args)
        print(f"It returned: {result}")
        return result

    return wrapper


@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)