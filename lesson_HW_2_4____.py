'''
4.Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если введённое слово длинное, выводить только первые 10 букв в слове
'''

#word_new = input(str())

#print(, sep='\n')

#print("Введите строку: ")
#my_str1 = input([])
#for elem in my_str1:
#    print(elem,'\n')
    #print(my_str1,sep='\n')
    #если print(my_str1,sep='\n'), то
    # получим: ['в', 'в', 'е', 'д', 'и', 'т', 'е', ' ', 'с', 'т', 'р', 'о', 'к', 'у', ' ']
    # с пробелами
list_1 = input().split()
#for item in enumerate(list_1):
  #  print(item)#(0, 'k') (1, 'j') (2, 'h')
for count, item in enumerate(list_1):
     if len(item) <= 10:
        print(count, item)
     else:
         print('Нужно выводить первые 10 букв в слове.Но как?')

#for count, item in enumerate(list_1, 100):
    #print(count, item)
    #11 u
#12 o
#100 k
#for i, score in enumerate(scores, 1):
  # print(i, score)
