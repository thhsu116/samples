"""A TCP server receiving and responding data
"""

import socket


def accept_conn_recv_data(s):
    """
    s : socket handle
    """
    print('wait for connection...')
    conn, addr = s.accept()
    print(f'Connected by {addr}')

    while True:
        data = conn.recv(1024)
        if data:
            print(data)
            print('sending response')
            conn.send(b'\r\nOK\r\n')
            break


if __name__ == '__main__':

    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 4754

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    s.bind((HOST, PORT))
    s.listen(5)
    s.settimeout(10)

    print(f'Server start at: {HOST}:{PORT}')
    accept_conn_recv_data(s)

    s.close()  # need to ensure socket closed before closing the thread
    
