from tkinter import *
window = Tk()
window.geometry("1000x600")

czcionka = ("Comic Sans MS", 15, "bold")

def submit1():              #obwod trojkata
    value = obwe.get()
    value = value + str("*3")
    value = str(eval(value))
    obw.set(value)

def submit2():              #pole rownolegloboku
    value1 = rwgbae.get()
    value2 = rwgbbe.get()
    value = str(value1) + str("*") + str(value2)
    value = str(eval(value))
    rwgb.set(value)

def submit3():      #pole kola
    value1 = koloe.get()
    value = str("3.14*") + str(value1) + str("**2")
    value = str(eval(value))
    kolo.set(value)

def submit4():      #objetosc prostopadloscianu
    value1 = prstpdlae.get()
    value2 = prstpdlbe.get()
    value3 = prstpdlce.get()
    value = str(value1) + str("*") + str(value2) + str("*") + str(value3)
    value = str(eval(value))
    prstpdl.set(value)

def submit5():          #objetosc kuli
    value1 = kulae.get()
    value = str("4/3*3.14*") + str(value1) + str("**3")
    value = str(eval(value))
    kula.set(value)


obw = StringVar()
obw.set("tu pojawi sie wynik dla obwodu trojkata rownobocznego")
rwgb = StringVar()
rwgb.set("tu pojawi sie wynik dla pola rownolegloboku")
kolo = StringVar()
kolo.set("tu pojawi sie wynik dla pola kola")
prstpdl = StringVar()
prstpdl.set("tu pojawi sie wynik dla objetosci prostopadloscianu")
kula = StringVar()
kula.set("tu pojawi sie wynik dla objetosci kuli")

#trojkat rownoboczny - obwod
label1 = Label(window, textvariable = obw)
obwl = Label(window,text="ponizej wpisz dlugosc boku trojkata rownobocznego:",font=czcionka).grid(row=1,column=1)
obwe = Entry(window,font=(20))
obwb = Button(window,text="oblicz",bg="gray",command=lambda: submit1(), height=3,width=8).grid(row=4,column=1)

#rownoleglobok - pole
label2 = Label(window,textvariable=rwgb)
rwgbal = Label(window,text="ponizej wpisz dlugosc a rownolegloboku",font=czcionka).grid(row=5,column=1)
rwgbae = Entry(window,font=(20))
rwgbbl = Label(window,text="ponizej wpisz dlugosc h rownolegloboku:",font=czcionka).grid(row=7,column=1)
rwgbbe = Entry(window,font=(20))
rwgbbtn = Button(window,text="oblicz",bg="gray",command=lambda: submit2(), height=3,width=8).grid(row=10,column=1)

#kolo - pole
label3 = Label(window,textvariable=kolo)
kolol = Label(window,text="ponizej wpisz dlugosc r kola",font=czcionka).grid(row=11,column=1)
koloe = Entry(window,font=(20))
kolob = Button(window,text="oblicz",bg="gray",command=lambda: submit3(), height=3, width=8).grid(row=14,column=1)

#prostopadloscian - objetosc
label4 = Label(window,textvariable=prstpdl)
prstpdlal = Label(window,text="ponizej wpisz dlugosc a prostopadloscianu",font=czcionka).grid(row=1,column=3)
prstpdlae = Entry(window,font=(20))
prstpdlbl = Label(window,text="ponizej wpisz dlugosc b prostopadloscianu",font=czcionka).grid(row=3,column=3)
prstpdlbe = Entry(window,font=(20))
prstpdlcl = Label(window,text="ponizej wpisz dlugosc c prostopadloscianu",font=czcionka).grid(row=5,column=3)
prstpdlce = Entry(window,font=(20))
prstpdlbtn = Button(window,text="oblicz",bg="gray",command=lambda:submit4(),height=3,width=8).grid(row=7,column=3)

#kula - objetosc
label5 = Label(window,textvariable=kula)
kulal = Label(window,text="ponizej wpisz dlugosc r kuli",font=czcionka).grid(row=9,column=3)
kulae = Entry(window,font=(20))
kulab = Button(window,text="oblicz",bg="gray",command=lambda: submit5(),height=3,width=8).grid(row=12,column=3)

obwe.grid(row=3,column=1)
label1.grid(row=2,column=1)

rwgbae.grid(row=6,column=1)
rwgbbe.grid(row=8,column=1)
label2.grid(row=9,column=1)

koloe.grid(row=13,column=1)
label3.grid(row=12,column=1)

prstpdlae.grid(row=2,column=3)
prstpdlbe.grid(row=4,column=3)
prstpdlce.grid(row=6,column=3)
label4.grid(row=8,column=3)

kulae.grid(row=11,column=3)
label5.grid(row=10,column=3)

rozdzielenie = Label(window,text=".").grid(row=1,column=2,rowspan=15,padx=10)

window.mainloop()