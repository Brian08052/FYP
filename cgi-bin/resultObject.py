from code import removeFirstValue

class resultObject:
  #OK. So. 
  #Takes in basically, the full sample, the searchArray, the index of where the values match.
  #Can get you the matching values (ooh)

  def __init__(self, dbID, key, index, data, searchArray):
    self.dbID = dbID
    self.key = key
    self.index = index
    self.data = data

    self.matchingValues = self.getMatchingValues()

    self.searchArray = searchArray
    arraysToGraph = self.getArraysToGraph()

    self.matchingData = arraysToGraph[0]
    self.matchingDataOffsets = arraysToGraph[1]
    self.adjustedFullArray = arraysToGraph[2]
    self.adjustedFullArrayOffsets = arraysToGraph[3]

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

  def getTableHTML(self):
    arrayEnd = None
    table = "<table><tr>"
    for i in range(len(self.data)):
      table += "<th>%s</th>"%(int(self.data[i]))
      if int(self.data[i]) == 0 and i >= self.index[len(self.index)-1]: 
        arrayEnd = i
        break
    table += "</tr><tr>"

    if arrayEnd != None:
      for i in range(arrayEnd):
        if i in self.index:
          table += "<td>%s</td>"%(int(self.searchArray[i-self.index[0]]))
        else:
          table += "<td></td>"

    else:
      for i in range(len(self.data)):
      
        if i in self.index:
          table += "<td>%s</td>"%(int(self.searchArray[i-self.index[0]]))
        else:
          table += "<td></td>"

    table += "</tr></table>"

    return table 

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
        else:
          prediction = self.data[i+1]
        loss = localLoss

    return(prediction, result, loss)