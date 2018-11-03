# Source of knowledge  = https://youtu.be/XQgXKtPSzUI
# https://youtu.be/eRSJSKG4mDA
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

def KM_hinded():
        raw_page2 = c.get("https://moodle.ut.ee/grade/report/user/index.php?id=2880")
        raw_soup2 = soup(raw_page2.content, "html.parser")
        konteiner = raw_soup2.findAll("td")#, {"headers":"cat_5042_121018 row_43315_121018 grade"}
        print(konteiner)

with requests.Session() as c:
    url = "https://moodle.ut.ee/login/index.php"
    USERNAME = "hainluud"
    L = [44, 84, 97, 108, 108, 83, 104, 105, 112, 115, 82, 97, 99, 101, 115, 46]
    PASSWORD = "".join(chr(i) for i in L) 
    c.get(url)
    login_data = dict(username= USERNAME, password = PASSWORD)
    c.post(url, data=login_data)
    raw_page = c.get("https://moodle.ut.ee/my/")
    #print(raw_page.content)

    raw_soup = soup(raw_page.content, "html.parser")
    #print(raw_soup)

    container = raw_soup.findAll("div", {"class":"box coursebox"})
    #print(container)
    #print(len(container))

    KM_hinded()
    
    #a = raw_soup.find(id="myutcourses")
    #print(a)

    

    


