"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('task_2.txt', 'r', encoding='utf-8') as file:
    lines = 0
    for line in file:
        lines += 1
        words = len(line.split())
        print(f'На строке № {lines}: {words} слов.')

print('В файле всего:', lines, 'строк(и)')




