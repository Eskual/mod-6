import os
import shutil
import sys

def sorting(directory):

    images = []
    videos = []
    documents = []
    music = []
    archives = []
    undefined = []
    links_to_folders = []

    special_folders = ['images','videos','documents','music','archives','undefined']

    objects = os.scandir(directory) #зчитування об'єктів в папці
    
    if len(os.listdir(directory)) == 0: #Видалення пустих папок напочатку рекурсії
        print(str(directory), 'is empty! DELETING')
        os.rmdir(os.path.abspath(directory))
        return ''
        
    else:

        known_formats = []
        unknown_formats = []
        for object in objects: # Додавання в відповідний список об'єктів та переміщення об'єкту у відповідну папку

            cooked_object = object.name.lower()
            
            
            if os.DirEntry.is_dir(object): # Перевірка, чи потрібно занурюватись у рекурсію (ігнорування спеціальних папок)

                if object.name not in special_folders:

                    links_to_folders.append(object)

                continue

            elif cooked_object.endswith(images_extensions): # Перевірка на закінчення відомих форматів
                images.append(object.name) # Додавання в список файлу
                os.replace(os.path.abspath(object), main_directory + '\\images\\' + normalize(os.path.splitext(object.name)[0]) + (os.path.splitext(object.name)[-1])) # Переміщення у відповідну папку файла
                if os.path.splitext(object)[-1] not in known_formats: # Будування списку зустрічаних форматів
                    known_formats.append(os.path.splitext(object)[-1])

            elif cooked_object.endswith(videos_extensions):

                videos.append(object.name)
                os.replace(os.path.abspath(object), main_directory + '\\videos\\' + normalize(os.path.splitext(object.name)[0]) + (os.path.splitext(object.name)[-1]))
                if os.path.splitext(object)[-1] not in known_formats:
                    known_formats.append(os.path.splitext(object)[-1])      

            elif cooked_object.endswith(documents_extensions):

                documents.append(object.name)
                os.replace(os.path.abspath(object), main_directory + '\\documents\\' + normalize(os.path.splitext(object.name)[0]) + (os.path.splitext(object.name)[-1]))
                if os.path.splitext(object)[-1] not in known_formats:
                    known_formats.append(os.path.splitext(object)[-1])

            elif cooked_object.endswith(music_extensions):

                music.append(object.name)
                os.replace(os.path.abspath(object), main_directory + '\\music\\' + normalize(os.path.splitext(object.name)[0]) + (os.path.splitext(object.name)[-1]))
                if os.path.splitext(object)[-1] not in known_formats:
                    known_formats.append(os.path.splitext(object)[-1])

            elif cooked_object.endswith(archives_extensions):
                
                shutil.unpack_archive(str(os.path.abspath(object)), main_directory + '\\archives\\' + str(object.name).rsplit('.', 1)[0])
                archives.append(object.name)
                if os.path.splitext(object)[-1] not in known_formats:
                    known_formats.append(os.path.splitext(object)[-1])
                os.remove(os.path.abspath(object))

            else: # Скидання невідомих форматів в окрему папку

                undefined.append(object.name)
                if os.path.splitext(object)[-1] not in unknown_formats: # Будування списку невідомих форматів
                    unknown_formats.append(os.path.splitext(object)[-1])

        if len(links_to_folders) >0: # рекурсивний виклик функції для перевірки вкладених папок
            print('!!!LEVEL DOWN!!!')
            for link in links_to_folders:
                print('CHECKING directory ', str(link.name))
                print(sorting(os.path.abspath(link)), ' ')
                if len(os.listdir(link)) == 0: #Видалення пустих папок на виході з рекурсії
                    print(str(link), 'is empty! DELETING')
                    os.rmdir(os.path.abspath(link))
                    return None
                os.rename(os.path.abspath(link), directory + '\\' + normalize(link.name)) # перейменування папки при виході з рекурсивного занурення в папку
        print('RESULT for ', str(directory))
        print('Known formats: ', known_formats)
        print('Unknown formats: ', unknown_formats)
        print('All files in ', str(directory), ':')
        return ('Images: ', images, 'Videos: ', videos, 'Documents: ', documents, 
        'Music: ', music, 'Archives: ', archives, 'Undefined: ', undefined)

def normalize(name_of_file):
    
    capital_letters = {
        ord('А') : 'A',
        ord('Б') : 'B',
        ord('В') : 'V',
        ord('Г') : 'H',
        ord('Ґ') : 'G',
        ord('Д') : 'D',
        ord('Е') : 'E',
        ord('Є') : 'Ie',
        ord('Ж') : 'Zh',
        ord('З') : 'Z',
        ord('И') : 'Y',
        ord('І') : 'I',
        ord('Ї') : 'I',
        ord('Й') : 'Y',
        ord('К') : 'K',
        ord('Л') : 'L',
        ord('М') : 'M',
        ord('Н') : 'N',
        ord('О') : 'O',
        ord('П') : 'P',
        ord('Р') : 'R',
        ord('С') : 'S',
        ord('Т') : 'T',
        ord('У') : 'U',
        ord('Ф') : 'F',
        ord('Х') : 'Kh',
        ord('Ц') : 'Ts',
        ord('Ч') : 'Ch',
        ord('Ш') : 'Sh',
        ord('Щ') : 'Shch',
        ord('Ь') : '',
        ord('Ю') : 'Iu',
        ord('Я') : 'Ia'
    }

    edited_name_of_file = ''

    for symbol in name_of_file: #Перебір назви файлу посимвольно

        if symbol.isalpha(): #Перевірка на літеру

            if symbol.isupper(): #Перевірка на регістр

                edited_name_of_file += symbol.translate(capital_letters)

            else:

                edited_name_of_file += (symbol.upper().translate(capital_letters)).lower()
            
        elif symbol.isdigit(): #Перевірка на цифру

            edited_name_of_file += symbol

        else:

            edited_name_of_file += '_' #Перевірка на решту символів
        
    return edited_name_of_file

if __name__ == "__main__":
    
    directory = sys.argv[1]

    main_directory = directory #Зберігання змінної "головної директорії" для подальшого сортування файлів в системні папки в корені

    os.makedirs(main_directory + '\\images\\', exist_ok=True)
    os.makedirs(main_directory + '\\videos\\', exist_ok=True)
    os.makedirs(main_directory + '\\documents\\', exist_ok=True)
    os.makedirs(main_directory + '\\music\\', exist_ok=True)
    os.makedirs(main_directory + '\\archives\\', exist_ok=True) # створення папок для сортування

    images_extensions = ('.jpeg', '.png', '.jpg', '.svg')
    videos_extensions = ('.avi', '.mp4', '.mov', '.mkv')
    documents_extensions = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
    music_extensions = ('.mp3', '.ogg', '.wav', '.amr')
    archives_extensions = ('.zip', '.gz', '.tar')

    sorting(directory)