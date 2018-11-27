# 2018NaNoGenMo
"The pilgrimage": a script generated novel of dubious readability. 

See here for notes taken during project planning: <a href="https://docs.google.com/document/d/e/2PACX-1vQDakFPuGF7lT94fR6fdbaq8aomGAQi5qzbWzwphf6v5fSrf0z5EaouQBOQC2e57LdzwY657O8rfT9e/pub"> NOTES </a>

<h3>"The Pilgrimage" is a simulated travel series of incarnations. Our hapless protagonist (You) walks, eats, is frightened, meets friends, sleeps, and over your lifetimes has, what I hope, is an entertaining adventure.</h3> 

The simulation is constructed from five continuously updated meters:
(check code for more accurate details)

*<b>Health</b>. Starts high, goes up with food, goes up with rest, goes down on injury, reduces max with injury, under 20% increases fear, at zero death, drives speed of travel

*<b>Vigor.</b> Starts high, Goes down with travel, goes up with rest, goes up with food, goes up with fellows, reduces max with injury, at zero subtracts from health

*<b>Satiety.</b> Starts high, goes up from food, goes down over time (4-6 hours), at zero subtracts from vigor

*<b>Fear</b>. Starts at zero, goes up from night noises, goes up from injury, goes up with strange animals, goes down with fellows, drives speed of travel, adrenaline response: quick health and satiate boost and crash after

*<b>Curiosity.</b> Starts middling, goes up with full heallth, goes up with zero fear, goes up with over 50% satiety, goes to zero with >0 fear, drives discovery of new things

---
I feel like I got 50% of what I wanted to get in there in there and spent about 1/3 of my time down dead ends and banging my head against technical problems (that I now know how to avoid).
---
<br>
I wanted, but wasn't able to get in:

* The curiosity meter of the simulation plugged into the narrative. It was a bottom up attribute where the driving forces (the ones that were easier to do) were all top down. 

* Weather and plants and more detailed converstaions with fellow travelers

* A degrading text function where the words get repeated, stemmed, or exchanged for similar word vectors as the book progressed and/or the protagonist becomes frightened or closer to death. 

* Ecosystem correct animals. I have a text file for each of seven different ones and plans to get it into the Darius Kazemi's Corpora Project but it still needed json formatting. 

* Scraped sentences from guttenberg project books. I have a pile of 50 or so books. 

* Summaries layer process for paragrahs of generated narrative. I have the library ready to go. 

* Queue system for behaviour instead of top down and piles of if statements


<b>Overall I am satisfied with the results. It is complete. And next year it can only be better!</b> 
