Project Name: RnbRot Encryption Tool

Description:
The RnbRot Encryption Tool is a versatile command-line utility designed to provide a straightforward and secure solution for encrypting and decrypting data using the AES encryption algorithm. Whether you're safeguarding sensitive information or transmitting confidential files, this tool offers a user-friendly interface to fortify your data protection.

Features:

Perform Fernet encryption and decryption to bolster data security.
Choice between file-based and interactive input modes for encryption/decryption.
Password-protected storage of encryption keys within zip archives.
Engaging and interactive command-line interface enriched with menu options.
Installation:

Clone or download the project repository to your local machine.
Open a terminal and navigate to the project directory.
Install Dependencies:
Before utilizing the tool, ensure you have the required dependencies installed by executing the following command:

pip install -r requirements.txt

This command will automatically install the necessary libraries.

Usage:

Launch the encryption tool by running the main.py script.
Follow the on-screen menu to select your desired action.
Input data or file paths as guided by the tool.
For encryption, the tool generates and securely stores an encryption key. For decryption, the key is retrieved from a password-protected zip archive.
Encrypted or decrypted data is saved to the specified file path.
Usage Examples:

Encrypt data from a file:

Choose option 1 from the menu.
Provide the absolute path to the file.
Specify the file path to save the encrypted text.
Securely store the encryption key in a password-protected zip archive.
Decrypt data from a file:

Choose option 3 from the menu.
Provide the absolute path to the encrypted file.
Specify the path to the directory containing the key zip archive.
Enter the password for the key zip archive.
Specify the file path to save the decrypted text.
Encrypt user input:

Choose option 2 from the menu.
Enter the text to encrypt.
Specify the file path to save the encrypted text.
Securely store the encryption key in a password-protected zip archive.
Decrypt user input:

Choose option 4 from the menu.
Enter the encrypted text.
Provide the path to the directory containing the key zip archive.
Enter the password for the key zip archive.
Specify the file path to save the decrypted text.
Additional Notes:

The tool employs Fernet encryption, a widely recognized and robust encryption algorithm.
Maintain the confidentiality of your encryption keys and passwords.
For comprehensive usage instructions, refer to the 5 point in menu.

Authors:
Nik1t7n

License:
This project is licensed under the MIT License. For detailed information, consult the LICENSE file.
