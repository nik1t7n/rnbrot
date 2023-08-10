import funcs
import label
from cryptography.fernet import Fernet
import zip
import getpass
import sys

label.label()
label.menu()

ans = int(input("\033[91m\033[1mВведите номер выбранного действия:\033[0m "))

# если работаем с файлами
if ans == 1 or ans == 3:
    filePath = input("\033[91m\033[1mВведите абсолютный путь до файла:\033[0m ")
    # читаем файл
    data = funcs.file_read(filePath)
    # если зашифровать данные с файла
    if ans == 1:
        # генерируем ключ шифрования
        key = Fernet.generate_key()
        # шифруем данные с помощью функции из файла функс
        encrypted_data = funcs.encrypt(data, key)
        # пользователь вводит путь до файла куда сохранит зашифрованные данные
        saveFilePath = input(
            "\033[91m\033[1mВведите путь до файла для сохранения текста:\033[0m "
        )
        # сохраняем данные файл функцией save из файла функс
        funcs.save(saveFilePath, encrypted_data)
        # просим пользователя сохранить ключ чтобы потом получить доступ к данным
        key_zip_file = input(
            "\033[91m\033[1mВведите путь до директории (без /) для сохранения ключа шифрования:\033[0m "
        )
        password = getpass.getpass("\033[91m\033[1mВведите пароль для файла:\033[0m ")
        # сохраняем ключ
        zip.zipping(key_zip_file, key, password)
        print("\033[91m\033[1mКлюч успешно сохранен.\033[0m")
    # если расшифровать данные с файла
    elif ans == 3:
        # получаем уже готовый ключ чтобы расшифровать данные
        key_file = input(
            "\033[91m\033[1mВведите путь до директории (без /) с ключом шифрования:\033[0m "
        )
        password = getpass.getpass("\033[91m\033[1mВведите пароль для файла:\033[0m ")
        # загружаем ключ
        key = zip.unzipping(key_file, password)
        # расшифровывем данные функцией decrypt из файла функс
        decrypted_data = funcs.decrypt(data, key)
        # пользователь вводит куда расшифровать данные
        saveFilePath = input(
            "\033[91m\033[1mВведите путь до файла для сохранения текста:\033[0m "
        )
        # сохраняем все в файл
        funcs.save(saveFilePath, decrypted_data)

# если работаем с вводом
if ans == 2 or ans == 4:
    # если зашифровать введенные данные
    if ans == 2:
        # получаем информацию
        data = input("\033[91m\033[1mВведите текст:\033[0m ")
        data = data.encode("utf-8")
        # создаем уникальный ключ шифрования
        key = Fernet.generate_key()
        # шифруем
        encrypted_data = funcs.encrypt(data, key)
        # куда сохранять
        saveFilePath = input(
            "\033[91m\033[1mВведите путь до файла для сохранения текста:\033[0m "
        )
        # сохраняем
        funcs.save(saveFilePath, encrypted_data)
        # сохраняем ключ
        key_zip_file = input(
            "\033[91m\033[1mВведите путь до директории (/) для сохранения ключа шифрования:\033[0m "
        )
        password = getpass.getpass("\033[91m\033[1mВведите пароль для файла:\033[0m ")
        # сохраняем ключ
        zip.zipping(key_zip_file, key, password)
        print("\033[91m\033[1mКлюч успешно сохранен.\033[0m")

    # если расшифровать введенные данные
    elif ans == 4:
        # читаем шифр
        data = input("\033[91m\033[1mВведите текст:\033[0m ")
        # получаем уже готовый ключ чтобы расшифровать данные
        key_file = input(
            "\033[91m\033[1mВведите путь до директории (без /) с ключом шифрования:\033[0m "
        )
        password = getpass.getpass("\033[91m\033[1mВведите пароль для файла:\033[0m ")
        # загружаем ключ
        key = zip.unzipping(key_file, password)
        # расшифровывем данные функцией decrypt из файла функс
        decrypted_data = funcs.decrypt(data, key)
        # пользователь вводит куда расшифровать данные
        saveFilePath = input(
            "\033[91m\033[1mВведите путь до файла для сохранения текста:\033[0m "
        )
        # сохраняем все в файл
        funcs.save(saveFilePath, decrypted_data)

if ans == 5:
    label.how_to_use()

if ans == 6:
    sys.exit()