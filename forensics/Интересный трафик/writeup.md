## Анализ трафика и поиск скрытого флага

### Шаг 1: Открытие файла
Перед нами находится файл `secret.pcapng`. Попытка его анализа в Wireshark приводит к ошибке: `bad magic number`. Это говорит о возможных проблемах с заголовком файла или его содержимым.

### Шаг 2: Редактирование в HxD
Открываем `secret.pcapng` в HEX-редакторе (например, HxD). В начале файла обнаруживаем лишние нулевые байты: `00 00 00 00`. Удаляем их и сохраняем файл.

### Шаг 3: Анализ в Wireshark
Заново открываем исправленный файл в Wireshark. Теперь анализ проходит успешно, и мы замечаем интересный UDP-пакет. В нем присутствует следующий фрагмент данных:

```
0000   45 00 00 44 00 01 00 00 40 11 f6 1e c0 a8 01 PTQ5MTEnIxgaDBAPABcsHB46BxcVPAIEFwAADQ4=
```

Часть данных выглядит как base64-строка: `PTQ5MTEnIxgaDBAPABcsHB46BxcVPAIEFwAADQ4=`.

### Шаг 4: Декодирование Base64
Напишем простой Python-скрипт для декодирования base64:

```python
import base64

data = "PTQ5MTEnIxgaDBAPABcsHB46BxcVPAIEFwAADQ4="
decoded = base64.b64decode(data)
print(decoded)
```

После выполнения получаем следующий набор байтов:

```
b"=4911'#\x18\x1a\x0c\x10\x0f\x00\x17,\x1c\x1e:\x07\x17\x15<\x02\x04\x17\x00\x00\r\x0e"
```

### Шаг 5: Декодирование XOR
Судя по структуре данных, они зашифрованы XOR'ом с ключом. Используем следующий код:

```python
data = b"=4911'#\x18\x1a\x0c\x10\x0f\x00\x17,\x1c\x1e:\x07\x17\x15<\x02\x04\x17\x00\x00\r\x0e"
key = "supersecretkey"

decoded = bytes([data[i] ^ ord(key[i % len(key)]) for i in range(len(data))])
print(decoded.decode('utf-8'))
```

После выполнения получаем флаг:

```
NAITCTF{hidden_in_udp_packet}
```

