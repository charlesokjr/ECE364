#######################################################
#    Author:      <Ethan Glaser>
#    email:       <glasere@purdue.edu>
#    ID:           <ee364a13>
#    Date:         <9/3/19>
#######################################################
import difflib
import os  # List of  module  import  statements
import sys  # Each  one on a line
import filecmp
#######################################################
# No Module -Level  Variables  or  Statements!
# ONLY  FUNCTIONS  BEYOND  THIS  POINT!
#######################################################
from difflib import ndiff


def getComponentCountByProject(projectID, componentSymbol):
    # identify all circuits within project (project.dat)
    # iterate through all components in circuit (circuit.dat)
    # collect all IDs in specified componentSymbol (component.dat)
    # increment if components in circuit in all IDs
    # Value Error if project doesnt exist
    projects = projectsReader()
    comps = componentReader(componentSymbol)
    circuits = set()
    distinct = set()
    count = 0
    valid = False
    for project in projects:
        if projectID == project[1]:
            valid = True
            circuits.add(project[0])
    if not valid:
        raise ValueError("invalid project ID")
    for circuit in circuits:
        _, components = circuitReader('circuits/' + "circuit_" + circuit + ".dat")
        for comp in components:
            if comp in comps:
                distinct.add(comp)
    return len(distinct)


def getComponentCountByStudent(studentName, componentSymbol):
    # find student ID (students.dat)
    # iterate through all circuits to search for ID (circuits.dat)
    # iterate through all components in circuit to identify if in component Symbol (circuit.dat)
    # collect all IDs in specified componentSymbol (component.dat)
    # increment
    # value error if student ID invalid
    students = studentsReader()
    comps = componentReader(componentSymbol)
    count = 0
    distinct = set()
    if studentName not in students:
        raise ValueError("invalid student name")
    for circuit in os.listdir('./circuits'):
        participants, components = circuitReader('circuits/' + circuit)
        if students[studentName] in participants:
            for comp in components:
                if comp in comps:
                    distinct.add(comp)
    return len(distinct)


def getParticipationByStudent(studentName):
    # find student ID (students.dat)
    # iterate through all circuits to search for ID (circuits.dat)
    # find circuit in projects file (projects.dat)
    # add to projectID set
    # value error if student ID invalid
    students = studentsReader()
    projects = projectsReader()
    circuitIDs = set()
    projectIDs = set()
    if studentName not in students:
        raise ValueError("invalid student name")
    for circuit in os.listdir('./circuits'):
        participants, _ = circuitReader('circuits/' + circuit)
        if students[studentName] in participants:
            circuitIDs.add(circuit[8:15])
    for project in projects:
        if project[0] in circuitIDs:
            projectIDs.add(project[1])
    return projectIDs


def getParticipationByProject(projectID):
    # identify all circuits within project (project.dat)
    # iterate through all components in circuit (circuit.dat)
    # add all IDs to unique list (set)
    # value error if project ID invalid
    participation = set()
    names = set()
    projects = projectsReader()
    studs = studentsReader()
    valid = False
    for proj in projects:
        if proj[1] == projectID:
            valid = True
            participants, _ = circuitReader('circuits/' + "circuit_" + proj[0] + ".dat")
            for part in participants:
                participation.add(part)
    for i in participation:
        for s in studs:
            if i == studs[s]:
                names.add(s)
    if not valid:
        raise ValueError("invalid project ID")
    return names


def getCostOfProjects():
    # iterate through project IDs (projects.dat)
    # iterate through circuits in project (circuits.dat)
    # identify component cost (components.dat)
    # increment cost
    projectCost = {}
    projects = projectsReader()
    devices = {}
    for com in [componentReader('C'), componentReader('I'), componentReader('R'), componentReader('T')]:
        devices.update(com)
    for proj in projects:
        projectCost[proj[1]] = 0
    for proj in projects:
        _, components = circuitReader('circuits/' + "circuit_" + proj[0] + ".dat")
        for comp in components:
            projectCost[proj[1]] = float(format(devices[comp] + projectCost[proj[1]], ".2f"))
    return projectCost


def getProjectByComponent(componentIDs):
    # iterate through component IDs
    # iterate through circuits to find component (circuits.dat)
    # iterate through projects to find circuit (projects.dat)
    # create set of projects to return
    circuitIDs = getCircuitByComponent(componentIDs)
    projects = projectsReader()
    finalProjects = set()
    for data in projects:
        if data[0] in circuitIDs:
            finalProjects.add(data[1])
    return finalProjects



def getCommonByProject(projectID1, projectID2):
    # create set for both projects:
    # iterate through circuits in project (projects.dat)
    # identify components in circuits (circuits.dat)
    # create set of all components
    # identify intersection of projects
    # value error if either project ID invalid
    proj1Comp = set()
    proj2Comp = set()
    valid1 = False
    valid2 = False
    shared = []
    projects = projectsReader()
    for proj in projects:
        if proj[1] == projectID1:
            valid1 = True
            _, components = circuitReader('circuits/' + "circuit_" + proj[0] + ".dat")
            for comp in components:
                proj1Comp.add(comp)
        elif proj[1] == projectID2:
            valid2 = True
            _, components = circuitReader('circuits/' + "circuit_" + proj[0] + ".dat")
            for comp in components:
                proj2Comp.add(comp)
    if not valid1 or not valid2:
        raise ValueError("Invalid project ID")
    for com in proj1Comp & proj2Comp:
        shared.append(com)
    shared.sort()
    return shared


def getComponentReport(componentIDs):
    # iterate through component IDs
    # iterate through project files to find instances of each circuit (projects.dat)
    # iterate through circuit files to find instances of each component (circuit.dat)
    # increment value in dictionary
    componentDict = {}
    for comp in componentIDs:
        componentDict[comp] = 0
    projects = projectsReader()
    for proj in projects:
        _, components = circuitReader('circuits/' + "circuit_" + proj[0] + ".dat")
        for component in components:
            if component in componentIDs:
                componentDict[component] += 1
    return componentDict


def getCircuitByStudent(studentNames):
    students = studentsReader()
    ids = []
    circuitIDs = set()
    for s in studentNames:
        ids.append(students[s])
    for circuit in os.listdir('./circuits'):
        participants, _ = circuitReader('circuits/' + circuit)
        for i in ids:
            if i in participants:
                circuitIDs.add(circuit[8:15])
    return circuitIDs


def getCircuitByComponent(componentIDs):
    circuitIDs = set()
    for circuit in os.listdir('./circuits'):
        _, components = circuitReader('circuits/' + circuit)
        for i in componentIDs:
            if i in components:
                circuitIDs.add(circuit[8:15])
    return circuitIDs


def circuitReader(circuitID):
    # with open("circuits/circuit_" + circuitID + ".dat") as f:
    with open(circuitID) as f:
        data = f.readlines()[2:]
        realData = []
        components = []
        participants = []
        for line in data:
            realData.append(line.split())
        for remove in [['Components:'], ['-------------'], []]:
            realData.remove(remove)
        for info in realData:
            if len(info[0]) == 11:
                participants.append(info[0])
            elif len(info[0]) == 7:
                components.append(info[0])
            else:
                raise ValueError("invalid info" + info[0])
        return participants, components


def componentReader(componentType):
    componentMap = {'C': 'capacitors', 'I': 'inductors', 'R': 'resistors', 'T': 'transistors'}
    with open("maps/" + componentMap[componentType] + ".dat") as f:
        data = f.readlines()[3:]
        realData = []
        componentDict = {}
        for line in data:
            realData.append(line.split())
        for info in realData:
            componentDict[info[0]] = float(info[1][1:])
        return componentDict


def projectsReader():
    with open("maps/projects.dat") as f:
        data = f.readlines()[2:]
        realData = []
        for line in data:
            realData.append(line.split())
        return realData


def studentsReader():
    with open("maps/students.dat") as f:
        data = f.readlines()[2:]
        realData = {}
        for line in data:
            line = line.split()
            if len(line) != 4:
                raise ValueError("name error" + str(line))
            realData[line[0] + ' ' + line[1]] = line[3]
        return realData


# This  block  is  optional  and  can be used  for  testing.
# We will  NOT  look  into  its  content.
#######################################################
if __name__ == "__main__":
    componentSet = set(['HOR-267', 'RLL-937'])
    studentSet = set(['Gray, Tammy'])
    #1
    prob1 = getComponentCountByProject('082D6241-40EE-432E-A635-65EA8AA374B6', 'R')
    print(prob1)
    #2
    prob2 = getComponentCountByStudent('Adams, Keith', 'R')
    print(prob2)
    #3
    prob3 = getParticipationByStudent('Gray, Tammy')
    print(prob3)
    #4
    prob4 = getParticipationByProject('7C376AFE-6D98-4E50-B29C-71FBF6260B2D')
    print(prob4)
    #5
    prob5 = getCostOfProjects()
    print(prob5)
    #6
    prob6 = getProjectByComponent(componentSet)
    print(prob6)
    #7
    prob7 = getCommonByProject('7C376AFE-6D98-4E50-B29C-71FBF6260B2D', 'FE647EE2-2EBD-4837-83F0-256C377365FE')
    print(prob7)
    #8
    prob8 = getComponentReport(componentSet)
    print(prob8)
    #9
    prob9 = getCircuitByStudent(studentSet)
    print(prob9)
    #10
    prob10 = getCircuitByComponent(componentSet)
    print(prob10)

    probs = [prob1, prob2, prob3, prob4, prob5, prob6, prob7, prob8, prob9, prob10]
    types = [int, int, set, set, dict, set, list, dict, set, set]
    for i in range(0, len(probs)):
        if type(probs[i]) != types[i]:
            raise ValueError("return type error in problem " + str(i))

    with open('mytest', 'w') as f:
        f.write('getComponentCountByProject("90BE0D09-1438-414A-A38B-8309A49C02EF", "I") =  ')
        f.write(str(getComponentCountByProject("90BE0D09-1438-414A-A38B-8309A49C02EF", "I")))
        f.write('\n')
        f.write('getComponentCountByStudent("Butler, Julia", "R") =  ')
        f.write(str(getComponentCountByStudent("Butler, Julia", "R")))
        f.write('\n')
        f.write('getParticipationByStudent("Butler, Julia") =  ')
        f.write(str(getParticipationByStudent("Butler, Julia")))
        f.write('\n')
        f.write('getParticipationByProject("90BE0D09-1438-414A-A38B-8309A49C02EF") =  ')
        f.write(str(getParticipationByProject("90BE0D09-1438-414A-A38B-8309A49C02EF")))
        f.write('\n')
        f.write('getCostOfProjects() =  ')
        f.write(str(getCostOfProjects()))
        f.write('\n')
        f.write("getProjectByComponent( {'RWR-683', 'KRU-458'} ) =  ")
        f.write(str(getProjectByComponent( {'RWR-683', 'KRU-458'} )))
        f.write('\n')
        f.write('getCommonByProject("90BE0D09-1438-414A-A38B-8309A49C02EF", "082D6241-40EE-432E-A635-65EA8AA374B6") =  ')
        f.write(str(getCommonByProject("90BE0D09-1438-414A-A38B-8309A49C02EF", "082D6241-40EE-432E-A635-65EA8AA374B6")))
        f.write('\n')
        f.write("getComponentReport( {'RWR-683', 'KRU-458'} ) =  ")
        f.write(str(getComponentReport( {'RWR-683', 'KRU-458'} )))
        f.write('\n')
        f.write("getCircuitByStudent( {'Carter, Sarah', 'Lowe, Karen'} ) =  ")
        f.write(str(getCircuitByStudent( {'Carter, Sarah', 'Lowe, Karen'} )))
        f.write('\n')
        f.write("getCircuitByComponent( {'RWR-683', 'KRU-458'} ) =  ")
        f.write(str(getCircuitByComponent( {'RWR-683', 'KRU-458'} )))
    print(getComponentCountByProject("90BE0D09-1438-414A-A38B-8309A49C02EF", "I") == 69)
    print(getComponentCountByStudent("Butler, Julia", "R") == 13)
    print(len(getParticipationByStudent("Butler, Julia") - {'77A1A82E-749E-43BF-B3BF-3E70F087F808', '3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287', '56B13184-D087-48DB-9CBA-84B40FE17CC5', '35C50EBA-E3A9-4AB7-A67C-64D4228C4DCA', '177EBF38-1C20-497B-A2EF-EC1880FEFDF9', '83383848-1D69-40D4-A360-817FB22769ED', '96CC6F98-B44B-4FEB-A06B-390432C1F6EA', 'D88C2930-9DA4-431F-8CDB-99A2AA2C7A05', '8E56417E-0D81-4F43-8137-F1F7AA005654', 'DE06228A-0544-4543-9055-A39D19DEDFA4', 'B9C94766-617A-4168-B2AA-44FFE8323E32', '6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9'}))
    print(len({'77A1A82E-749E-43BF-B3BF-3E70F087F808', '3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287', '56B13184-D087-48DB-9CBA-84B40FE17CC5', '35C50EBA-E3A9-4AB7-A67C-64D4228C4DCA', '177EBF38-1C20-497B-A2EF-EC1880FEFDF9', '83383848-1D69-40D4-A360-817FB22769ED', '96CC6F98-B44B-4FEB-A06B-390432C1F6EA', 'D88C2930-9DA4-431F-8CDB-99A2AA2C7A05', '8E56417E-0D81-4F43-8137-F1F7AA005654', 'DE06228A-0544-4543-9055-A39D19DEDFA4', 'B9C94766-617A-4168-B2AA-44FFE8323E32', '6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9'} - getParticipationByStudent("Butler, Julia")))
    print(len(getParticipationByProject("90BE0D09-1438-414A-A38B-8309A49C02EF") - {'Simmons, Cynthia', 'Patterson, Peter', 'Stewart, Earl', 'Sanders, Emily', 'Gonzalez, Kimberly', 'Bennett, Nancy', 'Evans, Johnny', 'Kelly, Joyce', 'Diaz, Tina', 'Campbell, Eugene', 'Moore, John', 'Smith, Jimmy', 'Flores, Andrea', 'Wood, Kevin', 'Cooper, Kelly', 'White, Diana', 'Carter, Sarah', 'Young, Frank', 'Garcia, Martha', 'Mitchell, Judith', 'Peterson, Daniel', 'Lewis, William', 'Watson, Martin', 'Collins, Anthony', 'James, Randy', 'Nelson, Louise', 'Walker, Terry', 'Harris, Anne', 'Reed, Bobby', 'Lowe, Karen', 'Wright, Eric', 'Green, Roy', 'Bryant, Evelyn', 'Gonzales, Arthur', 'Jenkins, Paul', 'Turner, Theresa', 'Washington, Annie', 'Hernandez, Lawrence', 'Roberts, Teresa', 'Ward, Sandra', 'Cook, Margaret', 'Ross, Frances', 'Jackson, Doris', 'Gray, Tammy', 'Hill, Jose', 'Martinez, David', 'Miller, Aaron', 'Thompson, Michelle', 'Powell, Gregory', 'Wilson, Howard', 'Lopez, Juan', 'Barnes, Sean', 'Rodriguez, Jeffrey', 'Clark, Joe', 'Henderson, Christopher', 'King, Carolyn', 'Rivera, Patricia', 'Edwards, Rachel', 'Scott, Michael', 'Johnson, Roger', 'Foster, Benjamin', 'Morris, Heather'}))
    print(len({'Simmons, Cynthia', 'Patterson, Peter', 'Stewart, Earl', 'Sanders, Emily', 'Gonzalez, Kimberly', 'Bennett, Nancy', 'Evans, Johnny', 'Kelly, Joyce', 'Diaz, Tina', 'Campbell, Eugene', 'Moore, John', 'Smith, Jimmy', 'Flores, Andrea', 'Wood, Kevin', 'Cooper, Kelly', 'White, Diana', 'Carter, Sarah', 'Young, Frank', 'Garcia, Martha', 'Mitchell, Judith', 'Peterson, Daniel', 'Lewis, William', 'Watson, Martin', 'Collins, Anthony', 'James, Randy', 'Nelson, Louise', 'Walker, Terry', 'Harris, Anne', 'Reed, Bobby', 'Lowe, Karen', 'Wright, Eric', 'Green, Roy', 'Bryant, Evelyn', 'Gonzales, Arthur', 'Jenkins, Paul', 'Turner, Theresa', 'Washington, Annie', 'Hernandez, Lawrence', 'Roberts, Teresa', 'Ward, Sandra', 'Cook, Margaret', 'Ross, Frances', 'Jackson, Doris', 'Gray, Tammy', 'Hill, Jose', 'Martinez, David', 'Miller, Aaron', 'Thompson, Michelle', 'Powell, Gregory', 'Wilson, Howard', 'Lopez, Juan', 'Barnes, Sean', 'Rodriguez, Jeffrey', 'Clark, Joe', 'Henderson, Christopher', 'King, Carolyn', 'Rivera, Patricia', 'Edwards, Rachel', 'Scott, Michael', 'Johnson, Roger', 'Foster, Benjamin', 'Morris, Heather'} - getParticipationByProject("90BE0D09-1438-414A-A38B-8309A49C02EF")))
    test5 = {'082D6241-40EE-432E-A635-65EA8AA374B6': 245.46, '90BE0D09-1438-414A-A38B-8309A49C02EF': 335.16, '96CC6F98-B44B-4FEB-A06B-390432C1F6EA': 268.48, 'FE647EE2-2EBD-4837-83F0-256C377365FE': 213.73, '77A1A82E-749E-43BF-B3BF-3E70F087F808': 369.48, '83383848-1D69-40D4-A360-817FB22769ED': 367.49, '8E56417E-0D81-4F43-8137-F1F7AA005654': 262.39, '56B13184-D087-48DB-9CBA-84B40FE17CC5': 355.36, '66FA081D-D1AA-4306-8650-9C39429CCDAB': 256.63, '4C5B295B-58E1-4CFB-80DF-88938B9A6300': 388.81, '17A946D3-A1B0-4335-8808-8594D9FBD62C': 295.25, '075A54E6-530B-4533-A2E4-A15226BE588C': 358.84, '0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A': 292.63, 'D88C2930-9DA4-431F-8CDB-99A2AA2C7A05': 428.72, '8C71F259-ECA8-4267-A8B3-6CAD6451D4CC': 325.13, '2E7649C2-574A-496A-850B-F15190031E11': 304.08, '32B9E998-97C3-4D5A-8005-C9685A08196F': 400.34, '6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9': 350.93, '7C376AFE-6D98-4E50-B29C-71FBF6260B2D': 249.63, '35C50EBA-E3A9-4AB7-A67C-64D4228C4DCA': 394.44, 'D230BAC0-249C-410F-84E4-41F9EDBFCB20': 235.24, 'D7EFB850-9A34-41B0-BD9D-FBCDF4C3C371': 241.42, '177EBF38-1C20-497B-A2EF-EC1880FEFDF9': 334.98, '3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287': 370.65, 'DE06228A-0544-4543-9055-A39D19DEDFA4': 375.37, 'B9C94766-617A-4168-B2AA-44FFE8323E32': 231.96, '6CCCA5F3-3008-46FF-A779-2D2F872DAF82': 233.6, '08EDAB1A-743D-4B62-9446-2F1C5824A756': 376.4}
    mytest5 = getCostOfProjects()
    print(len(test5) - len(mytest5))
    for key in test5.keys():
        if test5[key] != mytest5[key]:
            print(key)
    print(len(getProjectByComponent( {'RWR-683', 'KRU-458'} ) - {'0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A', '08EDAB1A-743D-4B62-9446-2F1C5824A756', '3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287', '35C50EBA-E3A9-4AB7-A67C-64D4228C4DCA', '8E56417E-0D81-4F43-8137-F1F7AA005654', '177EBF38-1C20-497B-A2EF-EC1880FEFDF9', '4C5B295B-58E1-4CFB-80DF-88938B9A6300', '8C71F259-ECA8-4267-A8B3-6CAD6451D4CC', '66FA081D-D1AA-4306-8650-9C39429CCDAB', '90BE0D09-1438-414A-A38B-8309A49C02EF', 'FE647EE2-2EBD-4837-83F0-256C377365FE', 'D88C2930-9DA4-431F-8CDB-99A2AA2C7A05', '6CCCA5F3-3008-46FF-A779-2D2F872DAF82', '56B13184-D087-48DB-9CBA-84B40FE17CC5', '2E7649C2-574A-496A-850B-F15190031E11', '082D6241-40EE-432E-A635-65EA8AA374B6', '17A946D3-A1B0-4335-8808-8594D9FBD62C', '96CC6F98-B44B-4FEB-A06B-390432C1F6EA', '6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9', 'D230BAC0-249C-410F-84E4-41F9EDBFCB20', '7C376AFE-6D98-4E50-B29C-71FBF6260B2D'}))
    print(len(getProjectByComponent( {'0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A', '08EDAB1A-743D-4B62-9446-2F1C5824A756', '3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287', '35C50EBA-E3A9-4AB7-A67C-64D4228C4DCA', '8E56417E-0D81-4F43-8137-F1F7AA005654', '177EBF38-1C20-497B-A2EF-EC1880FEFDF9', '4C5B295B-58E1-4CFB-80DF-88938B9A6300', '8C71F259-ECA8-4267-A8B3-6CAD6451D4CC', '66FA081D-D1AA-4306-8650-9C39429CCDAB', '90BE0D09-1438-414A-A38B-8309A49C02EF', 'FE647EE2-2EBD-4837-83F0-256C377365FE', 'D88C2930-9DA4-431F-8CDB-99A2AA2C7A05', '6CCCA5F3-3008-46FF-A779-2D2F872DAF82', '56B13184-D087-48DB-9CBA-84B40FE17CC5', '2E7649C2-574A-496A-850B-F15190031E11', '082D6241-40EE-432E-A635-65EA8AA374B6', '17A946D3-A1B0-4335-8808-8594D9FBD62C', '96CC6F98-B44B-4FEB-A06B-390432C1F6EA', '6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9', 'D230BAC0-249C-410F-84E4-41F9EDBFCB20', '7C376AFE-6D98-4E50-B29C-71FBF6260B2D'} - {'RWR-683', 'KRU-458'} )))
    print(getCommonByProject("90BE0D09-1438-414A-A38B-8309A49C02EF", "082D6241-40EE-432E-A635-65EA8AA374B6") ==  ['ART-641', 'AVL-897', 'BKC-326', 'BLT-317', 'BOT-567', 'BRT-453', 'BRT-517', 'BTP-574', 'CLW-864', 'CNA-814', 'CQL-174', 'CRK-275', 'CRU-015', 'CYS-314', 'DTH-293', 'ECI-702', 'ERK-824', 'EVC-461', 'FUR-815', 'GRD-506', 'GTV-294', 'GVR-469', 'HLL-239', 'HOR-267', 'HRI-734', 'HRL-126', 'HRM-419', 'HUC-107', 'IBC-258', 'ICV-048', 'IGT-143', 'ILP-016', 'ILT-213', 'JNL-870', 'JSC-743', 'JTM-187', 'KTW-062', 'LAD-263', 'LAI-791', 'LCD-472', 'LJR-923', 'LLR-943', 'LLW-108', 'LOK-793', 'LRZ-426', 'LVE-357', 'LWY-204', 'LXY-873', 'MAT-263', 'MRL-546', 'NCD-108', 'NOC-324', 'OPC-530', 'OPL-704', 'OUT-239', 'QIC-567', 'QSC-941', 'QXT-230', 'RCW-957', 'RFR-136', 'RFU-406', 'RHN-426', 'RJH-485', 'RKP-916', 'RLG-301', 'RLL-937', 'ROJ-198', 'RSH-743', 'RTW-487', 'SJL-465', 'SLJ-104', 'TCG-395', 'TCH-815', 'TED-890', 'TIR-328', 'TLQ-234', 'TLR-058', 'TQB-089', 'TQJ-016', 'TSW-590', 'TTC-861', 'TXC-972', 'UEL-264', 'UNL-746', 'VML-389', 'VNR-234', 'WCQ-031', 'WHT-451', 'XRY-260', 'YHT-695', 'YKC-827', 'YLN-057', 'YWT-432', 'ZLU-167', 'ZTN-927'])
    test8 = {'RWR-683': 17, 'KRU-458': 27}
    mytest8 = getComponentReport( {'RWR-683', 'KRU-458'} )
    print(len(test8) - len(mytest8))
    for key in test8.keys():
        if test8[key] != mytest8[key]:
            print(key)
    print(len(getCircuitByStudent( {'Carter, Sarah', 'Lowe, Karen'} ) - {'92-7-57', '33-5-22', '65-0-76', '54-6-09', '35-7-32', '41-0-17', '43-2-02', '19-9-86', '51-8-46', '16-7-59', '26-4-54'}))
    print(len({'92-7-57', '33-5-22', '65-0-76', '54-6-09', '35-7-32', '41-0-17', '43-2-02', '19-9-86', '51-8-46', '16-7-59', '26-4-54'} - getCircuitByStudent( {'Carter, Sarah', 'Lowe, Karen'})))
    print(len(getCircuitByComponent( {'RWR-683', 'KRU-458'} ) - {'75-9-18', '41-8-74', '63-9-60', '88-4-47', '88-6-24', '93-1-30', '16-8-96', '12-5-85', '52-6-35', '86-8-58', '41-2-39'}))
    print(len({'75-9-18', '41-8-74', '63-9-60', '88-4-47', '88-6-24', '93-1-30', '16-8-96', '12-5-85', '52-6-35', '86-8-58', '41-2-39'} - getCircuitByComponent( {'RWR-683', 'KRU-458'} )))
    print(getCircuitByStudent({'Sanders, Emily'}))