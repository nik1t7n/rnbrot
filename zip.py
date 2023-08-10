import pyminizip
import sys
from rich import print
import os

def zipping(directory, key, password):

    # Пути к файлам
    key_file_path = directory + "/here_is_key.txt"
    zip_file_path = directory + "/output.zip"

    # Создание текстового файла с ключом
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)

    # Создание зашифрованного zip-архива
    pyminizip.compress(key_file_path, None, zip_file_path, password, 5)

    # Удаление текстового файла после компрессии
    os.remove(key_file_path)

    print("Зашифрованный zip-архив успешно создан!")


def unzipping(directory, password):
    zip_file_path = directory + "/output.zip"
    output_file_path = directory + "/here_is_key.txt"

    try:
        pyminizip.uncompress(zip_file_path, password, directory, True)

        with open(output_file_path, "r", encoding="utf-8") as decrypted_file:
            decrypted_content = decrypted_file.read()

        print(f"[cyan italic]Ключ успешно извлечен:[/cyan italic]")
        return decrypted_content
    except Exception:
        print("\n| ОШИБКА | Пароль Неверный!\n")
        sys.exit()
