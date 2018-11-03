# Source of knowledge  = https://youtu.be/XQgXKtPSzUI
# https://youtu.be/eRSJSKG4mDA
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

"""def KM_hinded():
        raw_page2 = c.get("https://moodle.ut.ee/grade/report/user/index.php?id=2880")
        raw_soup2 = soup(raw_page2.content, "html.parser")
        konteiner = raw_soup2.findAll("td")#, {"headers":"cat_5042_121018 row_43315_121018 grade"}
        print(konteiner)"""

################################################################################
    # Funktsioon, mis võtab argumendiks kursuse id (nt 2880) ja annab välja kursuse hinnetelehelt saadud protsendid ning kursuse nime
    # Hetkel on meile vajalikud id-d [2880, 3403, 500]#

################################################################################


with requests.Session() as c: #Funktsiooni kutsed peaksid kõik toimuma selle sessiooni jooksul#
    url = "https://moodle.ut.ee/login/index.php"
    L = ***REMOVED***
    USERNAME = ***REMOVED*** ## Kasutajanimi ja parool vaja sisestada
    PASSWORD = "".join(chr(i) for i in L) 
    c.get(url)
    login_data = dict(username= USERNAME, password = PASSWORD)
    c.post(url, data=login_data)
    raw_page = c.get("https://moodle.ut.ee/my/")
    #print(raw_page.content)

    raw_soup = soup(raw_page.content, "html.parser") #Muudab puhta html-i supi objektiks ning saame supi funktsioone kasutada (nt findAll)#

    # ################################################################################
    #Programmi lõik mis loeb millistest kursustest võtab inimene osa
    
    container = raw_soup.findAll("div", {"class":"box coursebox"})
    #print(container)

    for div in container:
        new = div.findAll("a")
        for a in new:
            if a.get('title') == None or a.get('title') == "Foorum" or a.get('title') == "Ülesanne":
                pass
            else:
                kursuse_nimi = a.get('title')
                kursuse_url = a.get('href')
                kursuse_id = kursuse_url[kursuse_url.find("=")+1:]

                print(kursuse_nimi, kursuse_url, kursuse_id)
    
    ################################################################################
    #Matplotlibi programmilõik




    


