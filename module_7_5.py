import os
import time

directory = os.getcwd()

def walkdir(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            filetime = os.path.getmtime(file)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(file)
            parent_dir = os.path.dirname(filepath)
            print(f'Обнаружен файл: {file}, Путь: {filepath},\n'
                  f'Размер: {filesize} байт,\n'
                  f'Время изменения: {formatted_time},\n'
                  f'Родительская директория: {parent_dir}\n')
        for dir in dirs:
            os.chdir(dir)
            walkdir(os.getcwd())

walkdir(directory)