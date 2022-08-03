from bs4 import BeautifulSoup
import requests

URL = "https://vsedoramy.net/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="movie-cols clearfix")
    dorams = []
    for item in items:
        dorams.append({
            "title": item.find("a").getText(),
            "desc": item.find("div", class_="movie-desc").getText(),
            "year": item.find("div", class_="meta-qual").getText(),
            "link": item.find("a").get("href"),
            # "photo": "https://vsedoramy.net" + item.find("img").get("src")
        })
    return dorams


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = []
        for page in range(1, 3):
            html = get_html(f"{URL}page/{page}/")
            answer.extend(get_data(html.text))
        return answer
    else:
        raise Exception("Error in parser!")
