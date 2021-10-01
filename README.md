# Reaper tool



##   About.

Reaper program made for penetration testing, The program based on simple structure that anyone could upgrade and use, The current version of the program not completed, This program support linux & windows.









# Commands.

| Title               | command | arguments                                         | Windows | Linux |
| ------------------- | ------- | ------------------------------------------------- | ------- | ----- |
| Scan ip port's      | scan    | (ip or site domain) (starting port) (ending port) | yes     | yes   |
| Admin panel finder  | pscan   | (site url) (max thread (optional))                | yes     | yes   |
| Domain scanner      | dom     | (site name) (site protocol)                       | yes     | yes   |
| Banner finder       | bn      | (ip) (port)                                       | yes     | yes   |
| Clear console       | cls     | None                                              | yes     | yes   |
| Control cmd         | cmd     | (command)                                         | yes     | yes   |
| Ping a site         | ping    | (site url) (ping's count)                         | yes     | yes   |
| Request you're ip   | gog     | None                                              | yes     | yes   |
| Request ip info     | ip      | (ip)                                              | yes     | yes   |
| Request status code | gsc     | (url) (save (optional))                           | yes     | yes   |
| Request json info   | gs      | (url) (save (optional))                           | yes     | yes   |
| Request header's    | gh      | (url) (save (optional))                           | yes     | yes   |
| Request content     | gc      | (url) (save (optional))                           | yes     | yes   |
| Request site ip     | gwi     | (url)                                             | yes     | yes   |
|                     |         |                                                   |         |       |

## installation.

```bash
git clone https://github.com/greedalbadi/ReaperProgram.git
cd ReaperProgram
pip install -r requirements.txt
python run.py
```

This program uses MIT License.
