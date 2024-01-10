import requests
import threading
from queue import Queue
from tqdm import tqdm
import re
def worker(queue, http, host, regex, flags, lock, progress):
    while not queue.empty():
        l = queue.get()
        path = f"{host}{l}"
        try:
            res = http.get(path)
            if res.status_code != 404:
                with lock:
                    print(f"[+] /{l} - Status: {res.status_code} ")
                    if regex:
                        finds = re.search(regex, res.text)
                        if finds and finds.group(0) not in flags:
                            flags.append(finds.group(0))
                            print(f"\t Possible flag found -> {finds.group(0)}")
        except requests.exceptions.RequestException:
            print(f"[!] Could not connect to the remote host\nExiting...")
            break
        except KeyboardInterrupt:
            print(f"[!] Keyboard Interrupt detected\nExiting...")
            break
        finally:
            with progress.get_lock():
                progress.update(1)
            queue.task_done()

def dircheck_threaded(http, host, wordlist, regex, num_threads):
    queue = Queue()
    flags = []
    lock = threading.Lock()

    with open(wordlist) as w:
        wordlist = w.readlines()
    
    total_lines = len(wordlist)
    progress = tqdm(total=total_lines, ascii=True)

    for line in wordlist:
        queue.put(line.strip())

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(queue, http, host, regex, flags, lock, progress))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    progress.close()
    return flags

# Example usage
# http = requests.Session()  # Assuming a session object
# host = "http://example.com"
# wordlist = "wordlist.txt"
# regex = "some_regex"
# flags = dircheck_threaded(http, host, wordlist, regex)
# print("Flags found:", flags)

