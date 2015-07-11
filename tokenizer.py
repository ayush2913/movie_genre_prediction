import string

def tokenize(text):
	commonWords=['the','be','to','of','and','a','in','that','have','it','is','im','are','was','for','on','with','he','as','you','do','at','this','but','his','by','from','they','we','say','her','she','or','an','will','my','one','all','would','there','their','what','so','up','out','if','about','who','get','which','go','me','when','make','can','like','time','just','him','know','take','person','into','year','your','some','could','them','see','other','than','then','now','look','only','come','its','over','think','also','back','after','use','two','how','our','way','even','because','any','these','us']
	exclude = set(string.punctuation)
	text = ''.join(ch for ch in text if ch not in exclude)
	list = text.lower().split(' ')
	for word in list:
		if((len(word.strip())<=2)):
			list.remove(word)
		elif(word in commonWords):
			list.remove(word)
	return list
