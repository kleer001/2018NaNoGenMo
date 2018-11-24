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
        "isInjured":["Your hurt your ", "You banged your ","You fell and hit your ","Out of nowhere you injured your "],
        "isMoving":["You went for a walk in the ","You walked through the "],
        "isEating":["You ate ","You had ","Dinner was "],
        "isSleeping":["You went to sleep and drempt. ","You took a long nap. ","You slept some more. ","You dozed off. "],
        "isScared":["You were frightened by a ","You got scared by a ", "You were startled by a "],
        "isWithFriends":["Your friend dropped by for a chat. ","You saw your good friend. ","You met with an aquaintance. "],
        "isCurious": ["You looked around, fascinated by everything. ","The world was suffused by beauty. "]
    }

ender ={
        "isInjured":["You try to be more careful next time. ","You have no idea how that happened. "],
        "isMoving":["The terrain was rough. ","Your feet were tired. ","Somehow you couldn't recall the landscape. ","You forgot where you were. "],
        "isEating":["Your tummy growled. ","You felt ill. ","Your stomach was sour. "],
        "isSleeping":["You woke refreshed. ","But you were still tired. ","Your dreams faded immediately. "],
        "isScared":["If you see one again you'll freak out. ","Thankfully it was startled too. ","You stared at each other for a while. "],
        "isWithFriends":["They left suddenly without saying goodbye. ","But they stayed too long and bored you. ","Eventually they had to leave. "],
        "isCurious": ["The world is truly magnificent. ","You felt silly for staring so long. "]
    }

dayLike = [
    "isSleeping 120",
    "isEating 20",
    "isMoving 20",
    "isMoving 20",
    "isMoving 20"
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
bookFinalSize = 60000
incarnation = 0
daylength = 1000

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
    writeme = stringToWrite.encode('ascii','ignore')
    f = open(bookName,"a+" ) #append the file
    f.write(stringToWrite)
    f.close()
    lengthOfInput = len(stringToWrite.split())
    return lengthOfInput


preface = "\n\n\n Incarnation # 0 \n\nYou felt the overwhelming need to travel. You took nothing with you.\nYou walked naked into the world and died.\n"
preface += "\nYou went 0 miles on day 1. You were dead after going only 0 miles.\n"

bookLength += updateBook(preface)

while bookLength < bookFinalSize:
    #incarnation begin
    time.sleep(2)

    incarnation += 1
    maximumDays = incarnation+1
    dayspent = 0

    printIncarnation = "\n\n\n Incarnation #%s \n\n" % (incarnation)
    #pdb.set_trace()
    bookLength += updateBook(printIncarnation)
    print printIncarnation
    chapterQuote = "\n\n\""+random.sample(quotes,1)[0]+"\"\n\n"
    bookLength += updateBook(chapterQuote)
    alive = True

    englishActivity = ""

    world = landscape()

    friends = []
    friends += (random.sample(dramatasPersonae,min(incarnation,12)))

    creatures = []
    creatures += (random.sample(animals,min(incarnation+2,12)))

    bodyParts = []
    bodyParts += (random.sample(bodyparts,min(incarnation%5+2,12)))

    bodyFluids = bodilyfluids
    #bodyFluids + (random.sample(bodilyfluids,incarnation*2))

    foodstuffs = []
    foodstuffs += (random.sample(foods,min(incarnation,20)))

    gear = []
    gear + (random.sample(objects,min(incarnation,12)))
    gear += (random.sample(clothes,min(incarnation/2+1,12)))
    gear += (random.sample(guns,min(incarnation/10,12)))
    gear += (random.sample(appliances, min(incarnation/3,12)))

    supplies = {
        "equipment":[x.lower() for x in gear],
        "food":[x.lower() for x in foodstuffs]
        }

    bob = Protagonist()
    bob.initialize()

    bob.inventory.clear()
    bob.inventory = copy.deepcopy(supplies)

    bob.speed += (incarnation / 100.000)

    statuses = ""

    oldDistance = 0
    newDistance = 0
    dayNumber = 0

    if(incarnation == 1):
        bob.health = 10

    while alive:
        #setup the new day's list of activities
        specificDay = newDayMix(dayLike,randomEvent,incarnation%3+3,4)

        #pdb.set_trace()
        if dayNumber == 0:
            printFood = ", ".join(bob.inventory.get("food"))
            printGear = ", ".join(bob.inventory.get("equipment"))
            printSetOff = 'For food you packed {0}. \n\nAs for suplies you brought: {1} .\n'.format(printFood, printGear)
            bookLength += updateBook(printSetOff)

        totalDistance = (newDistance - oldDistance)

        if dayNumber > maximumDays: bob.isDead = True

        if dayNumber > 0:

            if bob.isDead==True: #DEATH
                jouneyEnd = newDistance
                printDeath = "\nYou went 0 miles on day %d. You were dead after going only %d miles. Not far enough... \n" % (dayNumber, jouneyEnd)
                #print printDeath
                bookLength += updateBook(printDeath)
                alive = False
                break
            dayDistance = "You went %d miles on day %d. " % (totalDistance, dayNumber)

            if(random.randrange(4)==1): #LOSS
                if len(bob.inventory.get("equipment","")) > 0:
                    lostitem = random.choice(bob.inventory.get("equipment",""))
                    bob.inventory.get("equipment","").remove(lostitem)
                    daysEvents += "You lost your %s. " % (lostitem)
                else:
                    daysEvents += "You feel like you're missing something else. "
            printDaysEvents = "\n"+dayDistance + daysEvents+"\n"
            #print printDaysEvents
            if(newDistance > 0):
                bookLength += updateBook(printDaysEvents)
            oldDistance = newDistance
        daysEvents = ""

        for activity in specificDay:
            if dayspent > daylength:
                dayspent = 0
                break
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

            if activityName == "isWithFriends": #HiIiiieeeee
                englishActivity += random.choice(friends).__getitem__('name')
                if(random.randrange(5)):
                    englishActivity += " "+random.choice(friends).__getitem__('famname')
                else:
                    englishActivity += " your "
                    englishActivity += random.choice(friends).__getitem__('relate')
                englishActivity += " stayed for a bit and made your day brighter. "

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
                    if(random.randrange(6)):
                        englishActivity += "No food was left. "
                    if(random.randrange(8)):
                        englishActivity += "Not a crumb. "

                    bob.states["isEating"]=False
            if(random.randrange(3)==1):
                englishActivity += random.choice(ender.__getitem__(activityName)) #boiler plate ender to activity
            daysEvents += englishActivity
            statuses += englishActivity + "\n"
            allStatus = deque(string.split(statuses,"\n"))

            if len(allStatus) > 8: deque.popleft(allStatus)
            statuses = string.join(allStatus,"\n")
            if gui: main.setStatus(statusString=statuses)
            if gui: main.update()

            for atime in range(activityValue+variation):
                dayspent += 1
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

incarnation += 1

epilogue = "\n\n\n Incarnation #%d " % (incarnation)
epilogue += "\n\nYou felt the overwhelming need to stay at home. You made yourself a cup of tea.\nYou read a book and enjoyed your time alone.\n"
epilogue += "\nYou went 0 miles on day 1... and that was enough.\n"

bookLength += updateBook(epilogue)


print "BOOK DONE"



