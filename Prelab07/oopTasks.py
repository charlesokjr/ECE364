#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >
#######################################################
import os
from enum import Enum
#######################################################
# No Module -Level  Variables  or  Statements!
# ONLY  CLASSES  AND  FUNCTIONS  BEYOND  THIS  POINT!
#######################################################


class Level(Enum):
    Freshman = 1
    Sophomore = 2
    Junior = 3
    Senior = 4


class ComponentType(Enum):
    Resistor = 1
    Capacitor = 2
    Inductor = 3
    Transistor = 4


class Student:
    def __init__(self, ID, firstName, lastName, level):
        if type(level) != Level:
            raise TypeError("The argument must be an instance of the 'Level' type")
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        self.level = level.name

    def __str__(self):
        return f"{self.ID}, {self.firstName} {self.lastName}, {self.level}"


class Component:
    def __init__(self, ID, ctype, price):
        if type(ctype) != ComponentType:
            raise TypeError("The argument must be an instance of the 'ComponentType' type")
        self.ID = ID
        self.ctype = ctype.name
        self.price = round(price, 2)

    def __str__(self):
        return f"{self.ctype}, {self.ID}, ${format(self.price, '.2f')}"

    def __hash__(self):
        return hash(self.ID)


class Circuit:
    def __init__(self, ID, components):
        cost = 0
        for comp in components:
            if type(comp) != Component:
                raise ValueError("The argument must be a set of the 'ComponentType' type")
            cost += comp.price
        self.ID = ID
        self.components = components
        self.cost = round(cost, 2)

    def __str__(self):
        componentCount = {"Resistor": 0, "Capacitor": 0, "Inductor": 0, "Transistor": 0}
        for comp in self.components:
            componentCount[comp.ctype] += 1
        return f"{self.ID}: (R = {format(componentCount['Resistor'], '02d')}, C = {format(componentCount['Capacitor'], '02d')}, I = {format(componentCount['Inductor'], '02d')}, T = {format(componentCount['Transistor'], '02d')}), Cost = ${format(self.cost, '.2f')}"

    def __hash__(self):
        return hash(self.ID)

    def getByType(self, eType):
        compSet = set()
        if type(eType) != ComponentType:
            raise ValueError("Invalid argument type. Must be type 'ComponentType'")
        for comp in self.components:
            if comp.ctype == eType.name:
                compSet.add(comp.ID)
        return compSet

    def __contains__(self, component):
        if type(component) is not Component:
            raise ValueError("Invalid argument. Must be type 'Component'")
        if component in self.components:
            return True
        else:
            return False

    def __add__(self, component):
        if type(component) is not Component:
            raise ValueError("Invalid argument. Must be type 'Component'")
        if component not in self.components:
            self.cost += component.price
            self.components.add(component)
        return self

    def __sub__(self, component):
        if type(component) is not Component:
            raise ValueError("Invalid argument. Must be type 'Component'")
        if component in self.components:
            self.cost -= component.price
            self.components.remove(component)
        return self

    def __lt__(self, circuit):
        if type(circuit) is not Circuit:
            raise ValueError("Invalid argument. Must be type 'Circuit'")
        return self.cost < circuit.cost

    def __gt__(self, circuit):
        if type(circuit) is not Circuit:
            raise ValueError("Invalid argument. Must be type 'Circuit'")
        return self.cost > circuit.cost

    def __eq__(self, circuit):
        if type(circuit) is not Circuit:
            raise ValueError("Invalid argument. Must be type 'Circuit'")
        return self.cost == circuit.cost


class Project:
    def __init__(self, ID, participants, circuits):
        cost = 0
        for p in participants:
            if type(p) != Student:
                raise ValueError("Invalid participant type. Should be type 'Student'")
        for c in circuits:
            if type(c) != Circuit:
                raise ValueError("Invalid circuit type. Should be type 'Circuit'")
            cost += c.cost
        self.ID = ID
        self.participants = participants
        self.circuits = circuits
        self.cost = round(cost, 2)

    def __str__(self):
        return f"{self.ID}: ({format(len(self.circuits), '02d')} Circuits, {format(len(self.participants), '02d')} Participants), Cost = ${format(self.cost, '.2f')}"

    def __contains__(self, item):
        if type(item) is Component:
            for circuit in self.circuits:
                if item in circuit.components:
                    return True
            return False
        elif type(item) is Circuit:
            if item in self.circuits:
                return True
            return False
        elif type(item) is Student:
            if item in self.participants:
                return True
            return False
        else:
            raise ValueError("invalid argument. Must be either type 'Component', type 'Student', or type 'Circuit'")

    def __add__(self, circuit):
        if type(circuit) is not Circuit:
            raise ValueError("Invalid argument. Must be type 'Circuit'")
        if circuit not in self.circuits:
            self.circuits.add(circuit)
            self.cost += circuit.cost
        return self

    def __sub__(self, circuit):
        if type(circuit) is not Circuit:
            raise ValueError("Invalid argument. Must be type 'Circuit'")
        if circuit in self.circuits:
            self.circuits.remove(circuit)
            self.cost -= circuit.cost
        return self

    def __getitem__(self, circuitID):
        for circuit in self.circuits:
            if circuit.ID is circuitID:
                return circuit
        raise ValueError("Invalid circuit ID. Circuit must be present in the project")


class Capstone(Project):
    def __init__(self, **kwargs):
        if 'project' in kwargs:
            super().__init__(kwargs['project'].ID, kwargs['project'].participants, kwargs['project'].circuits)
        else:
            super().__init__(**kwargs)
        for person in self.participants:
            if person.level != 'Senior':
                raise ValueError("Invalid participants. All participants must be level 'Senior'")


class team():
    def __init__(self, name, qb, rb, wr, te):
        if type(qb) != player:
            raise ValueError("Invalid quarterback")
        self.name = name
        self.quarterback = qb
        self.runningback = rb
        self.widereceiver = wr
        self.tightend = te
        self.points = qb.points + rb.points + wr.points + te.points

    def __str__(self):
        return self.quarterback.name + ", " + self.runningback.name + ", " + self.widereceiver.name + ", " + self.tightend.name + " combined for: " + str(self.points)

    def __gt__(self, other):
        if self.points > other.points:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.points == other.points:
            return True
        return False

    def __add__(self, other):
        if other.position is "QuarterBack":
            self.points -= self.quarterback.points
            self.quarterback = other
            self.points += self.quarterback.points
        return self

class matchup:
    def __init__(self, team1, team2):
        self.t1 = team1
        self.t2 = team2

    def __str__(self):
        if self.t1 == self.t2:
            return self.t1.name + " and " + self.t2.name + " tie at " + str(self.t1.points)
        elif self.t1 > self.t2:
            return self.t1.name + " defeats " + self.t2.name + ", " + str(self.t1.points) + " to " + str(self.t2.points)
        else:
            return self.t2.name + " defeats " + self.t1.name + ", " + str(self.t2.points) + " to " + str(self.t1.points)


class playertype(Enum):
    QuarterBack = 1
    RunningBack = 2
    WideReceiver = 3
    TightEnd = 4

class player():
    def __init__(self, name, pos, tds, yds):
        self.name = name
        if type(pos) != playertype:
            raise ValueError("Invalid position")
        self.position = pos.name
        if pos is playertype.QuarterBack:
            self.points = 4 * tds + 0.04 * yds
        else:
            self.points = 6 * tds + 0.1 * yds

    def __str__(self):
        return str(self.name) + " is a " + str(self.position) + " and has a score of " + str(self.points)

# This  block  is  optional  and  can be used  for  testing.
# We will  NOT  look  into  its  content.
#######################################################
if __name__ == "__main__":
    qb1 = player("Kirk Cousins", playertype.QuarterBack, 1, 275)
    print(qb1)
    rb1 = player("Christian McCaffrey", playertype.RunningBack, 5000, 280)
    print(rb1)
    wr1 = player("Chris Godwin", playertype.WideReceiver, 1, 240)
    print(wr1)
    te1 = player("TJ Hockenson", playertype.TightEnd, 0, 5)
    print(te1)
    glazenblaze = team("Glaze", qb1, rb1, wr1, te1)
    print(glazenblaze)
    qb2 = player("Russell Wilson", playertype.QuarterBack, 21, 450)
    rb2 = player("Nick Chubb", playertype.RunningBack, 17, 114)
    wr2 = player("Tyler Lockett", playertype.WideReceiver, 3.5, 1)
    te2 = player("Austin Hooper", playertype.TightEnd, 2, 140)
    brudda = team("Brudda", qb2, rb2, wr2, te2)
    print(brudda)
    qb3 = player("Deshaun Watson", playertype.QuarterBack, 7, 450)
    rb3 = player("Saquon Barkley", playertype.QuarterBack, 4, 190)
    wr3 = player("Julian Edelman", playertype.WideReceiver, 7, 213)
    te3 = player("Travis Kelce", playertype.TightEnd, 4, 3)
    bigchungus = team("Rowan", qb3, rb3, wr3, te3)
    print(bigchungus)
    qb4 = player("Baker Mayfield", playertype.QuarterBack, -3, -100)
    rb4 = player("Leveon Bell", playertype.RunningBack, -3, -200)
    wr4 = player("Antonio Brown", playertype.WideReceiver, 0, 0)
    te4 = player("Rob Gronkowski", playertype.TightEnd, 0, 0)
    divas = team("Charlie", qb4, rb4, wr4, te4)
    print(divas)
    if glazenblaze > brudda:
        print("Glaze #1, Nrod sacko")
    else:
        print("brudda")
    glazenblaze = glazenblaze + qb4
    print(matchup(glazenblaze, brudda))




"""

    #cir = Circuit('abc', 1)
    #student = Student('abc', "Ethan", "Glaser", 12)
    r1 = Component('r1', ComponentType.Resistor, 0.50)
    r2 = Component('r2', ComponentType.Resistor, 0.60)
    c1 = Component('c1', ComponentType.Capacitor, 0.40)
    c2 = Component('c2', ComponentType.Capacitor, 0.55)
    i1 = Component('i1', ComponentType.Inductor, 1.20)
    t1 = Component('t1', ComponentType.Transistor, 2.50)
    circuit1 = Circuit('abc-123', {r1, r2, t1})
    circuit2 = Circuit('def-456', {r1, r2, c1, c2, i1})
    print(circuit1.getByType(Level.Junior))
    print('oopTasks.py' in os.listdir('../Prelab07'))
    student1 = Student(1, "Ethan", "Glaser", Level.Junior)
    student2 = Student(2, "Moiz", "Rasheed", Level.Junior)
    student3 = Student(3, "Karthik", "Maiya", Level.Senior)
    student4 = Student(4, "Doug", "Yuuuuuuuu", Level.Junior)
    #student5 = Student(5, "person", "person", 'Junior')
    print(str(student1) == '1, Ethan Glaser, Junior')
    print((str(student1) + ", " + str(student2) + ", " + str(student3) + ", " + str(student4)) == '1, Ethan Glaser, Junior, 2, Moiz Rasheed, Junior, 3, Karthik Maiya, Senior, 4, Doug Yuuuuuuuu, Junior')
    r1 = Component('r1', ComponentType.Resistor, 0.50)
    r2 = Component('r2', ComponentType.Resistor, 0.60)
    c1 = Component('c1', ComponentType.Capacitor, 0.40)
    c2 = Component('c2', ComponentType.Capacitor, 0.55)
    i1 = Component('i1', ComponentType.Inductor, 1.20)
    t1 = Component('t1', ComponentType.Transistor, 2.50)
    #t2 = Component('t2', 5, 2.50)
    print(str(r1) == 'Resistor, r1, $0.50')
    print(str(i1) == 'Inductor, i1, $1.20')
    print(type(hash(t1)) == int)
    circuit1 = Circuit('abc-123', {r1, r2, t1})
    circuit2 = Circuit('def-456', {r1, r2, c1, c2, i1})
    print(str(circuit2) == 'def-456: (R = 02, C = 02, I = 01, T = 00), Cost = $3.25')
    print(str(circuit1) == 'abc-123: (R = 02, C = 00, I = 00, T = 01), Cost = $3.60')
    print(circuit2.getByType(ComponentType.Resistor) == {'r1', 'r2'})
    print(circuit1 + c1  + c2 + i1 - t1 == circuit2)
    print(str(circuit1 - t1) == 'abc-123: (R = 02, C = 02, I = 01, T = 00), Cost = $3.25')
    print(str(circuit1 - c1) == 'abc-123: (R = 02, C = 01, I = 01, T = 00), Cost = $2.85')
    print(circuit1 < circuit2)
    print(str(circuit1 + c1) == 'abc-123: (R = 02, C = 02, I = 01, T = 00), Cost = $3.25')
    circuits = set()
    circuits.add(circuit2)
    circuits.add(circuit1 - c1 - i1)
    project1 = Project('p1', {student1, student3}, circuits)
    print(str(project1) == 'p1: (02 Circuits, 02 Participants), Cost = $4.90')
    print(r1 in project1)
    print(t1 not in project1)
    print(student4 not in project1)
    print(circuit1 in project1)
    #print('Moiz Rasheed' in project1)
    circuit3 = Circuit('ghi-789', {r1, c2, i1})
    print(str(project1 + circuit3) == 'p1: (03 Circuits, 02 Participants), Cost = $7.15')
    print(str(project1 - circuit1) == 'p1: (02 Circuits, 02 Participants), Cost = $5.50')
    #print(str(project1['abc-123']))
    print(str(project1['def-456']) == 'def-456: (R = 02, C = 02, I = 01, T = 00), Cost = $3.25')
    #capstone2 = Capstone(ID='p2', participants={student1, student3}, circuits=circuits)
    print(str(Capstone(ID='p2', participants={student3}, circuits=circuits)) == str(Capstone(project=Project('p2', {student3}, circuits))))"""