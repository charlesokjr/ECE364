#######################################################
#    Author:      <Ethan Glaser>
#    email:       <glasere@purdue.edu>
#    ID:           <ee364a13>
#    Date:         <9/25/19>
#######################################################
import re
from uuid import UUID
#######################################################
# No Module -Level  Variables  or  Statements!
# ONLY  FUNCTIONS  BEYOND  THIS  POINT!
#######################################################
# search() , match() , compile() , fullmatch() , findall() , finditer() , escape() and purge()


def getUrlParts(url):
    initial = re.search(r'(?<=//)\S+(?=\?)', url).group()
    final = re.search(r'\S+?(?=/)', initial).group(), re.search(r'(?<=/)\S+(?=/)', initial).group(), \
        re.search(r'(?<=/)\w+?(?=$)', initial).group()
    final = re.search(r"(?P<Base>[\w.-]+)/(?P<next>[w.-]+)/(?P<last>[\w.-]+)", url)
    return final["Base"]


def getQueryParameters(url):
    paramList = []
    string = re.search(r'(?<=\?)\S+(?=$)', url).group()
    paramList = re.findall('([\w._-]+)[=]([\w.-_]+)', string)
    return paramList


def getSpecial(sentence, letter):
    specialList = []
    re.findall(r'\b%s[\w]+^%s\W]\b' %(letter, letter), sentence)
    for x in range(len(re.findall(' ', sentence))):
        word = re.search(r'\w+', sentence).group()
        pre = r'(\A)[' + re.escape(letter) + ']'
        post = r'[' + re.escape(letter) + '](\Z)'
        if bool(re.findall(pre, word, flags=re.I)) != bool(re.findall(post, word, flags=re.I)):
            specialList.append(word)
        sentence = re.search(r'(?<=\s).+', sentence).group()
    return specialList


def getRealMAC(sentence):
    a = re.findall(r'[0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2}[:-]'
                   r'[0-9A-Fa-f]{2}', sentence)
    if len(a):
        return a[0]
    return None


def getRejectedEntries():
    employees = employeeReader()
    rejected = []
    for employee in employees:
        if not (employees[employee]['id'] or employees[employee]['phone'] or employees[employee]['state']):
            rejected.append(employee)
    rejected = sorted(rejected)
    return rejected


def getEmployeesWithIDs():
    employees = employeeReader()
    idDict = {}
    for employee in employees:
        if employees[employee]['id']:
            idDict[employee] = employees[employee]['id']
    return idDict


def getEmployeesWithoutIDs():
    employees = employeeReader()
    rejected = getRejectedEntries()
    idList = []
    for employee in employees:
        if not employees[employee]['id'] and employee not in rejected:
            idList.append(employee)
    idList = sorted(idList)
    return idList


def getEmployeesWithPhones():
    employees = employeeReader()
    phoneDict = {}
    for employee in employees:
        if employees[employee]['phone']:
            phoneDict[employee] = employees[employee]['phone']
    return phoneDict


def getEmployeesWithStates():
    employees = employeeReader()
    stateDict = {}
    for employee in employees:
        if employees[employee]['state']:
            stateDict[employee] = employees[employee]['state']
    return stateDict


def getCompleteEntries():
    employees = employeeReader()
    complete = {}
    for employee in employees:
        if employees[employee]['id'] and employees[employee]['phone'] and employees[employee]['state']:
            complete[employee] = employees[employee]['id'], employees[employee]['phone'], employees[employee]['state']
    return complete


def employeeReader():
    with open("Employees.dat", "r") as f:
        data = f.readlines()
    employeesDict = {}
    for line in data:
        employeeDict = {}
        state = re.search(r'\w+\s\w+(?=$)', line)
        if not state:
            state = re.search(r'\w+(?=$)', line)
        if state:
            state = state.group()
        employeeDict['state'] = state

        phone = re.findall(r'[\s;,][(][0-9]{3}[)][\s][0-9]{3}[-][0-9]{4}[\s;,]', line) + re.findall\
            (r'[\s;,][0-9]{10}[\s;,]', line) + re.findall(r'[\s;,][0-9]{3}[-][0-9]{3}[-][0-9]{4}[\s;,]', line)
        if phone:
            phone = re.findall(r'\d', phone[0])
            phone = "(" + phone[0] + phone[1] + phone[2] + ") " + phone[3] + phone[4] + phone[5] + "-" + phone[6]\
                    + phone[7] + phone[8] + phone[9]
        else:
            phone = None
        employeeDict['phone'] = phone

        name = re.search(r'(?<=^)\w+\s\w+', line)
        if not name:
            name = re.search(r'(?<=\s)\w+', line).group() + ' ' + re.search(r'(?<=^)\w+', line).group()
        else:
            name = name.group()

        ID = re.findall(r'[A-Za-z0-9-]{36}', line) + re.findall(r'[A-Za-z0-9]{32}', line)
        if len(ID):
            if len(ID[0]) == 36:
                ID[0] = ID[0][0:8] + ID[0][9:13] + ID[0][14:18] + ID[0][19:23] + ID[0][24:36]
            ID = str(UUID(ID[0]))
        else:
            ID = None
        employeeDict['id'] = ID

        employeesDict[name] = employeeDict
    return employeesDict


# This  block  is  optional  and  can be used  for  testing.
# We will  NOT  look  into  its  content.
#######################################################
if __name__ == "__main__":
    string = "1oiahgaoillqq2qwe3oqiuwofuapsozklhizhsoppoullaks"
    array = re.search(r'[0-9](?P<one>[\w]+?)[0-9](?P<two>[\w]+)[0-9](?P<three>[\w]+?)', string).group()
    print(array)
    #print(getCompleteEntries())