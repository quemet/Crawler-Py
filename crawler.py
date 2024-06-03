import time
import requests
from bs4 import BeautifulSoup

visited_link = set()

def get_data(url: str):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    links = []
    correct_url = res.url[:-1]
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            if href[0] == "/":
                links.append(f"{correct_url}{href}")
            elif href[0] == "h":
                links.append(href)
    return links

links = get_data('https://python.org')

while links:
    link = links.pop(0)
    if link not in visited_link:
        visited_link.add(link)
        print("The current website is " + link)
        print("The number of websites visited is: " + str(len(visited_link)))
        
        try:
            allLinks = get_data(link)
            for new_link in allLinks:
                if new_link not in visited_link and new_link not in links:
                    links.append(new_link)
        except requests.RequestException as e:
            print(f"Request failed for {link}: {e}")
        
        time.sleep(0.5)
