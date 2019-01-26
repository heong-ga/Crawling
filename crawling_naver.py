import urllib.request
from bs4 import BeautifulSoup

def main():
    url = "http://www.naver.com"        
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    
    list = []

    for naver_top_search in soup.find_all("span", class_="ah_k"):
        list.append(naver_top_search.get_text())

    print(list)


if __name__ == "__main__":
    main()
