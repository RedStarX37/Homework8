import os
import shutil


def error():
    print('ОШИБКА!\nВы ввели не число\nВведите одно из чисел меню')


def error_separators(f): # декоратор
    def inner():
        print('\n' + '*' * 30)
        result = f()
        print('*' * 30)
        return result
    return inner


new_error = error_separators(error)


def menu_bar():
    global selection
    print('\nМЕНЮ\n1.  создать папку;\n2.  удалить (файл/папку);\n3.  копировать (файл/папку);'
          '\n4.  просмотр содержимого рабочей директории;\n5.  посмотреть только папки;\n6.  посмотреть только файлы;'
          '\n7.  выход\n')

    try:
        selection = int(input('Выберите один из пунктов: ')) # обработка исключений
    except ValueError:
        new_error()
    else:
        return selection



def create_folder():
    print('Создание новой папки\n')
    new_folder_name = input('Придумайте название новой папки: ')
    os.mkdir(f'{new_folder_name}')


def delete_folder():
    print('Удаление папки\n')
    del_folder_name = input('Название удаляемой папки: ')
    os.rmdir(f'{del_folder_name}')


def copy_file_folder():
    print('Копирование папки/файлв\n')
    unit_name = input('Название папки/файла: ')
    copy_loc = input('Место копирования: ')
    loc = f'{unit_name}'
    dest = f'{copy_loc}'
    shutil.copyfile(loc, dest)


def view_directory():
    print('Viewing directory\n')
    print(os.listdir())


def view_only_folders():
    print('Просмотр папок\n')
    folders = [f for f in os.listdir('.') if os.path.isdir(f)]
    print(folders)


def view_only_files():
    print('Просмотр файлов\n')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print(files)


def get_selection():
    selection = menu_bar()

    if selection == '1':
        create_folder()
    elif selection == '2':
        delete_folder()
    elif selection == '3':
        copy_file_folder()
    elif selection == '4':
        view_directory()
    elif selection == '5':
        view_only_folders()
    elif selection == '6':
        view_only_files()
    elif selection == '7':
        exit()
    else:
        get_selection()

    get_selection()


def first_call():
    print('\nДобро пожаловать в файловый менеджер с использованием тернальных операторов и генераторов списков!')
    proceed_to_menu = input('Вы хотите перейти в меню? (д/н): ')
    get_selection() if proceed_to_menu == 'д' else first_call() # тернарный оператор


first_call()
