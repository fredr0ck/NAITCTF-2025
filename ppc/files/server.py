import socket
import time
import random

sock = socket.socket()
hello = 'Привет! Тебе предстоит решить 100 математических примеров за 60 секунд. Если ты сможешь, то получишь флаг. \nУдачи!\n'
signs = ['+', '-', '*']

sock.bind(('', 6001))
sock.listen(40)

while True:
    try:
        conn, addr = sock.accept()
        print('Connected by: ', addr)
        conn.send(hello.encode('utf8'))
        timer = 60
        count = 100
        start_time = time.time()
        for i in range(1, count+1):
            remaining_time = timer - (time.time() - start_time)
            if remaining_time <= 0:
                conn.send(('Время вышло!').encode('utf8'))
                conn.close()
            fst = str(random.randint(-(i*10), (i*10)))  
            snd = str(random.randint((i*10), (i*10)))
            rand_sign = signs[random.randint(0,2)]
            problem = f'Осталось времени: {round(remaining_time)} секунд \nПример номер {i}: {fst} {rand_sign} {snd}\nОтвет: '
            cor_answ = int(eval(fst+rand_sign+snd))
            conn.send(problem.encode('utf8'))
            answ = conn.recv(1024)
            print('Received by ',addr,'.', '\n', 'Text: ', answ.decode('utf8'))
            if int(answ)!= cor_answ:
                    conn.send(('Неверно!').encode('utf8'))
                    conn.close()
                    break
    
        conn.send(('Поздравляем с решением! Ваш флаг: NAITCTF{M4TH_F1N4L_B0SS}'.encode('utf8')))
        print('Solved by: ', addr)
        conn.close()
    except:
        pass