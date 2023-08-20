from tkinter import *
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk


root = Tk()
root.geometry('1000x550')
root.title('Pharmacy Gps')
root.iconbitmap('pharmacy.png')
root.configure(background='white')
def elezabypharmacy():
    map = TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=600,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(30.135093621794617, 31.273027473183454)
    map.set_zoom(15)
    marker = map.set_marker(30.135093621794617, 31.273027473183454)
    marker.set_text('elezabypharmacy')

def eltarshoubipharmacy():
    map = TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=600,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(30.79804111207423, 30.99705673180426)
    map.set_zoom(15)
    marker = map.set_marker(30.79804111207423, 30.99705673180426
)
    marker.set_text('eltarshoubipharmacy')

def hishamandfouadpharmacies():
    map = TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=600,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(30.795946057168607, 30.991080642328)
    map.set_zoom(15)
    marker = map.set_marker(30.795946057168607, 30.991080642328
)
    marker.set_text('hishamandfouadpharmacies')



def cu():
    country = En.get()
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_address(country,marker=True)

#------- Title ------

title1 = Label(root, text='PHARMACY GPS',
               fg='white',
               bg='black',
               font=('Tajwal',18),
               )
title1.pack(fill=X)

#------- logo ------


logo = PhotoImage(file='Pharmacists.png')

lab_log = Label(root, image=logo, bd=0, bg='white' ,height=480, width=450, )
lab_log.place(x=30, y=40)

#----- label + entry + button ------
L = Label(root, text='Country:',font=('Tajawal 13'),fg= 'black',bg='white')
L.place(x=10,y=550)

En = Entry(root, font=('Tajawal',14),width=10,bd=2,relief=GROOVE)
En.place(x=80 ,y=550)

b1 = Button(root, text='Get country',
            bg='black',fg='white',bd=1, relief=SOLID,
            width=10 , cursor='hand2',command=cu)
b1.place(x=200,y=550)


#---- PHARMACY BUTTONS----
b= Button(
    root, text='صيدليه العزبى',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal 12'),
    width=13,command=elezabypharmacy
)
b.place(x=10,y=600)
b1= Button(
    root, text='صيدليه الطرشوبى',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal 12'),
    width=13,command=eltarshoubipharmacy
)
b1.place(x=140,y=600)
b2= Button(
    root, text='صيدلية هشام و فؤاد',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal 12'),
    width=13,command=hishamandfouadpharmacies
)
b2.place(x=270,y=600)

map = TkinterMapView(root , width=700, height=500,corner_radius=0)
map.place(x=600,y=45)


root.mainloop()