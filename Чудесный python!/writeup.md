# Writeup: Чудесный python!

## Анализ исполняемого файла

Мы получили .exe файл. Анализируем его и определяем, что это Python-приложение, упакованное через **PyInstaller**.

## Извлечение байткода

Используем **PyInstxtractor** для извлечения байткода:
```
python pyinstxtractor.py task1.exe
```
После выполнения получаем файл **task1.pyc**.

## Декомпиляция байткода

Существует несколько способов декомпиляции .pyc-файла. В данном случае воспользуемся онлайн-инструментом **pylingual.io**. Загружаем **task1.pyc** на сайт и получаем следующий исходный код:

```python
# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: task1.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import base64

def check_password(password):
    encoded_secret = b'TkFJVENURntINGNrX1MwXzN6fQ=='
    secret = base64.b64decode(encoded_secret).decode()
    if password == secret:
        return 'Flag Correct!'
    return 'Wrong! Try one more...'

if __name__ == '__main__':
    user_input = input('Write Flag: ')
    result = check_password(user_input)
    print(result)
```

## Извлечение флага

В коде используется **base64** для хранения зашифрованного секрета. Декодируем строку **TkFJVENURntINGNrX1MwXzN6fQ==** с помощью сайта [base64decode.org](https://www.base64decode.org/) или Python-скрипта:

```python
import base64
encoded_secret = b'TkFJVENURntINGNrX1MwXzN6fQ=='
print(base64.b64decode(encoded_secret).decode())
```

В результате получаем флаг:
```
NAITCTF{H4ck_S0_3z}
```