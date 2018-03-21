from code import getCursor
from sampleObject import *
from resultObject import *
import math

class dictionaryObject:
    def __init__(self, dbID):
        self.dbID = dbID
        self.dictionary = self.createDictionary(dbID)
        self.objectDictionary = {}

        
        for key in self.dictionary:
            self.objectDictionary[key] = sampleObject(self.dbID, key, self.dictionary[key])


        self.cleanDictionary = {}
        for key in self.objectDictionary:
            self.cleanDictionary[key] = self.objectDictionary[key].cleanArray


    def createDictionary(self, dbID):
        d = {}
        cursor = getCursor()
        string = ("""select * from fypDB where dataID = '%s'"""%(dbID))
        cursor.execute(string)

        for row in cursor.fetchall():
            d[row['sampleID']] = row['sampleData'].decode("utf-8") 

        return d

    def getResultObjectsSearchN(self, array, n=1, lossFunction = 0, pr = False):
        results = self.searchN(array, n, lossFunction, pr)
        resultObjects = []
        for result in results:
            ro = resultObject(self.dbID, result[0], result[2], result[3], array)
            resultObjects += [ro]

        return resultObjects

    def searchN(self, array, n=1, lossFunction = 0, pr = False):

        dic2 = self.cleanDictionary
        
        lossFunctions = ('log', 'absolute')
        highestItem = None
        example = ('key', 'score', 'index', 'data')
        values = []

        #for key in dic2:
            #print(key, dic2[key], '<br>')
        
        for key in dic2:
            t = False
            if key == 91819:
                t = True


            #Cycles through each value in the dictionary, finding the sequence within it with the lowest matching array.
            sample = dic2[key]
            score = 0
            localIndex = None
            nextValue = 0

            #print(array, len(array),'<br>')
            #print(sample)
            #print(key)
            #print(len(sample), '<br>')

            #print('<br> LENS:', len(sample), len(array), '<br>')
            
            if(len(array)>=len(sample)):
                #really should set a flag
                # print("Len error")
                # print("Sample: ", sample)
                pass
                
            else:
                # print('key:', key)
                # print(len(sample), len(array), '<br>')
                dif = len(sample)-len(array)
                #Cycles the short array over the long one

                for i in range(dif):
                    #print('key:', key)
                    offsetScore = 0
                    offsetScores = []


                    #Goes through each element of the search array.
                    #The loss is sum i = 0 to n(SEARCH[i] - SAMPLE[i])
                    for i2 in range(len(array)):

                        loss = abs(array[i2]-sample[i2+i])
                        if lossFunction == 0:
                            if loss != 0:
                                loss = math.log(loss)




                        offsetScores += [loss]
                        offsetScore += abs(array[i2]-sample[i2+i])


                    #So, at the end of this, the offsetScore is the overall score
                    #the offsetScores is a list of the the individual losses.

                    #It does this for every possible offset

                    #print('<br>', highestItem, '<br>', score, '<br>',  offsetScore, '<br>', '<br>')
                    
                    #rint('End of sample', key, 'for one offset')

                    #set the highest item initially 
                    if highestItem == None:
                        #print('Here')
                        highestItem = (key, offsetScore, i)
                        #print(highestItem)



                    #print(score, i)
                    if(score == 0 or offsetScore<score ):
                        
                        
                        score = offsetScore
                        localIndex = i


                        #print('New lowest score for sample', key, 'score', score)


                #So at this point, you have the lowest score and index of the sample.
                #print(score, localIndex)

                #print('<br>Finished with sample', key, 'score:', score)
                #print('<br>', 'sample:', dic2[key], 'local Index:', localIndex, '<br>.<br>')
                indexArr = []
                if localIndex != None:
                    for x in range(len(array)):
                        indexArr += [x+localIndex]
                scoreObject = (key, score, indexArr, dic2[key])



                #print(len(values), n, len(values) < n)
                if(len(values) < n):
                    values.append(scoreObject)
                    highestItem = self.getHighestItem(values)

                elif score<highestItem[1]:
                     #print(highestItem)
                     #print(values)
                    values.remove(highestItem)
                    values.append(scoreObject)
                    highestItem = self.getHighestItem(values)


        return(values)


    def getHighestItem(self, lst):
        maxVal = 0
        highestValue = None
        for i in range(len(lst)):
            if lst[i][1] >= maxVal:
                maxVal = lst[i][1]
                highestValue = lst[i]
        return highestValue




