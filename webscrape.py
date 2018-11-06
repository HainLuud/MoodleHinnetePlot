# Source of knowledge  = https://youtu.be/XQgXKtPSzUI
# https://youtu.be/eRSJSKG4mDA
from bs4 import BeautifulSoup as soup
import requests


################################################################################
    # Funktsioon, mis võtab argumendiks kursuse id (nt 2880) ja annab välja kursuse hinnetelehelt saadud protsendid ning kursuse nime
def get_hinded(nimi, url, id):
    produkt = [] # (kursuse nimi, sinu tulemus %, kursuse keskmine %)
    raw_hinded = c.get("https://moodle.ut.ee/grade/report/user/index.php?id="+id)
    hinded_soup = soup(raw_hinded.content, "html.parser")

    lõpphinde_container = hinded_soup.findAll("tr")[-1]
    #.find("td", {"class":"level1 levelodd oddd1 baggt b2b itemcenter column-percentage"})
    
    if lõpphinde_container.find("td", {"class":"level1 levelodd oddd1 baggt b2b itemcenter column-percentage"}) != None:
        sinu_protsent = lõpphinde_container.find("td", {"class":"level1 levelodd oddd1 baggt b2b itemcenter column-percentage"}).text
        kurusse_protsent = lõpphinde_container.find("td", {"class":"level1 levelodd oddd1 baggt b2b itemcenter column-average"}).text

    else: #Kui protsenti pole kirjas
        if lõpphinde_container.find("td", {"class":"level1 levelodd oddd1 baggt b2b itemcenter column-grade"}) != None:
            
            try:
                punktid = float(lõpphinde_container[0].text)  ####Veel töötan selle kallal
                max_punktid = float(lõpphinde_container[1].text[2:])
                kursuse_keskmine = float(lõpphinde_container[2].text)
            except:
                punktid, max_punktid, kursuse_keskmine = "-","-","-"
    

    else:
        punktid, max_punktid, kursuse_keskmine = 0,0,0
        #produkt.append((nimi, punktid, ))"""

    print(nimi)
    print(lõpphinde_container)
    print("\n")
    

    

################################################################################


with requests.Session() as c: #Funktsiooni kutsed peaksid kõik toimuma selle sessiooni jooksul#
    url = "https://moodle.ut.ee/login/index.php"
    L = [44, 84, 97, 108, 108, 83, 104, 105, 112, 115, 82, 97, 99, 101, 115, 46]
    USERNAME = "hainluud" ## Kasutajanimi ja parool vaja sisestada
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

                #print(kursuse_nimi, kursuse_url, kursuse_id)
                get_hinded(kursuse_nimi, kursuse_url, kursuse_id)

    #get_hinded("Programmeerimine (LTAT.03.001)", "https://moodle.ut.ee/grade/report/user/index.php?id=500", "3403")
    
    ################################################################################
    #Matplotlibi programmilõik




    


