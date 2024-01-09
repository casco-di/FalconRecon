import requests
from tqdm.auto import tqdm
import re


def dircheck(http, host, wordlist, regex):
    flags = []
    with open(wordlist) as w:
        total_lines = len(w.readlines())
        pass
    with open(wordlist) as wordlist:
        print("\n[+] Starting filesystem bruteforce ", end="")
        if regex:
            print("| flag matching ENABLED")
        else:
            print("| flag matching NOT ENABLED")
        for line in (pbar :=tqdm(wordlist,total=total_lines, ascii=True, position=0, leave=True)):
            l = line.strip()
            path =f"{host}{l}"
            try:
                res = http.get(path)
                # print(res.text)
                pbar.set_description(l)
                if res.status_code != 404:
                    pbar.write(f"[+] /{l} - Status: {res.status_code} ")
                    if regex:
                        finds = re.search(regex, res.text)
                        if finds != None:
                            if finds.group(0) in flags:
                                pass
                            else:
                                flags.append(finds.group(0))
                                pbar.write(f"\t Possible flag found -> {finds.group(0)}")
                        
            except requests.exceptions.RequestException as e:
                print(f"[!] Couldnt connect to the remote host\nExiting...")
                exit(1)
            except KeyboardInterrupt:
                print(f"[!] Keyboard Interrupt detected\nExiting...")
                break
    return flags
