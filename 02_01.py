#wap to display basic exception handling in python
x = 5
y = 1
try:
    print(x + y)
    print(x/y)
except ZeroDivisionError:
    print("Error : Any Value can not divide by Zero")
except TypeError:
    print('Error : Can not Add Int and String ')
