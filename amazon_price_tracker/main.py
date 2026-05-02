import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

url = "https://appbrewery.github.io/instant_pot/"
page = BeautifulSoup(requests.get(url, headers=header).text, "html.parser")
price = page.find(name="span", class_="a-price-whole").get_text()
fac = page.find(name="span", class_="a-price-fraction").get_text()
price = float(f"{price}{fac}")
print(price)
print(os.environ.get("EMAIL_ADDRESS"))
if price < 80:
    my_email = os.environ.get("EMAIL_ADDRESS")
    my_password = os.environ.get("EMAIL_PASSWORD")
    connection = smtplib.SMTP(os.environ.get("SMTP_ADDRESS"), 587)
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(from_addr= os.environ.get("EMAIL_ADDRESS"),
                        to_addrs="tracy.l@scopicsoftware.com",
                        msg=f"Subject: new price for amazon tracker {price}\n Buy stuff {url}")
    connection.close()