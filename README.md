
# FalconRecon

CTF web enumeration tool

```
___________      .__                        __________
\_   _____/____  |  |   ____  ____   ____   \______   \ ____   ____  ____   ____
 |    __) \__  \ |  | _/ ___\/  _ \ /    \   |       _// __ \_/ ___\/  _ \ /    \
 |     \   / __ \|  |_\  \__(  <_> )   |  \  |    |   \  ___/\  \__(  <_> )   |  \
 \___  /  (____  /____/\___  >____/|___|  /  |____|_  /\___  >\___  >____/|___|  /
     \/        \/          \/           \/          \/     \/     \/           \/

usage: falcon.py [-h] [-u URL] [-r REGEXPATTERN] [-b] [--burp-port BURPPORT] [-w WORDLIST]

CTF web enumeration tool

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     target url
  -r REGEXPATTERN, --regex REGEXPATTERN
                        Set a flag regex
  -b, --burp            Use burpsuite as a proxy
  --burp-port BURPPORT  burp default port
  -w WORDLIST, --wordlist WORDLIST
                        Wordlist for enumeration
  -t THREADS, --threads THREADS
                        Num of threads
```

## Features

- Server fingerprinting
- Directory bruteforce
- Flag regex matching
- Threading! (NEW)

## Demo



![demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnNoenl2OXA3Zm9pN2Zpb3M5MTQzeHFuMWxmc2g2cHFzN2t3NjVtZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GXmdlsDdg8MHiszC9K/giphy.gif)


## Installation



```bash
  git clone https://github.com/casco-di/FalconRecon
  cd FalconRecon
  pip install -r requirements.txt
  python3 falcon.py -u <target> 
```

