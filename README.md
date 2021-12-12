# Reaper tool



##   About.

Reaper program made for penetration testing, The program based on simple structure that anyone could upgrade and use, The current version of the program not completed, This program support linux & windows.









# Commands.

| Title                            | command | arguments                                         | Windows | Linux |
| -------------------------------- | ------- | ------------------------------------------------- | ------- | ----- |
| Get version & title              | v       | None                                              | yes     | yes   |
| Scan ip port's                   | scan    | (ip or site domain) (starting port) (ending port) | yes     | yes   |
| Admin panel finder               | pscan   | (site url) (max thread (optional))                | yes     | yes   |
| Domain scanner                   | dom     | (site name) (site protocol)                       | yes     | yes   |
| Banner finder                    | bn      | (ip) (port)                                       | yes     | yes   |
| Clear console                    | cls     | None                                              | yes     | yes   |
| Control cmd/Terminal             | cmd     | (command)                                         | yes     | yes   |
| Ping a site                      | ping    | (site url) (ping's count)                         | yes     | yes   |
| Request you're ip                | gog     | None                                              | yes     | yes   |
| Request ip info                  | ip      | (ip)                                              | yes     | yes   |
| Request status code              | gsc     | (url) (save (optional))                           | yes     | yes   |
| Request json info                | gs      | (url) (save (optional))                           | yes     | yes   |
| Request header's                 | gh      | (url) (save (optional))                           | yes     | yes   |
| Request content                  | gc      | (url) (save (optional))                           | yes     | yes   |
| Request site ip                  | gwi     | (url)                                             | yes     | yes   |
| Search if word in file           | is      | (file_name) (word)                                | yes     | yes   |
| Read files bytes                 | rb      | (file name)                                       | yes     | yes   |
| Read jpg injection               | irb     | (jpg image name)                                  | yes     | yes   |
| inject jpg image with files      | ab      | (jpg image name) (target file)                    | yes     | yes   |
| DDos                             | slay    | (host) (port) (thread count)                      | yes     | yes   |
| if/ipconfig                      | me      | None                                              | yes     | yes   |
| list network connected mac addr  | mc      | None                                              | yes     | no    |
| Remote Desktop Brute force       | rdcrack | a:(ip or name) u:(user) p:(password list)         | no      | yes   |
| Remote Desktop Connect           | rdcon   | (ip) (user:password)                              | no      | yes   |
| Run shell payload                | payload | f:(file name)                                     | yes     | yes   |
| Generate fake wifi access points | gap     | (adapter name) (wifi title's file(.lst))          | no      | yes   |
| Scan network (ip range scan)     | ips     | (ip) (range)                                      | yes     | yes   |



# Linux installation.

```bash
git clone https://github.com/greedalbadi/ReaperProgram.git
cd ReaperProgram
pip install -r requirements.txt
python3 run.py
```





## Windows installation.

```bash
git clone https://github.com/greedalbadi/ReaperProgram.git
cd ReaperProgram
setup.bat
python run.py
```

This program uses MIT License.





# Reaper argparse.

Faster way to execute commands using terminal.

### Remote Desktop connect

```bash
python3 Reaper.py --rdcon -a 192.168.0.10 -u greedy -p password123
```

##### This command will connect you to the target device.

> -a is the target device ip address or name
>
> -u the device account username
>
> -p the account password



### Remote Desktop BruteForce

```bash
python3 Reaper.py --rdcrack -a 192.168.0.10 -u greedy -w passwords.txt
```

##### This command will execute  Remote Desktop BruteForce on target.

> -a is the target device ip address or name
>
> -u the device account username
>
> -w passwords file



### Generate Fake wifi access points

```bash
python3 Reaper.py --gap -u wlan0 -w names.lst
```

##### This command will generate fake access points.

> -u is you're adapter name
>
> -w fake access points titles file 



### Execute Dos attack

```bash
python3 Reaper.py --dos -a 192.168.0.1 -port 80 -th 1200
```

##### This command will execute a dos attack.

> -a is the target device ip address
>
> -port targeted port 
>
> -th threads count



### Scan ip range scan

```bash
python3 Reaper.py --ips -a 192.168.0.1 -r 250
```

##### This'll scan targeted ip address.

> -a is the target device ip address
>
> -r the range

