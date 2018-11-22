# -*- coding: utf-8 -*-

from landscape import *
from gui import *
from persona import *
from nouns import *
import random
from collections import deque
import string
import os

import pdb

alookup ={
        "isInjured":["Your got injured very badly, it hurts. ","You got hurt and you're in a lot of pain. "],
        "isMoving":["You went for a walk in the ","You walked through the "],
        "isEating":["You ate ","You had ","Dinner was "],
        "isSleeping":["You went to sleep and drempt. ","You took a long nap. "],
        "adrenaline":["You were frightened by something. ","You got scared by something. "],
        "hasCompany":["Your friend dropped by for a chat. ","You saw your good friend. "],
        "isCurious": ["You looked around, fascinated by everything. ","The world was suffused by beauty. "]
    }

dayLike = {
    "isSleeping":240,
    "isEating":45,
    "isMoving":220,
    }

randomEvent = {
    "isInjured":60,
    "adrenaline":10,
    "hasCompany":30
    }

supplies = {
    "equipment":["knife","tent","frying pan","axe"],
    "food":["an apple","some meat","a hunk of bread","some cheese","squash",
        "some strawberries","some blueberries", "a sandwich","a leg of lamb" ]
    }

def newDayMix(main,mixin,ratio):
    newMix = {}
    for x, y in main.items():
        newMix[x]=y
        for a, b in mixin.items():
            if(random.randint(1,ratio)==1):
                newMix[a]=b
    return newMix

bookLength = 0
bookFinalSize = 2000
incarnation = 0

main = MainWindow()

bookName = "ThePilgramage.txt"

f = os.open(bookName, os.O_RDWR|os.O_CREAT ) #Create the file
os.write(f, " \"The Pilgramage\" \n\n")
os.close(f)

def updateBook(stringToWrite):
    f = open(bookName,"a+" ) #append the file
    f.write(stringToWrite)
    f.close()
    lengthOfInput = len(stringToWrite.split())
    return lengthOfInput


while bookLength < bookFinalSize:
    #incarnation begin

    englishActivity = ""
    world = landscape()

    bob = Protagonist()
    bob.initialize()

    bob.inventory = supplies

    statuses = ""

    oldDistance = 0
    newDistance = 0
    dayNumber = 0

    incarnation += 1
    printIncarnation = "\n\n Incarnation # %s \n\n" % (incarnation)

#    pdb.set_trace()

    bookLength += updateBook(printIncarnation)
    alive = True

    while alive:
        #setup the new day's list of activities
        specificDay = newDayMix(dayLike,randomEvent,5)

        if newDistance > 0:
            totalDistance = (newDistance - oldDistance)/10
            if totalDistance == 0 and dayNumber > 2:
                printDeath = "\nYou went 0 miles on day %d. You were dead." % (dayNumber)
                print printDeath
                bookLength += updateBook(printDeath)
                alive = False
                break
            dayDistance = "You went %d miles on day %d. " % (totalDistance, dayNumber)

            if(random.randint(0,5)==1):
                if len(bob.inventory.get("equipment","")) > 0:
                    lostitem = random.choice(bob.inventory.get("equipment",""))
                    bob.inventory.get("equipment","").remove(lostitem)
                    daysEvents += "You lost your %s." % (lostitem)
                else:
                    daysEvents += "You feel like you're missing something else.'"

            printDaysEvents = "\n"+dayDistance + daysEvents+"\n"
            print printDaysEvents
            bookLength += updateBook(printDaysEvents)
            oldDistance = newDistance
        daysEvents = ""

        print "today is %s" % (specificDay)

        for activity in specificDay:
            variation = random.randint(1,100)
            statusUpdate = "bob.states[\""+activity + "\"]=True"
            exec(statusUpdate)
            englishActivity = random.choice(alookup.__getitem__(activity))
            if activity == "isMoving":
                englishActivity += random.choice(world.landscapes.__getitem__('natural'))
                englishActivity += ". "
            if activity == "isEating":
                if(len(bob.inventory.get("food")))>0:
                    itemToEat = random.choice(bob.inventory.__getitem__('food'))
                    englishActivity += itemToEat
                    bob.inventory.get("food","").remove(itemToEat)
                    willBeFull = bob.satiety + 7*(specificDay[activity]+variation)
                    if willBeFull >= bob.maxScale:
                        englishActivity += " and felt full. "
                    else:
                        englishActivity += " but you still felt hungry. "
                else:
                    englishActivity += "You were hungry but had no food left."
                    break

            daysEvents += englishActivity
            statuses += englishActivity + "\n"
            allStatus = deque(string.split(statuses,"\n"))

            if len(allStatus) > 8: deque.popleft(allStatus)
            statuses = string.join(allStatus,"\n")
            main.setStatus(statusString=statuses)
            main.update()

            for atime in range(specificDay[activity]+variation):
                main.setTime(timeString=str(bob.time))
                bobStatus = bob.update()
                statesUpdate = bob.updateStates()
                if len(statesUpdate): print statesUpdate
                main.set(healthSet=bob.health, vigorSet=bob.vigor,satietySet=bob.satiety,
                    fearSet=bob.fear,curiousSet=bob.curiosity,distanceSet=bob.distance)
                #time.sleep(0.05)
                main.update()
            statusUpdate = "bob.states[\""+activity + "\"]=False"
            exec(statusUpdate)
            #if bob.isCurious: null
        newDistance = bob.distance
        dayNumber += 1


