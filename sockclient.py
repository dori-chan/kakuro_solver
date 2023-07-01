import socket


def sockets():
    """Запрашивает у сервера какуро и возвращает ее пользователю"""
    result = list()
    conn = socket.socket()
    try:
        conn.connect(("192.168.1.71", 14900))
    except Exception:
        return None
    tmp = conn.recv(16900)
    array = tmp.decode('utf-8')
    array = array[1:len(array) - 1]
    array = array.split(', ')
    for item in array:
        item = item.replace('\'', '')
        item = item.split(" ")
        result.append(item)
    conn.close()
    return result


if __name__ == "__main__":
    sockets()
