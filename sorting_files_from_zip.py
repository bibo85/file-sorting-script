# -*- coding: utf-8 -*-

import os
import zipfile

INCOMING_FILE = 'icons.zip'  # относительный путь к файлу
PATH_NORMALIZED = os.path.normpath(INCOMING_FILE)  # нормализация пути
DESTINATION_FOLDER = 'files_by_year'  # папка назначения


# Скрипт раскладывает файлы из zip архива по годам и месяцам в другую папку. Новая папка создается на этом же уровне.
#   результирующая папка
#       files_by_year/2018/05/cat.jpg
#       files_by_year/2018/05/man.jpg
#       files_by_year/2017/12/new_year_01.jpg


class ZipFileOrganizer:

    def __init__(self, incoming_file, output_folder):
        self.incoming_file_name = incoming_file
        self.output_folder = output_folder

    def sorting_files(self):
        with zipfile.ZipFile(self.incoming_file_name, 'r') as zf:
            # Проходим только по файлам
            for file in zf.infolist():
                if file.is_dir():  # не берем в работу каталоги
                    continue
                parent_dir = os.path.dirname(PATH_NORMALIZED)  # родительская директория входящего файла
                year = str(file.date_time[0])
                month = str(file.date_time[1])
                # оставляем у файла только базовое имя и убираем весь его путь в архиве,
                # чтобы при извлечении он не наложился на директорию назначения
                file.filename = os.path.basename(file.filename)
                # новый путь назначения для файла: родительская_директория/папка_назначения/год/месяц
                new_dir_name = os.path.join(parent_dir, self.output_folder, year, month)
                os.makedirs(new_dir_name, exist_ok=True)  # рекурсивное создание директории
                zf.extract(file, new_dir_name)  # извлекаем файл в новую папку
        print('Файлы перемещены')


icon_arrange = ZipFileOrganizer(incoming_file=PATH_NORMALIZED, output_folder=DESTINATION_FOLDER)
icon_arrange.sorting_files()
