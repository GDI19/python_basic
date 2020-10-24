num = int(input('Введите число в секундах чтобы получить чч:мм:сс: '))

hours = num // 3600
minutes = (num % 3600) // 60
seconds = (num % 3600) % 60

print('Получаем {:02}:{:02}:{:02}'.format(hours, minutes, seconds))
