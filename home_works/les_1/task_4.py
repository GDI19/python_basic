num = input('Введите число: ')

maxi = 0
for i in range(len(num)-1):
    if maxi < int(num[i]):
        maxi = int(num[i])

print('Максимальная цифра в заданом числе будет:', maxi)