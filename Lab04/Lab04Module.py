#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line


#######################################################
# No Module -Level  Variables  or  Statements!
# ONLY  FUNCTIONS  BEYOND  THIS  POINT!
#######################################################
def getDifference(provider1, provider2):
    p1, p2 = readProvider(provider1), readProvider(provider2)
    set1, set2 = set(), set()
    for p, pp in zip(p1, p2):
        set1.add(p)
        set2.add(pp)
    return set1 - set2


def getPriceOf(sbc, provider):
    p = readProvider(provider)
    if sbc not in p:
        raise ValueError("Invalid sbc for " + provider)
    return p[sbc]


def checkAllPrices(sbcSet):
    providerData, sbcDict = {}, {}
    for prov in os.listdir('providers/'):
        providerData[prov.split(".dat")[0]] = readProvider(prov.split(".dat")[0])
    for sbc in sbcSet:
        sbcDict[sbc] = 0, ''
        for prov in providerData:
            if sbc in providerData[prov]:
                price, provider = providerData[prov][sbc], prov
                curPrice, curProv = sbcDict[sbc]
                if curPrice == 0 or curPrice > price:
                    sbcDict[sbc] = price, prov
    return sbcDict


def getFilter():
    phoneBook = {}
    filterDict = {}
    with open("phones.dat", "r") as f:
        data = f.readlines()[1:]
    for line in data:
        line = line.split(',')
        phoneBook[line[1][1:4] + line[1][6:9] + line[1][10:14]] = line[1].split('\n')[0]
    for num in range(1000):
        val = format(num, "03")
        numList = []
        for phone in phoneBook:
            if val in str(phone):
                numList.append(phoneBook[phone])
        if len(numList) == 1:
            filterDict[val] = numList[0]
    return filterDict


def readProvider(p):
    if p + '.dat' not in os.listdir('providers/'):
        raise ValueError("Invalid provider name: " + p)
    with open("providers/" + p + ".dat", "r") as f:
        data = f.readlines()
        provDict = {}
        for line in data:
            info = line.split()
            if len(info) == 4:
                provDict[info[0] + ' ' + info[1]] = float(info[3][1:])
        return provDict


# This  block  is  optional  and  can be used  for  testing.
# We will  NOT  look  into  its  content.
#######################################################
if __name__  == "__main__":
    # Write  anything  here to test  your  code.
    #print(getDifference("provider4", "provider1"))
    #print(getPriceOf('Rasp. Pi-4702MQ', 'provider2') == 1028.7)
    testSet = set()
    testSet.add('Rasp. Pi-6970HQ')
    testSet.add('Rasp. Pi-4810MQ')
    testSet.add('Rasp. Pi-4800MQ')
    print(checkAllPrices(testSet))
    a, b = checkAllPrices(testSet)['Rasp. Pi-4810MQ']
    print(type(a))
    print(type(b))
    #print(len(getFilter()) == 357)
    #print(getFilter()['465'] == '(448) 797-9465')
    #print(getFilter()['709'] == '(770) 933-7311')
    #print(getFilter()['770'] == '(770) 933-7311')

