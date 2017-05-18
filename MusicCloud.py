from tkinter import *
from youtube_dl import YoutubeDL
import os
import webbrowser
import smtplib


def projeler():
    new=1;
    url="www.cetinprojeler.tk";
    webbrowser.open(url,new=new);
    
def indir():
    link=aramayeri.get()
    os.getcwd()
    os.chdir(os.getcwd())

    y_ayar={
        'noplaylist' :True
    }


    ydl = YoutubeDL(y_ayar)
    ydl.add_default_info_extractors()
    info = ydl.extract_info(link, download=True)
    aramayeri.delete(0, "end")

    
def phakkında():
    hak= Toplevel()
    hak.resizable(False, False)
    hak.title("Program Hakkında")
    simge= "music.ico"
    hak.wm_iconbitmap(simge)
    hak.geometry("400x400")
    pha=Label(hak,text="------------------------------------------------",font=("Comic Sans MS",11, "bold"),fg="red")
    pha.pack()
    phak=Label(hak,text="Program Pyhton Programlama Dili İle Geliştirilmiştir.",font=("Comic Sans MS", 11, "bold"))
    phak.pack()
    phak1=Label(hak,text="Program Eren Çetin Tarafından Kodlanmıştır.",font=("Comic Sans MS",11, "bold"))
    phak1.pack()
    phak2=Label(hak,text="-----------------------------------------------",font=("Comic Sans MS",11, "bold"),fg="red")
    phak2.pack()
    phak3=Label(hak,text="İletişim: ctneren2001@gmail.com",font=("Comic Sans MS",11, "bold"))
    phak3.pack()
   

     
    
def face():
    new=1;
    url="https://facebook.com";
    webbrowser.open(url,new=new);
    
def twit():
    new=1;
    url="https://twitter.com";
    webbrowser.open(url,new=new);
def yout():
    new=1;
    url="https://youtube.com";
    webbrowser.open(url,new=new);
def guncel():
    guncel= Toplevel()
    guncel.resizable(False, False)
    guncel.title("Güncelleme")
    simge= "music.ico"
    guncel.wm_iconbitmap(simge)
    guncel.geometry("400x400")
    guncel=Label(guncel,text="------------------------------------------------",font=("Comic Sans MS",11, "bold"),fg="red")
    guncel.pack()
    guncel1=Label(guncel,text="Bir Sonraki Güncellemede Gelecek Özellikler",fg="blue",font=("Comic Sans MS", 11, "bold"))
    guncel1.pack()
    guncel2=Label(guncel,text="İndirme Barı",font=("Comic Sans MS",11, "bold"))
    guncel2.pack()
    guncel3=Label(guncel,text="Çoklu Dil Desteği",font=("Comic Sans MS",11, "bold"))
    guncel3.pack()
    guncel4=Label(guncel,text="Video Kalite Seçeneği",font=("Comic Sans MS",11, "bold"))
    guncel4.pack()
    guncel4=Label(guncel,text="İyileştirmeler",font=("Comic Sans MS",11, "bold"))
    guncel4.pack()
    guncels=Label(guncel,text="-----------------------------------------------",font=("Comic Sans MS",11, "bold"),fg="red")
    guncels.pack()
    
pencere= Tk()



pencere.resizable(False, False)


menu= Menu(pencere)
pencere.config(menu=menu)


subMenu= Menu(menu)
menu.add_cascade(label="Program Hakkında",command=phakkında)
menu.add_cascade(label="Farklı Projeler",command=projeler)

foto= PhotoImage(file= "ekran.png")

etiket= Label(pencere,image=foto)
etiket.pack()

pencere.geometry("600x450")

pencere.title("MusicCloud")

simge= "music.ico"
pencere.wm_iconbitmap(simge)

aramayeri = Entry(fg="#F0501F", bg="#F0F0F0",relief="solid", bd=1 , font=("Helvetica", 12, "bold"),cursor="hand2")
aramayeri.pack()
aramayeri.place(x=150, y=200,width=300 )

#Sosyal Medya

facebook = PhotoImage(file= "facebook.png")
face = Button(image=facebook,height=30,width=30,bg="#F0F0F0",relief="flat",command=face,cursor="hand2")
face.place(x=525,y=50)

twitter = PhotoImage(file= "twitter.png")
twit = Button(image=twitter,height=30,width=30,bg="#F0F0F0",relief="flat",command=twit,cursor="hand2")
twit.place(x=525,y=90)

youtube= PhotoImage(file= "youtube.png")
yout = Button(image=youtube,height=30,width=30,bg="#F0F0F0",relief="flat",command=yout,cursor="hand2")
yout.place(x=525,y=130)


#güncelleme

güncelle=PhotoImage(file= "cloud.png")
gün= Button(image=güncelle,height=30,width=30,bg="#F0F0F0",relief="flat",cursor="hand2",command=guncel)
gün.place(x=15,y=385)

#bayrak
bayrak=PhotoImage(file= "Turkey.png")
flag= Button(image=bayrak,height=30,width=30,bg="#F0F0F0",relief="flat")
flag.place(x=525,y=385)


#Uyarı

uyarıb=Label(text="Uyarı :",fg="red",font=("Comic Sans MS",10))
uyarıb.place(x=130,y=290)

uyarı=Label(text="Link https://youtube.com/ Şeklinde Başlamalıdır.",font=("Comic Sans MS",10))
uyarı.place(x=180,y=290)


indir= Button(text="İndir", command=indir, fg="#F0F0F0",bg="#F0501F" ,relief="ridge", width=20 ,height=1,cursor="hand2",activeforeground="#F0F0F0",activebackground="#FF6633")
indir.pack()
indir.place(x=230, y=250)



sürüm=Label(text="Version 1.0",fg="black")
sürüm.place(x=0,y=430)


yapımcı=Label(text="Made By Eren ÇETİN",fg="black")
yapımcı.place(x=485,y=430)

pencere.mainloop()
