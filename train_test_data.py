import ast
def splitData(data):
	names = []
	genre = []
	train = []
	test = []
	traincount=0
	testcount=0
	totalcount=0

	for line in data.readlines():
		movie = ast.literal_eval(line)
		if(movie['name'].strip() in names):
			continue
		else:
			names.append(movie['name'].strip())
			if(movie['genre'].strip() in genre):
				if(traincount<8 and testcount==0):
#					print 'checktrain'
					train.append(movie)
					traincount=traincount+1
					totalcount=totalcount+1
				if(traincount==8 and testcount<2):
#					print 'checktest'
					test.append(movie)
					testcount=testcount+1
					totalcount=totalcount+1
				if(totalcount==10):
					traincount=0
					testcount=0
					totalcount=0
			else:
				genre.append(movie['genre'].strip())
				train.append(movie)
				traincount=1
				totalcount=1
				testcount=0
	print len(names)
	return [train,test]
