


def getInverse(l):
    l2 = []
    for i in l:
        l2 += [sum(l)-i]
    return l2

def searchSimilar(array, length, resultObjects):

  print('called')

  for i in range(length-len(array)):
    predictions = []
    predictedValues = []
    mostRecentValue = array[len(array)-1]
    #print('Number: ', mostRecentValue)
    for ro in resultObjects:
      #print('<br>', ro.data)
      result = ro.predict(mostRecentValue)
      #print('data: ', ro.data)
      #print('<br>result: ', result)
      predictions += [result]
      predictedValues += [result[0]]
    prediction = sum(predictedValues)/len(predictedValues)
    #print('<br> Prediction: ', prediction)
    array += [prediction]
  for i in range(len(array)):
    array[i] = int(array[i])
  return array

def searchSimilarLosses(array, length, resultObjects):

  print('called')

  for i in range(length-len(array)):
    predictions = []
    predictedValues = []
    predictedLosses = []
    mostRecentValue = array[len(array)-1]
    #print('Number: ', mostRecentValue)
    for ro in resultObjects:
      #print('<br>', ro.data)
      result = ro.predict(mostRecentValue)
      #print('data: ', ro.data)
      #print('<br>result: ', result)
      predictions += [result]
      predictedValues += [result[0]]
      predictedLosses += [result[2]]

    prediction = 0
    predictedLosses = getInverse(predictedLosses)

    for i in range(len(predictedValues)):
      prediction += predictedValues[i]*predictedLosses[i]
      if(sum(predictedLosses) == 0):
        prediction = 0
      else:
        prediction = prediction/sum(predictedLosses)
      


    array += [prediction]
  for i in range(len(array)):
    array[i] = int(array[i])
  return array

def getValuesK(array, length, resultObject)



def generatePrediction(method, array, length, resultObjects = None):
  predictionMethods = [(0, 'averageLoss'), (1, 'similarMatch'), (2, 'machineL1')]
  predictedArray = []

  if method == 0:
    predictedArray = averageLoss(array, length)

  if method == 1:
    predictedArray = searchSimilar(array, length)
    #pass

  if method == 2:
    predictedArray = averageLoss(array, length)

  return predictedArray



# class arrayPrediction:

#   def __init__(self, array, length):
#     self.array = array
#     self.length = length

#   


"""
Abstract class called predict
The rest are subclasses?
This actually makes sense, beyond the headache 

"""

def averageLoss(array, length):
  #handle bad length, bad arrays

  predictedArray = []

  if(len(array)) < 2:
    predictedArray = [array[0], array[0]/2]
  else:
    predictedArray = array

  percentLosses = []
  for i in range(1,len(array)):
    loss = array[i-1] - array[i] #usualy should be positive
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