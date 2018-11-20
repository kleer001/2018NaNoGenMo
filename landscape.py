# -*- coding: utf-8 -*-


class landscape:

    def __init__(self):

        self.moonphases=["New Moon","Waxing Crescent", "First Quarter", "Waxing Gibbous",
            "Full Moon", "Waning Gibbous", "Third Quarter", "Waxing Crescent"]

        self.landscapes = {
            "origin":["cave","ocean","beach"],
            "natural":["marsh","swamp","river","scrubland","forest","plains",
            "badlands","heath","valley","desert","oasis"],
            "human":["cabin","town","city","suburbs","farmlands","plantation","orchard","station"],
            "ending":["foothills","mountain","tundra","icefields","summit","cave"]}

        self.pathBlock = ["avalanche","rockslide","washed out","fog","bombing","currents","sinkhole","earthquake",
            "flash flood","flood","tar pits","high tide","forest fire","fire","brambles","angry animals","bad juju",
            "indescribable feeling","sheer wall","awful smell","football game","cricket game","frisbee game","casm",
            "field of beautiful flowers","milling animals"]

        self.habitats={
            "UrbanAreasAndFarms":["cabin","town","city","suburbs","farmlands","plantation","orchard","station"],
            "TemperateForest":["forest","valley","health"],
            "ConiferousForest":["cave","forest","foothills","scrubland"],
            "PolarRegion":["mountain","tundra","icefields","summit"],
            "Oceans":["ocean","beach"],
            "Mountains":["foothills","mountain","icefields","summit","cave"],
            "Grasslands":["plains","badlands","scrubland","heath"],
            "Freshwater":["marsh","swamp","river"],
            "Desert":["desert","oasis"],
            "CoralReefs":["beach","ocean"]}

        self.jouney = []

    def findHabitat(self,search_landscape):
        habitatList = []
        for habitat, landscape in self.habitats.iteritems():
            for part in landscape:
                if part == search_landscape:
                    habitatList.append(habitat)
        return habitatList

