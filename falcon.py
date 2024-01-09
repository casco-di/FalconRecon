import argparse
import os, sys
import requests
from modules.recon import dircheck

banner = """
___________      .__                        __________                            
\_   _____/____  |  |   ____  ____   ____   \______   \ ____   ____  ____   ____  
 |    __) \__  \ |  | _/ ___\/  _ \ /    \   |       _// __ \_/ ___\/  _ \ /    \ 
 |     \   / __ \|  |_\  \__(  <_> )   |  \  |    |   \  ___/\  \__(  <_> )   |  \\
 \___  /  (____  /____/\___  >____/|___|  /  |____|_  /\___  >\___  >____/|___|  /
     \/        \/          \/           \/          \/     \/     \/           \/ 
"""

parser = argparse.ArgumentParser(
    description="CTF web enumeration tool"
)

parser.add_argument(
    "-u", 
    "--url", 
    help="target url"
)

parser.add_argument(
    "-r",
    "--regex",
    dest="regexpattern",
    help="Set a flag regex",
)
parser.add_argument(
    "-b",
    "--burp",
    dest="useproxy",
    action="store_true",
    help="Use burpsuite as a proxy",
)

parser.add_argument(
    "--burp-port", default="8080", dest="burpport",help="burp default port", type=str
)

parser.add_argument(
    "-w",
    "--wordlist",
    dest="wordlist",
    default="wordlists/common.txt",
    type=str,
    help="Wordlist for enumeration"
)

args = parser.parse_args()

burp = {'http': 'http://127.0.0.1:'+args.burpport}

http = requests.Session()
http.headers.update({'User-Agent': 'FalconRecon'})

def fingerprint(host):
    print("[+] Starting initial fingerprint... \n")
    try:
        res = http.get(host)
        print(f"[+] Host: {host}")
        print(f"[+] Server: {res.headers['server']}")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error!! Connection refused by server\nExiting...")
        exit(1)

def main():
    print(banner)
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)
    
    if args.useproxy:
        print("[+] Enabling Burpsuite proxy...")
        http.proxies.update(burp)
    fingerprint(args.url)
    flags = dircheck(http, args.url, args.wordlist, args.regexpattern)
    if args.regexpattern:
        print(f"[+] Total of flags found: {len(flags)}\n[+] Flags: ")
        for flag in flags:
            print(f"\t{flag}")
if __name__ == "__main__":
    main()