# -*- coding: utf-8 -*-
from Tkinter import *
import ttk
import time

class MainWindow(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("The Pilgrimage.")
        #self.master.minsize(800, 600)
        self.grid(sticky=E+W+N+S)
        #-----
        self.LOOP_ACTIVE = BooleanVar(self)
        self.LOOP_ACTIVE.set(1)
        Button(self, text="close", command=self.close).grid(column=0, row=1, sticky=W)

        self.REINCARNATE = BooleanVar(self)
        self.REINCARNATE.set(1)
        Button(self, text="reincarnate", command=self.close).grid(column=0, row=2, sticky=W)


###health vigor satiety fear curiosity
        self.maxValue = 1000
        #-----health-----#
        self.gHealth = IntVar(self)
        self.lab_gHealth = Label(self, text="Health:")
        self.lab_gHealth.grid(row=1, column=1, pady=2, padx=2, sticky=E+W+N+S)
        self.gHealthBar = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", variable=self.gHealth, maximum=self.maxValue)
        self.gHealthBar.grid(row=1, column=2, pady=2, padx=2, sticky=E+W+N+S, columnspan=3)

        #-----vigor-----#
        self.gVigor = IntVar(self)
        self.lab_gVigor = Label(self, text="Vigor:")
        self.lab_gVigor.grid(row=2, column=1, pady=2, padx=2, sticky=E+W+N+S)
        self.gVigorBar = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", variable=self.gVigor, maximum=self.maxValue)
        self.gVigorBar.grid(row=2, column=2, pady=2, padx=2, sticky=E+W+N+S, columnspan=3)

        #-----satiety-----#
        self.gSatiety = IntVar(self)
        self.lab_gSatiety = Label(self, text="Satiety:")
        self.lab_gSatiety.grid(row=3, column=1, pady=2, padx=2, sticky=E+W+N+S)
        self.gSatietyBar = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", variable=self.gSatiety, maximum=self.maxValue)
        self.gSatietyBar.grid(row=3, column=2, pady=2, padx=2, sticky=E+W+N+S, columnspan=3)

        #----fear-----#
        self.gFear = IntVar(self)
        self.lab_gFear = Label(self, text="Fear:")
        self.lab_gFear.grid(row=4, column=1, pady=2, padx=2, sticky=E+W+N+S)
        self.gFearBar = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", variable=self.gFear, maximum=self.maxValue)
        self.gFearBar.grid(row=4, column=2, pady=2, padx=2, sticky=E+W+N+S, columnspan=3)

        #-----curious-----#
        self.gCurious = IntVar(self)
        self.lab_gCurious = Label(self, text="Curiousity:")
        self.lab_gCurious.grid(row=5, column=1, pady=2, padx=2, sticky=E+W+N+S)
        self.gCuriousBar = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate", variable=self.gCurious, maximum=self.maxValue)
        self.gCuriousBar.grid(row=5, column=2, pady=2, padx=2, sticky=E+W+N+S, columnspan=3)

        #-----distance-----#
        self.gDistance = DoubleVar(self)
        self.lab_gDistance = Label(self, text="Distance:")
        self.lab_gDistance.grid(row=6, column=1, pady=2, padx=2, sticky=E+N)

        #-----time update-----#
        self.gTime = StringVar(self)
        self. lab_gTime = Label(self, text="Time:")
        self.lab_gTime.grid(row=7, column=1, pady=2, padx=2, sticky=E+N)


        #-----status update-----#
        self.gStatus = StringVar(self)
        self. lab_gStatus = Label(self, text="Status:")
        self.lab_gStatus.grid(row=8, column=1, pady=2, padx=2, sticky=E+N)

        #-----
        self.update_labels_after = False
        self.update_labels()
        #-----

    def close(self):
        self.LOOP_ACTIVE.set(0)

    def reincarnate(self):
        self.REINCARNATE.set(0)

    def stepInRange(val, step, minval, maxval):
        newval = val + step
        if newval < minval: return minval
        if newval > maxval: return maxval
        return newval


    def set(self, healthSet, vigorSet,satietySet,fearSet,curiousSet,distanceSet):
        self.gHealth.set(healthSet)
        self.gVigor.set(vigorSet)
        self.gSatiety.set(satietySet)
        self.gFear.set(fearSet)
        self.gCurious.set(curiousSet)
        self.gDistance.set(distanceSet)
        self.lab_gDistance.config(text='Distance: %d' % self.gDistance.get())
        self.update_labels()

    def setStatus(self, statusString):
        sstring = "Status: \n"+statusString
        self.lab_gStatus.config(text=sstring)
        self.update_labels()

    def setTime(self, timeString):
        sstring = "Time: \n"+timeString
        self.lab_gTime.config(text=sstring)
        self.update_labels()


    def update_labels(self):
        self.lab_gHealth.config(text='Health: %0*d' % (4,self.gHealth.get()))
        self.lab_gVigor.config(text='Vigor: %0*d' % (4,self.gVigor.get()))
        self.lab_gSatiety.config(text='Satiety: %0*d' % (4,self.gSatiety.get()))
        self.lab_gFear.config(text='Fear: %0*d' % (4,self.gFear.get()))
        self.lab_gCurious.config(text='Curiousity: %0*d' % (4,self.gCurious.get()))



