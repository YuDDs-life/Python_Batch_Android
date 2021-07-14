import socket

HOST = '192.168.1.2'    # Cấu hình address server
PORT = 8000              # Cấu hình Port sử dụng
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cấu hình socket
s.connect((HOST, PORT)) # tiến hành kết nối đến server
inp = "First Point"
while(inp == "exit"): 
    inp = input("(Android) | >> ")
    s.sendall(bytes(inp,'utf-8')) # Gửi dữ liệu lên server 

    data = s.recv(1024).decode('utf-8').rstrip() # Đọc dữ liệu server trả về
    print('Server Respone: ', repr(data))