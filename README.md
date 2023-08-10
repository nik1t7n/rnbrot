Project Name: RnbRot Encryption Tool

Description:
This command-line tool provides a simple and secure way to encrypt and decrypt data using the AES encryption algorithm. Whether you need to safeguard sensitive information or transmit confidential files, this tool offers a user-friendly interface for securing your data.

Features:

Encrypt and decrypt data with AES encryption for enhanced security.
Support for both file-based and interactive input encryption/decryption modes.
Password-protected storage of encryption keys in zip archives.
Informative and interactive command-line interface with menu options.
Installation:

Clone or download the project repository to your local machine.
Open a terminal and navigate to the project directory.
Install Dependencies:
Before using the tool, ensure you have the required dependencies installed by running the following command:

bash
Copy code
pip install -r requirements.txt
This will automatically install the necessary libraries, including:

cryptography
rich
Usage:

Run the main.py script to launch the encryption tool.
Follow the on-screen menu to select your desired action.
Provide input or file paths as requested by the tool.
For encryption, an encryption key will be generated and securely stored. For decryption, the key will be retrieved from a password-protected zip archive.
Encrypted or decrypted data will be saved to the specified file path.
Usage Examples:

Encrypt data from a file:

Choose option 1 from the menu.
Provide the absolute path to the file.
Specify the file path to save the encrypted text.
Securely store the encryption key in a password-protected zip archive.
Decrypt data from a file:

Choose option 3 from the menu.
Provide the absolute path to the encrypted file.
Provide the path to the directory containing the key zip archive.
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

This tool utilizes AES encryption, a widely recognized and secure encryption algorithm.
Ensure you keep your encryption keys and passwords confidential.
For detailed instructions on how to use the tool, refer to the how_to_use section in the label module.
Authors:
Your Name

License:
This project is licensed under the MIT License. For more information, see the LICENSE file.
