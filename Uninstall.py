import os

class Main:
    def __init__(self):
        self.paths = [
            "DISCLAIMER",
            "FilterC.py",
            "LICENSE",
            "manage.py",
            "README.md",
            "RequestsC.py",
            "requirements.txt",
            "run.py",
            "SocketC.py",
            "SystemC.py",
            "/template/help.txt",
            "/template/banner.py",
            "/template/panel.txt"
        ]
    def Removeall(self):
        for file in self.paths:
            try:
                os.remove(file)
            except Exception as e:
                print(e)
if __name__ == "__main__":
    o = Main()
    o.Removeall()