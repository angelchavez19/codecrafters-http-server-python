import socket

HOST, PORT = "localhost", 4221

routes = ['/']

methods = {
    200: b'HTTP/1.1 200 OK\r\n\r\n',
    400: b'HTTP/1.1 400 Not Found\r\n\r\n'
}


def main():
    server = socket.create_server((HOST, PORT), reuse_port=True)
    print("Server in port:", PORT)
    conn, address = server.accept()
    print("Connected by:", address)

    data = conn.recv(1024).decode().splitlines()
    print(data[0])

    http_status = data[0].split(' ')
    if http_status[1] in routes:
        conn.sendall(methods.get(200))
    else:
        conn.sendall(methods.get(400))
    conn.close()


if __name__ == "__main__":
    main()
