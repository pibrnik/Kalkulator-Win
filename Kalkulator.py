# -*- coding: utf-8 -*-

#<editor-fold> Importi
from __future__ import division
import matplotlib
matplotlib.use("TkAgg")

import sys
sys.setrecursionlimit(1000000)
if sys.version_info < (3, 0):
    #Python2
    from Tkinter import *
    import tkinter.ttk as ttk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

else:
    #Python3
    from tkinter import *
    import tkinter.ttk as ttk
    from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


import math
from fractions import Fraction
import time
from numpy import poly1d, isreal
from decimal import Decimal
try:
    import sympy as sp
    from sympy import *
except RuntimeError:
    print("Error")
import numpy as np
import tkinter.messagebox
import tkinter.filedialog
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

#</editor-fold>

polinom = list()
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Definiramo, kreiramo okno
    def init_window(self):

        #Definiranje naslova okna
        self.master.title("Znanstveni kalkulator")

        #Dovoli da se zasede celotno root okno
        self.pack(fill=BOTH, expand=1)

        #Difiniramo frame za zaslon, da se ob spreminjanju velikosti pisave ne spremeni velikost okna
        zaslon_okno = Frame(self, width=330, height=200)
        zaslon_okno.grid(row=1, column=1)
        zaslon_okno.place(x = -4, y = -4)
        zaslon_okno.pack()
        zaslon_okno.grid_propagate(False)

        #Zaslon
        velika_pisava = ('Arial',40)
        mala_pisava = ("Arial", 19)
        najmanjsa_pisava = ("Arial", 8)
        self.izpis = Text(zaslon_okno, state='disabled',height = 2, width = 12, padx=8, background="#cfcfcf", foreground="#575757")
        self.izpis.place(x= -4, y=-1)
        self.izpis.config(font=velika_pisava, state="disabled")


        self.zgodovina = ""
        self.postopek = list()
        self.disk = list()
        self.koncni_rezultat = ""
        self.sprotno = ""

        #Zaslon samo za postopek
        self.postopek_trace = ""
        self.zaslon_postopek = Label(zaslon_okno, text=self.postopek_trace, background="#cfcfcf", foreground="#575757", anchor=W)
        self.zaslon_postopek.place(x=8, y=54)
        self.zaslon_postopek.configure(width=80)

        #Definiramo crto za ulomke
        crta=Frame(zaslon_okno, width=15, height=1, bg="#cfcfcf")
        crta.place(x=0, y=0)

        #Definiramo label za limito
        limita=Label(zaslon_okno, width=15, background="#cfcfcf")
        limita.place(x=-80, y=300)

        #Definiranje opozorila za rejanje Funkcije
        opozorilo_funkcija=Label(self, width=47 ,height=1, background="#f0f0f0", foreground="white")
        opozorilo_funkcija.place(x=0, y=500)





        #Definiraj spremembe zaslona pri pisavah
        def zaslon_minimize():
            self.izpis.config(height=9, width=55, font=najmanjsa_pisava)
        def zaslon_srednji():
            self.izpis.config(height=4, width=30, font=mala_pisava)
        def zaslon_maximize():
            self.izpis.config(height=2, width=12, font=velika_pisava)

        #Definiraj funkcije za funkcije
        def resetfun():

            #Resetiraj aktivne labele
            vnr_label.configure(fg="#cfcfcf")
            xky_label.configure(fg="#cfcfcf")
            cnr_label.configure(fg="#cfcfcf")
            pvnr_label.configure(fg="#cfcfcf")
            pcnr_label.configure(fg="#cfcfcf")
            xnay_label.configure(fg="#cfcfcf")
            logxy_label.configure(fg="#cfcfcf")
            oklepaj_label.configure(fg="#cfcfcf")
            EXP_label.configure(fg="#cfcfcf")
            fun_label.configure(fg="#cfcfcf")

            #Definiraj funkcijsko tipko
            self.funi = 0

            #Resetiraj funkcijsk
            self.vnri = 0
            self.pvnri = 0
            self.cnri = 0
            self.pcnri = 0
            self.xkyi = 0
            self.xnayi = 0
            self.logxyi = 0
            self.desetnaxi = 0
        def opdis():
            #Onemogoci osnovne operacije
            gumb_sestevanje.configure(state="disabled")
            gumb_odstevanje.configure(state="disabled")
            gumb_mnozenje.configure(state="disabled")
            gumb_deljenje.configure(state="disabled")
            gumb_enako.configure(state="disabled")
        def opnrm():
            #Omogoci osnovne operacije
            gumb_sestevanje.configure(state="normal")
            gumb_odstevanje.configure(state="normal")
            gumb_mnozenje.configure(state="normal")
            gumb_deljenje.configure(state="normal")
            gumb_enako.configure(state="normal")
        def fundis():
            #Onemogoci funkcijske tipke med aktivno funckcio
            gumb_fakulteta.configure(state="disabled")
            gumb_koren.configure(state="disabled")
            gumb_kvadrat.configure(state="disabled")
            gumb_sin.configure(state="disabled")
            gumb_cos.configure(state="disabled")
            gumb_tan.configure(state="disabled")
            gumb_cot.configure(state="disabled")
            gumb_log.configure(state="disabled")
            gumb_ln.configure(state="disabled")
            gumb_ex.configure(state="disabled")
            gumb_pow.configure(state="disabled")
            gumb_vbp.configure(state="disabled")
            gumb_vsp.configure(state="disabled")
            gumb_kbp.configure(state="disabled")
            gumb_ksp.configure(state="disabled")
            gumb_pkoren.configure(state="disabled")
            gumb_10x.configure(state="disabled")
            gumb_EXP.configure(state="disabled")
            gumb_obrni.configure(state="disabled")
        def funnrm():
            #Omogoci funkcijske tipke med aktivno funckcio
            gumb_fakulteta.configure(state="normal")
            gumb_koren.configure(state="normal")
            gumb_kvadrat.configure(state="normal")
            gumb_sin.configure(state="normal")
            gumb_cos.configure(state="normal")
            gumb_tan.configure(state="normal")
            gumb_cot.configure(state="normal")
            gumb_log.configure(state="normal")
            gumb_ln.configure(state="normal")
            gumb_ex.configure(state="normal")
            gumb_pow.configure(state="normal")
            gumb_vbp.configure(state="normal")
            gumb_vsp.configure(state="normal")
            gumb_kbp.configure(state="normal")
            gumb_ksp.configure(state="normal")
            gumb_pkoren.configure(state="normal")
            gumb_10x.configure(state="normal")
            gumb_EXP.configure(state="normal")
            gumb_obrni.configure(state="normal")


        self.funi = int()
        self.funi = 0
        def fun():
            self.funi = self.funi + 1
            if self.funi == 1:
                zaslon=self.izpis.get("1.0",END)

                if self.editing_x==False:
                    self.prej,b = zaslon.split("\n")
                print(self.prej)
                l = len(zaslon) - 1
                if l !=0:
                    del self.disk[-l:]
                    #del self.postopek[-l:]
                    postopek_trace()
                pocisti()
                trenutno = ("".join(str(x) for x in self.disk))
                print("Trenutno je", trenutno)
                self.zgodovina = trenutno
                del self.disk[:]
                fun_label.configure(fg="black")
                fun_button.configure(text="Onemogoči funkcije")
                fun2_button.config(state="normal")
                insert_zaslon(self.prej)
                opdis()
                funnrm()



            else:
                self.funi = 0

                fun_label.configure(fg="#cfcfcf")
                fun_button.configure(text="Omogoči funkcije")
                fun2_button.config(state="disabled")
                self.prej=""
                opnrm()
                fundis()

        #2ndF
        self.fun2i = int()
        self.fun2i = 0
        def fun2():
            self.fun2i = self.fun2i + 1

            if self.fun2i == 1:
                gumb_cos.configure(text="acos")
                gumb_sin.configure(text="asin")
                gumb_tan.configure(text="atan")
                gumb_cot.configure(text="acot")
                gumb_fakulteta.configure(text="Sn")
                gumb_ln.configure(text="e")
                gumb_log.configure(text="DMS")
                fun_label.config(text="2ndF")
                gumb_vbp.configure(text="lim")
                fun_button.config(state="disabled")
                gumb_vsp.config(text="∞")
                gumb_kbp.config(text="n")
                gumb_ksp.config(text="x")
            else:
                gumb_cos.configure(text="cos")
                gumb_sin.configure(text="sin")
                gumb_tan.configure(text="tan")
                gumb_cot.configure(text="cot")
                gumb_fakulteta.configure(text="n!")
                gumb_ln.configure(text="ln")
                gumb_log.configure(text="log")
                fun_label.config(text="fun")
                gumb_vbp.config(text="Vnr")
                fun_button.config(state="normal")
                gumb_vsp.configure(text="pVnr")
                gumb_kbp.configure(text="Cnr")
                gumb_ksp.configure(text="pCnr")
                self.fun2i = 0


        def postopek_pobrisi_trenutno():
            a=self.izpis.get("1.0", END)
            pocisti()
            l= len(a)
            del self.postopek[-(l-1):]
        def zgodovina():
            del self.disk[:]
            self.disk.insert(0, self.zgodovina)

        #Pretvori zapis v znanstveni zapis
        self.znanstveni_rezultat = ""
        def znanstveni():
            trenutno = float(self.koncni_rezultat)
            self.znanstveni_rezultat = '%.3E' % trenutno

        #Pretvori nazaj v neznanstvenega
        self.neznanstveni_rezultat = ""
        def neznanstveni():
            trenutno = float(self.koncni_rezultat)
            self.neznanstveni_rezultat = float(trenutno)


        #Izbira radiani oziroma stopinje
        gumb_kot = ttk.Button(self, text="deg ↔ rad", command = lambda: izbira_kota())
        gumb_kot.place(x=233, y=140)
        gumb_kot.config(width="11")
        label_kot = Label(self, text="deg", bg="#cfcfcf", fg="black")
        label_kot.place(x=285, y = 10)
        self.kot = int()
        self.kot = 0
        def izbira_kota():
            self.kot = self.kot + 1

            #Izberemo radiane
            if self.kot % 2 == 1:
                gumb_kot.config(text="rad ↔ deg")
                label_kot.config(text="rad")
            #Izberemo stopinje
            elif self.kot % 2 == 0:
                gumb_kot.config(text="deg ↔ rad")
                label_kot.config(text="deg")
            else:
                print("Error")

        #Funkcije za vnos stevilk in aritmeticnih znakov

        def vnesi(value):
            vnesi_postopek(value)
            insert_zaslon(value)
            if self.editing_x==True:
                self.funkcija.append(value)

        def vnesi_postopek(value):
            self.postopek.append(value)
            postopek_trace()



        #Definiraj matematicne funkcije
        def sestevanje():
            pocisti()
            vnesi("+")
            pocisti()
            self.ulomeki=0
        def mnozenje():
            pocisti()
            vnesi("*")
            pocisti()
            self.ulomeki=0
        def deljenje():
            pocisti()
            vnesi("/")
            pocisti()
            self.ulomeki=0
        def odstevanje():
            self.ulomeki=0
            if self.polinomi>1:
                pocisti()
                vnesi("-")
            else:
                pocisti()
                vnesi("-")
                pocisti()
        def pi():
            vnesi_postopek("π")
            insert_zaslon("3.14159265")
        self.oklepaji=int()
        self.oklepaji=0
        def oklepaj():
            oklepaj_label.config(fg="black")
            self.oklepaji = self.oklepaji + 1
            vnesi("(")
            pocisti()
        self.zaklepaji=int()
        self.zaklepaji=0
        def zaklepaj():
            self.zaklepaji = self.zaklepaji + 1
            if self.editing_x==True:
                vnesi(")")
            else:
                if self.zaklepaji == self.oklepaji:
                    oklepaj_label.config(fg="#cfcfcf")
                    self.oklepaji = 0
                    self.zaklepaji = 0
                vnesi(")")
                pocisti()
                if self.fun2i == 0:
                    r = math.factorial(b)
                    vnesi_postopek("!")
                else:
                    r = ((1+b)*b)/2
                    vnesi_postopek("S")

                self.izpis.configure(state="normal")
                d = len(a)
                pocisti_zaslon()
                zgodovina()

                dolzina = len(str(r))
                n = int()
                n = 6
                if dolzina > n:
                    sci_answer = '%.3E' % r
                    insert_zaslon(sci_answer)
                else:
                    insert_zaslon(r)


        #Funkcija za pretvarjanje razlicnih zapisov
        self.ulomeki = 0
        self.predulomkom = float()
        def ulomek():
            trenutno = self.izpis.get("1.0", END)
            zaslon_srednji()

            self.ulomeki = self.ulomeki + 1

            if self.ulomeki % 2 == 1:
                if self.ulomeki == 1:
                    self.predulomkom = float(trenutno)
                pocisti()
                del self.postopek[:]
                n = Decimal(trenutno)
                r = str((Fraction(n)).limit_denominator(100000))
                a,b = r.split("/", 1)
                presledek="  "
                self.izpis.configure(state='normal')

                #Reguliranje porovnave ulomka
                if len(a)>len(b):
                    l= len(a)
                    razdalja=(len(a)-len(b))/2
                    r1=int(razdalja)
                    if razdalja-r1 == 0:
                        b = presledek*r1 + b
                    else:
                        b = presledek*r1 + " " + b
                    print(razdalja)
                elif len(b)>len(a):
                    l=len(b)
                    razdalja=(len(b)-len(a))/2
                    r1=int(razdalja)
                    if razdalja-r1 == 0:
                        a = presledek*r1 + a
                    else:
                        a = presledek*r1 + " " + a

                    print(razdalja)
                else:
                    l=len(a)
                self.izpis.insert(END, a)
                self.izpis.insert(END, "\n" + b )
                self.izpis.configure(state='disabled')


                #Za risanje ulomka ustvarimo risalno povrsino
                crta.config( bg="#575757", width=l*14)
                crta.place(x=8, y=30)



            else:
                r = self.predulomkom
                pocisti()
                insert_no_count(r)
                zaslon_maximize()
                crta.config(bg="#cfcfcf")
                crta.place(x=0, y=0)
        self.polinom = list()
        self.polinomi = int()
        self.polinomii = int()
        def polinom():
            self.polinomi = self.polinomi + 1
            if self.polinomi == 1:
                self.polinomii = int(self.izpis.get("1.0", END)) + 2
                del self.postopek[:]
                pocisti()

            elif self.polinomi > 1:
                trenutno = self.izpis.get("1.0", END)

                self.polinom.append(trenutno)
                global polinom

                polinom.append(float(trenutno))


                #Vnesi v postopek
                if sys.version_info < (3, 0):
                    #Python2
                    if self.polinomii-self.polinomi == 0:
                        vnesi_postopek("")
                        polinomje()

                    elif self.polinomii-self.polinomi == 1:
                        vnesi_postopek("x + ")
                        gumb_polinom.config(text="n")
                    elif self.polinomii-self.polinomi == 2:
                        vnesi_postopek(("x"+u"\u00B2" + " + ").encode('utf-8').strip())
                        gumb_polinom.config(text="P(x)")
                    elif self.polinomii-self.polinomi == 3:
                        vnesi_postopek(("x"+u"\u00B3" + " + ").encode('utf-8').strip())
                        gumb_polinom.config(text=("P(x"+u"\u00B2" + ")").encode('utf-8').strip())
                    elif self.polinomii-self.polinomi == 4:
                        vnesi_postopek(("x"+u"\u2074" + " + ").encode('utf-8').strip())
                        gumb_polinom.config(text=("P(x"+u"\u00B3" + ")").encode('utf-8').strip())
                    elif self.polinomii-self.polinomi == 5:
                        vnesi_postopek(("x"+u"\u2075" + " + ").encode('utf-8').strip())
                        gumb_polinom.config(text=("P(x"+u"\u2074" + ")").encode('utf-8').strip())
                    elif self.polinomii-self.polinomi == 6:
                        vnesi_postopek(("x"+u"\u2076" + " + ").encode('utf-8').strip())
                        gumb_polinom.config(text=("P(x"+u"\u2075)").encode('utf-8').strip())
                    elif self.polinomii-self.polinomi == 7:
                        vnesi_postopek(("x"+u"\u2077" + " + ").encode('utf-8').strip())
                        gumb_polinom.config(text=("P(x"+u"\u2076" + ")").encode('utf-8').strip())
                    elif self.polinomii-self.polinomi == 8:
                        vnesi_postopek(("x"+u"\u2078" + " + ").encode('utf-8').strip())
                        gumb_polinom.config(text=("P(x"+u"\u2077" + ")").encode('utf-8').strip())
                    elif self.polinomii-self.polinomi == 9:
                        vnesi_postopek(("x"+u"\u2079" + " + ").encode('utf-8').strip())
                        gumb_polinom.config(text=("P(x"+u"\u2078").encode('utf-8').strip())


                else:
                    #Python3
                    if self.polinomii-self.polinomi == 0:
                        polinomje()
                    elif self.polinomii-self.polinomi == 1:
                        vnesi_postopek("x + ")
                        gumb_polinom.config(text="n")
                    elif self.polinomii-self.polinomi == 2:
                        vnesi_postopek("x"+u"\u00B2" + " + ")
                        gumb_polinom.config(text="P(x)")
                    elif self.polinomii-self.polinomi == 3:
                        vnesi_postopek("x"+"\u00B3" + " + ")
                        gumb_polinom.config(text="P(x"+"\u00B2" + ")")
                    elif self.polinomii-self.polinomi == 4:
                        vnesi_postopek("x"+"\u2074" + " + ")
                        gumb_polinom.config(text="P(x"+"\u00B3" + ")")
                    elif self.polinomii-self.polinomi == 5:
                        vnesi_postopek("x"+"\u2075" + " + ")
                        gumb_polinom.config(text="P(x\u2074)")
                    elif self.polinomii-self.polinomi == 6:
                        vnesi_postopek("x\u2076 + ")
                        gumb_polinom.config(text="P(x\u2075)")
                    elif self.polinomii-self.polinomi == 7:
                        vnesi_postopek("x"+"\u2077" + " + ")
                        gumb_polinom.config(text="P(x"+"\u2076" + ")")
                    elif self.polinomii-self.polinomi == 8:
                        vnesi_postopek("x"+"\u2078" + " + ")
                        gumb_polinom.config(text="P(x\u2077)")
                    elif self.polinomii-self.polinomi == 9:
                        vnesi_postopek("x\u2079 + ")
                        gumb_polinom.config(text="P(x\u2078)")


            del self.disk[:]
            pocisti()
            postopek_trace()
        def polinomje():
            pol = (poly1d(self.polinom)).r

            realni = pol[isreal(pol)]
            r = '\n'.join(str(x) for x in realni)
            del self.disk[:]
            pocisti()
            new_window(Window2)
            try:
                zaslon_minimize()
                insert_zaslon("Rešitve (realne):" + "\n" + r)
                #del self.postopek[:]
                #self.izpis.config(font=mala_pisava)
                #insert_postopek("")

                gumb_polinom.config(text="P(n)")
                insert_postopek("")
            except NameError:
                insert_postopek("")
            self.polinomii=0
            self.polinomi=0

            gumb_polinom.config(text="P(n)")
        def fakulteta(b):
            a = self.izpis.get("1.0", END)
            f = float(a)
            try:
                b = int(a)
                try:
                    if self.fun2i == 0:
                        r = math.factorial(b)
                        vnesi_postopek("!")
                    else:
                        r = ((1+b)*b)/2
                        vnesi_postopek("S")

                    self.izpis.configure(state="normal")
                    d = len(a)
                    pocisti_zaslon()
                    zgodovina()
                except ValueError:
                    pocisti_vse()
                    insert_zaslon("Err")
                    insert_postopek("Potrebno je naravno število")
            except ValueError:
                pocisti_vse()
                insert_zaslon("Err")
                vnesi_postopek("Potrebno je naravno število")


            dolzina = len(str(r))
            n = int()
            n = 6
            if dolzina > n:
                sci_answer = '%.3E' % r
                insert_zaslon(sci_answer)
            else:
                insert_zaslon(r)
            fun()
        def k_koren(b):
            a = self.izpis.get("1.0", END)
            b = Decimal(a)
            if self.editing_x==True:
                vnesi_postopek("^0.5")
                insert_zaslon("^0.5")
                self.funkcija.append("^0.5")
            else:
                pocisti()

                c = int(len(a))
                s = str()
                r = math.sqrt(b)
                del self.postopek[-(c-1):]
                postopek_trace()
                vnesi_postopek("√")
                vnesi_postopek(float(a))
                self.izpis.configure(state="normal")
                pocisti_zaslon()
                zgodovina()
                insert_zaslon('{:.{}f}'.format(r, 5 ))
                fun()
        def kvadrat(b):
            a = self.izpis.get("1.0", END)
            if self.editing_x==True:
                self.insert_zaslon("^2")
                if sys.version_info < (3, 0):
                    #Python2
                    print(trenutno)
                    vnesi_postopek((u"\u00B2").encode('utf-8').strip())
                else:
                    vnesi_postopek("\u00B2")
                self.funkcija.append("^2")
            else:
                b = float(a)
                r = b*b
                vnesi_postopek("²")
                self.izpis.configure(state="normal")
                pocisti_zaslon()
                zgodovina()
                insert_zaslon(r)
                fun()
        def sin(b):
            a = self.izpis.get("1.0", END)
            b = float(a)
            l= len(a)
            pocisti()
            del self.postopek[-(l-1):]
            if (self.kot % 2 == 0) or (self.kot == 0):
                if self.fun2i == 1:
                    r = math.degrees(math.asin(b))
                    vnesi_postopek("asin")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi_postopek(")")
                    fun2()
                else:
                    r = math.sin(math.radians(b))
                    vnesi_postopek("sin")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi_postopek("°"+")")
            if self.kot == 1:
                if self.fun2i == 1:
                    r = math.asin(b)
                    vnesi_postopek(" asin")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi_postopek(")")
                    fun2()
                else:
                    r = math.sin(b)
                    vnesi_postopek(" sin")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi("rd)")
            self.izpis.configure(state="normal")
            pocisti_zaslon()
            zgodovina()
            insert_zaslon('{:.{}f}'.format(r, 8 ))
            fun()
        def cos(b):
            a = self.izpis.get("1.0", END)
            b = float(a)
            l= len(a)
            pocisti()
            del self.postopek[-(l-1):]
            if (self.kot % 2 == 0) or (self.kot == 0):
                if self.fun2i == 1:
                    r = math.degrees(math.acos(b))
                    vnesi_postopek("acos")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi_postopek(")")
                    fun2()
                else:
                    r = math.cos(math.radians(b))
                    vnesi_postopek("cos")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi_postopek("°"+")")
            if self.kot == 1:
                if self.fun2i == 1:
                    r = math.acos(b)
                    vnesi_postopek("acos")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi_postopek(")")
                    fun2()
                else:
                    r = math.cos(b)
                    vnesi_postopek("cos")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi("rd)")
            self.izpis.configure(state="normal")
            pocisti_zaslon()
            zgodovina()
            insert_zaslon('{:.{}f}'.format(r, 8 ))
            fun()
        def tan(b):
            a = self.izpis.get("1.0", END)
            b = float(a)
            l= len(a)
            pocisti()
            del self.postopek[-(l-1):]
            if (self.kot % 2 == 0) or (self.kot == 0):
                if self.fun2i == 1:
                    r = math.degrees(math.atan(b))
                    vnesi_postopek("atan")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi_postopek(")")
                    fun2()
                else:
                    r = math.tan(math.radians(b))
                    vnesi_postopek("tan")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi_postopek("°"+")")
            if self.kot == 1:
                if self.fun2i == 1:
                    r = math.atan(b)
                    vnesi_postopek("atan")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi_postopek(")")
                    fun2()
                else:
                    r = math.tan(b)
                    vnesi_postopek("tan")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi("rd)")
            self.izpis.configure(state="normal")
            pocisti_zaslon()
            zgodovina()
            insert_zaslon('{:.{}f}'.format(r, 8 ))
            fun()
        def cot(b):
            a = self.izpis.get("1.0", END)
            b = float(a)
            l= len(a)
            pocisti()
            del self.postopek[-(l-1):]
            self.izpis.configure(state="normal")
            if (self.kot % 2 == 0) or (self.kot == 0):
                if self.fun2i == 1:
                    r = 1/tan(math.degrees(math.asin(b)))
                    vnesi_postopek("acot")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi_postopek(")")
                    fun2()
                else:
                    r = 1/tan(math.sin(math.radians(b)))
                    vnesi_postopek("cot")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi_postopek("°"+")")

            if self.kot == 1:
                if self.fun2i == 1:
                    r = 1/tan(math.asin(b))
                    vnesi_postopek("acot")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi_postopek(")")
                    fun2()
                else:
                    r = 1/tan(math.sin(b))
                    vnesi_postopek("cot")
                    vnesi_postopek("(")
                    vnesi_postopek(float(a))
                    vnesi("rd)")
            pocisti_zaslon()
            zgodovina()
            insert_zaslon('{:.{}f}'.format(r, 8 ))
            fun()
        def ln(b):
            if self.fun2i == 1:
                r = math.e
                vnesi_postopek("e")
                fun2()
            else:
                a = self.izpis.get("1.0", END)
                b = float(a)
                c = len(a)
                r = math.log(b)
                pocisti()
                del self.postopek[-(c-1):]
                vnesi_postopek("ln")
                vnesi_postopek(b)
            self.izpis.configure(state="normal")
            pocisti_zaslon()
            zgodovina()
            insert_zaslon('{:.{}f}'.format(r, 8 ))
            fun()
        def xtomem():
            self.mem = self.izpis.get("1.0", END)
        def xplusmem():
            self.mem = self.izpis.get("1.0", END) + self.mem
        def recallmem():
            vnesi(self.mem)
        def trenutno():

            trenutno.input = self.izpis.get("1.0", END)
        def invert(b):
            a = self.izpis.get("1.0", END)
            b = float(a)
            r = 1/b
            postopek_pobrisi_trenutno()
            self.izpis.configure(state="normal")
            if sys.version_info < (3, 0):
                vnesi_postopek("(")
                vnesi_postopek(b)
                vnesi_postopek((")"+u"\u207B" + u"\u00B9").encode('utf-8').strip())
            else:
                vnesi_postopek("(")
                vnesi_postopek(b)
                vnesi_postopek(")"+"\u207B" + "\u00B9")
            pocisti_zaslon()
            zgodovina()
            insert_zaslon('{:.{}f}'.format(r, 5 ))
        def earse():
            self.izpis.configure(state="normal")
            self.izpis.delete("end-2c")
            del self.disk[:]
            self.disk = self.vracun
        def plusminus():
            a = self.izpis.get("1.0", END)
            b = float(a)
            c = b*(-1)
            l=len(a)
            del self.disk[-(l-1):]
            postopek_pobrisi_trenutno()
            vnesi_postopek("±")
            vnesi_postopek(b)
            pocisti_zaslon()
            insert_zaslon(c)
        def enax(b):
            if self.editing_x==True:
                trenutno = self.izpis.get("1.0", END)
                try:
                    c=int(trenutno)
                except ValueError:
                    c=str(trenutno)
                postopek_pobrisi_trenutno()
                vnesi_postopek("e")
                self.funkcija.append("2.71828183")
                self.funkcija.append("^")
                pocisti()
                if sys.version_info < (3, 0):
                    #Python2


                    if c == 1:
                        vnesi_postopek((u"\u00B9").encode('utf-8').strip())
                    elif c == 2:
                        vnesi_postopek((u"\u00B2").encode('utf-8').strip())
                    elif c == 3:
                        vnesi_postopek((u"\u00B3").encode('utf-8').strip())
                    elif c == 4:
                        vnesi_postopek((u"\u2074").encode('utf-8').strip())
                    elif c == 5:
                        vnesi_postopek((u"\u2075").encode('utf-8').strip())
                    elif c == 6:
                        vnesi_postopek((u"\u2076").encode('utf-8').strip())
                    elif c == 7:
                        vnesi_postopek((u"\u2077").encode('utf-8').strip())
                    elif c== 8:
                        vnesi_postopek((u"\u2078").encode('utf-8').strip())
                    elif c== 9:
                        vnesi_postopek((u"\u2079").encode('utf-8').strip())
                    elif "n" in trenutno:
                        vnesi_postopek((u"\u207F").encode('utf-8').strip())
                    else:
                        vnesi_postopek("^")
                        vnesi_postopek(trenutno)
                        del self.postopek[-2:]

                else:
                    #Python3
                    if c == 1:
                        vnesi_postopek("\u00B9")
                    elif c == 2:
                        vnesi_postopek("\u00B2")
                    elif c == 3:
                        vnesi_postopek("\u00B3")
                    elif c == 4:
                        vnesi_postopek("\u2074")
                    elif c == 5:
                        vnesi_postopek("\u2075")
                    elif c == 6:
                        vnesi_postopek("\u2076")
                    elif c == 7:
                        vnesi_postopek("\u2077")
                    elif c== 8:
                        vnesi_postopek("\u2078")
                    elif c== 9:
                        vnesi_postopek("\u2079")
                    elif  "n" in trenutno:
                        vnesi_postopek("\u207F")
                    else:
                        vnesi_postopek("^")
                        vnesi_postopek(trenutno)
                        del self.postopek[-2:]
            else:
                trenutno = self.izpis.get("1.0", END)
                c = float(trenutno)
                r = math.exp(c)
                pocisti()
                postopek_pobrisi_trenutno()
                vnesi_postopek("e")
                if sys.version_info < (3, 0):
                    #Python2

                    if c == 1:
                        vnesi_postopek((u"\u00B9").encode('utf-8').strip())
                    elif c == 2:
                        vnesi_postopek((u"\u00B2").encode('utf-8').strip())
                    elif c == 3:
                        vnesi_postopek((u"\u00B3").encode('utf-8').strip())
                    elif c == 4:
                        vnesi_postopek((u"\u2074").encode('utf-8').strip())
                    elif c == 5:
                        vnesi_postopek((u"\u2075").encode('utf-8').strip())
                    elif c == 6:
                        vnesi_postopek((u"\u2076").encode('utf-8').strip())
                    elif c == 7:
                        vnesi_postopek((u"\u2077").encode('utf-8').strip())
                    elif c== 8:
                        vnesi_postopek((u"\u2078").encode('utf-8').strip())
                    elif c== 9:
                        vnesi_postopek((u"\u2079").encode('utf-8').strip())
                    else:
                        del self.postopek[-1:]
                        vnesi_postopek("e^")
                        vnesi_postopek(c)

                else:
                    #Python3
                    if c == 1:
                        vnesi_postopek("\u00B9")
                    elif c == 2:
                        vnesi_postopek("\u00B2")
                    elif c == 3:
                        vnesi_postopek("\u00B3")
                    elif c == 4:
                        vnesi_postopek("\u2074")
                    elif c == 5:
                        vnesi_postopek("\u2075")
                    elif c == 6:
                        vnesi_postopek("\u2076")
                    elif c == 7:
                        vnesi_postopek("\u2077")
                    elif c== 8:
                        vnesi_postopek("\u2078")
                    elif c== 9:
                        vnesi_postopek("\u2079")
                    else:
                        del self.postopek[-1:]
                        vnesi_postopek("e^")
                        vnesi_postopek(c)
                R=0
                self.izpis.configure(state="normal")
                pocisti_zaslon()
                zgodovina()
                insert_zaslon('{:.{}f}'.format(r, 3 ))
        self.xnay=""
        self.xnayi = int()
        self.xnayi = 0
        def xnay():
            if self.editing_x==True:
                self.xnayi += 1
                if self.xnayi==1:
                    self.funkcija.append("^")
                    pocisti()
                else:
                    trenutno=self.izpis.get("1.0",END)
                    try:
                        c=int(trenutno)
                    except ValueError:
                        c=str(trenutno)
                    postopek_pobrisi_trenutno()
                    if sys.version_info < (3, 0):
                        #Python2
                        print(trenutno)

                        if c == 1:
                            vnesi_postopek((u"\u00B9").encode('utf-8').strip())
                        elif c == 2:
                            vnesi_postopek((u"\u00B2").encode('utf-8').strip())
                        elif c == 3:
                            vnesi_postopek((u"\u00B3").encode('utf-8').strip())
                        elif c == 4:
                            vnesi_postopek((u"\u2074").encode('utf-8').strip())
                        elif c == 5:
                            vnesi_postopek((u"\u2075").encode('utf-8').strip())
                        elif c == 6:
                            vnesi_postopek((u"\u2076").encode('utf-8').strip())
                        elif c == 7:
                            vnesi_postopek((u"\u2077").encode('utf-8').strip())
                        elif c== 8:
                            vnesi_postopek((u"\u2078").encode('utf-8').strip())
                        elif c== 9:
                            vnesi_postopek((u"\u2079").encode('utf-8').strip())
                        elif "n" in trenutno:
                            vnesi_postopek((u"\u207F").encode('utf-8').strip())
                        else:
                            vnesi_postopek("^")
                            vnesi_postopek(trenutno)
                            del self.postopek[-2:]

                    else:
                        #Python3
                        if c == 1:
                            vnesi_postopek("\u00B9")
                        elif c == 2:
                            vnesi_postopek("\u00B2")
                        elif c == 3:
                            vnesi_postopek("\u00B3")
                        elif c == 4:
                            vnesi_postopek("\u2074")
                        elif c == 5:
                            vnesi_postopek("\u2075")
                        elif c == 6:
                            vnesi_postopek("\u2076")
                        elif c == 7:
                            vnesi_postopek("\u2077")
                        elif c== 8:
                            vnesi_postopek("\u2078")
                        elif c== 9:
                            vnesi_postopek("\u2079")
                        elif  "n" in trenutno:
                            vnesi_postopek("\u207F")
                        else:
                            vnesi_postopek("^")
                            vnesi_postopek(trenutno)
                            del self.postopek[-2:]


            else:
                self.xnayi = self.xnayi + 1
                xnay_label.config(fg="black")
                fundis()
                gumb_pow.configure(state="normal")
                if self.xnayi == 2:
                    b = self.izpis.get("1.0", END)
                    c = int(b)
                    d = float(self.xnay)
                    r = d**c

                    xnay_label.config(fg="#cfcfcf")
                    postopek_pobrisi_trenutno()
                    pocisti()
                    zgodovina()
                    self.xnay = ""
                    self.xnayi = 0
                    dolzina = len(str(r))
                    n = int()
                    n = 6
                    if dolzina > n:
                        sci_answer = '%.3E' % float(r)
                        insert_zaslon(sci_answer)
                    else:
                        insert_zaslon(r)

                    #Vnesi v postopek
                    vnesi_postopek(d)
                    if sys.version_info < (3, 0):
                        #Python2

                        if c == 1:
                            vnesi_postopek((u"\u00B9").encode('utf-8').strip())
                        elif c == 2:
                            vnesi_postopek((u"\u00B2").encode('utf-8').strip())
                        elif c == 3:
                            vnesi_postopek((u"\u00B3").encode('utf-8').strip())
                        elif c == 4:
                            vnesi_postopek((u"\u2074").encode('utf-8').strip())
                        elif c == 5:
                            vnesi_postopek((u"\u2075").encode('utf-8').strip())
                        elif c == 6:
                            vnesi_postopek((u"\u2076").encode('utf-8').strip())
                        elif c == 7:
                            vnesi_postopek((u"\u2077").encode('utf-8').strip())
                        elif c== 8:
                            vnesi_postopek((u"\u2078").encode('utf-8').strip())
                        elif c== 9:
                            vnesi_postopek((u"\u2079").encode('utf-8').strip())
                        else:
                            vnesi_postopek("ˆ")
                            vnesi_postopek(float(c))



                    else:
                        #Python3
                        if c == 1:
                            vnesi_postopek("\u00B9")
                        elif c == 2:
                            vnesi_postopek("\u00B2")
                        elif c == 3:
                            vnesi_postopek("\u00B3")
                        elif c == 4:
                            vnesi_postopek("\u2074")
                        elif c == 5:
                            vnesi_postopek("\u2075")
                        elif c == 6:
                            vnesi_postopek("\u2076")
                        elif c == 7:
                            vnesi_postopek("\u2077")
                        elif c== 8:
                            vnesi_postopek("\u2078")
                        elif c== 9:
                            vnesi_postopek("\u2079")
                        else:
                            vnesi_postopek("ˆ")
                            vnesi_postopek(float(c))
                    fun()
                if self.xnayi == 1:
                    self.xnay = self.izpis.get("1.0", END)
                    postopek_pobrisi_trenutno()
                    pocisti()
        self.vnr=""
        self.vnri = int()
        self.vnri = 0
        self.limitai = 0
        self.meja=""
        #vnr+limita
        def vnr():
            if self.fun2i==0:
                self.vnri = self.vnri + 1
                vnr_label.config(fg="black")
                fundis()
                gumb_vbp.configure(state="normal")
                if self.vnri == 2:
                    b = self.izpis.get("1.0", END)
                    c = int(b)
                    d = int(self.vnr)
                    r = math.factorial(d)/(math.factorial(d - c))
                    vnr_label.config(fg="#cfcfcf")
                    pocisti()
                    zgodovina()
                    self.vnr = ""
                    self.vnri = 0
                    dolzina = len(str(r))
                    n = int()
                    n = 6
                    if dolzina > n:
                        sci_answer = '%.3E' % r
                        insert_zaslon(sci_answer)
                    else:
                        insert_zaslon(r)
                    fun()
                if self.vnri == 1:
                    self.vnr = self.izpis.get("1.0", END)
                    vnesi_postopek("V")
                    pocisti()
            else:
                self.limitai=self.limitai +1
                meja=str()
                if self.limitai == 3:
                    simbol = sp.symbols("n")
                    izraz = ("".join(str(x) for x in self.funkcija))
                    postopek = ("".join(str(x) for x in self.postopek))
                    inf = float("inf")
                    try:
                        r= sp.limit(izraz,simbol,float(self.meja))
                        if str(r)=="oo":
                            r="∞"
                    except SympifyError:
                        pocisti_vse()
                        insert_zaslon("Err")
                        vnesi_postopek("Napaka pri zapisu funkcije")
                    except RuntimeError:
                        r= sp.limit(izraz,simbol,float(self.meja))
                    if "Inf" in self.meja:
                        meja="∞"
                    else:
                        meja = self.meja
                    pocisti_vse()
                    zaslon_srednji()
                    insert_zaslon("lim(" + str(postopek) + ") = "+ str(r))
                    limita.place(x=6, y=27)
                    limita.config(text="n→ " + meja,foreground="#575757", anchor=W)
                    #vnesi_postopek("x -> ∞")
                    fun2()
                    fun()
                    fundis()
                    fun_button.config(text="Omogoči funkcije")
                if self.limitai == 2:
                    self.meja=self.izpis.get("1.0", END)
                    postopek_pobrisi_trenutno()
                    pocisti()
                    editing_x()
                    limita.place(x=6, y=27)
                    if "Inf" in self.meja:
                        meja="∞"
                    else:
                        meja = self.meja
                    limita.config(text="n→ " + meja,foreground="#575757", anchor=W)
                if self.limitai == 1:
                    limita.place(x=6, y=27)
                    limita.config(text="n→",foreground="#575757", anchor=W)
                    zaslon_srednji()



        #OKOLJE ZA UREJANJE FUNKCIJE
        self.editing_x=False
        self.funkcija = list()
        def editing_x():
            #Omogocimmo okolje za urejanje funkcij
            self.editing_x=True
            del self.funkcija[:]
            #Onemogocimo dolocene Funkcije
            gumb_fakulteta.configure(state="disabled")
            gumb_sin.configure(state="disabled")
            gumb_cos.configure(state="disabled")
            gumb_tan.configure(state="disabled")
            gumb_cot.configure(state="disabled")
            gumb_vsp.configure(state="disabled")
            gumb_kbp.configure(state="disabled")
            gumb_ksp.configure(state="disabled")
            gumb_10x.configure(state="disabled")
            gumb_EXP.configure(state="disabled")
            gumb_obrni.configure(state="disabled")
            gumb_mnozenje.configure(state="normal")
            gumb_deljenje.configure(state="normal")
            gumb_sestevanje.configure(state="normal")
            gumb_odstevanje.configure(state="normal")
            #Prikazemo opozorilo_funkcija
            opozorilo_funkcija.config(text="Urejanje funkcije", background="#ab3030")

        self.pvnr=""
        self.pvnri = int()
        self.pvnri = 0
        def pvnr():
            if self.fun2i==1:
                inf=float("inf")
                vnesi(inf)
            else:
                self.pvnri = self.pvnri + 1
                pvnr_label.config(fg="black")
                fundis()
                gumb_vsp.configure(state="normal")
                if self.pvnri == 2:
                    b = self.izpis.get("1.0", END)
                    c = int(b)
                    d = int(self.pvnr)
                    r = d**c
                    pvnr_label.config(fg="#cfcfcf")
                    pocisti()
                    zgodovina()
                    self.pvnr = ""
                    self.pvnri = 0
                    dolzina = len(str(r))
                    n = int()
                    n = 6
                    if dolzina > n:
                        sci_answer = '%.3E' % r
                        insert_zaslon(sci_answer)
                    else:
                        insert_zaslon(r)
                    fun()
                if self.pvnri == 1:
                    self.pvnr = self.izpis.get("1.0", END)
                    vnesi_postopek("pV")
                    pocisti()
        self.cnr=""
        self.cnri = int()
        self.cnri = 0
        def cnr():
            self.cnri = self.cnri + 1
            cnr_label.config(fg="black")
            fundis()
            gumb_kbp.configure(state="normal")
            if self.cnri == 2:
                b = self.izpis.get("1.0", END)
                c = int(b)
                d = int(self.cnr)
                r = math.factorial(d)/(math.factorial(d - c)*math.factorial(c))
                cnr_label.config(fg="#cfcfcf")
                pocisti()
                zgodovina()
                self.cnr = ""
                self.cnri = 0
                dolzina = len(str(r))
                n = int()
                n = 6
                if dolzina > n:
                    sci_answer = '%.3E' % r
                    insert_zaslon(sci_answer)
                else:
                    insert_zaslon(r)
                fun()
            if self.cnri == 1:
                self.cnr = self.izpis.get("1.0", END)
                vnesi_postopek("C")
                pocisti()
        self.pcnr=""
        self.pcnri = int()
        self.pcnri = 0
        def pcnr():
            if self.fun2i==1:
                vnesi("x")
            else:
                self.pcnri = self.pcnri + 1
                pcnr_label.config(fg="black")
                fundis()
                gumb_ksp.configure(state="normal")
                if self.pcnri == 2:
                    b = self.izpis.get("1.0", END)
                    c = int(b)
                    d = int(self.pcnr)
                    r = math.factorial(d + c - 1)/(math.factorial(d - 1)*math.factorial(c))
                    pcnr_label.config(fg="#cfcfcf")
                    pocisti()
                    zgodovina()
                    self.pcnr = ""
                    self.pcnri = 0
                    dolzina = len(str(r))
                    n = int()
                    n = 6
                    if dolzina > n:
                        sci_answer = '%.3E' % r
                        insert_zaslon(sci_answer)
                    else:
                        insert_zaslon(r)
                    fun()
                if self.pcnri == 1:
                    self.pcnr = self.izpis.get("1.0", END)
                    vnesi_postopek("pC")
                    pocisti()
        self.xky=""
        self.xkyi = int()
        self.xkyi = 0
        def xky():
            self.xkyi = self.xkyi + 1
            if self.editing_x==True:
                if self.xkyi==1:
                    self.xky=self.izpis.get("1.0",END)
                    print(self.xky)
                    postopek_pobrisi_trenutno()
                    pocisti()
                    self.funkcija.append("^1/")
                else:
                    trenutno=self.izpis.get("1.0",END)
                    try:
                        c=int(trenutno)
                    except ValueError:
                        c=str(trenutno)
                    postopek_pobrisi_trenutno()
                    if sys.version_info < (3, 0):
                        #Python2

                        if c == 1:
                            vnesi_postopek((u"\u00B9").encode('utf-8').strip())
                        elif c == 2:
                            vnesi_postopek((u"\u00B2").encode('utf-8').strip())
                        elif c == 3:
                            vnesi_postopek((u"\u00B3").encode('utf-8').strip())
                        elif c == 4:
                            vnesi_postopek((u"\u2074").encode('utf-8').strip())
                        elif c == 5:
                            vnesi_postopek((u"\u2075").encode('utf-8').strip())
                        elif c == 6:
                            vnesi_postopek((u"\u2076").encode('utf-8').strip())
                        elif c == 7:
                            vnesi_postopek((u"\u2077").encode('utf-8').strip())
                        elif c== 8:
                            vnesi_postopek((u"\u2078").encode('utf-8').strip())
                        elif c== 9:
                            vnesi_postopek((u"\u2079").encode('utf-8').strip())
                        elif "n" in trenutno:
                            postopek_pobrisi_trenutno()
                            vnesi_postopek((u"\u207F").encode('utf-8').strip())
                        else:
                            vnesi_postopek(c)

                    else:
                        #Python3
                        if c == 1:
                            vnesi_postopek("\u00B9")
                        elif c == 2:
                            vnesi_postopek("\u00B2")
                        elif c == 3:
                            vnesi_postopek("\u00B3")
                        elif c == 4:
                            vnesi_postopek("\u2074")
                        elif c == 5:
                            vnesi_postopek("\u2075")
                        elif c == 6:
                            vnesi_postopek("\u2076")
                        elif c == 7:
                            vnesi_postopek("\u2077")
                        elif c== 8:
                            vnesi_postopek("\u2078")
                        elif c== 9:
                            vnesi_postopek("\u2079")
                        elif "n" in trenutno:
                            vnesi_postopek("\u207F")
                        else:
                            vnesi_postopek(c)
                    vnesi_postopek("√")
                    try:
                        vnesi_postopek(float(self.xky))
                    except ValueError:
                        pocisti_vse()
                        vnesi("Err")
                        vnesi_postopek("Neustrezno število")
            else:
                xky_label.config(fg="black")
                fundis()
                gumb_pkoren.configure(state="normal")
                if self.xkyi == 2:
                    b = self.izpis.get("1.0", END)
                    c = float(b)
                    d = float(self.xky)
                    r = d**(1/c)
                    xky_label.config(fg="#cfcfcf")
                    pocisti_zaslon()
                    self.xky = ""
                    self.xkyi = 0
                    zgodovina()
                    postopek_pobrisi_trenutno()
                    self.zgodovina = ""
                    if sys.version_info < (3, 0):
                        #Python2

                        if c == 1:
                            vnesi_postopek((u"\u00B9").encode('utf-8').strip())
                        elif c == 2:
                            vnesi_postopek((u"\u00B2").encode('utf-8').strip())
                        elif c == 3:
                            vnesi_postopek((u"\u00B3").encode('utf-8').strip())
                        elif c == 4:
                            vnesi_postopek((u"\u2074").encode('utf-8').strip())
                        elif c == 5:
                            vnesi_postopek((u"\u2075").encode('utf-8').strip())
                        elif c == 6:
                            vnesi_postopek((u"\u2076").encode('utf-8').strip())
                        elif c == 7:
                            vnesi_postopek((u"\u2077").encode('utf-8').strip())
                        elif c== 8:
                            vnesi_postopek((u"\u2078").encode('utf-8').strip())
                        elif c== 9:
                            vnesi_postopek((u"\u2079").encode('utf-8').strip())
                        else:
                            vnesi_postopek(c)




                    else:
                        #Python3
                        if c == 1:
                            vnesi_postopek("\u00B9")
                        elif c == 2:
                            vnesi_postopek("\u00B2")
                        elif c == 3:
                            vnesi_postopek("\u00B3")
                        elif c == 4:
                            vnesi_postopek("\u2074")
                        elif c == 5:
                            vnesi_postopek("\u2075")
                        elif c == 6:
                            vnesi_postopek("\u2076")
                        elif c == 7:
                            vnesi_postopek("\u2077")
                        elif c== 8:
                            vnesi_postopek("\u2078")
                        elif c== 9:
                            vnesi_postopek("\u2079")
                        else:
                            vnesi_postopek(c)

                    vnesi_postopek("√")
                    vnesi_postopek(float(d))
                    fun()
                    insert_zaslon('{:.{}f}'.format(r, 5 ))
                if self.xkyi == 1:
                    self.xky = self.izpis.get("1.0", END)
                    pocisti()
                    postopek_pobrisi_trenutno()

        self.logxy=""
        self.logxyi = int()
        self.logxyi = 0
        def logxy():
            if self.fun2i % 2 == 1:
                dms()
                fun2()
            else:
                self.logxyi = self.logxyi + 1
                logxy_label.config(fg="black")
                fundis()
                gumb_log.configure(state="normal")
                if self.logxyi == 2:
                    b = self.izpis.get("1.0", END)
                    c = int(b)
                    d = int(self.logxy)
                    r = math.log(d, c)
                    logxy_label.config(fg="#cfcfcf")
                    zgodovina()


                    postopek_pobrisi_trenutno()
                    insert_zaslon('{:.{}f}'.format(r, 8 ))
                    vnesi_postopek("log")
                    if sys.version_info < (3, 0):
                        #Python2

                        if c == 1:
                            vnesi_postopek((u"\u2081").encode('utf-8').strip())
                        elif c == 2:
                            vnesi_postopek((u"\u2082").encode('utf-8').strip())
                        elif c == 3:
                            vnesi_postopek((u"\u2083").encode('utf-8').strip())
                        elif c == 4:
                            vnesi_postopek((u"\u2084").encode('utf-8').strip())
                        elif c == 5:
                            vnesi_postopek((u"\u2085").encode('utf-8').strip())
                        elif c == 6:
                            vnesi_postopek((u"\u2086").encode('utf-8').strip())
                        elif c == 7:
                            vnesi_postopek((u"\u2087").encode('utf-8').strip())
                        elif c== 8:
                            vnesi_postopek((u"\u2088").encode('utf-8').strip())
                        elif c== 9:
                            vnesi_postopek((u"\u2089").encode('utf-8').strip())
                        else:
                            vnesi_postopek("(")
                            vnesi_postopek(c)
                            vnesi_postopek(")")

                    else:
                        #Python3
                        if c == 1:
                            vnesi_postopek("\u2081")
                        elif c == 2:
                            vnesi_postopek("\u2082")
                        elif c == 3:
                            vnesi_postopek("\u2083")
                        elif c == 4:
                            vnesi_postopek("\u2084")
                        elif c == 5:
                            vnesi_postopek("\u2085")
                        elif c == 6:
                            vnesi_postopek("\u2086")
                        elif c == 7:
                            vnesi_postopek("\u2087")
                        elif c== 8:
                            vnesi_postopek("\u2088")
                        elif c== 9:
                            vnesi_postopek("\u2089")
                        else:
                            vnesi_postopek("(")
                            vnesi_postopek(c)
                            vnesi_postopek(")")

                    vnesi_postopek(d)
                    self.logxy = ""
                    self.logxyi = 0
                    fun()
                if self.logxyi == 1:
                    self.logxy = self.izpis.get("1.0", END)
                    postopek_pobrisi_trenutno()
                    pocisti()

        self.exp=""
        self.expi = int()
        self.expi = 0
        def EXP():
            self.expi = self.expi + 1
            EXP_label.config(fg="black")
            fundis()
            gumb_EXP.configure(state="normal")
            if self.expi == 2:
                b = self.izpis.get("1.0", END)
                c = int(b)
                d = float(self.exp)
                r = d*(10**c)
                ans = '%.3E' % r
                EXP_label.config(fg="#cfcfcf")
                pocisti()
                zgodovina()
                self.expi = ""
                self.expi = 0
                insert_zaslon(ans)
                fun()
            if self.expi == 1:
                self.exp = self.izpis.get("1.0", END)
                vnesi_postopek("·10^")
                pocisti()
        def procent():
            b = self.izpis.get("1.0", END)
            c = float(b)
            r = c*100
            pocisti()
            zgodovina()
            vnesi_postopek("%")
            insert_zaslon(r)
        def desetnax():
            b = self.izpis.get("1.0", END)
            c = float(b)
            r = 10**c
            pocisti()
            zgodovina()
            vnesi_postopek("(10^)")
            insert_zaslon(r)
        def dms():
            kot = self.izpis.get("1.0",END)
            #Razcleni kot na posmezne dele
            stevilo, decimalke = kot.split(".",1)
            d=int(float(kot))
            m=int((float(kot)-d)*60)
            s=int((((float(kot)-d-(m/60))*3600))*100)

            pocisti()
            zaslon_srednji()
            insert_no_count(str(d)+"°"+str(m)+"' "+str(s)+'"')

        #Pretvrjanje v sisteme
        self.hexi=0
        def fhex():
            self.hexi += 1
            if self.hexi==1:
                self.hex = ""
                trenutno = int(self.izpis.get("1.0", END))
                self.hex = hex(trenutno)
                pocisti()
                insert_zaslon(self.hex)
                del self.disk[:]
            else:
                self.hexi=0
                trenutno=self.izpis.get("1.0",END)
                pocisti()
                insert_zaslon(int(trenutno, 0))
                del self.disk[:]
        self.octi=0
        def foct():
            self.octi+=1
            if self.octi==1:
                self.oct = ""
                trenutno = int(self.izpis.get("1.0", END))
                self.oct = oct(trenutno)
                pocisti()
                insert_zaslon(self.oct)
                del self.disk[:]
            else:
                self.octi=0
                trenutno=self.izpis.get("1.0", END)
                pocisti()
                insert_zaslon(int(trenutno,0))
                del self.disk[:]
        self.bini=0
        def fbin():
            self.bini+=1
            if self.bini==1:
                self.bin = ""
                trenutno = int(self.izpis.get("1.0", END))
                self.bin = bin(trenutno).replace("0b", "")
                pocisti()
                insert_zaslon(self.bin)
                del self.disk[:]
            else:
                self.bini=0
                trenutno=self.izpis.get("1.0", END)
                pocisti()
                insert_zaslon(int(trenutno,2))
                del self.disk[:]
        #Definiraj spremijane zapisa rezultata
        self.fe = 0
        def FE():
            self.fe = self.fe + 1
            if self.fe % 2 == 1:
                znanstveni()
                pocisti_zaslon()
                insert_zaslon(self.znanstveni_rezultat)
            else:
                neznanstveni()
                pocisti_zaslon()
                insert_zaslon(self.neznanstveni_rezultat)

        self.racuni = 0
        def racun():
            self.racuni = self.racuni + 1
            if self.racuni % 2 == 0 or self.racuni == 0:
                pocisti()
                self.izpis.config(font=velika_pisava, state="disabled",pady=2, height=2, width=12)
                self.izpis.configure(state="normal")
                self.izpis.insert(END, self.koncni_rezultat)
                self.izpis.configure(state="disabled")

            else:
                pocisti()
                #Zamenjaj * s krat simbolom
                for (i, x) in enumerate(self.postopek):
                    if x == "*":
                        self.postopek[i] = "×"
                    if x == "/":
                        self.postopek[i] = "÷"



                izpis_postopka = ("".join(str(x) for x in self.postopek))
                self.izpis.config(font=mala_pisava, state="disabled",pady=5, height=4, width=25)
                self.izpis.configure(state="normal")
                self.izpis.insert(END, izpis_postopka)
                self.izpis.configure(state="disabled")
                print(izpis_postopka)

        #<editor-fold> KeyBindi
        #Key bindi za osnovne funkcije in številke
        self.master.bind('1', lambda event: vnesi("1"))
        self.master.bind('2', lambda event: vnesi("2"))
        self.master.bind('3', lambda event: vnesi("3"))
        self.master.bind('4', lambda event: vnesi("4"))
        self.master.bind('5', lambda event: vnesi("5"))
        self.master.bind('6', lambda event: vnesi("6"))
        self.master.bind('7', lambda event: vnesi("7"))
        self.master.bind('8', lambda event: vnesi("8"))
        self.master.bind('9', lambda event: vnesi("9"))
        self.master.bind('0', lambda event: vnesi("0"))
        self.master.bind('j', lambda event: vnesi("0"))
        self.master.bind('e', lambda event: vnesi('{:.{}f}'.format(math.e, 8 )))
        self.master.bind('.', lambda event: vnesi("."))
        self.master.bind(',', lambda event: vnesi("."))
        self.master.bind('(', lambda event: oklepaj())
        self.master.bind(')', lambda event: zaklepaj())
        self.master.bind('+', lambda event: sestevanje())
        self.master.bind('-', lambda event: odstevanje())
        self.master.bind('*', lambda event: mnozenje())
        self.master.bind('/', lambda event: deljenje())
        self.master.bind('<Return>', lambda event: rezultat())
        self.master.bind("<BackSpace>", lambda event: pobrisi_eno_mesto())
        #self.master.bind('<KeyPress-BackSpace>', lambda event: pritisk_brisi())
        #self.master.bind('<KeyRelease-BackSpace>', lambda event: spust_brisi())
        self.master.bind('<F1>', lambda event: fun())
        self.master.bind('<F2>', lambda event: fun2())
        self.master.bind('<F3>', lambda event: FE())
        self.master.bind('n', lambda event: vnesi("n"))
        self.master.bind('x', lambda event: vnesi("x"))

        #Pocisti vse za razlicne platforme
        self.master.bind("<space>", lambda evenc: pocisti_vse())

        #</editor-fold>


        prikaz_int=1

        #Definiraj zacetno visino gumbov
        visina = int()
        visina = 360

        #Function
        fun_button = ttk.Button(self, text="Omogoči funkcije", command = lambda: fun())
        fun_button.place(x = 15, y=140)
        fun_button.config(width="22")

        #2ndF
        fun2_button = ttk.Button(self, text="2ndF",state="disabled", command = lambda: fun2())
        fun2_button.place(x = 165, y=140)
        fun2_button.config( width="7")

        #Drugi znaki
        fun_label = Label(self, text="fun", fg="#cfcfcf", bg = "#cfcfcf")
        fun_label.place(x = 285, y=30)

        oklepaj_label = Label(self, text="(  )", fg="#cfcfcf", bg = "#cfcfcf")
        oklepaj_label.place(x = 285, y=50)

        vnr_label = Label(self, text="Vnr", fg="#cfcfcf", bg = "#cfcfcf")
        vnr_label.place(x = 30, y=93)

        pvnr_label = Label(self, text="(p)Vnr", fg="#cfcfcf", bg = "#cfcfcf")
        pvnr_label.place(x = 60, y=93)

        cnr_label = Label(self, text="Cnr", fg="#cfcfcf", bg = "#cfcfcf")
        cnr_label.place(x = 105, y=93)

        pcnr_label = Label(self, text="(p)Cnr", fg="#cfcfcf", bg = "#cfcfcf")
        pcnr_label.place(x = 135, y=93)

        xnay_label = Label(self, text="x^y", fg="#cfcfcf", bg = "#cfcfcf")
        xnay_label.place(x = 180, y=93)

        xky_label = Label(self, text="x√y", fg="#cfcfcf", bg = "#cfcfcf")
        xky_label.place(x = 210, y=93)

        logxy_label = Label(self, text="log(y)x", fg="#cfcfcf", bg = "#cfcfcf")
        logxy_label.place(x = 240, y=93)

        EXP_label = Label(self, text="EXP", fg="#cfcfcf", bg = "#cfcfcf")
        EXP_label.place(x = 30, y=73)

        #Prva vrstica gumbov
        gumb_sedem = ttk.Button(self, text="7", command = lambda: vnesi("7"))
        gumb_sedem.place(x=15, y=visina)
        gumb_sedem.config( width=6)

        gumb_osem = ttk.Button(self, text="8", command = lambda: vnesi("8"))
        gumb_osem.place(x=75, y=visina)
        gumb_osem.config( width=6)

        gumb_devet = ttk.Button(self, text="9", command = lambda: vnesi("9"))
        gumb_devet.place(x=135, y=visina)
        gumb_devet.config( width=6)

        gumb_deljenje = ttk.Button(self, text="÷", command = lambda: deljenje())
        gumb_deljenje.place(x=195, y=visina)
        gumb_deljenje.config( width=6)

        gumb_vspomin = ttk.Button(self, text="x->M", command = lambda: xtomem())
        gumb_vspomin.place(x=255, y=visina)
        gumb_vspomin.config( width=8)

        #Druga vrstica gumbov
        gumb_stiri = ttk.Button(self, text="4", command = lambda: vnesi("4"))
        gumb_stiri.place(x=15, y=visina+35)
        gumb_stiri.config(width=6)

        gumb_pet = ttk.Button(self, text="5", command = lambda: vnesi("5"))
        gumb_pet.place(x=75, y=visina+35)
        gumb_pet.config(width=6)

        gumb_sest = ttk.Button(self, text="6", command = lambda: vnesi("6"))
        gumb_sest.place(x=135, y=visina+35)
        gumb_sest.config(width=6)

        gumb_mnozenje = ttk.Button(self, text="x", command = lambda: mnozenje())
        gumb_mnozenje.place(x=195, y=visina+35)
        gumb_mnozenje.config(width=6)

        gumb_izspomina = ttk.Button(self, text="RM", command = lambda: recallmem())
        gumb_izspomina.place(x=255, y=visina+35)
        gumb_izspomina.config(width=8)

        #Tretja vrstica gumbov
        gumb_ena = ttk.Button(self, text="1", command = lambda: vnesi("1"))
        gumb_ena.place(x=15, y=visina+70)
        gumb_ena.config( width=6)

        gumb_dva = ttk.Button(self, text="2", command = lambda: vnesi("2"))
        gumb_dva.place(x=75, y=visina+70)
        gumb_dva.config( width=6)

        gumb_tri = ttk.Button(self, text="3", command = lambda: vnesi("3"))
        gumb_tri.place(x=135, y=visina+70)
        gumb_tri.config( width=6)

        gumb_odstevanje = ttk.Button(self, text="-", command = lambda: odstevanje())
        gumb_odstevanje.place(x=195, y=visina+70)
        gumb_odstevanje.config( width=6)

        gumb_dodajspomin = ttk.Button(self, text="M+", command = lambda: xplusmem())
        gumb_dodajspomin.place(x=255, y=visina+70)
        gumb_dodajspomin.config( width=8)

        #Cetrt vrstica gumbov
        gumb_nic = ttk.Button(self, text="0", command = lambda: vnesi("0"))
        gumb_nic.place(x=15, y=visina+105)
        gumb_nic.config( width=6)

        gumb_plusminus = ttk.Button(self, text="+/-", command = lambda: plusminus())
        gumb_plusminus.place(x=75, y=visina+105)
        gumb_plusminus.config( width=6)

        gumb_vejica = ttk.Button(self, text=",", command = lambda: vnesi("."))
        gumb_vejica.place(x=135, y=visina+105)
        gumb_vejica.config( width=6)

        gumb_sestevanje = ttk.Button(self, text="+", command = lambda: sestevanje())
        gumb_sestevanje.place(x=195, y=visina+105)
        gumb_sestevanje.config( width=6)

        gumb_enako = ttk.Button(root, write=None, text="=", command= lambda: insert_zaslon(rezultat()))
        gumb_enako.place(x=255, y=visina+105)
        gumb_enako.config( width=8)

        #Dodajanje funkcijskih tipk
        vfun = int()
        vfun = 170

        # background="..." doesn't work...

        #Fukncijske tipke, prva vrsta
        gumb_sin = ttk.Button(self, text="sin", command = lambda: sin(prikaz_int))
        gumb_sin.place(x=15, y=vfun)
        gumb_sin.config( width=5)

        gumb_cos = ttk.Button(self, text="cos", command = lambda: cos(prikaz_int))
        gumb_cos.place(x=65, y=vfun)
        gumb_cos.config( width=5)

        gumb_tan = ttk.Button(self, text="tan", command = lambda: tan(prikaz_int))
        gumb_tan.place(x=115, y=vfun)
        gumb_tan.config( width=5)

        gumb_cot = ttk.Button(self, text="cot", command = lambda: cot(prikaz_int))
        gumb_cot.place(x=165, y=vfun)
        gumb_cot.config( width=5)

        gumb_ce = ttk.Button(self, text="⌫")
        gumb_ce.place(x=215, y=vfun)
        gumb_ce.config( width=5, command=lambda: pobrisi_eno_mesto())

        gumb_ce = ttk.Button(self, text="C")
        gumb_ce.place(x=265, y=vfun)
        gumb_ce.config( width=5, command=lambda: pocisti_vse())

        #Fukncijske tipke, druga vrsta
        gumb_ln = ttk.Button(self, text="ln", command = lambda: ln(prikaz_int))
        gumb_ln.place(x=15, y=vfun+35)
        gumb_ln.config( width=5)

        gumb_log = ttk.Button(self, text="log", command = lambda: logxy())
        gumb_log.place(x=65, y=vfun+35)
        gumb_log.config( width=5)

        gumb_ex = ttk.Button(self, text="e^x", command = lambda: enax(prikaz_int))
        gumb_ex.place(x=115, y=vfun+35)
        gumb_ex.config( width=5)

        gumb_10x = ttk.Button(self, text="10^x", command = lambda: desetnax())
        gumb_10x.place(x=165, y=vfun+35)
        gumb_10x.config( width=5)

        gumb_pow = ttk.Button(self, text="x^y", command = lambda: xnay())
        gumb_pow.place(x=215, y=vfun+35)
        gumb_pow.config( width=5)

        gumb_EXP = ttk.Button(self, text="EXP", command = lambda: EXP())
        gumb_EXP.place(x=265, y=vfun+35)
        gumb_EXP.config( width=5)

        #Fukncijske tipke, tretja vrsta
        gumb_pi = ttk.Button(self, text="π", command = lambda: pi())
        gumb_pi.place(x=15, y=vfun+70)
        gumb_pi.config( width=5)

        gumb_koren = ttk.Button(self, text="√", command = lambda: k_koren(prikaz_int))
        gumb_koren.place(x=65, y=vfun+70)
        gumb_koren.config( width=5)

        gumb_pkoren = ttk.Button(self, text="y√x", command= lambda: xky())
        gumb_pkoren.place(x=115, y=vfun+70)
        gumb_pkoren.config( width=5)

        gumb_kvadrat = ttk.Button(self, text="x²", command = lambda: kvadrat(prikaz_int))
        gumb_kvadrat.place(x=165, y=vfun+70)
        gumb_kvadrat.config( width=5)

        gumb_oklepaj = ttk.Button(self, text="(", command= lambda: oklepaj())
        gumb_oklepaj.place(x=215, y=vfun+70)
        gumb_oklepaj.config( width=5)

        gumb_zaklepaj = ttk.Button(self, text=")", command= lambda: zaklepaj())
        gumb_zaklepaj.place(x=265, y=vfun+70)
        gumb_zaklepaj.config( width=5)

        #Fukncijske tipke, cetrta vrsta
        gumb_fakulteta = ttk.Button(self, text="n!", command = lambda: fakulteta(prikaz_int))
        gumb_fakulteta.place(x=15, y=vfun+105)
        gumb_fakulteta.config( width=5)

        gumb_obrni = ttk.Button(self, text="1/x", command = lambda: invert(prikaz_int))
        gumb_obrni.place(x=65, y=vfun+105)
        gumb_obrni.config( width=5)

        gumb_vbp = ttk.Button(self, text="Vnr", command=lambda: vnr())
        gumb_vbp.place(x=115, y=vfun+105)
        gumb_vbp.config( width=5)

        gumb_vsp = ttk.Button(self, text="pVnr", command= lambda: pvnr())
        gumb_vsp.place(x=165, y=vfun+105)
        gumb_vsp.config( width=5)

        gumb_kbp = ttk.Button(self, text='Cnr', command = lambda: cnr())
        gumb_kbp.place(x=215, y=vfun+105)
        gumb_kbp.config( width=5)

        gumb_ksp = ttk.Button(self, text="pCnr", command = lambda: pcnr())
        gumb_ksp.place(x=265, y=vfun+105)
        gumb_ksp.config( width=5)

        #Fukncijske tipke, peta
        gumb_bin = ttk.Button(self, text="bin", command = lambda: fbin())
        gumb_bin.place(x=15, y=vfun+140)
        gumb_bin.config( width=5)

        gumb_oct = ttk.Button(self, text="oct", command = lambda: foct())
        gumb_oct.place(x=65, y=vfun+140)
        gumb_oct.config( width=5)

        gumb_hex = ttk.Button(self, text="hex", command = lambda: fhex())
        gumb_hex.place(x=115, y=vfun+140)
        gumb_hex.config( width=5)

        gumb_polinom = ttk.Button(self, text="P(n)", command = lambda: polinom())
        gumb_polinom.place(x=165, y=vfun+140)
        gumb_polinom.config( width=5)

        gumb_procent = ttk.Button(self, text="⟳", command = lambda: ulomek())
        gumb_procent.place(x=215, y=vfun+140)
        gumb_procent.config( width=5)

        gumb_FE = ttk.Button(self, text="F↔E",  command = lambda: FE())
        gumb_FE.place(x=265, y=vfun+140)
        gumb_FE.config( width=5)

        #Onemogoci funkcijske tipke
        gumb_fakulteta.configure(state="disabled")
        gumb_koren.configure(state="disabled")
        gumb_kvadrat.configure(state="disabled")
        gumb_sin.configure(state="disabled")
        gumb_cos.configure(state="disabled")
        gumb_tan.configure(state="disabled")
        gumb_cot.configure(state="disabled")
        gumb_log.configure(state="disabled")
        gumb_ln.configure(state="disabled")
        gumb_ex.configure(state="disabled")
        gumb_pow.configure(state="disabled")
        gumb_vbp.configure(state="disabled")
        gumb_vsp.configure(state="disabled")
        gumb_kbp.configure(state="disabled")
        gumb_ksp.configure(state="disabled")
        gumb_pkoren.configure(state="disabled")
        gumb_10x.configure(state="disabled")
        gumb_EXP.configure(state="disabled")
        gumb_obrni.configure(state="disabled")

        def rezultat():
            try:

                izpis_postopka = ("".join(str(x) for x in self.postopek))
                print(izpis_postopka)
                #List pretvori v condensed string
                izpis_rezultata = ("".join(str(x) for x in self.disk))
                answer = str("%g" % (eval(izpis_rezultata)))
                #Preveri kako dolg je rezultat in ga pretvori ce je daljsi od n znakov
                dolzina = len(answer)
                print(self.disk)
                n = int()
                n = 10
                if dolzina > n and ((float(answer) >= 1000 or float(answer) <= 0.00000001)):
                    ans = float(answer)
                    sci_answer = '%.3E' % ans
                    pocisti_zaslon()
                    insert_no_count(sci_answer, newline=True)
                    self.izpis.configure(state="disabled")
                    self.koncni_rezultat=sci_answer
                elif dolzina > n and ((float(answer) < 1000 or float(answer) > 0.00000001)):
                    pocisti_zaslon()
                    ans = float(answer)
                    insert_no_count('{:.{}f}'.format(ans, 8 ))
                    self.koncni_rezultat='{:.{}f}'.format(ans, 8 )
                else:
                    pocisti_zaslon()
                    insert_no_count(answer, newline=True)
                    self.izpis.configure(state="disabled")
                    self.koncni_rezultat=answer

                del self.postopek[:]
                self.postopek.append(answer)

                del self.disk[:]
                self.disk.append(answer)

            except TypeError:
                pocisti_vse()
                insert_zaslon("Err")
                del self.disk[:]
            except NameError:
                pocisti_vse()
                insert_zaslon("Err")
                del self.disk[:]
            except ValueError:
                pocisti_vse()
                insert_zaslon("Err")
                insert_postopek("Napaka števila")
                del self.disk[:]
        def rezultat_int():
            return int(eval(self.disk))
        def pocisti_zaslon():
            #to clear screen
            #set equation to empty before deleting screen

            self.izpis.configure(state='normal')
            self.izpis.delete('1.0', END)
            self.izpis.configure(state="disabled")
        def pocisti():
            #to clear screen
            #set equation to empty before deleting screen
            self.izpis.configure(state='normal')
            self.izpis.delete('1.0', END)
            self.izpis.configure(state="disabled")
        def insert_no_count(value, newline = False):
            self.izpis.configure(state='normal')
            self.izpis.insert(END,value)
        def insert_zaslon(value,newline=False):
            self.izpis.configure(state='normal')
            self.izpis.insert(END,value)
            self.disk.append(value)
            print(self.disk)

            #Sprotno prikazovanje postopka
            postopek_trace()
        def postopek_trace():
            #Sprotno prikazovanje postopka

            for (i, x) in enumerate(self.postopek):
                if x == "*":
                    self.postopek[i] = "·"
                if x == "/":
                    self.postopek[i] = "÷"
            self.postopek_trace = ("".join(str(x) for x in self.postopek))
            self.zaslon_postopek.configure(text=self.postopek_trace)
        def pobrisi_eno_mesto():
            izpis = self.izpis.get("1.0", END)
            l = len(izpis) - 1
            if l > 0: #Nic stevilk
                self.izpis.configure(state="normal")
                self.izpis.delete("end-2c")
                self.izpis.configure(state="disabled")
                del self.disk[-1]
                del self.funkcija [-1]
                del self.postopek[-1]
                postopek_trace()
        #Brisanje vsega - tukaj zaradi inita
        def pocisti_vse():

            #ponastavi sisteme

            del self.disk[:]
            del self.postopek[:]
            del self.polinom [:]

            # Funkcije
            resetfun()
            fundis()
            fun_button.configure(state="normal")
            fun2_button.configure(state="disabled")
            self.editing_x=False
            opozorilo_funkcija.config(background="#f0f0f0")
            self.limitai=0

            self.izpis.configure(state='normal')
            self.izpis.delete('1.0', END)

            crta.config(bg="#cfcfcf")
            crta.place(x=0, y=0)
            limita.place(x=80, y=300)

            #Ponastavi stringe
            self.racun=""
            self.prej=""
            self.koncni_rezultat =""
            self.sprotno=""
            self.postopek_trace=""

            #Ponsatavi gumbr
            gumb_polinom.config(text="P(n)")
            fun_button.config(text="Omogoči funkcije")

            #Ponastavi stevce
            self.polinomii=0
            self.polinomi=0
            self.ulomeki=0
            self.fe = 0
            self.racuni = 0
            self.oklepaji = 0
            self.zaklepaji = 0
            self.bini=0
            self.octi=0
            self.hexi=0

            postopek_trace()
            # Nastavi nastavitve ne privzeto
            self.izpis.config(font=velika_pisava, state="disabled",pady=2, height=2, width=12)

            oklepaj_label.config(fg="#cfcfcf")
            self.izpis.configure(state="disabled")


        pocisti_vse()



        self.izpis.configure(state ='disabled')

        self.pocisti_zaslon = pocisti_zaslon
        self.insert_zaslon = insert_zaslon
        self.rezultat_int = rezultat_int

        def new_window(_class):
            new = Toplevel(root)
            _class(new)


class Window2(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Definiramo, kreiramo okno
    def init_window(self):

        #Definiranje naslova okna
        self.master.title("Graf")
        self.master.geometry("600x650+1100+400")
        self.master.attributes("-alpha", 0.97)
        self.master.resizable(0,0)

        okno = Frame(self, width=600, height=600)
        okno.grid(row=1, column=1)
        okno.place(x = 0, y = 0)
        okno.pack()
        okno.grid_propagate(False)
        #Dovoli da se zasede celotno root okno
        self.pack(fill=BOTH, expand=1)

        #Risanje grafa


        def PolyCoefficients(x, coeffs):
            """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

            The coefficients must be in ascending order (``x**0`` to ``x**o``).
            """
            o = len(coeffs)
            y = 0
            for i in range(o):
                y += coeffs[i]*x**i
            return y

        najmanjsa_pisava = ("Arial", 10)

        #Definiraj sliderje za vnos obsega na x
        labelmin = Label(self, text="-200", font=najmanjsa_pisava)
        labelmin.place(x=5, y=605)
        labell1 = Label(self, text="-100", font=najmanjsa_pisava)
        labell1.place(x=140, y=605)
        labell2 = Label(self, text="-150", font=najmanjsa_pisava)
        labell2.place(x=75, y=605)
        labell3 = Label(self, text="-50", font=najmanjsa_pisava)
        labell3.place(x=210, y=605)
        labelmax = Label(self, text="200", font=najmanjsa_pisava)
        labelmax.place(x=575, y=605)
        labeld1 = Label(self, text="50", font=najmanjsa_pisava)
        labeld1.place(x=370, y=605)
        labeld2 = Label(self, text="100", font=najmanjsa_pisava)
        labeld2.place(x=440, y=605)
        labeld3 = Label(self, text="150", font=najmanjsa_pisava)
        labeld3.place(x=505, y=605)
        labelcenter = Label(self, text="0", font=najmanjsa_pisava)
        labelcenter.place(x=293, y=605)


        slider1 = ttk.Scale(self, from_=(-200), to=0)
        slider1.place(x=0, y=625)
        slider1.config(value=-5, length=300)
        slider2 = ttk.Scale(self, from_=0, to=200)
        slider2.place(x=300, y=625)
        slider2.config(value=5, length=300)




        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        x = np.linspace(-5, 5, 1000)
        coeffs = polinom[::-1]
        print(polinom)
        a.plot(x, PolyCoefficients(x, coeffs), color="green")




        a.set_title ("Graf polinoma", fontsize=10)


        canvas = FigureCanvasTkAgg(fig, okno)
        canvas.get_tk_widget().pack()
        canvas.draw()

        def posodobi():
            a.clear()
            leva = slider1.get()
            desna = slider2.get()
            x = np.linspace(leva, desna, 1000)
            a.plot(x, PolyCoefficients(x, coeffs), color="green")
            canvas.draw()

        slider1.config(command = lambda x: posodobi())
        slider2.config(command = lambda x: posodobi())

root = Tk()


#Velikost okna
root.geometry("330x520+550+200")
root.attributes("-alpha", 0.99)
root.configure(background="white")
root.resizable(0,0)
root.iconbitmap(r"C:\Users\Marko Zupan\OneDrive\Namizje\Kalkulator App\AppIcon.ico")


app = Window(root)
root.mainloop()
