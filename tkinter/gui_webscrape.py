
from tkinter import *
from PIL import ImageTk,Image 
#ONCLICK käivita siia tuleb siis link ülejäänud koodile teha
def clicked():
    #Asenda pilt
    vlabel.configure(image=photo1)

#loob akna
window = Tk()
window.geometry('950x600')
window.title("Webscrape projekt")


# loob  alam-aknad
frame_labels = Frame(window, borderwidth="2", relief="ridge") # alam aken vormi jaoks
frame_labels.pack(side=LEFT,padx=50, pady=20)
frame_image = Frame(window, borderwidth="4", relief="ridge") # Pildi jaoks
frame_image.pack(side=LEFT)


#Vorm
lbl1 = Label(frame_labels, text="Kasutajanimi:")
txt1 = Entry(frame_labels,width=30)
lbl2 = Label(frame_labels, text="Parool")
txt2 = Entry(frame_labels,width=30)
#Kleepimine  aknale
lbl1.pack()
txt1.pack()
lbl2.pack()
txt2.pack()
#Nupp
btn = Button(frame_labels, text="Näita graafikut", command=clicked)
btn.pack()


#Graafik
photo = "graafik1.png"
photo1 = "graafik.png"
photo = ImageTk.PhotoImage(Image.open(photo))
photo1 = ImageTk.PhotoImage(Image.open(photo1))
vlabel=Label(frame_image,image=photo)
vlabel.pack(side=LEFT)






#
window.mainloop()