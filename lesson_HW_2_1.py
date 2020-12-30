''''
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''''

my_list = ['text is text', int(5), float(6.1), None, ['1,23'], tuple('a,b,c,d'), 
           {'автомобиль': 'Тесла', 'производство': 'США'}]
for i in my_list:
    print(f'{i} is {type(i)}')

#my_int = int(5)
#my_float = 1.2
#my_str = "Hello world"
#my_list = ['a', '2']
#my_tuple = ('b', '3')
#my_dict = {'city': 'Moscow', 'country': 'Russia'}

#super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
#for i in super_list:
#    print(f'{i} is {type(i)}')