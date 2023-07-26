# Максим Мусулезный Задача 5
# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет,их содержимое в виде одноимённых pickle файлов.
import os
import pickle
from typing import BinaryIO


def search_files(ext: str = '.json', dir_: str = '.') -> None:

    files = (file for file in os.listdir(dir_) if file.endswith(ext))

    for file in files:
        name, _ = os.path.splitext(file)
        w_file: BinaryIO
        with (
            open(file, 'r') as r_file,
            open(name + '.pickle', 'wb') as w_file
        ):
            data: str = r_file.read()
            pickle.dump(file=w_file, obj=data)