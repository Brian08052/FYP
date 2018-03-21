import matplotlib as plt
import math

plt.use('Agg')

def getHighestScore(lst):
    maxVal = 0
    index = -1
    for i in range(len(lst)):
        if lst[i][1] >= maxVal:
            maxVal = lst[i][1]
            index = i 
    return (index, maxVal)

def getHighestItem(lst):
    maxVal = 0
    highestValue = None
    for i in range(len(lst)):
        if lst[i][1] >= maxVal:
            maxVal = lst[i][1]
            highestValue = lst[i]
    return highestValue


def getValues(dic, value):
    key = value[0]
    loss = value[1]
    offsets = value[2]
    arr = []
    for i in offsets:
        print(dic[key][i])
        arr += [dic[key][i]]
    return arr

def search(array, dic2, pr = False):
    #needs to handle if array is longer than a sample
    globalLowestScore = None
    lowestSampleKey = None
    index = None

    
    
    for key in dic2:
        #Goes through each key.
        if(pr):
            print("Key ", key)
        
        sample = dic2[key]
        score = 0
        localIndex = None
        nextValue = 0
        
        if(len(array)>len(sample)):
            print("Len error")
            print("Sample: ", sample)
            
        else:
                
            dif = len(sample)-len(array)




            for i in range(dif):
                #Goes through the array, moving the search array along the sample, and calculating the loss.
                offsetScore = 0
                for i2 in range(len(array)):
                    # if(pr):
                    #     print('offsetScore: ', offsetScore, ' + ', array[i2]-sample[i2+i], '(', array[i2], ' - ', sample[i2+i], ')')


                    offsetScore += abs(array[i2]-sample[i2+i])


                #Ok, so here you have the score for the given offset.

                #is it the local lowest?
                    
                    
                if(pr):
                    print('Score, ID, offset, offsetScore: ', score, key, i, offsetScore)
                if(score == 0 or offsetScore<score ):
                    if(pr):
                        print("NEW LOWEST LOCAL, index: ", i)
                    score = offsetScore
                    localIndex = i
                else:
                    if(pr):
                        print("NOT LOWER.")

            #So at this point, you have the lowest score and index of the sample.
                    
            if(pr):
                print("Loop complete for ", key, " globalLowestScore == None: ", globalLowestScore == None)
                if globalLowestScore != None:
                    print(" score<globalLowestScore: ", score<globalLowestScore)
            if(globalLowestScore == None or score<globalLowestScore):
                if(pr):
                    print("NEW GLOBAL LOWEST SCORE: Score, Index, Key: ", score, localIndex, key)
                globalLowestScore = score
                index = localIndex
                lowestSampleKey = key


                
        indexArr = []
        for x in range(len(array)):
            indexArr += [x+index]

    if indexArr[len(indexArr)-1]>=len(dic2[lowestSampleKey]):
        nextValue = dic2[lowestSampleKey][indexArr[len(indexArr)-1]]
    else: 
        nextValue = dic2[lowestSampleKey][indexArr[len(indexArr)-1] + 1]

    
    return(lowestSampleKey, indexArr, globalLowestScore, nextValue)
    #return (1, [1], 1)

def searchN(array, dic2, n=1, lossFunction = 0, pr = False):
    
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
            print("Len error")
            print("Sample: ", sample)
            
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
                highestItem = getHighestItem(values)

            elif score<highestItem[1]:
                 #print(highestItem)
                 #print(values)
                values.remove(highestItem)
                values.append(scoreObject)
                highestItem = getHighestItem(values)


    return(values)


def scatter(matchingArray, offset, searchValues, imageName):
    pass
    #needs error raising if this doesn't work
    
    #If offset is an array, xAx2 = offset
    #if offset is an int, xAx2 is generated, ie if offset = 3, and search len is 4, offset = [3,4,5,6]

    # if isinstance(offset, int):
    #     xAx2 = []
    #     for i in range(len(searchValues)):
    #         xAx2 += [offset + i]
    # else:
    #     xAx2 = offset

    # xAx = []
    # for i in range(len(matchingArray)):
    #     xAx += [i]


    # plt.scatter(xAx, matchingArray, 25, 'blue')
    # plt.scatter(xAx2, searchValues,  25, 'red')

    # plt.draw()
    # plt.savefig(imageName)
    # plt.clf()
    # return imageName + '.png'
