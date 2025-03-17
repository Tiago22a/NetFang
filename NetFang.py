import argparse
import socket
import subprocess
import sys
import threading

def execute_command(command):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    return output

def handle_client(client_socket, execute):
    if execute:
        output = execute_command(execute)
        client_socket.send(output.encode())
    else:
        while True:
            client_socket.send(b'Netcat Clone> ')
            cmd = client_socket.recv(1024).decode().strip()
            if cmd.lower() in ['exit', 'quit']:
                break
            output = execute_command(cmd)
            client_socket.send(output.encode())
    client_socket.close()

def server_loop(bind_ip, bind_port, execute):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print(f'[*] Listening on {bind_ip}:{bind_port}')
    while True:
        client_socket, addr = server.accept()
        print(f'[*] Accepted connection from {addr[0]}:{addr[1]}')
        client_thread = threading.Thread(target=handle_client, args=(client_socket, execute))
        client_thread.start()

def client_sender(target, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((target, port))
        while True:
            response = client.recv(4096).decode()
            print(response, end='')
            buffer = input() + '\n'
            client.send(buffer.encode())
            if buffer.strip().lower() in ['exit', 'quit']:
                break
    except Exception as e:
        print(f'[*] Exception! Exiting... {e}')
    client.close()

def main():
    parser = argparse.ArgumentParser(description='Netcat Clone')
    parser.add_argument('-t', '--target', help='Target IP')
    parser.add_argument('-p', '--port', type=int, required=True, help='Target Port')
    parser.add_argument('-l', '--listen', action='store_true', help='Listen for incoming connections')
    parser.add_argument('-e', '--execute', help='Execute a command upon connection')
    args = parser.parse_args()

    if args.listen:
        server_loop('0.0.0.0', args.port, args.execute)
    else:
        if not args.target:
            print('Target IP required for client mode.')
            sys.exit(1)
        client_sender(args.target, args.port)

if __name__ == '__main__':
    main()

