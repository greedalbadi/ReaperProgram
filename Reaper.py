import argparse
import Remote
import SocketC
import SystemC
import moves
import rscan
import template.banner, os
import Wifipoint
class Main:
    def __init__(self):
        gap = Wifipoint.AccessPointGenerat()
        ips = rscan.Ip_range_scanner()
        Rdcon = Remote.Rdp_connect()
        Rdcrack = Remote.Rdp_breach()
        socket = SocketC.SocketCommands()
        system = SystemC.System_Commands()
        slay = moves.slay_attack()
        parser = argparse.ArgumentParser()
        parser.add_argument("--gap", action="store_true", help="Generate Fake access point, require [-u, -w]")
        parser.add_argument("--rdcon", action="store_true", help="Remote Desktop Connect, require [-a, -u, p]")
        parser.add_argument("--rdcrack", action="store_true", help="Remote Desktop Brute force, require [-a, -u, -w]")
        parser.add_argument("--ips", action="store_true", help="Scan ip range, require [-a, -r]")
        parser.add_argument("--wip", action="store_true", help="Request web ip, require [-url]")
        parser.add_argument("--fuc", action="store_true", help="require [-a, -port]")
        parser.add_argument("--dos", action="store_true", help="Server dos, require [-a, -port, -th]")
        parser.add_argument("-w", "-f", "--wordlist", help="word list / Password list / file")
        parser.add_argument("-r", "--range", help="Range", type=int)
        parser.add_argument("-th", "--thread", help="Threads", type=int)
        parser.add_argument("-port", "--port", help="Port", type=int)
        parser.add_argument("-url", "--url", help="url")
        parser.add_argument("-a", "--address", help="Ip address / Device name")
        parser.add_argument("-u", "--user", help="username / name")
        parser.add_argument("-p", "--password", help="Password")
        args = parser.parse_args()
        if args.rdcon:
            Rdcon.connect(args.address, args.user, args.password)
        elif args.rdcrack:
            Rdcrack.Cracker(args.address, args.user, args.wordlist)
        elif args.fuc:
            ls = [None, args.address, args.port]
            socket.Focus(ls)
        elif args.dos:
            ls = [None, args.address, args.port, args.thread]
            slay.Ready(ls)
        elif args.wip:
            ls = [None, args.url]
            print(socket.pageip(ls))
        elif args.ips:
            ls = [None, args.address, args.range]
            ips.Filter_info(ls)
        elif args.gap:
            ls = [None, args.user, args.wordlist]
            gap.Process(ls)
if __name__ == "__main__":
    if os.path.isfile("template/banner.py"):
        template.banner.banner()
    Main()

