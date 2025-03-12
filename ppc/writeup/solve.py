from pwn import *

r = remote('127.0.0.1', 6001)
line = ''

while not 'NAITCTF' in line: # Повторяем, пока сервер не возвращает строку со словом "NAITCTF" (флаг)
    problem = (r.recvuntil('Ответ')).decode('utf8') # Получаем весь пример до слова "Ответ"
    answ = str(eval(problem[problem.rfind(':')+1:problem.find('Ответ')])) # Выделяем пример из строки с помощью срезов и сразу рассчитываем ответ через eval()  
    r.send(answ.encode('utf8')) # Отправляем ответ на сервер, предварительно кодируя в utf8
    line = r.recvline().decode('utf8') # Получаем ответ сервера на наш пример
    
print(line)
