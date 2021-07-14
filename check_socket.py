import socket
import os

def checkdata(data):
    if (data == "music"):
        os.system("start C:\\Users\\ADMIN\\Desktop\\ma.lnk")
    elif (data == "stopmusic"):
        os.system("Taskkill  /F /IM main.exe")
        os.system("Taskkill  /F /IM wscript.exe")  
    elif (data == "techtom"):
        os.system("start C:\\Users\\ADMIN\\Desktop\\techtom.mp4")   
    elif (data == "stoptechtom"):
        os.system("Taskkill  /F /IM Video.UI.exe")     
    else:
        return 

HOST = '192.168.1.2' # Thiết lập địa chỉ address
PORT = 8000 # Thiết lập post lắng nghe
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cấu hình kết nối
s.bind((HOST, PORT)) # lắng nghe
s.listen(1) # thiết lập tối ta 1 kết nối đồng thời
conn, addr = s.accept() # chấp nhận kết nối và trả về thông số
with conn:
    try:
        # in ra thông địa chỉ của client
        print('Connected by', addr)
        while True:
            # Đọc nội dung client gửi đến
            data = conn.recv(1024).decode('utf-8').rstrip()
            # Và gửi nội dung về máy khách
            if (data != "exit"):
                # In ra Nội dung 
                print(">> ",data)
                checkdata(data)
                conn.sendall(b'->>OKE<<-')
            else:
                conn.sendall(b'---Good bye---')
                break
            #if not data: # nếu không còn data thì dừng đọc
            #    break
    finally:
        os.system("cls")
        s.close() # đóng socket
        os.system("python check_socket.py") #Khoi dong lai Socket!
        
