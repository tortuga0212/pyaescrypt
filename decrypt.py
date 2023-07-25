import pyAesCrypt

password = input('Введите пароль для шифрования файла: ')

#decrypt
pyAesCrypt.decryptFile('text.aes', 'textout', password)