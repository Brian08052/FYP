import matplotlib as plt
plt.use('Agg')



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



def scatter(matchingArray, offset, searchValues, imageName):
    #needs error raising if this doesn't work
    
    #If offset is an array, xAx2 = offset
    #if offset is an int, xAx2 is generated, ie if offset = 3, and search len is 4, offset = [3,4,5,6]

    if isinstance(offset, int):
        xAx2 = []
        for i in range(len(searchValues)):
            xAx2 += [offset + i]
    else:
        xAx2 = offset

    xAx = []
    for i in range(len(matchingArray)):
        xAx += [i]


    plt.scatter(xAx, matchingArray, 25, 'blue')
    plt.scatter(xAx2, searchValues,  25, 'red')

    plt.draw()
    plt.savefig(imageName)
    plt.clf()
    return imageName + '.png'
