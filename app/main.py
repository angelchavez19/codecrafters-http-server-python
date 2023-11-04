"""A simple HTTP server."""
import argparse
import socket
import threading

from constants.constants import *
from server.server import Request
from router.router import router
from utils.logger import logger


def client_handler(conn, directory_path):
    data = conn.recv(BUFFER_ZISE)
    request = Request(data)
    response = router(request, directory_path)
    logger(response)
    conn.sendall(response.encode())
    conn.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", help="the directory path")
    args = parser.parse_args()
    directory_path = args.directory if args.directory else None

    # Dev
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))

    # Deploy
    # server = socket.create_server(("localhost", 4221), reuse_port=True)
    server.listen()
    print("Server in port:", PORT)

    while True:
        conn, _ = server.accept()
        thread = threading.Thread(
            target=client_handler, args=(conn, directory_path)
        )
        thread.start()


if __name__ == "__main__":
    main()
