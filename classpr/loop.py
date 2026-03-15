# Using range() function to iterate for 10 times
# odd = list(range(1,22,23))
# print (odd)

# multiples = list(range(3,31,3))
# print(multiples)

# for loop with dictionary
# 
# student = {
#     'name': 'Dinesh',
#     'age': 23,
#     'address': 'Kanchanpur',
# }
# for key, value in student.items():
#     print(f'The {key} is {value}')

# for tuple
# student = {
#     'name': 'Dinesh',
#     'age': 23,
#     'address': 'Kanchanpur',
# }
# for a in student.items():
#     print(a)

# The enumerate function

# items =[chr(val) for val in range(65, 91)]
# print(items)
# casts = ['Aayush', 'Aabaran','aagya','Aabash','aashna','Akash','Bishnu','Binit','Bishal','Bikash','Dinesh','Evens','Indra','Ipsita','Iemin','Kripa','Karun','Kashis','Mohan','Nirjala','nishant','supriya','safal']
# for index, cast in enumerate(casts):
#     print(f'{index})\t{cast}')





# A A A A A
# A A A A A
# A A A A A
# A A A A A
# A A A A A

# for i in range(5):
#  for j in range(5):
#       print('A',end=' ')
#  print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

#         1
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1
# for row in range(1,6):
#     print('  ' * (5 - row), end=' ')
#     for col in range (row, 0, -1):
#         print(col, end=' ')
#     print()

# new_list = []
# for x in range(1, 11):
#   new_list.append(x*2)
# print(new_list)
  
# dictionary comprehension
# dict_1= {x: x**2 for x in range(1, 6)}

# dict_2= {x: x**3 for x in range(1, 6)}
# print (dict_2)
