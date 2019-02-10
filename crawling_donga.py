import urllib.request
from bs4 import BeautifulSoup

def main():
    list_pagination = []

    for i in range(0, 5):
        url = "http://sports.donga.com/Enter?p=" + str((i * 20) + 1) + "&c=02"
        req = urllib.request.Request(url)
        sourcecode = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
                
        for i in (3, 23):
            list_pagination.append(soup.find_all("span", class_="tit")[i].get_text())

    print(list_pagination)


if __name__ == "__main__":
    main()
