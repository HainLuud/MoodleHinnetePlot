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
        hinded = hinded_soup.findAll("tr")[-3]
        punktid = float(hinded.find("td",{"class":"level2 leveleven item b1b itemcenter column-grade"}).text)
        max_punktid = float(hinded.find("td",{"class":"level2 leveleven item b1b itemcenter column-range"}).text[2:])
        kursuse_keskmine = float(hinded.find("td",{"class":"level2 leveleven item b1b itemcenter column-average"}).text)
        sinu_protsent = str(round((punktid/max_punktid)*100)) + " %"
        kursuse_protsent = str(round((kursuse_keskmine/max_punktid)*100)) + " %"
        del produkt[-1]
        produkt.append((nimi, sinu_protsent, kursuse_protsent))
    
    return produkt

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
    raw_soup = soup(raw_page.content, "html.parser") #Muudab puhta html-i supi objektiks ning saame supi funktsioone kasutada (nt findAll)#

    #################################################################################
    #Programmi lõik mis loeb millistest kursustest võtab inimene osa

    container = raw_soup.findAll("div", {"class":"box coursebox"})
    #print(container)
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

                #print(kursuse_nimi, kursuse_url, kursuse_id)
                kõik_vajalik.append(get_hinded(kursuse_nimi, kursuse_url, kursuse_id))
    print(kõik_vajalik)
    #get_hinded("Programmeerimine (LTAT.03.001)", "https://moodle.ut.ee/grade/report/user/index.php?id=500", "3403")
    
    ################################################################################
    #Matplotlibi programmilõik




    


