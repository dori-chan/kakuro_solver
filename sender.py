import socket
import random


def reader(filename):
    """
    Считывает какуро, возвращает ее массив
    """
    filename = str(filename)
    result = list()
    with open(filename) as f:
        for lines in f:
            lines = ' '.join(lines.split())
            result.append(lines)
    if len(result) == 0:
        print('Некорректный ввод')
        exit(1)
    return result


def sockets():
    """Отсылает пользователю прочитанную карту"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", 14900))
    sock.listen(10)
    while True:
        conn, addr = sock.accept()
        rnd = random.randint(1, 3)
        name = str(rnd) + ".txt"
        message = reader(name)
        conn.send(bytes(str(message), encoding='utf-8'))
        conn.close()


if __name__ == "__main__":
    sockets()
