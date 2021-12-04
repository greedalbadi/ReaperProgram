# Reaper tool



##   About.

Reaper program made for penetration testing, The program based on simple structure that anyone could upgrade and use, The current version of the program not completed, This program support linux & windows.









# Commands.

| Title                           | command | arguments                                         | Windows | Linux |
| ------------------------------- | ------- | ------------------------------------------------- | ------- | ----- |
| Scan ip port's                  | scan    | (ip or site domain) (starting port) (ending port) | yes     | yes   |
| Admin panel finder              | pscan   | (site url) (max thread (optional))                | yes     | yes   |
| Domain scanner                  | dom     | (site name) (site protocol)                       | yes     | yes   |
| Banner finder                   | bn      | (ip) (port)                                       | yes     | yes   |
| Clear console                   | cls     | None                                              | yes     | yes   |
| Control cmd/Terminal            | cmd     | (command)                                         | yes     | yes   |
| Ping a site                     | ping    | (site url) (ping's count)                         | yes     | yes   |
| Request you're ip               | gog     | None                                              | yes     | yes   |
| Request ip info                 | ip      | (ip)                                              | yes     | yes   |
| Request status code             | gsc     | (url) (save (optional))                           | yes     | yes   |
| Request json info               | gs      | (url) (save (optional))                           | yes     | yes   |
| Request header's                | gh      | (url) (save (optional))                           | yes     | yes   |
| Request content                 | gc      | (url) (save (optional))                           | yes     | yes   |
| Request site ip                 | gwi     | (url)                                             | yes     | yes   |
| Search if word in file          | is      | (file_name) (word)                                | yes     | yes   |
| Read files bytes                | rb      | (file name)                                       | yes     | yes   |
| Read jpg injection              | irb     | (jpg image name)                                  | yes     | yes   |
| inject jpg image with files     | ab      | (jpg image name) (target file)                    | yes     | yes   |
| DDos                            | slay    | (host) (port) (thread count)                      | yes     | yes   |
| if/ipconfig                     | me      | None                                              | yes     | yes   |
| list network connected mac addr | mc      | None                                              | yes     | no    |
| Remote Desktop Brute force      | rdcrack | a:(ip or name) u:(user) p:(password list)         | no      | yes   |
| Remote Desktop Connect          | rdcon   | (ip) (user:password)                              | no      | yes   |
| Run shell payload               | payload | f:(file name)                                     | yes     | yes   |



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



## Linux reaper uninstalling.

```
python3 uninstall.py
```



## Windows reaper uninstalling.

```
python uninstall.py
```

This program uses MIT License.
