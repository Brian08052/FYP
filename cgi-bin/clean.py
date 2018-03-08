import matplotlib as plt
import string
plt.use('Agg')

def strToArray(s):
    #For some reason theres a single quotation mark at the start of the string
    #maybe a database problem
    s = s.replace("'", "")

    chars = set(string.ascii_lowercase + string.ascii_uppercase + string.punctuation)
    chars.remove(',')
    #chars.remove("'")
    for c in chars:
        if c in s:
            print('None numeric or ',' value found', c, s)
            returnArray = [0]
    #if any((c in chars) for c in s):
        
    else:
    #turns a string line into an array
        arr = s.split(',')
        returnArray = []
        for s in arr:
            if s == '':
                returnArray += [None]
            else:
                #error checking
                returnArray += [float(s)]
    return returnArray

def stringToArr(fullSet):
    #Converts a text file into a an array of arrays
    #gets rid of the bit of string at the top of the txt file
    fullSet[0][0] = fullSet[0][0][3:]

    #make a new arr that will hold all our new arrays
    out = []
    for l in fullSet:
        #makes an array out of each string
        arr = strToArray(l[0])
        out += [arr]
    return out


###################################################################################################

def cleanSet(fullArray):

    cleanArray = []
    for sample in fullArray:
        fillZeroForNone(sample)
        clearRecurrence(sample)
        if not tooManyBlanks(sample):
            cleanArray += [replaceNones(sample)]

    return cleanArray


def cleanSample(sample, alteredArray = False):
    origSample = sample.copy()
    alteredArray = []
    indexOfLast = 0


    for i in range(len(origSample)):

        if origSample[i] == None:
            alteredArray += [1]
        else:
            indexOfLast = i
            alteredArray += [0]
    
    sample, alteredArray = sample[:indexOfLast], alteredArray[:indexOfLast]
    sample = fillZeroForNone(sample)
    sample = clearRecurrence(sample)

    if not tooManyBlanks(sample):
        if alteredArray:
            return replaceNones(sample), alteredArray
        else:
            return replaceNones(sample)
    else:
        return None #This is if theres too many blanks
    
def cleanDict(d, isString = True):
    cleanD = {}
    badKeys = []
    for key in d:
        if d[key] == 'XXX' or d[key] == 'Not entered':
            pass
        else:
            if isString:
                #print('clean', key, 'x', d[key], 'x')
                sample = strToArray(d[key])
            else:
                sample = d[key].copy()
            
            sample = cleanSample(sample)
            if sample == None:
                badKeys += [key]
            if sample != None:
                cleanD[key] = sample
                #cleanD[key] = sample

    print(badKeys)
    return cleanD




#************************************* Helper Functions*********************************


def fillZeroForNone(sample):
    #recursive function that replaces Nones with 0 if the next value in the array is 0.
    #clear recurrence handles nones that come after
    for i in range(len(sample)):
        if sample[i] == 0:
            if sample[i-1] == None:
                sample[i-1] = 0
                sample = fillZeroForNone(sample)
    return sample

def clearRecurrence(sample):
    #We're not interested in the cases where the cancer comes back.
    #If the number gets low enoguh, everything that comes after is set to zero.

    #if the sample gets low enough, everything after is set to zero.
    #this is to learn the general sequence of decay without reoccurance
    flag = False
    for i in range(len(sample)):
        if flag == True:
            sample[i] = 0
        if sample[i] != None and sample[i] <= 3:
            flag = True

    return sample

def tooManyBlanks(sample):###
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

def replaceNones(sample):
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



#     tempArr = []
#     for i in range(len(sample)):
#         if sample[i] == None:
#             tempArr +=[sample[i-1] , sample[i], sample[i+1]]
#             if sample[i+1] == None:
#                 tempArr += [sample[i+2]]
#             tempArr = fillInNones(tempArr)
#             for j in range(len(tempArr)):
#                 sample[i+j] = tempArr[j]
#     return sample

            #So now you have a temp array with either one or two Nones in the middle.

def fillInNones(tempArray):
    #Helper Fuction for replace Nones!
    #print(tempArray)
    #Assumes the middle is entirely Nones
    if len(tempArray) <= 2:
        return False

    first = tempArray[0]
    last = tempArray[len(tempArray) - 1]
    gap = (first - last)

    average = gap/(len(tempArray)-1)

    for i in range(len(tempArray)-2):#so if four, goes 1, 2
        tempArray[i+1] = int(round(first - (average * (i +1))))
    return tempArray






        ################################## Set statistics
###############################

def highestValuesInEachSample(dataSet):
    arr = []
    for d in dataSet:
        arr += [max(d)]
    return arr

def graphSample(sampleNumber):
    return
    #plot line


def updateDataframe():
    return
    #connect to DB
    #
