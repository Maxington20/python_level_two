# x = 25

# def my_func():
#     x = 50
#     return x

# # prints 25
# # print(x)
# # prints 50
# # print(my_func())

# my_func()
# # prints 25, the global x
# print(x)


# enclosing function locals
name = "This is a global name"

def greet():
    name = "sammy"

    def hello():
        print("Hello " + name)

    hello()

# prints hello sammy
greet()

x = 50

def func(x):
    print("x is :",x)
    x = 1000
    print('local x changed to:',x)

# prints 50, then 1000
func(x)

# prints 50
print(x)