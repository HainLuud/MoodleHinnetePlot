from tkinter import *
from PIL import ImageTk,Image
import time
import tkinter.messagebox



#ONCLICK käivita siia tuleb siis link ülejäänud koodile teha
def clicked():
    #Asenda pilt
    viga = jooksuta()

    if not viga:
        #Uuus graaaaaaaafik meeeeeeees
        photo1 = "graafik.png"
        photo1 = ImageTk.PhotoImage(Image.open(photo1))
        vlabel.configure(image=photo1)
        vlabel.image = photo1

#Kutse scriptile
def jooksuta():
    viga = False
    try:
        myvars = {"USERNAME":txt1.get() , "PASSWORD": txt2.get()}
        exec(open("webscrape.py", "r", encoding="UTF-8").read(),myvars)
    except:
        tkinter.messagebox.showinfo("Tähelepanu!", "Sisestasid vale kasutajanime või parooli.")
        viga = True
    
    return viga
#loob akna
window = Tk()
window.geometry('970x600')
window.title("Webscrape projekt")


# loob  alam-aknad
frame_labels = Frame(window, borderwidth="0", relief="ridge") # alam aken vormi jaoks
frame_labels.pack(side=LEFT,padx=50, pady=20)
frame_image = Frame(window, borderwidth="4", relief="ridge") # Pildi jaoks
frame_image.pack(side=LEFT)

#loob alam-alam aken
frame_tekst = Frame(frame_labels, borderwidth="2", relief="ridge") # alam aken vormi jaoks
frame_tekst.pack(side=TOP)
frame_vorm = Frame(frame_labels, borderwidth="0", relief="ridge") # alam aken vormi jaoks
frame_vorm.pack(side=BOTTOM,pady=10)



# Tutvustav tekst
tekst = Label(frame_tekst, text="Tere tulemast! \n Programm on mõeldud selleks,\n et näidata teie hinnete seis \n graafiku kujul. \n  Selleks sisestage oma Moodle \n kasutajanimi ja parool.\n Graafiku loomine võib võtta veits aega!")
tekst.pack(pady=20)


#Vorm
lbl1 = Label(frame_vorm, text="Kasutajanimi:")
txt1 = Entry(frame_vorm,width=30)
lbl2 = Label(frame_vorm, text="Parool")
txt2 = Entry(frame_vorm,width=30, show="*")
lbl1.pack()
txt1.pack()
lbl2.pack()
txt2.pack()


#Nupp
btn = Button(frame_vorm, text="Näita graafikut", command=clicked)
btn.pack()

#Nähtamatu kast et lükata vorm ülespoole
frame_kast = Frame(frame_vorm, borderwidth="0", relief="ridge") # alam aken vormi jaoks
frame_kast.pack(side=BOTTOM,pady=100)

#Graafik
photo = "graafik1.png"
photo = ImageTk.PhotoImage(Image.open(photo))
vlabel=Label(frame_image,image=photo)
vlabel.pack(side=LEFT)


window.mainloop()