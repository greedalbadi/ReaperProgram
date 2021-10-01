import threading
from socket import *
from IPy import IP
class SocketCommands:
        def __init__(self):
            self.active_thread = 0
        def Get_og(self, *args):
            try:
                s = gethostname()
                s = gethostbyname(s)
                return s
            except Exception as e:
                return e
        def PortScanner(self, user_input):
            try:
                target = SocketCommands.Checkip(self, user_input[1])
                target = gethostbyname(target)
                print('scan started', target)
                for port in range(int(user_input[2]), int(user_input[3])):
                    threading.Thread(target=SocketCommands.Scan, args=[self, port, target]).start()
            except Exception as e:
                return e
        def Scan(self, port, target):
            self.active_thread += 1
            s = socket(AF_INET, SOCK_STREAM)
            conn = s.connect_ex((target, port))
            if (conn == 0):
                print(f'[+]Open port: {port}')
            s.close()
            self.active_thread = self.active_thread - 1
            if self.active_thread == 0:
                print("Search ended.")
        def Checkip(self, ip):
            try:
                IP(ip)
                return ip
            except ValueError:
                return gethostbyname(ip)
            except Exception as e:
                return e

        def Serverec(self, socke):
            try:
                return socke.recv(1024)
            except:
                pass
        def pageip(self, user_input):
            try:
                ip = gethostbyname(user_input[1])
                return f"iP: {ip}"
            except Exception as e:
                return e
        def Getbanner(self, user_input):
            try:
                setdefaulttimeout(2)
                ip = user_input[1]
                port = int(user_input[2])
                s = socket()
                s.connect((ip, port))
                banner = s.recv(1024)
                return banner
            except Exception as e:
                return e