from bs4 import BeautifulSoup

from fake_useragent import UserAgent

html = "<p>Hello, world!</p>"
soup = BeautifulSoup(html, "html.parser")
print("Output from BeautifulSoup:", soup.p.text)

ua = UserAgent()
print(ua.random)
