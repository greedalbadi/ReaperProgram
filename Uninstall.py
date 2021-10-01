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
            "template/help.txt",
            "template/banner.py",
            "template/panel.txt",
            "template/__pycache__/banner.cpython-39.pyc",
            "__pycache__/FilterC.cpython-39.pyc",
            "__pycache__/manage.cpython-39.pyc",
            "__pycache__/NmapC.cpython-39.pyc",
            "__pycache__/RequestsC.cpython-39.pyc",
            "__pycache__/SocketC.cpython-39.pyc",
            "__pycache__/SystemC.cpython-39.pyc",
            "Uninstall.py"
        ]
        self.folders = [
            "template/__pycache__",
            "template",
            "__pycache__"
        ]
    def Removeall(self):
        for file in self.paths:
            try:
                os.remove(file)
                print(f"removed {file}")
            except Exception as e:
                print(e)
        for folder in self.folders:
            try:
                os.rmdir(folder)
                print(f"removed {folder}")
            except Exception as e:
                print(e)
        input('Press "ENTER" to exit : ')
        exit()
if __name__ == "__main__":
    o = Main()
    o.Removeall()