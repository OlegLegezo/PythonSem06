
# находим те числа, что встречаются один раз
# [1,1,2] ->[2]


# map - пропускает через себя все элементы и возвращает (не сокращая)
# filter - уже есть возможность изменить то, что получил (просеять)
# включения - по сути генератор
# zip - расставлят группы элементов
# numirate - нумирует


import tkinter


print('простой вариант решения:')
a=[12,2122,1223,12,334]
print(a.count(12))

print('lambda вариант решения:')
my_list=list(filter(lambda x:a.count(x)==1,a))
print(my_list)

print('включение вариант решения:')
my_list = [i for i in a if a.count(i)==1]
# взять i из листа а
print(my_list)
print('включение вариант решения (поиск позиций):')
my_list = [i for i in range(len(a)) if a.count(a[i])==1]

print(my_list)

# распаковка кортежа:
print('распаковка кортежа:')
glist=[('a',1), ('b',2),('c',3),('d',4)]
for i in glist:
    print(glist[0])
    print(glist[1])
print('распаковка кортежа2:')
# glist=[('a',1), ('b',2), ('c',3), ('d',4)]
# for i in glist:
#     for j in i:
#         print("{i}" * j)
#         i=i+2
repack=[]
for i in range(len(glist)):
    print('начало')
    print(i)
    for j in glist[i]:
        print(j)
        print('конец')
print(repack)
print('распаковка кортежа3:')
print(*glist)


list_tuple = [('a', 3), ('b', 5)]
result = ''
for item in list_tuple:
    result += item[0] * item[1]
print(result)

# (0,len(glist),2)
'''
from tkinter - импортировали всю библиотеку
tkinter.label - обращаемся в функции внутри импортированной библиотеки


from tkinter import label as lb1 - импортировали оперделенную функцию из библиотеки и переназвали ее для своего пользования
from tkinter import * - импортировали всю библиотеку с названиями из библиотеки (лучше не использовать)
pip - установщик библиотек


'''
# print(f'{:4}чтобы сделать ровный отстсуп')
from tkinter import label as lb1

