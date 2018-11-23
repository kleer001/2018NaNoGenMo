# -*- coding: utf-8 -*-

from landscape import *
from gui import *
from persona import *
from nouns import *
import random
from collections import deque
import string
import os
import time
import copy

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#import pdb

alookup ={
        "isInjured":["Your hurt your ","You fell and hit your ","Out of nowhere your "],
        "isMoving":["You went for a walk in the ","You walked through the "],
        "isEating":["You ate ","You had ","Dinner was "],
        "isSleeping":["You went to sleep and drempt. ","You took a long nap. ","You slept some more. ","You dozed off. "],
        "isScared":["You were frightened by a ","You got scared by a ", "You were startled by a "],
        "isWithFriends":["Your friend dropped by for a chat. ","You saw your good friend. "],
        "isCurious": ["You looked around, fascinated by everything. ","The world was suffused by beauty. "]
    }

ender ={
        "isInjured":["Your hurt your ","You fell and hit your ","Out of nowhere your "],
        "isMoving":[""],
        "isEating":["You ate ","You had ","Dinner was ", "You gobbled down ", "Breakfast was ", "Lunch was "],
        "isSleeping":["You went to sleep and drempt. ","You took a long nap. ","You slept some more. ","You dozed off. "],
        "isScared":["You were frightened by a ","You got scared by a ", "You were startled by a "],
        "isWithFriends":["Your friend dropped by for a chat. ","You saw your good friend. "],
        "isCurious": ["You looked around, fascinated by everything. ","The world was suffused by beauty. "]
    }

dayLike = [
    "isSleeping 120",
    "isEating 20",
    "isMoving 20",
    ]

randomEvent = [
    "isInjured 10",
    "isScared 10",
    "isWithFriends 30"
    ]

def fdKey(fakeDict):
    fakeKey = ""
    fakeKey = fakeDict.split(" ")
    return fakeKey[0]

def fdValue(fakeDict):
    fakeValue = []
    fakeValue = fakeDict.split(" ")
    return int(fakeValue[1])


def newDayMix(main,mixin,total,ratio):
    newMix = []
    for x in range(total):
        newMix.append(random.choice(main))
        if(random.randrange(ratio)==1):
            newMix.append(random.choice(mixin))
    return newMix

bookLength = 0
bookFinalSize = 20000
incarnation = 0

gui = False


if gui: main = MainWindow()

i = 0
while os.path.exists("ThePilgramage_%s.txt" % i):
    i += 1

bookName = "ThePilgramage_%s.txt" % i

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
    time.sleep(2)

    incarnation += 1
    printIncarnation = "\n\n\n Incarnation # %s \n\n" % (incarnation)
    #pdb.set_trace()
    bookLength += updateBook(printIncarnation)
    print printIncarnation
    chapterQuote = "\n\n\""+random.sample(quotes,1)[0].encode('ascii','ignore')+"\"\n\n"
    bookLength += updateBook(chapterQuote)
    alive = True

    englishActivity = ""
    world = landscape()

    creatures = []
    creatures += (random.sample(animals,incarnation))

    bodyParts = []
    bodyParts += (random.sample(bodyparts,incarnation))

    bodyFluids = bodilyfluids
    #bodyFluids + (random.sample(bodilyfluids,incarnation*2))

    foodstuffs = []
    foodstuffs += (random.sample(foods,incarnation))

    gear = []
    gear + (random.sample(objects,incarnation*1))
    gear += (random.sample(clothes,incarnation * 1))
    gear += (random.sample(guns,1))
    gear += (random.sample(appliances, int(incarnation / 3)))

    supplies = {
        "equipment":[x.lower() for x in gear],
        "food":[x.lower() for x in foodstuffs]
        }

    bob = Protagonist()
    bob.initialize()

    bob.inventory.clear()
    bob.inventory = copy.deepcopy(supplies)

    statuses = ""

    oldDistance = 0
    newDistance = 0
    dayNumber = 0

    while alive:
        #setup the new day's list of activities
        specificDay = newDayMix(dayLike,randomEvent,6,7)
        #pdb.set_trace()
        if dayNumber == 0:
            printFood = ", ".join(bob.inventory.get("food"))
            printGear = ", ".join(bob.inventory.get("equipment"))
            printSetOff = 'For food you packed {0}. \nAs for suplies you brought: {1} .\n'.format(printFood, printGear)
            bookLength += updateBook(printSetOff)

        if newDistance > 0:
            totalDistance = (newDistance - oldDistance)/20

            if totalDistance == 0 and dayNumber > 2: #DEATH
                jouneyEnd = newDistance / 20
                printDeath = "\nYou went 0 miles on day %d. You were dead after going only %.f1 miles." % (dayNumber, jouneyEnd)
                #print printDeath
                bookLength += updateBook(printDeath)
                alive = False
                break
            dayDistance = "You went %d miles on day %d. " % (totalDistance, dayNumber)

            if(random.randrange(5)==1): #LOSS
                if len(bob.inventory.get("equipment","")) > 0:
                    lostitem = random.choice(bob.inventory.get("equipment",""))
                    bob.inventory.get("equipment","").remove(lostitem)
                    daysEvents += "You lost your %s. " % (lostitem)
                else:
                    daysEvents += "You feel like you're missing something else. "

            printDaysEvents = "\n"+dayDistance + daysEvents+"\n"
            #print printDaysEvents
            bookLength += updateBook(printDaysEvents)
            oldDistance = newDistance
        daysEvents = ""

        for activity in specificDay:
            variation = random.randrange(100)
            activityName = fdKey(activity)
            activityValue = fdValue(activity)
            statusUpdate = "bob.states[\""+activityName + "\"]=True"
            exec(statusUpdate)
            englishActivity = random.choice(alookup.__getitem__(activityName)) #boiler plate intro to activity

            if activityName == "isInjured": # OUCH
                englishActivity += random.choice(bodyParts)
                if random.randrange(4)==1:
                    englishActivity += " and it is leaking "
                    englishActivity += random.choice(bodyFluids)
                englishActivity += ", it hurts so much. "

            if activityName == "isScared": #WHAAA
                englishActivity += random.choice(creatures)
                englishActivity += ". "

            if activityName == "isMoving":# WHEEE
                englishActivity += random.choice(world.landscapes.__getitem__('natural'))
                englishActivity += ". "

            if activityName == "isEating":# YUMMY
                if(len(bob.inventory.get("food")))>0:
                    itemToEat = random.choice(bob.inventory.__getitem__('food'))
                    englishActivity += itemToEat
                    bob.inventory.get("food","").remove(itemToEat)
                    willBeFull = bob.satiety + 7*(activityValue+variation)
                    if willBeFull >= bob.maxScale:
                        englishActivity += " and you felt full. "
                    else:
                        englishActivity += " but you still felt hungry. "
                else:
                    englishActivity += "nothing. "
                    if(random.randrange(4)):
                        englishActivity += "No food was left. " 
                    if(random.randrange(6)):
                        englishActivity += "Not a crumb. " 
                    
                    bob.states["isEating"]=False

            daysEvents += englishActivity
            statuses += englishActivity + "\n"
            allStatus = deque(string.split(statuses,"\n"))

            if len(allStatus) > 8: deque.popleft(allStatus)
            statuses = string.join(allStatus,"\n")
            if gui: main.setStatus(statusString=statuses)
            if gui: main.update()

            for atime in range(activityValue+variation):
                if gui: main.setTime(timeString=str(bob.time))
                bobStatus = bob.update()
                statesUpdate = bob.updateStates()
                if gui: main.set(healthSet=bob.health, vigorSet=bob.vigor,satietySet=bob.satiety,
                    fearSet=bob.fear,curiousSet=bob.curiosity,distanceSet=bob.distance)
                #time.sleep(0.05)
                if gui: main.update()
            statusUpdate = "bob.states[\""+activityName + "\"]=False"
            exec(statusUpdate)
            #if bob.isCurious: null
        newDistance = bob.distance
        dayNumber += 1

print "BOOK DONE"

