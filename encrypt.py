import pyAesCrypt

password = input('Введите пароль для шифрования файла: ')

#encrypt
pyAesCrypt.encryptFile('text', 'text.aes', password)