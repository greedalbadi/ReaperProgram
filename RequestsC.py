
import requests, SystemC, json, threading
class RequestsCommands:
    def __init__(self):
        self.SystemCommands = SystemC.System_Commands()
    def Get_content(self, user_input):
        try:
            r = requests.get(user_input[1])
            content = r.content
            print(content)
            try:
                if user_input[2] == "save":
                    self.SystemCommands.Save_content(content)
            except IndexError:
                pass
        except Exception as e:
            return e
    def Getheaders(self, user_input):
        try:
            r = requests.get(user_input[1])
            headers = r.headers
            print(
                "\r\n".join("{}: {}".format(k, v) for k, v in r.headers.items())
                  )
            try:
                if user_input[2] == "save":
                    self.SystemCommands.Save_content(headers)
            except IndexError:
                pass
            try:
                if user_input[2] == "search":
                        if user_input[3] in f"{headers}":
                            return f"{user_input[3]} found in headers"
                        else:
                            return f"{user_input[3]} Not found in headers."
            except:
                pass

        except Exception as e:
            print("error")
            return e
    def Ipinfo(self, user_input):
        try:
            ip = user_input[1]
            r = requests.get(f"http://ip-api.com/json/{ip}")
            return json.dumps(r.json(), indent=1)
        except Exception as e:
            return e
    def Getjsondata(self, user_input):
        try:
            r = requests.get(user_input[1])
            data = r.json()
            try:
                if user_input[2] == "save":
                    self.SystemCommands.Save_content(data)
            except IndexError:
                pass
            return json.dumps(data, indent=1)
        except Exception as e:
            return e
    def Getstatuscode(self, user_input):
        try:
            r = requests.get(user_input[1])
            status = r.status_code
            try:
                if user_input[2] == "save":
                    self.SystemCommands.Save_content(f"{status}")
            except IndexError:
                pass
            return status
        except Exception as e:
            return e
class Requestportscanner:
    def __init__(self):
        self.SystemCommands = SystemC.System_Commands()
        self.active_threads = 0
    def Panelscanner(self, user_input):
        print("Panel search started.")
        link = user_input[1]
        try:
            require_threads = user_input[2]
            exists = True
        except IndexError:
            exists = False
        file = open("template/panel.txt")
        for path in file.read().splitlines():
            if not path.startswith("/") and not link.endswith("/"):
                path = "/" + path
                if exists == True:
                    while self.active_threads == int(require_threads):
                        ''
            new_link = link + path
            threading.Thread(target=Requestportscanner.panel, args=[self, new_link, path]).start()
    def panel(self,link, path):
        self.active_threads += 1
        try:
            request = requests.get(url=link, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'})
            status = request.status_code
            if status == 200:
                print(f"[+] Checked: {path} - status: {status}")
                print(self.SystemCommands.Quicksave(request.url))
        except Exception as e:
            print(e)
        self.active_threads = self.active_threads - 1

        if self.active_threads == 0:
            print("Search ended.")




class RequestsScanners:
    def __init__(self):
        self.acive_thread = 0
    def Domainscanner(self, user_input):
        print("Domain search started..")
        try:
            domains = ['.com', '.org', '.net', '.int', '.edu', '.gov', '.mil', '.arpa', '.ac', '.ad', '.ae', '.af', '.ag', '.ai', '.al', '.am', '.ao', '.aq', '.ar', '.as', '.at', '.au', '.aw', '.ax', '.az', '.ba', '.bb', '.bd', '.be', '.bf', '.bg', '.bh', '.bi', '.bj', '.br', '.bs', '.bt', '.bw', '.by', '.bz', '.ca', '.cc', '.cd', '.cf', '.cg', '.ch', '.ci', '.ck', '.cl', '.cm', '.cn', '.co', '.cr', '.cu', '.cv', '.cw', '.cx', '.cy', '.cz', '.de', '.dj', '.dk', '.dm', '.do', '.dz', '.ec', '.ee', '.eg', '.eh', '.er', '.es', '.et', '.eu', '.fj', '.fk', '.fm', '.fo', '.fr', '.ga', '.gd', '.ge', '.gf', '.gg', '.gh', '.gi', '.gl', '.gm', '.gp', '.gq', '.gr', '.gs', '.gt', '.gu', '.gy', '.hk', '.hm', '.hn', '.hr', '.ht', '.hu', '.id', '.ie', '.je', '.jl', '.im', '.in', '.io', '.jq', '.jr', '.js', '.jt', '.je', '.jm', '.jo', '.jp', '.ke', '.kg', '.kh', '.ki', '.km', '.kn', '.kb', '.kr', '.kw', '.ky', '.kz', '.la', '.ld', '.lc', '.li', '.lk', '.lr', '.ls', '.lt', '.lu', '.lv', '.ly', '.ma', '.mc', '.md', '.me', '.mg', '.mh', '.ml', '.mm', '.mn', '.mp', '.mr', '.ms', '.mt', '.ms', '.mr', '.mq', '.mp', '.mo', '.mt', '.mu', '.mv', '.my', '.mw', '.mx', '.my', '.mz', '.na', '.nc', '.ne', '.nf', '.ng', '.ni', '.nl', '.no', '.np', '.nr', '.nu', '.nz', '.om', '.pa', '.pe', '.pf', '.pg', '.ph', '.pk', '.pl', '.pm', '.pn', '.re', '.ro', '.rs', '.ru', '.rw', '.sa', '.sb', '.sc', '.sd', '.sr', '.sg', '.sh', '.si', '.sk', '.sl', '.sm', '.sn', '.so', '.sr', '.ss', '.st', '.su', '.sv', '.sx', '.sy', '.sz', '.tc', '.tf', '.tg', '.tf', '.th', '.tj', '.tk', '.tl', '.tm', '.to', '.tr', '.tt', '.tv', '.tw', '.tz', '.ua', '.ug', '.uk', '.us', '.uy', '.uz', '.va', '.vc', '.ve', '.vg', '.vi', '.vn', '.vu', '.wf', '.ws', '.ye', '.yt', '.za', '.zm', '.zw']

            for domain in domains:
                threading.Thread(target=RequestsScanners.Codscanner, args=[self,user_input[2], user_input[1], domain]).start()
        except Exception as e:
            print(e)
    def Codscanner(self, prot, site, domain):
        self.acive_thread += 1
        try:
            url = f"{prot}://www.{site + domain}"
            request = requests.get(url, timeout=10)
            status = request.status_code
            if status == 200:
                print(f"{domain} - status = {status}")
        except Exception:
            pass
        self.acive_thread = self.acive_thread - 1
        if self.acive_thread == 0:
            print("Search ended.")