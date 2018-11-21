import markovify
import random
import glob
import os
from io import open
import sys
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
from nltk.tokenize import word_tokenize, sent_tokenize
reload(sys)
sys.setdefaultencoding("utf-8")

#basepath = os.path.dirname(os.path.realpath(__file__))
basepath = os.getcwd()
#allpaths = glob.glob(basepath)
#allpaths = [os.path.basename(x) for x in glob.glob(basepath)]
#allpaths = os.listdir(basepath)
allpaths = glob.glob(basepath+"\*_raw.txt")
#print allpaths
numfiles = len(allpaths)

text_model = []
textprobs = []
stopWords = set(stopwords.words('english'))

def cleanupWords(wordTokens):
    filtered = []
    stemmed = []
    for w in wordTokens:
        if w not in stopWords:
            filtered.append(w)
    for w in filtered:
        stemmed.append(stemmer.stem(w))
    return stemmed



for eachpath in allpaths:
	print "will make model from %s " % (eachpath)
	with open(eachpath,mode='r', errors='ignore') as a:
		texta = a.read()
		texta.encode('utf-8').strip()
	#textFiltered=cleanupWords(texta)
	#texta = cleanupWords(texta)
	tm = markovify.Text(texta,state_size=3)
	tm_write = tm.to_json()
	#write out
	text_file = open(eachpath+".tm", "w+")
	text_file.write(unicode(tm_write,"utf-8"))
	text_file.close()
	print "written %s model to file %s" % (eachpath,text_file)
	#read it back in:
	tm_read = markovify.Text.from_json(text_file.name)
	#sentence = tm_read.make_short_sentece(140)
	sentence = tm.make_short_sentence(150)
	print sentence
