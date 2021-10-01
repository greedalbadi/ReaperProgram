from colorama import Fore as f
import os, json
def Getdisplay():
    try:
        file = open("template/version.json", "r")
        data = json.loads(file.read())
        file.close()
        version = data["data"][0]["version"]
        title = data["data"][0]["title"]
        return [title, f" {version}"]
    except Exception as e:
        print(e)
        return ["Reaper", "v unknown"]
def banner():
    os.system(f"title {Getdisplay()[0]}{Getdisplay()[1]}")
    print(f"""
    {f.LIGHTCYAN_EX}        [+]Github: Greedalbadi
    {f.LIGHTWHITE_EX}                   ...
    {f.LIGHTWHITE_EX}                 ;::::;
    {f.LIGHTWHITE_EX}               ;::::; :;
    {f.LIGHTWHITE_EX}             ;:::::'   :;
    {f.LIGHTWHITE_EX}            ;:::::;     ;.
    {f.LIGHTWHITE_EX}           ,:::::'       ;    {f.RED}       OOO
    {f.LIGHTWHITE_EX}           ::::::;       ;    {f.RED}      OOOOO
    {f.LIGHTWHITE_EX}           ;:::::;       ;    {f.RED}     OOOOOOOO
    {f.LIGHTWHITE_EX}          ,;::::::;     ;'         / {f.RED}OOOOOOO
    {f.LIGHTWHITE_EX}        ;:::::::::`. ,,,;.        /  / {f.RED}DOOOOOO
    {f.LIGHTWHITE_EX}      .';:::::::::::::::::;,     /  /  {f.RED}   DOOOO
    {f.LIGHTWHITE_EX}     ,::::::;::::::;;;;::::;,   /  /    {f.RED}    DOOO
    {f.LIGHTWHITE_EX}    ;`::::::`'::::::;;;::::: ,#/  /     {f.RED}     DOOO
    {f.LIGHTWHITE_EX}    :`:::::::`;::::::;;::: ;::#  /      {f.LIGHTRED_EX}      DOOO
    {f.LIGHTWHITE_EX}    ::`:::::::`;:::::::: ;::::# /       {f.LIGHTRED_EX}       DOO
    {f.LIGHTWHITE_EX}    `:`:::::::`;:::::: ;::::::#/        {f.LIGHTRED_EX}       DOO
    {f.LIGHTWHITE_EX}     :::`:::::::`;; ;:::::::::##        {f.LIGHTRED_EX}        OO
    {f.LIGHTWHITE_EX}     ::::`:::::::`;::::::::;:::#        {f.LIGHTRED_EX}        OO
    {f.LIGHTWHITE_EX}     `:::::`::::::::::::;'`:;::#        {f.LIGHTRED_EX}        O
    {f.LIGHTWHITE_EX}      `:::::`::::::::;' /  / `:#
    {f.LIGHTWHITE_EX}       ::::::`:::::;'  /  /   `#
    
    {f.LIGHTCYAN_EX}    [+]{Getdisplay()[1]}         [+] Help 
    {f.WHITE}
    """)