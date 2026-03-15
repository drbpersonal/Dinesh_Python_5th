# # A function that has loop inside it

# def print_multiple(value, iteration):
#     new_list = []
#     for i in range(1, iteration+1):
#         new_list.append(value)
#     return new_list

# print(print_multiple('Aayush', 5))

# x ='Hello world'
# def my_function():
#     global x
#     x = 'Hello from function'
# my_function()
# print(x)

#function with nonlocal variable
# x = 10
# def outer_function():
#     x = 5
#     def inner_function():
#         nonlocal x
#         x += 10
#         print('The value of non local x is:', x)
#     print('Before calling inner function,x:', x)
#     inner_function()
#     print('After calling inner function,x:', x)

# outer_function()
# print('After calling outer function x:', x)

# Default parameter in function



# def add_numbers(a, b, *args):
#     sum_value = a + b
#     print('Additional arguments:', args)
#     for item in args:
#         sum_value += item
#     return sum_value
# print(add_numbers(2, 3))
# print(add_numbers(2, 3, 4, 5, 6))
# print(add_numbers(1, 2, 3, 4, 5, 6, 7, ))
# print(add_numbers(10, 20, 30))


# ARGUMENTS AS KEYWORD-VALUE PAIRS.
# def display_st_details(name, age, **kwargs):
#     print(f'[details of {age} year old student {name}]')
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')

# display_st_details(
#     'Aayush', 20,
#     city='Kathmandu',
#     College='Nepal commerce campus', 
#     subject='Python Programming',
#     class_teacher='Subrat Gyawali'
#     )

# RECURSIVE FUNCTION TO CALCULATE FACTORIAL OF A NUMBER

# def factorial(n):
#     if n>0:
#         return n * factorial(n-1)
#     return 1
# print(factorial(7))

# RECURSIVE FUNCTION TO CALCULATE FIBONACCI SERIES
# def fibonacci(n):
#     if n >1:
#         return fibonacci(n-1) + fibonacci(n-2)
#     return n
# item = fibonacci(7)
# print(item)

# LAMBDA FUNCTION TO CHECK ODD AND EVEN NUMBER
# odd_evenb = lambda num: 'Even' if num % 2 == 0 else 'Odd'
# print(odd_evenb(14))

# A lambda function that accepts a number and returns the square of that number
square = lambda x: x * x
print(square(6))
