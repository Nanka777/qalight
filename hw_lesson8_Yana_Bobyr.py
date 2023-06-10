import logging
import re

#Запис у файл:
with open('file.txt', 'r') as file:
    print(file.readline())

with open('file.txt', 'a') as file:
    file.write('Good evening\n')
    file.write('something\n')


#Пошук і заміна:

with open('file.txt', 'r') as file:
    print(file.read(5))
with open('file.txt', 'r') as file:
    content = file.read()
    modified_content = content.replace("nanka", "Goga")
with open('file.txt', 'w') as file:
    file.write(modified_content)

#Лічильник слів:
with open('file.txt', 'r') as file:
    content1 = file.read()
    modified_content1 = len(content1)
print(modified_content1)

#Аналіз лог-файлу:
with open('log.txt', 'r') as fd:
    content = fd.read()
pattern = content.find('error')
if pattern != -1:
    print('Pattern found')
else:
    print("Pattern not found")

#Копіювання файлу:
import shutil

source_file = 'log.txt'
destination_file = 'file.txt'
shutil.copy(source_file, destination_file)
with open('log.txt', 'r') as file_1:
    print(file_1.readline())