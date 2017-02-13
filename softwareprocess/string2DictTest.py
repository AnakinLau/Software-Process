'''
Created on Feb 13th, 2017

@author Anakin Lau
'''
import urllib
import softwareprocess.convertString2Dictionary as cs2d

print "First test blank"
print "Should be False"
print cs2d.convertString2Dictionary()
print "\n"

print "Now test random string"
print "Should be False"
print cs2d.convertString2Dictionary("a normal string")
print "\n"

print "abc%3D123"
print cs2d.convertString2Dictionary("abc%3D123")
print "\n"

print "function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse"
print cs2d.convertString2Dictionary("function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse")
print "\n"

print "Try with more spaces"
print "%20function%20%3D%20calculatePosition%20%20%2C%20%20%20sighting%20%20%3DBetelgeuse"
print cs2d.convertString2Dictionary("%20function%20%3D%20calculatePosition%20%20%2C%20%20%20sighting%20%20%3DBetelgeuse")
print "\n"

print "Try with space inbetween single word"
print "a%20bc%3D12%203"
print "Should be False"
print cs2d.convertString2Dictionary("a%20bc%3D12%203")
print "\n"

print "Try with Key starting with digit"
print "1bc%3D123"
print "Should be False"
print cs2d.convertString2Dictionary("1bc%3D123")

print "output"
print "function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse"
print cs2d.convertString2Dictionary("function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse")
print "\n"

outputValue = cs2d.convertString2Dictionary("function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse")
for key in outputValue.keys():
    print("key= {0}, value= {1}".format(key, outputValue[key]))

inputValue = urllib.quote("key=value, key1= value1, key2  =  value2,"
                          " key3  =  value3")
outputValue = cs2d.convertString2Dictionary(inputString=inputValue)
for key in outputValue.keys():
    print("key= {0}, value= {1}".format(key, outputValue[key]))

print "\nBelow we will try with same key, \nthis should fail!"
inputValue = urllib.quote("key=value, key1= value1, key  =  value2,"
                          " key3  =  value3")
outputValue = cs2d.convertString2Dictionary(inputString=inputValue)
for key in outputValue.keys():
    print("key= {0}, value= {1}".format(key, outputValue[key]))

print "\nBelow we will try using invalid seperator, \nthis should fail!"
print "urllib.quote(key=value, key1= value1 & key2  =  value2, key3  =  value3)"
inputValue = urllib.quote("key=value, key1= value1 & key2  =  value2,"
                          " key3  =  value3")
outputValue = cs2d.convertString2Dictionary(inputString=inputValue)
for key in outputValue.keys():
    print("key= {0}, value= {1}".format(key, outputValue[key]))

print "\nBelow we will try using NO seperator, \nthis should fail!"
print "urllib.quote(key=value, key1= value1  key2  =  value2, key3  =  value3)"
inputValue = urllib.quote("key=value, key1= value1  key2  =  value2,"
                          " key3  =  value3")
outputValue = cs2d.convertString2Dictionary(inputString=inputValue)
for key in outputValue.keys():
    print("key= {0}, value= {1}".format(key, outputValue[key]))


print "\nBelow we will try using invalid assigner, \nthis should fail!"
print "urllib.quote(key=value, key1 -> value1 , key2  =  value2, key3  =  value3)"
inputValue = urllib.quote("key=value, key1 -> value1 , key2  =  value2, key3  =  value3")
outputValue = cs2d.convertString2Dictionary(inputString=inputValue)
for key in outputValue.keys():
    print("key= {0}, value= {1}".format(key, outputValue[key]))

print "\nBelow we will try using invalid assigner but AlphaNumeric, \nthis should fail!"
print "urllib.quote(key=value, key1 4 value1 , key2  =  value2, key3  =  value3)"
inputValue = urllib.quote("key=value, key1 4 value1 , key2  =  value2, key3  =  value3")
outputValue = cs2d.convertString2Dictionary(inputString=inputValue)
for key in outputValue.keys():
    print("key= {0}, value= {1}".format(key, outputValue[key]))

print "\nBelow we will try using NO assigner, \nthis should fail!"
print "urllib.quote(key=value, key1  value1 , key2  =  value2, key3  =  value3)"
inputValue = urllib.quote("key=value, key1  value1 , key2  =  value2, key3  =  value3")
outputValue = cs2d.convertString2Dictionary(inputString=inputValue)
for key in outputValue.keys():
    print("key= {0}, value= {1}".format(key, outputValue[key]))

print "\nBelow we will try using 2 assigner, \nthis should fail!"
print "urllib.quote(key=value, key1 == value1 , key2  =  value2, key3  =  value3)"
inputValue = urllib.quote("key=value, key1 == value1 , key2  =  value2, key3  =  value3")
outputValue = cs2d.convertString2Dictionary(inputString=inputValue)
for key in outputValue.keys():
    print("key= {0}, value= {1}".format(key, outputValue[key]))

print "\nBelow we will try using correct number of assigner, but non-correct format \nthis should fail!"
print "urllib.quote(key=value, key1 == value1 , key2    value2, key3  =  value3)"
inputValue = urllib.quote("key=value, key1 == value1 , key2    value2, key3  =  value3")
outputValue = cs2d.convertString2Dictionary(inputString=inputValue)
for key in outputValue.keys():
    print("key= {0}, value= {1}".format(key, outputValue[key]))

print "\nBelow we will try using correct number of assigner, but non-correct format \nthis should fail!"
print "urllib.quote(key value =, key1 == value1 , key2    value2, key3  =  value3)"
inputValue = urllib.quote("key value =, key1 == value1 , key2    value2, key3  =  value3")
outputValue = cs2d.convertString2Dictionary(inputString=inputValue)
for key in outputValue.keys():
    print("key= {0}, value= {1}".format(key, outputValue[key]))

print "\nBelow we will try using correct number of assigner, but non-correct format \nthis should fail!"
print "urllib.quote(key=value, key1 = value1 , key2  4  value2, key3  ==  value3)"
inputValue = urllib.quote("key=value, key1 = value1 , key2  4  value2, key3  ==  value3")
outputValue = cs2d.convertString2Dictionary(inputString=inputValue)
for key in outputValue.keys():
    print("key= {0}, value= {1}".format(key, outputValue[key]))

print "\nBelow we will try using NON-AlphaNumeric, \nthis should fail!"
print "urllib.quote(key=value, key1= value1 , key2  =  val^ue2, key3  =  value3)"
inputValue = urllib.quote("key=value, key1= value1 , key2  =  val^ue2,"
                          " key3  =  value3")
outputValue = cs2d.convertString2Dictionary(inputString=inputValue)
for key in outputValue.keys():
    print("key= {0}, value= {1}".format(key, outputValue[key]))
