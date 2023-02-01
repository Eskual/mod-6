def normalize(name_of_file):
    capital_letters = {
        ord('А'): 'A',
        ord('Б'): 'B',
        ord('В'): 'V',
        ord('Г'): 'H',
        ord('Ґ'): 'G',
        ord('Д'): 'D',
        ord('Е'): 'E',
        ord('Є'): 'Ie',
        ord('Ж'): 'Zh',
        ord('З'): 'Z',
        ord('И'): 'Y',
        ord('І'): 'I',
        ord('Ї'): 'I',
        ord('Й'): 'Y',
        ord('К'): 'K',
        ord('Л'): 'L',
        ord('М'): 'M',
        ord('Н'): 'N',
        ord('О'): 'O',
        ord('П'): 'P',
        ord('Р'): 'R',
        ord('С'): 'S',
        ord('Т'): 'T',
        ord('У'): 'U',
        ord('Ф'): 'F',
        ord('Х'): 'Kh',
        ord('Ц'): 'Ts',
        ord('Ч'): 'Ch',
        ord('Ш'): 'Sh',
        ord('Щ'): 'Shch',
        ord('Ь'): '',
        ord('Ю'): 'Iu',
        ord('Я'): 'Ia'
    }

    edited_name_of_file = ''

    for symbol in name_of_file:  # Перебір назви файлу посимвольно

        if symbol.isalpha():  # Перевірка на літеру

            if symbol.isupper():  # Перевірка на регістр

                edited_name_of_file += symbol.translate(capital_letters)

            else:

                edited_name_of_file += (symbol.upper().translate(capital_letters)).lower()

        elif symbol.isdigit():  # Перевірка на цифру

            edited_name_of_file += symbol

        else:

            edited_name_of_file += '_'  # Перевірка на решту символів

    return edited_name_of_file