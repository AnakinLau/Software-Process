'''
Created on Feb 12th, 2017

@author Anakin Lau
'''
import urllib

# Takes in a percent endcoded string, and output it as keys and values in
# a normal string.
def convertString2Dictionary(inputString = ""):
    # Continue value: this is false when the string is not as we want and we
    # want to quit the operation
    errorDict = {'error':'true'}
    if inputString == "":  # quit immediately if string is blank
        return errorDict

    global unquotedString
    unquotedString = urllib.unquote(inputString)
    # store number of entries by counting ","
    global entryCount
    entryCount = unquotedString.count(",") + 1
    # Creation of an output Dictionary
    outputDict = {}

    while (entryCount > 0):
        # if only one entry no need to count commas
        if entryCount == 1:
            commaPos = len(unquotedString)
        else:
            commaPos = unquotedString.index(",") # find pos of first comma

        # Substring each set of key and values with the below
        rawEntrySnippet = unquotedString[0: commaPos]
        #Shorten the unquoted string to be without that selection we just cut
        unquotedString = unquotedString[commaPos + 1: len(unquotedString)]
        if rawEntrySnippet.count("=") != 1:  # find num of = signs
            break
        equalPos = rawEntrySnippet.find("=")  # find pos of = sign
        keyString = rawEntrySnippet[0: equalPos]  # substring of key
        valueString = rawEntrySnippet[equalPos + 1: len(rawEntrySnippet)] # substring of value
        # strips the white spaces
        keyString = keyString.strip()
        valueString = valueString.strip()
        # Test first letter of Key to be alphabhet
        if not (keyString[0].isalpha()):
            break
        #check if the rest of key and value are both alphanumeric
        if not (keyString.isalnum() and valueString.isalnum()):
            break

        # Now we insert them into a dictionary
        # First we check if the key exists already
        if keyString in outputDict:
            break
        else:
            outputDict[keyString] = valueString

        if entryCount == 1:
            return outputDict
        entryCount = entryCount - 1

    return errorDict
