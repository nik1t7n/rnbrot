import funcs
import label
from cryptography.fernet import Fernet
import zip
import getpass
import sys
import os

label.label()
label.menu()

ans = int(input("\033[91m\033[1mEnter the number of the selected action:\033[0m "))

# If working with files
if ans == 1 or ans == 3:
    filePath = input("\033[91m\033[1mEnter the absolute path to the file:\033[0m ")
    filePath = os.path.abspath(os.path.expanduser(filePath))
    # Read the file
    data = funcs.file_read(filePath)
    # If encrypting data from a file
    if ans == 1:
        # Generate encryption key
        key = Fernet.generate_key()
        # Encrypt data using the function from the funcs file
        encrypted_data = funcs.encrypt(data, key)
        # User inputs the path to the file to save encrypted data
        saveFilePath = input(
            "\033[91m\033[1mEnter the path to the file to save the text:\033[0m "
        )
        saveFilePath = os.path.abspath(os.path.expanduser(saveFilePath))
        # Save data to file using the save function from the funcs file
        funcs.save(saveFilePath, encrypted_data)
        # Ask the user to save the key for future access
        key_zip_file = input(
            "\033[91m\033[1mEnter the directory path to save the encryption key:\033[0m "
        )
        key_zip_file = os.path.abspath(os.path.expanduser(key_zip_file))
        password = getpass.getpass("\033[91m\033[1mEnter a password for the file:\033[0m ")
        # Save the key
        zip.zipping(key_zip_file, key, password)
        print("\033[91m\033[1mKey successfully saved.\033[0m")
        funcs.restart_program()
    # If decrypting data from a file
    elif ans == 3:
        # Get the existing key to decrypt the data
        key_file = input(
            "\033[91m\033[1mEnter the directory path with the encryption key:\033[0m "
        )
        key_file = os.path.abspath(os.path.expanduser(key_file))
        password = getpass.getpass("\033[91m\033[1mEnter a password for the file:\033[0m ")
        # Load the key
        key = zip.unzipping(key_file, password)
        # Decrypt the data using the decrypt function from the funcs file
        decrypted_data = funcs.decrypt(data, key)
        # User inputs where to save the decrypted data
        saveFilePath = input(
            "\033[91m\033[1mEnter the path to the file to save the text:\033[0m "
        )
        saveFilePath = os.path.abspath(os.path.expanduser(saveFilePath))
        # Save everything to a file
        funcs.save(saveFilePath, decrypted_data)
        funcs.restart_program()

# If working with user input
if ans == 2 or ans == 4:
    # If encrypting user input data
    if ans == 2:
        # Get user input
        data = input("\033[91m\033[1mEnter the text:\033[0m ")
        data = data.encode("utf-8")
        # Generate a unique encryption key
        key = Fernet.generate_key()
        # Encrypt
        encrypted_data = funcs.encrypt(data, key)
        # Specify where to save
        saveFilePath = input(
            "\033[91m\033[1mEnter the path to the file to save the text:\033[0m "
        )
        saveFilePath = os.path.abspath(os.path.expanduser(saveFilePath))
        # Save
        funcs.save(saveFilePath, encrypted_data)
        # Save the key
        key_zip_file = input(
            "\033[91m\033[1mEnter the directory path to save the encryption key:\033[0m "
        )
        key_zip_file = os.path.abspath(os.path.expanduser(key_zip_file))
        password = getpass.getpass("\033[91m\033[1mEnter a password for the file:\033[0m ")
        # Save the key
        zip.zipping(key_zip_file, key, password)
        print("\033[91m\033[1mKey successfully saved.\033[0m")
        funcs.restart_program()

    # If decrypting user input data
    elif ans == 4:
        # Read the cipher
        data = input("\033[91m\033[1mEnter the text:\033[0m ")
        # Get the existing key to decrypt the data
        key_file = input(
            "\033[91m\033[1mEnter the directory path with the encryption key:\033[0m "
        )
        key_file = os.path.abspath(os.path.expanduser(key_file))
        password = getpass.getpass("\033[91m\033[1mEnter a password for the file:\033[0m ")
        # Load the key
        key = zip.unzipping(key_file, password)
        # Decrypt the data using the decrypt function from the funcs file
        decrypted_data = funcs.decrypt(data, key)
        # User inputs where to save the decrypted data
        saveFilePath = input(
            "\033[91m\033[1mEnter the path to the file to save the text:\033[0m "
        )
        saveFilePath = os.path.abspath(os.path.expanduser(saveFilePath))
        # Save everything to a file
        funcs.save(saveFilePath, decrypted_data)
        funcs.restart_program()

if ans == 5:
    label.how_to_use()

if ans == 6:
    sys.exit()
