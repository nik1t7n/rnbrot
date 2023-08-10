import sys
import os
import time
from cryptography.fernet import Fernet

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
def file_read(filePath):
    try:
        with open(filePath, "rb") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print("\n| ERROR | File not found!\n")
        time.sleep(1)
        restart_program()
def encrypt(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)
    return encrypted_data

def decrypt(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data

def save(filePath, data):
    with open(filePath, "wb") as file:
        file.write(data)

