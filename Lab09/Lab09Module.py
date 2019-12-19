#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import re
#######################################################
# No Module -Level  Variables  or  Statements!
# ONLY  CLASSES  AND  FUNCTIONS  BEYOND  THIS  POINT!
#######################################################
class Action:
    def __init__(self, at, am):
        if at != 'W' and at != 'D':
            print(at)
            raise ValueError("Invalid action type: must be 'W' or 'D'")
        self.actionType = at
        self.amount = am


class Client:
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Account:
    def __init__(self, an, c, a, min):
        self.accountNumber = an
        self.client = c
        self.amount = a
        self.minThreshold = min

    def __str__(self):
        if self.amount < 0:
            return self.accountNumber + ', ' + str(self.client) + ', Balance = ($' + format(-1 * self.amount, ".2f") + ')'
        else:
            return self.accountNumber + ', ' + str(self.client) + ', Balance = $' + format(self.amount, ".2f")

    def performAction(self, act):
        if act.actionType == 'D':
            self.amount += act.amount
            self.amount = round(self.amount, 2)
        else:
            if self.amount - act.amount > self.minThreshold:
                self.amount -= act.amount
                self.amount = round(self.amount, 2)
            elif self.amount - act.amount < 0:
                raise ValueError("Invalid Transaction: account balance must not drop below 0")
            elif self.amount - act.amount < self.minThreshold:
                self.amount -= (act.amount + 10.00)
                self.amount = round(self.amount, 2)

class Institute:
    def __init__(self, accs):
        self.accounts = accs

    def createNew(self, fn, ln, an):
        if an not in self.accounts:
            newAcc = Account(an, Client(fn, ln), 500, 1000)

    def performAction(self, an, act):
        if an in self.accounts:
            self.accounts[an].performAction(act)

def getNumberPattern():
    return '([0-9-+][0-9-+e.]+[0-9])'
#def getLinkPattern():

def getDataPattern():
    return '["](.+?)\" : \"(.+?)["]'

# This  block  is  optional  and  can be used  for  testing.
# We will  NOT  look  into  its  content.
#######################################################
if __name__  == "__main__":
    pattern = getNumberPattern()
    s = 'Weoiaso 1290 +90 -10 asdf -129e10 10293.12 With the electrons -1.019'
    print(re.findall(pattern, s))
    #html = 'aslkfjla <a href="asdflk">ethan</a> alsdf'
    #pattern = getLinkPattern()
    #print(re.search())
    #pattern = getDataPattern()
    #s = '{"firstName" : "Ethan", "lastName" : "Glaser", "homeTown" : "Plymouth, MN"'
    #print(re.findall(pattern, s))
    person = Client('Ethan', 'Glaser')
    person2 = Client('James', 'Bond')
    dep = Action('D', 10)
    wit = Action('W', 10)
    print(str(person))
    acc = Account('12345-67890', person, 40, 10.00)
    acc2 = Account('09876-543421', person2, 100000, 1000)
    print(acc)
    acc.performAction(wit)
    print(acc)
    dict = {}
    dict['12345-67890'] = acc
    dict['09876-543421'] = acc2
    print(dict)
    institute = Institute(dict)
    institute.createNew('Abc', 'Def', '12409-08270')
    institute.performAction('12345-67890', wit)
    print("account")
    print(acc)
    print(institute)