import socket
from datetime import datetime
import argparse
import sys

def send_timestamp(server_ip, server_port, note):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"{timestamp} - {note}"
    client_socket.sendall(message.encode('utf-8'))
    client_socket.close()

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Send note with timestamp to the server.')
    # parser.add_argument('server_ip', type=str, help='IP address of the server')
    # parser.add_argument('server_port', type=int, help='Port of the server')
    # parser.add_argument('note', type=str, help='Note to send')
    # args = parser.parse_args()

    ip = sys.argv[1]
    port = int(sys.argv[2])
    note = sys.argv[3]
    # send_timestamp(args.server_ip, args.server_port, args.note)
    send_timestamp(ip, port, note)
