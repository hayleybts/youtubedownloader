import smtplib
import requests
import bs4
import random
base_url = 'http://quotes.toscrape.com/'
res = requests.get(base_url)

soup = bs4.BeautifulSoup(res.text, "lxml")
books = soup.select(".author")

quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)
k = random.choice(quotes)
my_email = exampe@gmail.com"
password = 'example'

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="example@yahoo.com",
                    msg="Subject:Hii\n\n"+(str(k.encode('ascii', errors='ignore'))))
connection.close()
