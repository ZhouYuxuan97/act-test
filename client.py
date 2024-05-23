import socket
from datetime import datetime
import argparse
import sys

def send_message(server_ip, server_port, note):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"{timestamp} - {note}"
    client_socket.sendall(message.encode('utf-8'))
    client_socket.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send a message to the server.')
    parser.add_argument('server_ip', type=str, help='IP address of the server')
    parser.add_argument('server_port', type=int, help='Port of the server')
    parser.add_argument('message', type=str, help='Message to send to the server')
    parser.add_argument('test', type=int, help='Message to send to the server')
    args = parser.parse_args()
    
    if not args.server_ip or not args.server_port or not args.message:
        print("Error: Missing arguments. Usage: python client_push.py <server_ip> <server_port> <message>")
        sys.exit(1)
    print(args.test)
    print(999)
    print("9"+"9"+"9")
    send_message(args.server_ip, args.server_port, args.message)

    # ip = sys.argv[1]
    # port = int(sys.argv[2])
    # note = sys.argv[3]
    # send_timestamp(ip, port, note)
