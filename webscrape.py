from bs4 import BeautifulSoup as soup
import requests
import re
import lxml.html
from matplot import tulpdiagram

################################################################################
# Funktsioon, mis võtab argumendiks kursuse id ja annab välja kursuse protsendid ning kursuse nime

def get_hinded(nimi, url, id):
    produkt = [] # (kursuse nimi, sinu tulemus %, kursuse keskmine %)
    raw_hinded = c.get("https://moodle.ut.ee/grade/report/user/index.php?id="+id)
    hinded_soup = soup(raw_hinded.content, "html.parser")
    #print(hinded_soup)
    lõpphinde_container = hinded_soup.findAll("tr")[-1]
    
    
    #Proovin leida kursuse protsenti
    if lõpphinde_container.find("td", {"class":"level1 levelodd oddd1 baggt b2b itemcenter column-percentage"}) != None: #Kui on olemas protsent
        sinu_protsent = lõpphinde_container.find("td", {"class":"level1 levelodd oddd1 baggt b2b itemcenter column-percentage"}).text
        kursuse_protsent = lõpphinde_container.find("td", {"class":"level1 levelodd oddd1 baggt b2b itemcenter column-average"}).text
        if ")" in kursuse_protsent:
            kursuse_protsent = kursuse_protsent.split("(")[-1][:len(kursuse_protsent)+1]
        elif "%" not  in kursuse_protsent:
            max_punktid = float(lõpphinde_container.find("td",{"class":"level1 levelodd oddd1 baggt b2b itemcenter column-range"}).text[2:])
            kursuse_protsent = str(round((float(kursuse_protsent)/max_punktid )*100)) + " %"
        produkt.append((nimi, sinu_protsent, kursuse_protsent))

    else: #Kui protsenti pole kirjas
        punktide_var1 = lõpphinde_container.find("td",{"class":"level1 levelodd oddd1 baggt b2b itemcenter column-grade"})
        punktide_var2 = lõpphinde_container.find("td",{"class":"level1 levelodd oddd1 baggt b2b itemcenter gradefail column-grade"})
        if punktide_var1 != None or punktide_var2 != None:
            try:
                if punktide_var1 == None:
                    punktid = float(punktide_var2.text)
                else:
                    punktid = float(punktide_var1.text)

                max_punktid = float(lõpphinde_container.find("td",{"class":"level1 levelodd oddd1 baggt b2b itemcenter column-range"}).text[2:])
                kursuse_keskmine = float(lõpphinde_container.find("td",{"class":"level1 levelodd oddd1 baggt b2b itemcenter column-average"}).text)
                sinu_protsent = (punktid/max_punktid)*100
                kursuse_protsent = (kursuse_keskmine/max_punktid)*100

            except:
                sinu_protsent, kursuse_protsent = "-","-"
                produkt.append((nimi, sinu_protsent, kursuse_protsent))
        else:
            sinu_protsent, kursuse_protsent = "-","-"
            produkt.append((nimi, sinu_protsent, kursuse_protsent))
    
    if nimi == "Programmeerimine (LTAT.03.001)": #Pagana proge ainel on erinevas kohas jooksvad punktid
        hinded = hinded_soup.findAll("tr")[-2]
        punktid = float(hinded.find("td",{"class":"level2 leveleven item b1b itemcenter column-grade"}).text)
        max_punktid = float(hinded.find("td",{"class":"level2 leveleven item b1b itemcenter column-range"}).text[2:])
        kursuse_keskmine = float(hinded.find("td",{"class":"level2 leveleven item b1b itemcenter column-average"}).text)
        sinu_protsent = str(round((punktid/max_punktid)*100)) + " %"
        kursuse_protsent = str(round((kursuse_keskmine/max_punktid)*100)) + " %"
        del produkt[-1]
        produkt.append((nimi, sinu_protsent, kursuse_protsent))
    return produkt

################################################################################
# Filteerimisfunktsioon viimaste muudatuste jaoks

def filtreeri(kõik, mida): #(mida = 0 => kursuse nimi, mida = 1 => sinu %, mida = 2 => kursuse %)
    filtreeritud = []

    if mida == 0:
        for i in kõik:
            a = i[0][0]
            a = a[:a.index("(")-1].upper()
            lühend = ""
            for i in a.split(" "):
                lühend += i[0]
            filtreeritud.append(lühend)

    else:
        for i in kõik:
            a = i[0][mida]
            if a != "-":
                a = float(a.replace("%", "").replace(")","").strip())
            else:
                a = 0
            filtreeritud.append(a)

    return filtreeritud

################################################################################
# Põhiprogrammi osa (sisselogimine, registreeritud kursuste otsimine)

with requests.Session() as c: 
    url = "https://moodle.ut.ee/login/index.php"
    login_page = c.get(url)
    lxml_login_page = lxml.html.fromstring(login_page.content)
    LOGINTOKEN = lxml_login_page.xpath('//input[@name="logintoken"]/@value')[0]
    
    login_data = dict(username= USERNAME, password = PASSWORD, logintoken=LOGINTOKEN)
    c.post(url, data=login_data)
    raw_page = c.get("https://moodle.ut.ee/my/")
    

    raw_soup = soup(raw_page.content, "html.parser") 

    #################################################################################
    #Siin loeb millistest kursustest võtab inimene osa

    container = raw_soup.findAll("div", {"class":"box coursebox"})
    kõik_vajalik = []

    for div in container:
        new = div.findAll("a")
        for a in new:
            if a.get('title') == None or a.get('title') == "Foorum" or a.get('title') == "Ülesanne":
                pass
            else:
                kursuse_nimi = a.get('title')
                kursuse_url = a.get('href')
                kursuse_id = kursuse_url[kursuse_url.find("=")+1:]
                try:
                    kõik_vajalik.append(get_hinded(kursuse_nimi, kursuse_url, kursuse_id))
                except:
                    pass
    
    # Andmete eraldamine eraldi järjenditesse
    
    kõik_sinu_protsendid = filtreeri(kõik_vajalik, 1)
    kõik_kursused = filtreeri(kõik_vajalik, 0)
    kõik_kursuste_protsendid = filtreeri(kõik_vajalik, 2)

################################################################################   
# Matplotlibi programmilõik

tulpdiagram(kõik_sinu_protsendid, kõik_kursuste_protsendid, kõik_kursused)


    


