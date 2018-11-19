# -*- coding: utf-8 -*-


from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import os.path

def gutToText(number,name):
    filename = name+"_raw.txt"
    if os.path.isfile(filename)==Fale:
        book = open(filename,"w")
        text = strip_headers(load_etext(number)).strip()
        words = text
        print "Loaded and writing %s" % (name)
        book.write(words.encode('utf-8'))
        print "Done writing %s" % (name)
        book.close()

gutToText(215,"TheCallOfTheWild")
gutToText(1227,"ExpressionOfEmotion")
gutToText(910,"WhiteFang")
gutToText(9574,"PoemsOfNature")
gutToText(1322,"LeavesOfGrass")
gutToText(56436,"TheGreatValley")
gutToText(926,"TenThousandDreams")
gutToText(58118,"UsefulKnowledge3Animals")
gutToText(34063,"FiftyYearsTrapper")
gutToText(46884,"OriginManSuperstition")
gutToText(53419,"25GhostStories")
gutToText(145,"MiddleMarch")
gutToText(140,"TheJungle")
gutToText(12243,"RoundTheBlock")
gutToText(37423,"HowWeThink")
gutToText(30973,"EastSunWestMoon")
gutToText(42055,"YourMindUseIt")
gutToText(39064,"HegelsPhilosophyMind")
gutToText(41771,"HistoryOfSulu")
gutToText(56436,"TheGreatValley")
gutToText(8133,"GlipsesOfJapan")
gutToText(25948,"FiftyTwoStoriesForGirls")
gutToText(17208,"MotherGoose")
gutToText(38208,"AnimalStoryBook")
gutToText(24593,"OrientalStoryBook")
gutToText(56665,"TalesAndStories")
gutToText(55539,"KoreanTales")
gutToText(11339,"AesopFablesNew")
gutToText(39074,"CuriositiesOfMedical")
gutToText(26754,"OneThousandSecrets")
gutToText(57168,"LandBeyondForest")
gutToText(942,"GreenMansions")
gutToText(9846,"Excersions")
gutToText(18674,"ChineseWonder")
gutToText(27365,"TalesOfSpace")
gutToText(55626,"ScienceInShort")
gutToText(25267,"AstronomyForAmateurs")
gutToText(8855,"AstralWorship")
gutToText(14471,"EmptyHouseGhost")
gutToText(34607,"WoodcraftAndCamping")
gutToText(48929,"BackwoodsSurgery")
#NOmore!!!, you crazy





