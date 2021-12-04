import subprocess
class Payload_runner:
    def Valuescheck(self, user_input):
        print("Checking payload..")
        checked = False
        user_input.remove(user_input[0])
        for command in user_input:
            if "f:" in command:
                payload = command.split("f:")[1]
                checked = True
        if checked == True:
            try:
                file = open(payload, "r")
                payload = file.read().splitlines()
                file.close()
            except Exception as e:
                return e
            return Payload_runner.runpayload(self, payload)
        if checked == False:
            return "Please specify payload file using f:(file name)"
    def runpayload(self, payload):
        print("Running payload")
        for line in payload:
            res = subprocess.Popen(
                line,
                shell=True
            )
            res.wait()
        return "Done."
