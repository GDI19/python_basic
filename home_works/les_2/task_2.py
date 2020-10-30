"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

lst = input('Введите значения для списка: ')

length_lst = len(lst)

lst2 =[]
if length_lst %2 == 0:
    for i in range(0, length_lst-1, 2):
        lst2.append(lst[i+1])
        lst2.append(lst[i])
else:
    for i in range(0, length_lst-1, 2):
        lst2.append(lst[i+1])
        lst2.append(lst[i])
    lst2.append(lst[-1])
   

print(''.join(lst2))
        
        
        
