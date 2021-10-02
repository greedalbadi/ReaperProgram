class Imageinj:
    def Apbytes(self, user_input):
        try:
            main_file = open(user_input[1], 'ab')
            target = open(user_input[2], 'rb')
            main_file.write(target.read())
            main_file.close()
            target.close()
            return "Done."
        except Exception as e:
            return f"ERROR {e}"
    def Restoredata(self, user_input):
        try:
            file = open(user_input[1], 'rb')
            content = file.read()
            content = content.index(bytes.fromhex('FFD9'))
            file.seek(content + 2)
            new_file = open(user_input[2], 'wb')
            new_file.write(file.read())
            return "Done."
        except Exception as e:
            return f"ERROR {e}"
    def Readinj(self, user_input):
        try:
            file = open(user_input[1], 'rb')
            content = file.read()
            content = content.index(bytes.fromhex('FFD9'))
            file.seek(content + 2)
            return file.read()
        except Exception as e:
            return e
