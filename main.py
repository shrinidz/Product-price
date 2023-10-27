import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.in/HP-X1000-Wired-Mouse-Black/dp/B009VCGPSY/ref=sr_1_1_sspa?crid=365SWPZ2R65CH&keywords=mouse&qid=1691424073&sprefix=mouse%2Caps%2C224&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())
title = soup.find(id="productTitle").get_text().strip()
print(title)

price = soup.find(class_="a-price-whole").getText()

price_without_dot = price.split(".")

price_as_str = ''.join(price_without_dot[:-1])
price_as_float = float(price_as_str)
print(price_as_float)
BUY_PRICE = 200
YOUR_EMAIL = "codewithshrini52@gmail.com"
YOUR_PASSWORD = "irbordzfsnctdysh"

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price_as_float}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
else:
    print(f"The price {price_as_float} is too high, wait for festival offer. ")
