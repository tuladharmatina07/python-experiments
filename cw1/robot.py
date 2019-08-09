userString = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

stringList = [each for each in userString.split(' ')]

countDict = {}

for each in stringList:
    if each not in countDict:
        countDict[each] = stringList.count(each)
print(countDict)

for k, v in countDict.items():
    print(k,':',v)