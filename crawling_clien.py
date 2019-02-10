import urllib.request
from bs4 import BeautifulSoup

def main():
    url = "https://www.clien.net/service/group/community"
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

    list_title = []
    list_nickname = []

    for news_title in soup.find_all("span", class_ = "subject_fixed"):
        list_title.append(news_title.get_text())

    for news_content in soup.find_all("span", class_ = "nickname") :
        list_nickname.append(news_content.get_text())

    print(list_title)
    print(list_nickname)


if __name__ == "__main__":
    main()