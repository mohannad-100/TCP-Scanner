import socket

target = '10.33.113.17'

print('Scanning host from port 0 to port 1024')

for port in range(0,1024):
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    stat = s.connect_ex((target, port))
    print(stat)
    if(stat == 0):
        print("[+] port: ",port,'--[open]--')
    else:
        print("[-] port: ",port,'--[close]--')
    s.close