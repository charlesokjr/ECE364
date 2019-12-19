#######################################################
#    Author:      <Ethan Glaser>
#    email:       <glasere@purdue.edu>
#    ID:           <ee364a13>
#    Date:         <9/24/19>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line


#######################################################
# No Module -Level  Variables  or  Statements!
# ONLY  FUNCTIONS  BEYOND  THIS  POINT!
#######################################################
def getDriversFor(carID):
    drivers = driverReader()
    cars = carReader()
    driveSet = set()
    if carID not in cars:
        raise ValueError("invalid car ID")
    for driver in drivers:
        if carID in drivers[driver]:
            driveSet.add(driver)
    return driveSet


def getCommonDriversFor(*args):
    drivers = driverReader()
    cars = carReader()
    d = set()
    carDict = getCarsFor(drivers.keys())
    for driver in carDict:
        status = True
        for arg in args:
            if arg not in carDict[driver]:
                status = False
        if status:
            d.add(driver)
    return d

def getCarsFor(names):
    cars = carReader()
    drivers = driverReader()
    carDict = {}
    for driver in names:
        carDict[driver] = set()
        for val in drivers[driver]:
            carDict[driver].add(cars[val])
    return carDict


def getBounds():
    signals = signalsReader()
    boundDict = {}
    for signal in signals:
        if signal != "Time":
            boundDict[signal] = min(signals[signal]), round(sum(signals[signal])/len(signals[signal]), 3), max(signals[signal])
    return boundDict


def getSampled(name):
    signals = signalsReader()
    if name not in signals:
        raise ValueError("invalid signal name")
    time = signals["Time"]
    data = signals[name]
    listSampled = []
    for index, val in enumerate(data):
        if (time[index] * 1000) % 1000 == 0:
            listSampled.append(data[index])
    return listSampled


def getDuration(start, end):
    signals = signalsReader()
    rangeDict = {}
    for index, val in enumerate(signals["Time"]):
        if val == start:
            min = index
        elif val == end:
            max = index
    for signal in signals:
        if signal != "Time":
            rangeDict[signal] = signals[signal][min:max+1]
    return rangeDict


def getValueAt(name, timestamp):
    timestamp = float(timestamp)
    signals = signalsReader()
    min = abs(signals["Time"][0] - timestamp)
    minIndex = 0
    for index, val in enumerate(signals["Time"]):
        if abs(val - timestamp) < min:
            min = abs(val - timestamp)
            minIndex = index
    finalVal = signals[name][minIndex]
    return finalVal


def signalsReader():
    with open('signals.dat', 'r') as f:
        signalDict = {}
        signalKey = f.readline()
        signalData = f.readlines()[1:]
    signalData2 = []
    signalKey = signalKey.split()
    for key in signalKey:
        signalDict[key] = []
    for line in signalData:
        signalData2.append(line.split())
    for line in signalData2:
        for index, val in enumerate(line):
            signalDict[signalKey[index]].append(float(line[index]))
    return signalDict


def driverReader():
    with open("drivers.dat", "r") as f:
        driverData = f.readlines()
    cars = driverData[1].split()
    data = driverData[3:]
    driverDict = {}
    for driver in data:
        driverArray = []
        dictArray = []
        line = driver.split('|')
        for val in line:
            driverArray.append(val.strip())
        for index, val in enumerate(driverArray):
            if val == 'X':
                dictArray.append(cars[index - 1])
        driverDict[driverArray[0]] = dictArray
    return driverDict


def carReader():
    carDict = {}
    with open("cars.dat", 'r') as f:
        carData = f.readlines()[2:]
    for line in carData:
        newLine = line.split('|')
        carDict[newLine[0].strip()] = newLine[1].strip()
    return carDict


# This  block  is  optional  and  can be used  for  testing.
# We will  NOT  look  into  its  content.
#######################################################
if __name__  == "__main__":
# Write  anything  here to test  your  code.
    #print(getValueAt('XDF846', 15.817))
    #print(carReader())
    #print(getCarsFor({'Sang, Chanell', 'Chock, Velvet'}))
    print(len(getCommonDriversFor('Mercedes Sprinter', 'Honda Accord', 'Ford Focus')))