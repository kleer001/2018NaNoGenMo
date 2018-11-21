import markovify
import random
import glob
import string
import os
import unicodedata
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
getpath= os.path.abspath(basepath+'/*_raw.txt')
allpaths = glob.glob(getpath)
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
    #for w in filtered:
    #    stemmed.append(stemmer.stem(w))
    return filtered


for eachpath in allpaths:
	print "will make model from %s " % (eachpath)
	
	with open(eachpath,"r") as a:
		texta = a.read().replace('\n',' ')

	textList = texta.split(" ")
	textAscii = cleanupWords(textList)

	textUnicode = " ".join(textAscii)

	tm = markovify.Text(textUnicode,state_size=3)

	tm_write = tm.to_json()

	#write out
	text_file_name = eachpath+".json"
	text_file = open(text_file_name, "w+")
	text_file.write(unicode(tm_write,"utf-8"))
	text_file.close()
	#read it back in:
	with open(text_file_name) as f:
		jsonData=f.read()
	tm_read = markovify.Text.from_json(jsonData)
	sentence = tm_read.make_short_sentence(250)
	print sentence
