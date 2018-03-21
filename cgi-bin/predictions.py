#!/usr/local/bin/python3
from dictionaryObject import *
from cgitb import enable 
enable()

class predictionObject:


    def __init__(self):
        self.x = 'x'

    def getInverse(self, l):
        l2 = []
        for i in l:
            l2 += [sum(l)-i]
        return l2

    def searchSimilar(self, array, length, n, dictionaryObject):
        resultObjects = dictionaryObject.getResultObjectsSearchN(array, n)
        resultArray = self.searchSimilarPredict(array, length, resultObjects)
        return resultArray



    def searchSimilarPredict(self, array, length, resultObjects):
        for i in range(length-len(array)):
            predictions = []
            predictedValues = []
            mostRecentValue = array[len(array)-1]
            for ro in resultObjects:
                result = ro.predict(mostRecentValue)
                predictions += [result]
                predictedValues += [result[0]]
            prediction = sum(predictedValues)/len(predictedValues)
            array += [prediction]

        for i in range(len(array)):
            array[i] = int(array[i])

        return array

    def searchSimilarLosses(self, array, length, n, dictionaryObject):
        resultObjects = dictionaryObject.getResultObjectsSearchN(array, n)
        resultArray = self.searchSimilarLossesPredict(array, length, resultObjects)
        return resultArray


    def searchSimilarLossesPredict(self, array, length, resultObjects):
        for i in range(length - len(array)):
            predictions = []
            predictedValues = []
            predictedLosses = []
            mostRecentValue = array[len(array) - 1]

            # print('Number: ', mostRecentValue)

            for ro in resultObjects:

              # print('<br>', ro.data)

                result = ro.predict(mostRecentValue)

              # print('data: ', ro.data)
              # print('<br>result: ', result)

                predictions += [result]
                predictedValues += [result[0]]
                predictedLosses += [result[2]]

            prediction = 0
            predictedLosses = self.getInverse(predictedLosses)

            for i in range(len(predictedValues)):
                prediction += predictedValues[i] * predictedLosses[i]
                if sum(predictedLosses) == 0:
                    prediction = 0
                else:
                    prediction = prediction / sum(predictedLosses)

            array += [prediction]
        for i in range(len(array)):
            array[i] = int(array[i])
        return array


    def averageLoss(self, array, length, n = None, dictionaryObject = None):
    #handle bad length, bad arrays
        predictedArray = []

        if(len(array)) < 2:
            predictedArray = [array[0], array[0]/2]
        else:
            predictedArray = array

        percentLosses = []
        for i in range(1,len(array)):
            loss = array[i-1] - array[i] #usualy should be positive
            if array[i-1] == 0:
            	break
            percentLosses += [loss/array[i-1]]



        for i in range(len(predictedArray), length-1):#need to get a value for i+1 to # so if its 3, 3 to 30
            #previous value is i-1
            if(array[i-1] == 0 or array[i-2] == 0): #dont know if you need i-2 #you do
                predictedArray += [0]

            else:
                loss = array[i-2] - array[i-1]
                percentLosses += [loss/array[i-2]]
                averageLoss = sum(percentLosses)/len(percentLosses)
                value = array[i-1]*averageLoss

                if value < 2:
                    predictedArray += [0]
                else:
                    predictedArray += [int(array[i-1]*averageLoss)]


        return predictedArray



print('Content-Type: text/html')
print()


def compare(array1, array2):
	lossScore = 0
	for i in range(len(array1)):
		difference = abs(array1[i]-array2[i])

		if array1[i] == 0:
			percentDifference = difference

		else:
			percentDifference = difference/array1[i]

		lossScore += percentDifference

	return lossScore


def predict(function, sample, dictionaryObject, n = 3, cutOff = 5):

	newSample = sample[:cutOff]
	result = function(newSample, len(sample)+1, n, dictionaryObj)
	return result



dictionaryObj = dictionaryObject('CancerMolar')
result = dictionaryObj.searchN([1,2,3], 3)
resultO = dictionaryObj.getResultObjectsSearchN([1,2,3], 3) 
po = predictionObject()
a = [1000, 900, 876, 232]
n = 3
length = 25

# averageLoss = po.averageLoss(a.copy(), length)
# print(averageLoss)

# result = po.searchSimilarLosses(a.copy(), n, dictionaryObj, length)
# print(result)

a = [1000, 943, 755,432, 321,211,111,63,43,21]

functions = [po.averageLoss, po.searchSimilarLosses, po.searchSimilar]


r = predict(functions[1], a.copy(), dictionaryObj, cutOff = 5)


print(a)
cutOff = 5

for f in functions:
    print(f)
    losses = []
    for key in dictionaryObj.cleanDictionary:
        sample = dictionaryObj.cleanDictionary[key]
    if len(sample) > 5:
        r = predict(f, a.copy(), dictionaryObj, cutOff)
        # print(r)
        loss = compare(a, r)
        # print(loss)
        losses += [loss]
    print(sum(losses)/len(losses))

print(dictionaryObj)