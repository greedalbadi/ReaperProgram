import subprocess
import threading
import requests
import socket
from prettytable import PrettyTable
import os
from getmac import get_mac_address
class Scan_info:
    shell = True
    Prot = "http://"
    RDP_port = 3389
class Ip_range_scanner:
    def __init__(self):
        self.os = os.name
        self.Activethreads = 0
        self.table = PrettyTable(["Address", "Hostname", "Browser", "RDP", "MAC"])
    def Rdpcheck(self, target, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        conn = s.connect_ex((target, port))
        if (conn == 0):
            return True
        else:
            return False
    def command(self, ip):
        if self.os == "nt":
            return f"ping {ip} -n 1"
        else:
            return f"ping {ip} -c 1"
    def Getmac(self, ip):
        address = get_mac_address(ip=ip)
        return address
    def scanner(self, ip, rang):
        print("Scanning network..")
        ip = ip[:-1]
        for ran in range(int(rang)):
            new_ip = ip + str(ran)
            cmd = Ip_range_scanner.command(self, new_ip)
            threading.Thread(target=Ip_range_scanner.scan, args=[self,cmd, new_ip]).start()
        while int(self.Activethreads) != 0:
            ''
        print(self.table)
    def Gethostname(self, ip):
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            return hostname
        except:
            return None
    def Filter_info(self, user_input):
        ip = user_input[1]
        rang = user_input[2]
        Ip_range_scanner.scanner(self,ip, rang)
    def Checkbrowser(self, ip):
        try:
            requests.get(url=Scan_info.Prot + ip, timeout=5)
            return True
        except:
            return False
    def scan(self, cmd, ip):
        self.Activethreads += 1
        res = subprocess.Popen(cmd, shell=Scan_info.shell,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        res.wait()
        if res.returncode == 0:
            browser = Ip_range_scanner.Checkbrowser(self, ip)
            hostname = Ip_range_scanner.Gethostname(self, ip)
            RDP = Ip_range_scanner.Rdpcheck(self, ip, Scan_info.RDP_port)
            mac = Ip_range_scanner.Getmac(self, ip)
            self.table.add_row([ip, hostname, browser, RDP, mac])
        self.Activethreads -= 1