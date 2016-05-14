from bs4 import BeautifulSoup

def main():
    fi = open("out.txt")
    soup = BeautifulSoup(fi.read(), 'html.parser')
    content = soup.findAll(class_ = 'entry-content')
    title = soup.findAll(class_ = 'entry-title')
    timestamps = soup.findAll(True, {'class' : {'entry-date', 'published'}})
    print len(timestamps), len(title), len(content)

if __name__ == "__main__":
    main()
