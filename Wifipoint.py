import subprocess
class AccessInfo:
    shell = True
    airmon = "airmon-ng"
    StartMonitor = f"sudo {airmon} start "
    StopMonitor = f"sudo {airmon} stop "
    main_command = "mdk3"
    ex_commands = "b -c 1"
class AccessPointGenerat:
    def StartMonitor(self, adaptar_name):
        print("Running Monitor mode..")
        cmd = AccessInfo.StartMonitor + str(adaptar_name)
        command = subprocess.Popen(cmd, shell=AccessInfo.shell, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        command.wait()
        if command.returncode == 0:
            print("Started Monitor mode.")
            return 0
        else:
            print("Monitor mode error.")
            return 1
    def StopMonitor(self, adaptar_name):
        print("Disable Monitor mode..")
        cmd = AccessInfo.StopMonitor + str(adaptar_name)
        command = subprocess.Popen(cmd, shell=AccessInfo.shell, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        command.wait()
        if command.returncode == 0:
            print("Disabled Monitor mode.")
        else:
            print("Monitor mode error.")
    def GenerateAccessPoint(self, adaptar_name, file_path):
        print("Generating access ponts..")
        cmd = f"sudo {AccessInfo.main_command} {adaptar_name}mon {AccessInfo.ex_commands} -f {file_path}"
        command = subprocess.Popen(cmd, shell=True)
        command.wait()
    def Process(self, user_input):
        if str(user_input[1]) == "stop":
            return AccessPointGenerat.StopMonitor(self, user_input[2])
        adaptar_name = user_input[1]
        file_path = user_input[2]
        if int(AccessPointGenerat.StartMonitor(self, adaptar_name)) == 0:
            AccessPointGenerat.GenerateAccessPoint(self, adaptar_name, file_path)
        else:
            print("Quiting command..")