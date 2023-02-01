import os
import sys
from for_sorting import sorting

def main():
    directory = sys.argv[1]

    main_directory = directory  # Зберігання змінної "головної директорії" для подальшого сортування файлів в системні папки в корені

    os.makedirs(directory + '\\images\\', exist_ok=True)
    os.makedirs(directory + '\\videos\\', exist_ok=True)
    os.makedirs(directory + '\\documents\\', exist_ok=True)
    os.makedirs(directory + '\\music\\', exist_ok=True)
    os.makedirs(directory + '\\archives\\', exist_ok=True)  # створення папок для сортування
    print(sorting(directory, main_directory))


if __name__ == "__main__":
    main()