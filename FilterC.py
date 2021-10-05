import  RequestsC, SystemC, SocketC, IinjC, moves

class Filter_class:
    def __init__(self):
        self.slay = moves.slay_attack()
        self.files = SystemC.Fiels()
        self.request = RequestsC.RequestsCommands()
        self.imageinj = IinjC.Imageinj()
        self.request_S = RequestsC.RequestsScanners()
        self.system = SystemC.System_Commands()
        self.request_pannel_scanner = RequestsC.Requestportscanner()
        self.sockets = SocketC.SocketCommands()
        self.commands = {
            "cmd": self.system.Cmd,
            "slay": self.slay.Ready,
            "ab": self.imageinj.Apbytes,
            "rs": self.imageinj.Restoredata,
            "rb": self.files.Readbytes,
            "irb": self.imageinj.Readinj,
            'dom': self.request_S.Domainscanner,
            "cls": self.system.Clear,
            "is": self.system.Wordsearch,
            "ping": self.system.Ping,
            "gog": self.sockets.Get_og,
            "bn": self.sockets.Getbanner,
            "scan": self.sockets.PortScanner,
            "gc": self.request.Get_content,
            "ip": self.request.Ipinfo,
            "gh": self.request.Getheaders,
            "gsc": self.request.Getstatuscode,
            "pscan": self.request_pannel_scanner.Panelscanner,
            "gwi": self.sockets.pageip,
            "gs": self.request.Getjsondata,
            "help": self.system.help,
        }
    def Filter(self, user_input):
        try:
            user_input = user_input[0].split()
            commands = self.commands.get(user_input[0])(user_input)
            return commands
        except TypeError:
            return None
