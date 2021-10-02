import os, datetime, template.banner


class System_Commands:
    def Cmd(self, users_input):
        command = f"{users_input[1]}"
        return os.system(command)
    def Clear(self, *args):
        if os.name == 'nt':
            os.system("cls")

        else:
            os.system('clear ')
        if os.path.isfile("template/banner.py"):
            return template.banner.banner()
    def help(self, *args):
        try:
            help_file = open("template/help.txt", "r")
            return help_file.read()
        except Exception as e:
            return e
    def Ping(self, user_input):
        try:
            browser = user_input[1]
            for i in range(int(user_input[2])):
                os.system(f"ping {browser}")
            return "Ended."
        except Exception as e:
            return e
    def Quicksave(self, content):
        try:
            date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = "".join(date)
            file = open(f"{file_name}.txt", "w")
            file.write(content)
            file.flush()
            file.close()
            return f"Saved as {file.name}"
        except Exception as e:
            return e
    def Save_content(self, content):
        try:
            name = input("Save as: ")
            file = open(name, "w")
            file.write(content)
            file.flush()
            file.close()
            return "Content saved."
        except Exception as e:
            return e
    def Wordsearch(self, users_input):
        try:
            line = 0
            file_name = users_input[1]
            file = open(file_name, "r").read().splitlines()
            for snt in file:
                line += 1
                if users_input[2] in snt:
                    return f"{users_input[2]}\n Found in line {line}\nline: {snt}"
        except Exception as e:
            return e
class Fiels:
    def Readbytes(self, user_input):
        try:
            file_name = user_input[1]
            file = open(file_name, "rb")
            filebytes = file.read()
            file.close()
            return filebytes
        except Exception as e:
            return e