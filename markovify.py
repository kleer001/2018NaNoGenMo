import markovify
import random
import glob
import os

basepath = os.path.dirname(os.path.abspath(__file__))

allpaths = glob.glob(basepath)
numfiles = len(allpaths)

text_model = []
textprobs = []


for eachpath in allpaths:
	if os.path.isfile(eachpath+".tm")==False:
		print "will make model from %s " % (eachpath)
		with open(eachpath) as a:
			texta = a.read()
		tm = markovify.Text(texta,state_size=3)
		tm_write = tm.to_json()
		#write out
		text_file = open(eachpath+".tm", "w")
		text_file.write(tm_write)
		text_file.close()
		print "written %s model to file" % (eachpath)
		#read it back in:
		#tm_read = markovify.Text.from_json(tm_write)
		#sentence = tm_read.make_short_sentece(140)
