# -*- coding: utf-8 -*-

import random
import pycorpora as pyc

from pycorpora import humans
from pycorpora import animals

from pycorpora import foods
from pycorpora import materials
from pycorpora import objects
from pycorpora import technology
from pycorpora import geography
from pycorpora import plants
from pycorpora import science
from pycorpora import words
from pycorpora import religion

#corpora
plant = pyc.plants
animal = pyc.animals
human = pyc.humans
food = pyc.foods
material = pyc.materials
objects = pyc.objects
tech = pyc.technology
arch = pyc.architecture
color = pyc.colors
medical = pyc.medicine
science = pyc.science
myth = pyc.mythology
words = pyc.words

#piles
proverbs = words.proverbs["proverbs"]
#/Friendship /Love /Relationships /Life /Health & Food  /Converation
#/Wisdom /Work /Animal Related  /Rural /Growth /Money /Business /Fools
quotes = words.oprah_quotes["oprahQuotes"]

encourage = words.encouraging_words["encouraging_words"]
interject = words.interjections["interjections"]
moods = human.moods["moods"]

greekgods = myth.greek_gods["greek_gods"]
monsters = myth.monsters["names"]
lovecraftgods = myth.lovecraft["deities"]
lovecraftmonsters = myth.lovecraft["supernatural_creatures"]

weather = science.weather_conditions["conditions"]

diagnosis = medical.diagnoses["codes"] # /desc
#explicity because the corpus is broke, sadface.jpg
bodilyfluid = [ "amniotic fluid", "aqueous humour", "vitreous humour", "bile", "blood", "blood serum", "cerebrospinal fluid", "cerumen", "earwax", "chyle", "chyme", "endolymph", "perilymph", "gastric acid", "gastric juice", "lymph", "mucus", "pericardial fluid", "peritoneal fluid", "pleural fluid", "pus", "rheum", "saliva", "sebum", "sputum", "synovial fluid", "sweat", "tears", "vomit" ]
bodypart = human.bodyParts["bodyParts"]

colors = color.paints["colors"] # /color

flowers = plants.flowers["flowers"]
plants = plants.plants["instruments"] # /name

passage = arch.passages["passages"]
cities = geography.us_cities["cities"] # /city
rivers = geography.rivers["rivers"] # /name
seas = geography.oceans["seas"] #/name

clothes = objects.clothing["clothes"]
objects = objects.objects["objects"]
appliances = tech.appliances["appliances"]
knots = tech.knots["knots"]
guns = tech.guns_n_rifles["weapons"]

horses = animals.horses["horses"]
donkeys = animals.donkeys["donkeys"]
cats = animals.cats["cats"] #one word only?
dogs = animals.dogs["dogs"] #two words only?
common = animals.common["animals"]
animals =  common #+ cats + dogs + horses + donkeys


descriptions = human.descriptions["descriptions"]
prefixes  = human.prefixes["prefixes"]
occupations = human.occupations["occupations"]
honorifics = human.englishHonorifics["englishHonorifics"]

american_firsts = human.firstNames["firstNames"]
american_lasts = human.lastNames["lastNames"]
spanish_firsts = human.spanishFirstNames["firstNames"]
spanish_lasts = human.spanishLastNames["lastNames"]
norway_firstBoys = human.norwayFirstNamesBoys["firstnames_boys_norwegian"]
norway_firstGirls = human.norwayFirstNamesGirls["firstnames_girls_norwegian"]
norway_lasts = human.norwayLastNames["lastnames_norwegian"]
fantasy_firsts = human.tolkienCharacterNames["names"]
author_lasts = human.authors["authors"]
wrestlers = human.wrestlers["wrestlers"]
richpeople = human.richPeople["richPeople"] # /name
firstnames = american_firsts + spanish_firsts + norway_firstBoys + norway_firstGirls + fantasy_firsts
lastnames = american_lasts + spanish_lasts + norway_lasts + author_lasts

rshipsMod = ["great","great-great"]
rships = ["mother","father","sister","brother","aunt","uncle","cousin","nephew","niece","grandpa","grandma"]
rshipsTert = ["once removed","twice removed","three times removed"]
rshipsEnd = "in-law"

def makeRelative():
    makeRelation = ""
    makeRelation += random.choice(rships) + " "
    if makeRelation[0] == "g":
        if random.randrange(0,5)==1: #grands only
            makeRelation = random.choice(rshipsMod) + " " + makeRelation
    if random.randrange(0,4)==1:
        makeRelation += random.choice(rshipsTert) + " "
    if random.randrange(0,3)==1:
        makeRelation += rshipsEnd + " "
    return makeRelation[:-1] #take off trailing space


""" #mix and match code
----------------------------- moar ---------------
"""

"""

totalpeeps = 15
prefix = random.sample(prefixes,totalpeeps)
name = random.sample(firstnames,totalpeeps)
famname = random.sample(lastnames,totalpeeps)
occupation = random.sample(occupations, totalpeeps)

animal = random.sample(animals,totalpeeps)

for person in zip(name,famname,occupation,animal):
    dramatasPersonae.append(" ".join(person))

for n in dramatasPersonae:
    print makeRelative() + n

"""

def deepsample(corpora,cdict,number):
    return [s[cdict] for s in random.sample(corpora,number)]

#BUILD IT#
tempdict = {}
#dumping grounds
dramatasPersonae = []# firstname-lastname aka wrestler
supplies = [] #clothes, gun, objects, appliance, knot
places = [] #rivers, cities, seas
interst = [] #plants, color-flowers
injuries = [] #color-body part, color-bodily fluid
quotes = [] # oprah_quotes & proverbs
dreams = [] # monsters, lovecraftgods, lovecraftmonsters
prayers = [] #greekgods

totalmix = 3

#bucket of things centric dictionary
tempdict.clear()
tempdict["gear"]=random.sample(objects,totalmix)
tempdict["clothing"]=random.sample(clothes,totalmix)
tempdict["gun"]=random.sample(guns,totalmix)
tempdict["appliance"]=random.sample(appliances,totalmix)
tempdict["knot"]=random.sample(knots,totalmix)
supplies.append(dict(tempdict))
print supplies

#person centric dictionary
relate = [makeRelative() for a in range(totalmix)]
name = random.sample(firstnames,totalmix)
famname = random.sample(lastnames,totalmix)
occupation = random.sample(occupations, totalmix)
nickname = random.sample(wrestlers, totalmix)
realname = deepsample(richpeople,"name",totalmix)
tempdict.clear()
for a,b,c,d,e,f in zip(relate, name, famname,occupation,nickname,realname):
    tempdict["relate"]=a
    tempdict["name"] = b
    tempdict["famname"] = c
    tempdict["occupation"] = d
    tempdict["nickname"] = e
    tempdict["realname"] = f
    dramatasPersonae.append(dict(tempdict))
    #print "My %s %s %s is a %s. They love %s and dream of %s sometimes." % (a,b,c,d,e,f)
print dramatasPersonae

tempdict.clear()
tempdict["seanames"] = [s['name'] for s in random.sample(seas,totalmix)]
tempdict["rivernames"] = [s['name'] for s in random.sample(rivers,totalmix)]
tempdict["citynames"] = [s['city'] for s in random.sample(cities,totalmix)]
places.append(dict(tempdict))
print places

