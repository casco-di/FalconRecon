import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse

def extract_texts_after_slash(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            soup = BeautifulSoup(content, 'html.parser')
            body_content = soup.find('body').get_text()
            texts_after_slash = [text.split('/')[-1] for text in body_content.split() if '/' in text]
            return texts_after_slash
        else:
            return []
    except Exception as e:
        return []

url = "http://127.0.0.1:5500/index.html"
found_texts = True
while found_texts:
    texts = extract_texts_after_slash(url)
    if not texts:
        print("No more texts found. Exiting loop.")
        found_texts = False
        break
    for text in texts:
        print(f"Text: {text}")
        parsed_url = urlparse(url)
        new_path = "/".join(parsed_url.path.split("/")[:-1]) + "/" + text
        new_url = urlunparse((parsed_url.scheme, parsed_url.netloc, new_path, parsed_url.params, parsed_url.query, parsed_url.fragment))
        try:
            response = requests.get(new_url)
            if response.status_code == 200:
                print("New request successful.")
                url = new_url
            else:
                print(f"Error: Status {response.status_code}")
        except Exception as e:
            print(f"Error processing request for {new_url}: {e}")
    if len(texts) == 1 and response.status_code == 404:
        print("No more texts found. Exiting loop.")
        break
