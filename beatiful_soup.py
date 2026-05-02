from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/news")
html_content = BeautifulSoup(res.text, "html.parser")

all_spans = html_content.find_all(name="span", class_="titleline")
for span in all_spans:
    a = span.a
    print(a.getText())
    print(a.get("href"))
