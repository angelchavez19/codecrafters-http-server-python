import socket

HOST, PORT = "localhost", 4221


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print("Server in port:", PORT)
    conn, address = server.accept()
    print("Connected by:", address)
    conn.recv(1024)
    conn.sendall(b'HTTP/1.1 200 OK\r\n\r\n')


if __name__ == "__main__":
    main()
