from bs4 import BeautifulSoup
import requests
import smtplib

my_email = "armaanpythontesting@gmail.com"
password = "gwwfwfdkmmfszxfb"

URL = "https://www.amazon.in/gp/product/B00S6JCFB4/ref=ewc_pr_img_3?smid=A9XP90DC1X0F8&psc=1"

HEADERS = {"User-Agent": "Chrome", "Accept-Language": "en-US,en;q=0.9"}

response = requests.get(url=URL, headers=HEADERS)

amazon_website = response.text

soup = BeautifulSoup(amazon_website, "html.parser")

price = float(soup.find(name="span", class_="a-price-whole").get_text())
# print(price.get_text())

if price < 800:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Amazon Price Alert!\n\nSwiss Military Toiletry Bag is now {price}."
                                f"Buy it now. Click- {URL}")

