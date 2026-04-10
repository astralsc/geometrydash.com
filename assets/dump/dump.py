import json

with open("data.har", "r", encoding="utf-8") as f:
    data = json.load(f)

urls = []

for entry in data["log"]["entries"]:
    url = entry["request"]["url"]
    if "/assets/icons/" in url:
        urls.append(url)

# remove duplicates
urls = list(set(urls))

with open("urls.txt", "w") as f:
    for url in urls:
        f.write(url + "\n")

print(f"Saved {len(urls)} URLs")