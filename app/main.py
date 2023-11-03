import socket

HOST, PORT = "localhost", 4221

ROUTES = ['/']


def get_response(code: int) -> bytes:
    responses = {
        200: 'OK',
        400: 'Not Found',
    }
    return f"HTTP/1.1 {code} {responses.get(code)}\r\n\r\n".encode()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print("Server in port:", PORT)
    conn, address = server.accept()
    print("Connected by:", address)

    data = conn.recv(1024).decode().splitlines()
    print(data[0])

    http_status = data[0].split(' ')
    if http_status[1] in ROUTES:
        conn.sendall(get_response(200))
    else:
        conn.sendall(get_response(400))


if __name__ == "__main__":
    main()
