import urllib.request
from bs4 import BeautifulSoup

def main():
    url = "http://www.naver.com"

    req = urllib.request.Request(url)
    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source, "html.parser")

    list = []
    for naver_text in soup.find_all("span", class_ = "ah_k"):
        list.append(naver_text.get_text())

    print(list)

if __name__ == "__main__":
    main()