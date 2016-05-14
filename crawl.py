from bs4 import BeautifulSoup
import requests
import re

url = "https://mxchai.wordpress.com"

def remove_ext(ext, arr):
    x = len(ext)
    arr = [a for a in arr if ext not in a['href']]
    return arr

def main():
    r  = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    fo = open("out.txt", "w")
    links = soup.find_all(id = re.compile('post-*'))
    print links
    for link in links:
        fo.write(str(link) + "\n")
    fo.close()


if __name__ == "__main__":
    main()
