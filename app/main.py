import socket

HOST, PORT = "localhost", 4221

ROUTES = ['/']


def get_response(code: int) -> str:
    responses = {
        200: 'OK',
        404: 'Not Found',
    }
    return f"HTTP/1.1 {code} {responses.get(code)}"


def main():
    # Dev
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    # Deploy
    # server = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Server in port:", PORT)
    conn, address = server.accept()
    print("Connected by:", address)

    data = conn.recv(1024).decode().splitlines()
    print(data[0])

    http_status = data[0].split(' ')
    if http_status[1][0] == '/' and http_status[1][-1] == '/':
        conn.sendall(f"{get_response(200)}\r\n\r\n".encode())
    else:
        param = http_status[1].split('/')[-1]
        response = f"{get_response(200)}\r\nContent-Type: text/plain\r\n" + \
            f"Content-Length: {len(param)}\r\n\r\n{param}"
        conn.sendall(response.encode())


if __name__ == "__main__":
    main()
