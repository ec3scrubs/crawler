from bs4 import BeautifulSoup

def main():
    fi = open("out.txt")
    soup = BeautifulSoup(fi.read(), 'html.parser')
    content = soup.findAll(class_ = 'entry-content')
    title = soup.findAll(class_ = 'entry-title')
    timestamps = soup.findAll(True, {'class' : {'entry-date', 'published'}})

    posts = []
    for i in xrange(len(content)) :
        c, t, tm = content[i].get_text(), title[i].get_text(), timestamps[i].get_text()
        posts.append([c, t, tm])
    print posts

if __name__ == "__main__":
    main()
