#######################################################
#    Author:      <Ethan Glaser>
#    email:       <glasere@purdue.edu>
#    ID:           <ee364a13>
#    Date:         <9/3/19>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
#######################################################
# No Module -Level  Variables  or  Statements!
# ONLY  FUNCTIONS  BEYOND  THIS  POINT!
#######################################################
def getLeastFrequent():
    with open("numbers.dat", "r") as f:
        stringArray = f.readlines()
        numRow = []
        for row in stringArray:
            row = row.split(" ")
            for val in row:
                numRow.append(int(val))
        nums = []
        freqs = []
        for num in numRow:
            exists = False
            for existing in range(0, len(nums)):
                if nums[existing] == num:
                    freqs[existing] += 1
                    exists = True
            if exists == False:
                nums.append(num)
                freqs.append(1)
        low = freqs[0]
        for freq in range(0, len(freqs)):
            if freqs[freq] < low:
                low = freqs[freq]
                index = freq
        return nums[index]


def getCodeFor(coordinate):
    with open("coordinates.dat", "r") as f:
        stringArray = f.readlines()[2:]
        latList = []
        longList = []
        zipList = []
        finalList = []
        for stringRow in stringArray:
            latList.append(float(stringRow.split()[0]))
            longList.append(float(stringRow.split()[1]))
            zipList.append(stringRow.split()[2])
        for coord in range(0, len(zipList)):
            if latList[coord] == coordinate or longList[coord] == coordinate:
                finalList.append(zipList[coord])
        finalList.sort(key = str)
        return finalList


def getSubMatrixSum(startRowIndex, endRowIndex, startColumnIndex, endColumnIndex):
    with open("numbers.dat", "r") as f:
        stringArray = f.readlines()
        numRow = []
        for row in stringArray:
            row = row.split(" ")
            newRow = []
            for val in row:
                newRow.append(int(val))
            numRow.append(newRow)
        sum = 0
        for i in range(startRowIndex, endRowIndex + 1):
            for j in range(startColumnIndex, endColumnIndex + 1):
                sum += numRow[i][j]
        return(sum)


# This  block  is  optional  and  can be used  for  testing.
# We will  NOT  look  into  its  content.
#######################################################
if __name__  == "__main__":
    print(getLeastFrequent())