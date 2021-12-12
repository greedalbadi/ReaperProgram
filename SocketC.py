import socket
import threading
import time
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
                self.end = False
                target = SocketCommands.Checkip(self, user_input[1])
                target = gethostbyname(target)
                start_range = user_input[2]
                end_range = user_input[3]
                print('scan started', target)
                for port in range(int(start_range), int(end_range)):
                    if self.end != True:
                        threading.Thread(target=SocketCommands.Scan, args=[self, port, target]).start()
            except Exception as e:
                return e
        def Scan(self, port, target):
            self.active_thread += 1
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(3)
            conn = s.connect_ex((target, port))
            if (conn == 0):
                print(f'[+]Open port: {port}')
            s.close()
            self.active_thread = self.active_thread - 1
            if self.active_thread == 0 and self.end == False:
                self.end = True
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
        def Focus(self, user_input):
            def fuc(user_input):
                try:
                    start = time.time()
                    target = user_input[1]
                    port = user_input[2]
                    print(f"focusing thread started at host: {target}| port: {port}..")
                    while True:
                        try:
                            s = socket(AF_INET, SOCK_STREAM)
                            conn = s.connect_ex((target, int(port)))
                            if (conn == 0):
                                print(f"server: {target} | port: {port} | is live|Focus time {time.time() - start}")
                                break
                        except Exception as e:
                            print(e)
                except Exception as e:
                    return e
            return threading.Thread(target=fuc, args=[user_input]).start()