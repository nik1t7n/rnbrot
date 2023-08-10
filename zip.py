import pyminizip
import sys
from rich import print
import os

def zipping(directory, key, password):

    # Paths to files
    key_file_path = directory + "/here_is_key.txt"
    zip_file_path = directory + "/output.zip"

    # Creating a text file with the key
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)

    # Creating an encrypted zip archive
    pyminizip.compress(key_file_path, None, zip_file_path, password, 5)

    # Removing the text file after compression
    os.remove(key_file_path)

    print("Encrypted zip archive successfully created!")


def unzipping(directory, password):
    zip_file_path = directory + "/output.zip"
    output_file_path = directory + "/here_is_key.txt"

    try:
        pyminizip.uncompress(zip_file_path, password, directory, True)

        with open(output_file_path, "r", encoding="utf-8") as decrypted_file:
            decrypted_content = decrypted_file.read()

        print(f"[cyan italic]Key successfully extracted:[/cyan italic]")
        return decrypted_content
    except Exception:
        print("\n| ERROR | Incorrect Password!\n")
        sys.exit()
