#######################################################
#    Author:      Ethan Glaser
#    email:       glasere@purdue.edu
#    ID:           ee364a13
#    Date:         8/20/19
#######################################################
import os  # List of  module  import  statements
import sys  # Each  one on a line

#######################################################
# No Module -Level  Variables  or  Statements!
# ONLY  FUNCTIONS  BEYOND  THIS  POINT!
#######################################################
def find(pattern):
    # read string from sequence.txt
    # find matches of pattern - combo of digits and X (placeholder)
    # can return empty or single element list

    # load data into variable
    # create list of testable sequences
    # test each sequence
    testList = []
    finalList = []
    f = open("sequence.txt", "r")
    fullString = f.read()
    for i in range(0, len(fullString) - len(pattern) + 1):
        testList.append(fullString[i:(i + len(pattern))])

    for j in testList:
        status = True
        for k in range(0, len(pattern)):
            if pattern[k] != 'X' and pattern[k] != j[k]:
                status = False
        if status:
            finalList.append(j)

    f.close()
    return finalList


def getStreakProduct(sequence, maxSize, product):
    # search subsequences between 2 and maxSize for digital product of product
    # return list of all subsequences, in order of when they appear
    finalList = []
    testList = []
    for i in range(0, len(sequence) - 1):
        endIndex = maxSize
        if len(sequence) - i < maxSize:
            endIndex = len(sequence) - i
        for j in range(2, endIndex + 1):
            testList.append(sequence[i:i + j])
    for sub in testList:
        prod = 1
        for k in range(0, len(sub)):
            prod *= int(sub[k])
        if prod == product:
            finalList.append(sub)

    return finalList


def writePyramids(filePath, baseSize, count, char):
    # count number of pyramids with base size
    # separate by single space at the base
    # generate line for pyramid
    # generate whole pyramid
    # combine pyramids in list
    # write list to file
    f = open(filePath, "w")
    for i in range(0, int(((baseSize + 1) / 2))):
        line = ""
        fullLine = ""
        for j in range(0, int(((baseSize - 1 - 2 * i) / 2))):
            line += " "
        for j in range(0, 1 + 2 * i):
            line += char
        for j in range(0, int(((baseSize - 1 - 2 * i) / 2))):
            line += " "
        for k in range(0, count):
            if k:
                fullLine += " "
            fullLine += line
        f.write(fullLine)
        f.write("\n")

    f.close()
    return


def getStreaks(sequence, letters):
    # in order of appearance
    # any time letter appears
    currentString = ""
    streakList = []
    for i in range(0, len(sequence)):
        for letter in letters:
            if currentString:
                if sequence[i] != currentString[0]:
                    streakList.append(currentString)
                    currentString = ""
            if sequence[i] == letter:
                currentString += sequence[i]
    if currentString:
        streakList.append(currentString)

    return streakList


def findNames(nameList, part, name):
    # F, L, or FL for part
    # case does not matter in name
    finalList = []
    for test in nameList:
        if part == 'F':
            if test.split(' ')[0].lower() == name.lower():
                finalList.append(test)
        elif part == 'L':
            if test.split(' ')[1].lower() == name.lower():
                finalList.append(test)
        else:
            if test.split(' ')[0].lower() == name.lower() or test.split(' ')[1].lower() == name.lower():
                finalList.append(test)
    return finalList


def convertToBoolean(num, size):
    # represent input num as binary using boolean list
    # list must be at least size long - can add false to beginning
    boolList = []
    if type(num) != int:
        return boolList
    while num > 0 or size > len(boolList):
        if num % 2:
            boolList.insert(0, True)
            num -= 1
        else:
            boolList.insert(0, False)
        num /= 2
    return boolList


def convertToInteger(boolList):
    # opposite of convertToBoolean
    # take list of bools and convert to int
    # input must be LIST of BOOLEANS that is NOT EMPTY or else return 'None'
    if type(boolList) != list or len(boolList) == 0:
        return None

    if len(boolList) == 0:
        return None
    num = 0
    for i in range(0, len(boolList)):
        if type(boolList[i]) != bool:
            return None
        if boolList[i]:
            num += 2 ** (len(boolList) - i - 1)

    return num


# This  block  is  optional  and  can be used  for  testing.
# We will  NOT  look  into  its  content.
#######################################################
if __name__ == "__main__":
    # Write  anything  here to test  your  code.
    print(find("1234"))
    #print(getStreakProduct("11111", 10, 1))
    #writePyramids("pyramidTest.txt", 13, 6, "*")
    #print(getStreaks("abcdefghijklmnop", "ponmlkjihgfedcba"))
    #names = ["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield",
    #         "Johnson Cadence"]
    #print(findNames(names, "FL", "johNSOn"))
    #print(convertToBoolean(1.5, 10))
    #bList = [True, False, True]
    #print(convertToInteger(bList))