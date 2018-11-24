# -*- coding: utf-8 -*-

import random

#protagonist engine

class Protagonist:
    def __init__(self):
#        super(self,Protagonist).__init__() #what? why?
        self.maxScale = 1000
        self.vigorMax = 1000
        self.healthMax = 1000
        self.health = self.maxScale
        self.vigor = self.maxScale
        self.satiety = self.maxScale
        self.fear = 0
        self.curiosity = self.maxScale/2
        self.speed = 0.02
        self.distance = 0.0
        self.isDead = False
        self.isSleeping = False

        self.stateList = ['Curious','Injured','Tired','Camping','Moving','Eating',
        'Adrenaline','Storytelling','SettingUpCamp','WithFriends','Scared']
        self.states = dict()
        for eachState in self.stateList:
            self.states["is"+eachState]=False
            self.states["was"+eachState]=False

        self.inventory = {}
        self.time = 0
        self.stateChange = []

    def initialize(self):
        self.maxScale = 1000
        self.vigorMax = 1000
        self.healthMax = 1000
        self.health = self.maxScale
        self.vigor = self.maxScale
        self.satiety = self.maxScale
        self.fear = 0
        self.curiosity = self.maxScale/2
        self.speed = 0.02
        self.distance = 0.0
        self.isDead = False
        self.isSleeping = False

        self.stateList = ['Curious','Injured','Tired','Camping','Moving','Eating',
        'Adrenaline','Storytelling','SettingUpCamp','WithFriends','Scared','Sleeping']
        self.states = dict()
        for eachState in self.stateList:
            self.states["is"+eachState]=False
            self.states["was"+eachState]=False

        self.inventory = {}
        self.time = 0
        self.stateChange = []

    def updateStates(self):
        self.changes = []
        for eachState in self.stateList:
                if self.states.get("is"+eachState) and not self.states.get("was"+eachState):
                    self.states["was"+eachState] = True
                    self.changes.append(eachState)
                if not self.states.get("is"+eachState) and self.states.get("was"+eachState):
                    self.states["was"+eachState] = False
        return self.changes

    def probable(self,value=0,atOne=0, atZero=1000):
        chance = float (random.randint(atOne,atZero)/value)
        if chance > 0.5: return False
        else: return True

    def update(self):
        #basic logic updates
        self.stateChange = []
        self.time += 1
        #if you're dead you're dead''
        if self.isDead: return 0
        if self.health < 1 :
            self.isDead = True
            self.stateChange += "dead"
            return self.stateChange
        #if you're sleeping you're not doing anything else
        if self.states.get("isSleeping"):
            self.health += 2
            self.vigor += 2
            self.fear = 0
            self.states["isInjured"]=False
            self.curiosity = self.maxScale/2
            self.stateChange += "sleeping"

        if not self.states.get("isSleeping"):
            #basic meter relationships
            if self.health < self.maxScale/5:
                self.fear += 1 #20% near death fear
            if self.vigor == 0:
                self.health -= 1
                self.states["isTired"] = True
            if self.health == self.maxScale: self.curiosity += 3
            if self.health < (self.healthMax/5): self.fear += 5 #near death
            #self.speed = float(self.health)/float(self.maxScale)
            if self.satiety == 0: self.vigor -= 1
            if self.fear == 0:
                self.curiosity += 1
            else:
                self.curiosity = 0
            if self.health == self.healthMax: self.curiosity += 1
            if self.states.get("isWithFriends"): self.fear -= 2
            if self.curiosity == self.maxScale:
                self.states["isCurious"] = True
            #state and change to meter change
            if self.vigor < self.vigorMax*0.2: self.isTired = True
            if self.vigor > self.vigorMax*0.6: self.isTired = False
            if self.states.get("isInjured"):
                self.health -= 1
                self.fear += 1
            if not self.states.get("wasInjured") and self.states.get("isInjured"): #init hit
                self.healthMax -= 200
                self.vigorMax -= 200
                self.fear += 100
            if not self.states.get("wasScared") and self.states.get("isScared"): #init hit
                self.curiosity = 0
                self.fear += 250
                self.satiety += 250
                self.health += 250
                self.speed += .005
            if self.states.get("isMoving"):
                self.distance += self.speed
                self.satiety -= 2
                self.fear -= 1
            else: self.satiety -= 1
            if self.states.get("isEating"):
                self.satiety += 7 #full ?
                self.health += 3 # just a little
                self.vigor += 5 # more
            if not self.states.get("isMoving"): self.vigor += 2
            if self.states.get("isWithFriends"): self.vigor += 1
        #basic meter clamping
        if self.health > self.healthMax: self.health = self.healthMax
        if self.vigor > self.vigorMax: self.vigor = self.vigorMax
        if self.satiety > self.maxScale: self.satiety = self.maxScale
        if self.fear > self.maxScale: self.fear = self.maxScale
        if self.curiosity > self.maxScale: self.curiosity = self.maxScale
        if self.health <0: self.health = 0
        if self.vigor <0: self.vigor = 0
        if self.satiety <0: self.satiety = 0
        if self.fear <0: self.fear = 0
        if self.curiosity <0: self.curiosity = 0
        return self.stateChange


"""
    def updateOnlyOnce(state, isState, wasState):
        if self.wasState: self.wasState = False
        if self.isState and not self.wasState:
            self.wasState = True
            self.stateChange += str(state)
            self.state = False
"""
