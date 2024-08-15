#A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.
x = lambda a, b, c : a + b + c
print(x(5, 6, 7))

#The power of lambda is better shown when you use them as an anonymous function inside another function. Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def funcion(n):
    return lambda a: n*a

doble = funcion(2)
print(doble(11))