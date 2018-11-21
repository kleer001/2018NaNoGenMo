# -*- coding: utf-8 -*-

from landscape import *
from gui import *
from persona import *
import random
from collections import deque
import string

def newDayMix(main,mixin,ratio):
    newMix = {}
    for x, y in main.items():
        newMix[x]=y
        for a, b in mixin.items():
            if(random.randint(1,ratio)==1):
                newMix[a]=b
    return newMix

alookup ={
        "isInjured":["You got injured very badly, it hurts. ","You got hurt and you're in a lot of pain. "],
        "isMoving":["You went for a walk in the ","You walked through the "],
        "isEating":["You ate ","You had ","Dinner was "],
        "isSleeping":["You went to sleep and drempt. ","You took a long nap. "],
        "adrenaline":["You were frightened by something. ","You got scared. "],
        "hasCompany":["A friend dropped by for a chat. ","You saw a good friend. "],
        "isCurious": ["You looked around, fascinated. ","The world was suffused by beauty. "]
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

world = landscape()
main = MainWindow()
bob = Protagonist()
bob.inventory = supplies

statuses = ""

oldDistance = 0
newDistance = 0
dayNumber = 0

while main.LOOP_ACTIVE.get()==1:
    #setup the new day's list of activities
    specificDay = newDayMix(dayLike,randomEvent,5)


    if newDistance > 0:
        totalDistance = (newDistance - oldDistance)/10
        if totalDistance == 0 and dayNumber > 2:
            print "You went 0 miles on day %d. You were dead." % (dayNumber)
            break
        dayDistance = "You went %d miles on day %d. " % (totalDistance, dayNumber)

        if(random.randint(0,5)==1):
            if len(supplies.get("equipment","")) > 0:
                lostitem = random.choice(supplies.get("equipment",""))
                supplies.get("equipment","").remove(lostitem)
                daysEvents += "You lost your %s." % (lostitem)
            else:
                daysEvents += "You feel like you're missing something.'"

        print dayDistance + daysEvents
        oldDistance = newDistance

    daysEvents = ""

    for activity in specificDay:
#        newActivity = activity
        variation = random.randint(1,100)
        statusUpdate = activity + "=True"
        exec("bob."+statusUpdate)

        englishActivity = random.choice(alookup.__getitem__(activity))
        if activity == "isMoving":
            englishActivity += random.choice(world.landscapes.__getitem__('natural'))
            englishActivity += ". "
        if activity == "isEating":
            englishActivity += random.choice(bob.inventory.__getitem__('food'))
            willBeFull = bob.satiety + 7*(specificDay[activity]+variation)
            if willBeFull >= bob.maxScale:
                englishActivity += " and felt full. "
            else:
                englishActivity += " but you still felt hungry. "


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
            main.set(healthSet=bob.health, vigorSet=bob.vigor,satietySet=bob.satiety,
                fearSet=bob.fear,curiousSet=bob.curiosity,distanceSet=bob.distance)
            #time.sleep(0.05)
            main.update()
        statusUpdate = activity + "=False"

        exec("bob."+statusUpdate)
        #if bob.isCurious: null
    newDistance = bob.distance
    dayNumber += 1


