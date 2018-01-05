from gensim.models import KeyedVectors
from gensim.models import Word2Vec

def load_model_w2v(filename):
	return KeyedVectors.load_word2vec_format(filename, binary=True)

def loadtxt(file):
	with open(file,"r",encoding='utf8') as myfile:
		return myfile.read()
def train_model_new(text):
	texts = text.split("\n")
	sentences = []
	for t in texts:
		words = t.split(" ")
		sentences.append(words)
	model = Word2Vec(sentences,min_count=1)
	return model

txt = loadtxt("raw01_cleaned.txt")
model = train_model_new(txt)
model.save('model.bin')
