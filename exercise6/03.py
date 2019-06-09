import argparse
import socket


def read_argument():
    """ Return port """
    parser = argparse.ArgumentParser(description='Sum or multiply integers.')
    parser.add_argument('port', metavar='N', nargs='+', type=int, help='TCP-Port')
    return parser.parse_args().port[0]


def open_tcp_connection(tcp_port):
    """
    Open TCP connection with the given port
    Two lines will be ignored by pylint due to a false positive:
    https://stackoverflow.com/questions/10300082/how-to-prevent-python-pylint-complaining-about-socket-class-sendall-method
    """

    # Build up connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', tcp_port))

    sock.listen(1)
    conn, addr = sock.accept()
    # pylint: disable=no-member
    data = conn.recv(1024)
    # pylint: enable=no-member

    # Parse values
    content = bytes.decode(data).strip('\n')
    x, y = [x.strip() for x in content.split(';')]
    result = str(int(x) + int(y)) + '\n'

    # Show address
    print('Connected by', addr)

    # pylint: disable=no-member
    conn.send(result.encode())
    # pylint: enable=no-member
    conn.close()


if __name__ == '__main__':
    # Open connection
    open_tcp_connection(read_argument())
