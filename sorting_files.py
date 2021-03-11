# -*- coding: utf-8 -*-

import os
import time
import shutil

INCOMING_FOLDER = 'icons'  # относительный путь к папке
PATH_NORMALIZED = os.path.normpath(INCOMING_FOLDER)  # нормализация пути
DESTINATION_FOLDER = 'icons_by_year'  # папка назначения


# Скрипт раскладывает файлы из одной папки по годам и месяцам в другую. Новая папка создается на этом же уровне.
# Пример:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg

class FileOrganizer:

    def __init__(self, incoming_folder, output_folder):
        self.incoming_folder_name = incoming_folder
        self.output_folder = output_folder

    def sorting_files(self):
        for dirpath, dirnames, filenames in os.walk(self.incoming_folder_name):
            for file in filenames:
                parent_dir = os.path.dirname(PATH_NORMALIZED)  # родительская директория входящей папки
                full_dir_file = os.path.join(dirpath, file)  # полный путь к файлу
                unix_time = os.path.getmtime(full_dir_file)  # дата последнего изменения файла unix
                file_time = time.gmtime(unix_time)  # структурированное время
                year = str(file_time[0])
                month = str(file_time[1])
                # новый путь назначения для файла: папка_назначения/год/месяц
                new_dir_name = os.path.join(parent_dir, self.output_folder, year, month)
                os.makedirs(new_dir_name, exist_ok=True)  # рекурсивное создание директории
                shutil.copy2(full_dir_file, new_dir_name)  # копирование файлов в новую папку
        print('Файлы перемещены')


icon_arrange = FileOrganizer(incoming_folder=PATH_NORMALIZED, output_folder=DESTINATION_FOLDER)
icon_arrange.sorting_files()
