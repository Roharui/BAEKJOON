
from dotenv import load_dotenv

load_dotenv()

import os

from requests import get
from bs4 import BeautifulSoup

user_id = os.environ.get("USER_ID")
cookie = os.environ.get("COOKIE")
# user_id = input("User Id - ")
# cookie = input("Cookie - ")

base = "https://www.acmicpc.net"

url = f"https://www.acmicpc.net/status?user_id={user_id}"

def request(url):
  return BeautifulSoup(get(url, cookies={"OnlineJudge":cookie}).text, "html.parser")

content = request(url)

while True:
  table = content.find("table", id="status-table")

  for tr in table.find_all("tr")[1:]:
    tds = tr.find_all("td")
    ac = "result-ac" in tr.find("td", {"class":"result"}).find("span")["class"]
    if ac:
      link = tds[6].find("a")["href"]

      code_content = request(base + link)

      open(f"problems/{tds[2].text}.py", "w", encoding="utf8").write(code_content.find("textarea").text)
  
  next_page = content.find("a", id="next_page")
  
  if next_page == None:
    break

  content = request(base + next_page["href"])