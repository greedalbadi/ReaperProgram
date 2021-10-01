import os, SystemC, FilterC, template.banner
class Main_class:
    def __init__(self):
        self.filter = FilterC.Filter_class()
        self.system = SystemC.System_Commands()
    def Getbanner(self):
        if os.path.isfile("template/banner.py"):
            return template.banner.banner()
        else:
            return "Error: Banner not found."
    def Main(self):
        while True:
            try:
                user_input = [input("")]
                res = self.filter.Filter(user_input)
                if res != None:
                    print(res)
            except:
                pass
