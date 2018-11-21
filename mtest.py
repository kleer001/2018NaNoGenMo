import markovify
import json

corpus = open("/Users/3crows/Dropbox/ai/code/2018NaNoGenMo/faeriesIhavemet_raw.txt").read()

text_model = markovify.Text(corpus, state_size=3)
model_json = text_model.to_json()
# In theory, here you'd save the JSON to disk, and then read it back later.

text_filename = "/Users/3crows/Dropbox/ai/code/2018NaNoGenMo/faeriesIhavemet_raw.json"
text_file = open(text_filename, "w+")
text_file.write(model_json)
text_file.close()

with open(text_filename) as f:
	jsonData = f.read()

reconstituted_model = markovify.Text.from_json(jsonData)
print reconstituted_model.make_short_sentence(200)