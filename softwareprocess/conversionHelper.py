import math

# Helper methods getting degrees and minutes
# Does not work with a negative zero~
def getObservationDegToInt(observationInput):
    posOfd = observationInput.find('d')
    degString = observationInput[0: posOfd]
    print('degString= {0}'.format(degString))
    if(degString == '-0'):
        return -0.0
    return int(degString)


def getObservationMinToFloat(observationInput):
    posOfd = observationInput.find('d')
    minString = observationInput[posOfd + 1: len(observationInput)]
    return float(minString)


def convertMinToNumber(minNum):
    return float(minNum/60)

# Does not work with a negative zero~
def convertDegMinToNumber(degInput, minInput):
    print('convertDegMinToNumber degInput= {0}'.format(degInput))
    if(degInput < 0 ):
        return degInput - convertMinToNumber(minInput)
    else:
        return degInput + convertMinToNumber(minInput)

def convertDegMinStrToNumber(degMinStr):
    posOfd = degMinStr.find('d')
    degString = degMinStr[0: posOfd]
    if(degString == '-0'):
        return convertDegMinToNumber(-1,
                          getObservationMinToFloat(degMinStr)) +1
    else:
        return convertDegMinToNumber(getObservationDegToInt(degMinStr),
                          getObservationMinToFloat(degMinStr))

def convertNumToDegMinString(numInput):
    print ("convertNumToDegMinString numInput= {0}".format(numInput))
    if numInput >= 0:
        decimalNum = float(numInput % 1)
    else:
        decimalNum = float((numInput * -1) % 1)
    deg = 0
    mins = round((decimalNum * 60),1)
    leftOver = mins / 60
    if(leftOver >= 1):
        print ("leftOver {0} is >= 1")
        deg = int(leftOver)
        mins = mins - (60 * leftOver)
    if(numInput < 0):
        deg = -1 * deg
    deg = deg + int(numInput)

    # make sure if it's bigger than 360deg it is chopped
    if(deg > 360):
        deg = deg % 360
    elif (deg < -360 ):
        deg = deg * -1
        deg = (deg % 360) * -1

    return str(deg) + 'd' + str(mins)

def convertDegMinToArcMinInt(degMinString):
    posOfd = degMinString.find('d')
    degString = degMinString[0: posOfd]
    minString = degMinString[posOfd + 1: len(degMinString)]
    #int(minString)
    #print('degString= {0}'.format(degString))
    if('-' in degString):
        return (int(degString) * 60) - round((minString))
    else:
        return (int(degString) * 60) + round((minString))
