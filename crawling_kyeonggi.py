import urllib.request
from bs4 import BeautifulSoup

def main():   
    url = "http://www.kyeonggi.com/?mod=news&act=articleList&view_type=S&sc_code=1439458030"
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

    list_title = []
    list_summary = []

    for news_title in soup.find_all("div", class_ = "list-titles"):
        list_title.append(news_title.get_text())

    for news_summary in soup.find_all("p", class_ = "list-summary") :
        list_summary.append(news_summary.get_text())

    print(list_title)
    print(list_summary)


if __name__ == "__main__":
    main()
