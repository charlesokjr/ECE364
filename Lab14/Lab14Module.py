import os
import measurement
from enum import Enum
from pprint import pprint
import re

class Direction(Enum):
    Incoming = 1
    Outgoing = 2
    Both = 3


class Leg:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        return self.source + " => " + self.destination

    def calculateLength(self, locationMap):
        zip1 = self.source.split()[-1].strip("\"")
        zip2 = self.destination.split()[-1].strip("\"")
        dist = round(measurement.calculateDistance(locationMap[zip1], locationMap[zip2]), 2)
        return dist


class Trip:
    def __init__(self, person, legs):
        self.person = person
        self.legs = legs

    def calculateLength(self, locationMap):
        dist = round(sum(l.calculateLength(locationMap) for l in self.legs), 2)
        return dist

    def getLegsByZip(self, ZIP, direction):
        legz = []
        if direction != Direction.Incoming:
            for l in self.legs:
                if l.source.split()[-1].strip("\"") == ZIP:
                    legz.append(l)
        if direction != Direction.Outgoing:
            for l in self.legs:
                if l.destination.split()[-1].strip("\"") == ZIP:
                    legz.append(l)
        return legz

    def getLegsByState(self, state, direction):
        legz = []
        if direction != Direction.Incoming:
            for l in self.legs:
                if l.source.split()[-2] == state:
                    legz.append(l)
        if direction != Direction.Outgoing:
            for l in self.legs:
                if l.destination.split()[-2] == state:
                    legz.append(l)
        return legz

    def __add__(self, other):
        if isinstance(other, Leg):
            if self.legs[-1].destination == other.source:
                newLegs = self.legs
                newLegs.append(other)
                return Trip(self.person, newLegs)
            else:
                raise ValueError("Destination of new Leg must match source of last leg")
        if isinstance(other, Trip):
            if self.person == other.person:
                newLegs = self.legs + other.legs
                return Trip(self.person, newLegs)
            else:
                raise ValueError("The person must be the same for both trips")
        else:
            raise TypeError("Addition can only be done with Leg or Trip class")

    def __radd__(self, other):
        return self.__add__(other)


def getTotalDistanceFor(person):
    with open('trips.dat', 'r') as f:
        data = f.readlines()
    dist = 0
    for line in data:
        spl = line.split(':')
        if spl[0].strip("\"") == person:
            aa = []
            adds = re.findall(r'\"(.+?)\"', spl[1])
            for index, a in enumerate(adds[1:]):
                leg = Leg(adds[index], adds[index + 1])
                aa.append(leg)
            t = Trip(person, aa)
            dist += t.calculateLength(getLocationMap())
    return dist


def getLocationMap():
    with open('locations.dat', 'r') as f:
        data = f.readlines()[1:]
    locationMap = {}
    for line in data:
        line = line.split(',')
        locationMap[line[0].strip().strip("\"")] = (float(line[2].strip().strip("\"")), float(line[3].strip().strip("\"")))
    return locationMap


class RoundTrip(Trip):
    def __init__(self, person, legs):
        if legs[0].source.split()[-1].strip("\"") != legs[-1].destination.split()[-1].strip("\""):
            raise ValueError("Source ZIP from first leg must match destination ZIP from last leg")
        else:
            super().__init__(person, legs)


def getRoundTripCount():
    with open('trips.dat', 'r') as f:
        data = f.readlines()
        count = 0
    for line in data:
        spl = line.split(':')
        adds = re.findall(r'\"(.+?)\"', spl[1])
        if adds[0].split()[-1] == adds[-1].split()[-1]:
            count += 1
    return count


def getTrafficCount(**kwargs):
    if not ("direction" in kwargs and ("state" in kwargs or "code" in kwargs)):
        raise ValueError("Invalid arguments, must have direction and either state or code")


if __name__ == "__main__":
    locationMap = getLocationMap()
    l = Leg("Morganton, NC 28655", "Groton, MA 01450")
    print(l.calculateLength(locationMap))

    l1 = Leg("Packwood, WA 98361", "Naples, FL 34108")
    l2 = Leg("Naples, FL 34108", "Hilliard, FL 32046")
    l3 = Leg("Hilliard, FL 32046", "Putnam Station, NY 12861")
    #l4 = Leg("Putnam Station, NY 12861", "Packwood, WA 98361")
    print(l1, l2, l3)
    t = Trip("Taylor, Brian", [l1, l2, l3])
    t.calculateLength(locationMap)
    ls = t.getLegsByZip("99999", Direction.Both)
    for l in ls:
        print(l)

    ls = t.getLegsByState("FL", Direction.Outgoing)
    for l in ls:
        print(l)
    ls = t.getLegsByState("TX", Direction.Both)
    for l in ls:
        print(l)

    print(getTotalDistanceFor("Coleman, Lori"))
    print(getRoundTripCount())

    getTrafficCount(direction = Direction.Both)

