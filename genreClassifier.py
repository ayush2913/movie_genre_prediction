import tokenizer
from train_test_data import *
from trainer import Trainer
from classifier import Classifier
import json

Data = []

file = open('data', 'r')

Data = splitData(file)

genrePredictor = Trainer(tokenizer)

# You need to train the system passing each text one by one to the trainer module.

for movie in Data[0]:
    genrePredictor.train(movie['review'].strip(), movie['genre'].strip())

# When you have sufficient trained data, you are almost done and can start to use
# a classifier.
genreClassifier = Classifier(genrePredictor.data, tokenizer)

# Now you have a classifier which can give a try to classifiy text of news whose
# category is unknown, yet.

for movie in Data[1]:

	classification = genreClassifier.classify(movie['review'].strip())

# the classification variable holds the detected categories sorted
	print'{0}\t{1}'.format((classification),movie['genre'].strip())

