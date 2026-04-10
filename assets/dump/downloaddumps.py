import os
import requests

os.makedirs("icons", exist_ok=True)

with open("urls.txt") as f:
    urls = [line.strip() for line in f]

for url in urls:
    filename = url.split("/")[-1]
    path = os.path.join("icons", filename)

    try:
        r = requests.get(url)
        if r.status_code == 200:
            with open(path, "wb") as f:
                f.write(r.content)
            print(f"[+] {filename}")
    except:
        print(f"[!] Failed: {url}")