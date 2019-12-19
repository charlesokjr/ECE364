#######################################################
#    Author:      <Ethan Glaser>
#    email:       <glasere@purdue.edu>
#    ID:           <ee364a13 >
#    Date:         <9/10/19>
#######################################################
import os  # List of  module  import  statements
import sys  # Each  one on a line
from collections import Counter
#######################################################
# No Module -Level  Variables  or  Statements!
# ONLY  FUNCTIONS  BEYOND  THIS  POINT!
#######################################################


def stockReader():
    with open("stocks.dat", "r") as f:
        data = f.readlines()[2:]
        realData = []
        for line in data:
            realData.append(line.split("\n")[0].split(","))
        return realData


def transactionReader():
    with open('transactions.dat', 'r') as f:
        data = f.readlines()
        realData = {}
        for line in data:
            realData[line.split(": ")[0]] = Counter(line.split(': ')[1].split('\n')[0].split(', '))
        return realData


def getMonthlyVolume():
    stockDict = {}
    stocks = stockReader()
    for stock in stocks:
        if stock[0][:7] not in stockDict:
            stockDict[stock[0][:7]] = 0
        stockDict[stock[0][:7]] += int(float(stock[2]))
    return stockDict


def getCommonDays(year1, year2):
    year1Set = set()
    year2Set = set()
    stocks = stockReader()
    for stock in stocks:
        if stock[0][:4] == year1:
            year1Set.add((stock[0][5:7], stock[0][8:10]))
        elif stock[0][:4] == year2:
            year2Set.add((stock[0][5:7], stock[0][8:10]))
    return year1Set & year2Set


def getNamesBySymbol(n):
    trans = transactionReader()
    transDict = {}
    for key in trans.keys():  # all names
        for key1 in trans[key]:  # all companies
            if int(trans[key][key1]) >= n:
                if key1 not in transDict:
                    transDict[key1] = set()
                transDict[key1].add(key)
    return transDict


# This  block  is  optional  and  can be used  for  testing.
# We will  NOT  look  into  its  content.
#######################################################
if __name__ == "__main__":
    # Write  anything  here to test  your  code.
    print(getMonthlyVolume()['2017/07'] == 415923470)
    print(len(getCommonDays('2014', '2017')) == 138 and ('06', '20') in getCommonDays('2014', '2017'))
    print(getNamesBySymbol(19))