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
def processFile(symbol):
    try:
        with open(symbol + ".dat", "r") as f:
            newArray = []
            array = f.readlines()[2:]
            for line in array:
                if line[len(line) - 1: len(line)] == '\n':
                    line = line[:len(line) - 1]
                line = line.split(',')
                newArray.append(line)
            return newArray
    except IOError:
        return None


def getMaxDifference(symbol):
    data = processFile(symbol)
    if data == None:
        return None
    maxDif = 0
    for date in data:
        if float(date[4]) - float(date[5]) > maxDif:
            maxDif = float(date[4]) - float(date[5])
            maxDate = date[0]
    return maxDate

def getGainPercent(symbol):
    data = processFile(symbol)
    if data == None:
        return None
    numPos = 0
    numTot = 0
    for date in data:
        numTot += 1
        if float(date[1]) > float(date[3]):
            numPos += 1
    pctPos = float(format(100.0 * numPos / numTot, ".4f"))
    return pctPos


def getVolumeSum(symbol, date1, date2):
    data = processFile(symbol)
    if data == None:
        return None
    vol = 0
    for index in range(0, len(data)):
        if data[index][0] == date1:
            index1 = index
        if data[index][0] == date2:
            index2 = index
    if index1 <= index2:
        return None
    for index in range(index2, index1 + 1):
        vol += int(float(data[index][2]))
    return vol


def getBestGain(date):
    files = []
    bestGain = 0
    for file in os.listdir():
        if file[len(file) - 4:] == ".dat":
            files.append(file)
    for file in files:
        data = processFile(file[:len(file) - 4])
        for row in data:
            if row[0] == date:
                if (float(row[1]) - float(row[3])) / float(row[3]) * 100 > bestGain:
                    bestGain = (float(row[1]) - float(row[3])) / float(row[3]) * 100

    return float(format(bestGain, ".4f"))


def getAveragePrice(symbol, year):
    data = processFile(symbol)
    if data == None:
        return None
    avgSum = 0
    yearData = []
    for date in data:
        if int(float(date[0][:4])) == year:
            yearData.append(date)
    for date in yearData:
        avgSum += (float(date[1]) + float(date[3])) / 2
    avgSum /= len(yearData)
    return float(format(avgSum, ".4f"))


def getCountOver(symbol, price):
    data = processFile(symbol)
    if data == None:
        return None
    numDays = 0
    for date in data:
        if float(date[1]) >= price and float(date[3]) >= price and float(date[4]) >= price and float(date[5]) >= price:
            numDays += 1
    return numDays

# This  block  is  optional  and  can be used  for  testing.
# We will  NOT  look  into  its  content.
#######################################################
if __name__ == "__main__":
    # Write  anything  here to test  your  code.
    print(getAveragePrice('MSFT', 2019))