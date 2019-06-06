import socket

IP = '0.0.0.0'
TCP_PORT = 1337
# BUFFER_SIZE = 20

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP, TCP_PORT))
    sock.listen(1)

    conn, addr = sock.accept()
    while 1:
        data = conn.recv(1024)
        if not data: break

        # Parse values
        content = bytes.decode(data).strip('\n')
        x, y = [x.strip() for x in content.split(';')]
        result = int(x) + int(y)

        conn.send(str(result).encode())

    conn.close()
