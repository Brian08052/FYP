import matplotlib as plt
import string

class sampleObject:
  COMPLETE_VALUE = 5



  def __init__(self, dbID, key, data):
    self.dbID = dbID
    self.key = key
    self.errorMessage = "Data OK"
    self.dataString = self.stripCharacters(str(data))
    self.dataArray = self.strToArray(self.dataString)
    self.dataArray = self.removeTailingNones(self.dataArray)

    self.cleanArray, self.cleanArrayIndex = self.cleanData(self.dataArray)
    self.removeindex = self.removeValues()
    self.isComplete = self.cleanArray != None and self.cleanArray[len(self.cleanArray)-1] < self.COMPLETE_VALUE


  def cleanDataAvailable(self):
    return not self.cleanArray == None

  def figuresRemoved(self):
    return self.removeindex > 0

  def removeValues(self):
    i = 0
    if self.cleanArray != None and len(self.cleanArray) > 4:
      if self.cleanArray[i+2] > self.cleanArray[i+3] * 15:
        return 3
      elif self.cleanArray[i+1] > self.cleanArray[i+2] * 15:
        return 2
      elif self.cleanArray[i] > self.cleanArray[i+1] * 15:
        return 1
      
    return 0

  def getAlteredAxes(self, adjusted = False):

    if adjusted:
      array, index = self.getAdjustedArray(True) 
    else:
      array, index = self.cleanArray, self.cleanArrayIndex

    if sum(index) == 0:
      return [[array, [i for i in range(len(array))]]]

    xAx1 = []
    xAx2 = []
    yAx1 = []
    yAx2 = []

    for i in range(len(index)):
      if index[i] == 0:
        xAx1 += [array[i]]
        yAx1 += [i]
      else:
        xAx2 += [array[i]]
        yAx2 += [i]
    return [[xAx1, yAx1], [xAx2, yAx2]]

  def getCleanArray(self, withAxis = False):
    if withAxis:
      return [self.cleanArray, self.cleanArrayIndex]
    else:
      return self.cleanArray

  def getAdjustedArray(self, withAxis = False):
    print('CA ', self.cleanArray)
    if self.cleanArray == None:
      adjustedArray, adjustedArrayIndex = None, None
    else:
      adjustedArray, adjustedArrayIndex = self.cleanArray[self.removeindex:], self.cleanArrayIndex[self.removeindex:]

    if withAxis:
      return [adjustedArray, adjustedArrayIndex]
    else:
      return adjustedArray



  def stripCharacters(self, s):
    s.replace(' ', '')
    chars = set(string.ascii_lowercase + string.ascii_uppercase + string.punctuation)
    chars.remove(',')
    #chars.remove("'")
    for c in chars:
      s = s.replace(c, '')

    return s

  def strToArray(self, s):
    s = self.stripCharacters(s)


    arr = s.split(',')
    returnArray = []
    for s in arr:
        if s == '' or s == ' ':
            returnArray += [None]
        else:
            #error checking
            returnArray += [float(s)]
    return returnArray

  def cleanData(self, array):
    #I don't think that would ever happen?
    if len(array) < 1:
      return None, None

    array = self.removeTailingNones(array)
  
    origArray = array.copy()
    alteredArray = []
    indexOfLast = 0

    for i in range(len(origArray)):
        if origArray[i] == None:
            alteredArray += [1]
        else:
            indexOfLast = i
            alteredArray += [0]
    
    array, alteredArray = array[:indexOfLast+1], alteredArray[:indexOfLast+1]
    array = self.fillZeroForNone(array)
    array = self.clearRecurrence(array)

    if self.tooManyBlanks(array):
      return None, None
    else:
      return self.replaceNones(array), alteredArray


  def removeTailingNones(self, array):
    lastIndex = len(array)-1
    if array[lastIndex] == None:
      lastIndex -= 1
    return array[:lastIndex+1]


  def fillZeroForNone(self, sample):
      #recursive function that replaces Nones with 0 if the next value in the array is 0.
      #clear recurrence handles nones that come after
      for i in range(len(sample)):
          if sample[i] == 0:
              if sample[i-1] == None:
                  sample[i-1] = 0
                  sample = self.fillZeroForNone(sample)
      return sample

  def clearRecurrence(self, sample):
      #We're not interested in the cases where the cancer comes back.
      #If the number gets low enough, everything that comes after is set to zero.

      #if the sample gets low enough, everything after is set to zero.
      #this is to learn the general sequence of decay without reoccurance
      flag = False
      for i in range(len(sample)):
          if flag == True:
              sample[i] = 0
          if sample[i] != None and sample[i] <= 3:
              flag = True

      return sample

  def tooManyBlanks(self, sample):###
      #Checks if the sample has 3 Nones in a row.

      #Must be clearRecurrence() sample first!
      i = 0
      counter = 0
      while i < len(sample):
          if sample[i] == None:
              counter+=1
          else:
              counter = 0
          if counter == 3:
              return True
          i+= 1
      return False

  def replaceNones(self, sample):
      #Data needs to be checked first that first element isnt none
      #if sample[0] is None: return None
      #if there's 3 Nones, toss it I'd say.

      tempArr = []

      for i in range(len(sample)):
          if sample[i] == None:
              if sample[i+1] != None:
                  value = (sample[i-1] + sample[i+1])/2
                  sample[i] = value
              else:
                  difference = sample[i-1] - sample[i+2]
                  sample[i] = round(sample[i-1] - difference/3)
                  sample[i + 1] = round(sample[i] - difference/3)

      return sample


  def fillInNones(self, tempArray):
      #Helper Fuction for replace Nones!
      #print(tempArray)
      #Assumes the middle is entirely Nones
      #This is nice code. Put in a better function than average tho
      if len(tempArray) <= 2:
          return False

      first = tempArray[0]
      last = tempArray[len(tempArray) - 1]
      gap = (first - last)

      average = gap/(len(tempArray)-1)

      for i in range(len(tempArray)-2):#so if four, goes 1, 2
          tempArray[i+1] = int(round(first - (average * (i +1))))
      return tempArray




  def getTableHTML(self, adjusted = False):
    if adjusted:
      array, index = self.getAdjustedArray(True)
    else:
      array = self.cleanArray
      index = self.cleanArrayIndex


    arrayEnd = None
    table = """<table style = "border: 1px solid black;"><tr>"""
    for i in range(len(array)):
      if index[i] == 0:
        table += """<td style = "border: 1px solid black;" >%s</td>"""%(int(array[i]))
      else:
        table += """<td style="color:red; border: 1px solid black;">%s</td>"""%(int(array[i]))

    table += "</tr></table>"

    return table 























































  def getMatchingValues(self):
    matchingValues = []
    for i in self.index:
      matchingValues += [self.data[i]]
    return matchingValues

  def getLoss(self):
    loss = []
    for i in range(len(self.matchingValues)):

      loss += [abs(self.matchingValues[i] - self.searchArray[i])]

    return (self.searchArray, self.matchingValues, loss)

  def getTotalLoss(self):
    loss = 0
    for i in self.getLoss()[2]:
      loss += i

    return loss


  def getArraysToGraph(self):
    arrays = ('array1', 'offsets')
    
    #The data from the first matching value onward. The offsets are here just [0, 1, 2...]
    matchingData = self.data[self.index[0]:]
    matchingDataOffsets = []
    for i in range(len(self.searchArray)):
      matchingDataOffsets += [i]


    valueToRemove = removeFirstValue(self.data)
    if self.index[0] < valueToRemove:
      valueToRemove = self.index[0]

    adjustedFullArray = self.data[valueToRemove:]
    adjustedFullArrayOffsets = []
    for i in range(len(self.searchArray)):
      adjustedFullArrayOffsets += [self.index[i] - valueToRemove]

    
    return (matchingData, matchingDataOffsets, adjustedFullArray, adjustedFullArrayOffsets)

  def getMatchingAxes(self):
    return [[self.matchingData, [i for i in range(len(self.matchingData))]],[self.searchArray, self.matchingDataOffsets]]

  def getFullAxes(self):
    return [[self.adjustedFullArray, [i for i in range(len(self.adjustedFullArray))]], [self.searchArray, self.adjustedFullArrayOffsets]]

  # def getTableHTML(self):
  #   arrayEnd = None
  #   table = "<table><tr>"
  #   for i in range(len(self.data)):
  #     table += "<th>%s</th>"%(int(self.data[i]))
  #     if int(self.data[i]) == 0 and i >= self.index[len(self.index)-1]: 
  #       arrayEnd = i
  #       break
  #   table += "</tr><tr>"

  #   if arrayEnd != None:
  #     for i in range(arrayEnd):
  #       if i in self.index:
  #         table += "<td>%s</td>"%(int(self.searchArray[i-self.index[0]]))
  #       else:
  #         table += "<td></td>"

  #   else:
  #     for i in range(len(self.data)):
      
  #       if i in self.index:
  #         table += "<td>%s</td>"%(int(self.searchArray[i-self.index[0]]))
  #       else:
  #         table += "<td></td>"

  #   table += "</tr></table>"

  #   return table 

  def getName(self):
    return str(self.dbID) + '-' + str(self.key)

  def predict(self, number):
    loss = None
    result = None
    prediction = None
    for i in range(len(self.data)):
      localLoss = abs(number - self.data[i])
      if loss == None or localLoss < loss:
        result = self.data[i]
        if i == len(self.data)-1:
          prediction = self.data[i]
        prediction = self.data[i+1]
        loss = localLoss

    return(prediction, result, loss)

