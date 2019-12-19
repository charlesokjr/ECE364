#######################################################
#    Author:      Ethan Glaser
#    email:       glasere@purdue.edu
#    ID:           ee364a13
#    Date:         8/27/19
#######################################################
import os  # List of  module  import  statements
import sys  # Each  one on a line
import pprint as pp
#######################################################
# No Module -Level  Variables  or  Statements!
# ONLY  FUNCTIONS  BEYOND  THIS  POINT!
#######################################################
def searchForNumber():
    n = 1

    while(n):
        if isPermutation(n, 2*n) and isPermutation(n, 3*n) and isPermutation(n, 4*n) and isPermutation(n, 5*n) \
                and isPermutation(n, 6*n):
            return n
        n += 1

def isPermutation(a, b):
    aArray = []
    bArray = []

    while a > 0:
        aArray.append(a % 10)
        a = int(a/10)
    while b > 0:
        bArray.append(b % 10)
        b = int(b/10)

    if len(aArray) != len(bArray):
        return False
    num = 1
    while aArray and num:
        num = 0
        for valA in aArray:
            for valB in bArray:
                if valA == valB:
                    aArray.remove(valA)
                    bArray.remove(valB)
                    num += 1
                    break

    if aArray == []:
        return True
    else:
        return False


def calculateChain():
    maxLength = 0
    for index in range(1, 1000001):
        if findLength(index) > maxLength:
            maxIndex = index
            maxLength = findLength(index)
    return maxIndex


def findLength(number):
    numArray = [number]
    while number != 1:
        if number % 2:
            number = 3 * number + 1
        else:
            number /= 2
        numArray.append(int(number))
    print(numArray)
    return len(numArray)


def calculateTensor(M1, M2):
    row = []

    final = []
    for index in range(0, len(M1)):
        for index2 in range(0, len(M1[index])):
            new = []
            for i in range(0, len(M2)):
                neww = []
                for i2 in range(0, len(M2[i])):
                    neww.append(M2[i][i2] * M1[index][index2])
                    neww.append(M2[i][i2] * M1[index][index2])
                if new:
                    new = [new, neww]
                else:
                    new = neww
        if final:
            final = [final, new]
        else:
            final = new

    return final



# This  block  is  optional  and  can be used  for  testing.
# We will  NOT  look  into  its  content.
#######################################################
if __name__ == "__main__":
    # Write  anything  here to test  your  code.
    #print(findLength(999999))

    M1 = [[1,2], [3,4]]
    M2 = [[0,5], [6,7]]
    print(calculateTensor(M1, M2))