import manage, SystemC
class runner_class:
    def __init__(self):
        self.manage = manage.Main_class()
        self.system = SystemC.System_Commands()
    def start(self):
        self.system.Clear()
        self.manage.Main()
if __name__ == "__main__":
    runner_class().start()