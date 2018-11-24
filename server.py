import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.103",9000))
while True:
    send_data = input("[+] Client :").encode("utf-8")
    s.send(send_data)
    edata = (s.recv(1024).decode("utf-8"))
    print("[+] Server :",edata)
s.close()
