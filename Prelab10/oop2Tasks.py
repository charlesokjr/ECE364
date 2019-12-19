#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >
#######################################################
import os
import math
import copy
import collections
from enum import Enum
from functools import total_ordering

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

DataPath = os.path.expanduser('<Path  Provided  to You >')


@total_ordering
class Datum:
    def __init__(self, *args):
        l = []
        for arg in args:
            if type(arg) is not float and type(arg) is not int:
                raise ValueError("Wrong type: all args must be floats")
            l.append(arg)
        self._storage = tuple(l)

    def __str__(self):
        string = '('
        for val in self._storage:
            string += "{0:.2f}, ".format(val)
        string = string[:-2] + ')'
        return string

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(self._storage)

    def distanceFrom(self, d):
        if type(d) is not Datum:
            raise ValueError("Incorrect type: arg must be of type datum")
        sum = 0
        for i in range(min(len(self._storage), len(d._storage))):
            sum += (self._storage[i] - d._storage[i]) ** 2
        for i in range(min(len(self._storage), len(d._storage)), max(len(self._storage), len(d._storage))):
            if len(self._storage) > len(d._storage):
                sum += self._storage[i] ** 2
            else:
                sum += d._storage[i] ** 2
        sum = math.sqrt(sum)
        return sum

    def clone(self):
        return copy.deepcopy(self)

    def __contains__(self, f):
        if f in self._storage:
            return True
        return False

    def __neg__(self):
        arr = []
        for val in self._storage:
            arr.append(-val)
        neww = Datum()
        neww._storage = tuple(arr)
        return neww

    def __len__(self):
        return len(self._storage)

    def __iter__(self):
        return iter(self._storage)

    def __getitem__(self, index):
        return self._storage[index]

    def __add__(self, d):
        if type(d) is float or type(d) is int:
            new = Datum()
            newStorage = tuple(d + x for x in self._storage)
            new._storage = newStorage
            return new
        if type(d) is Datum:
            new = []
            for i in range(min(len(self._storage), len(d._storage))):
                new.append(self._storage[i] + d._storage[i])
            for i in range(min(len(self._storage), len(d._storage)), max(len(self._storage), len(d._storage))):
                if len(self._storage) < len(d._storage):
                    new.append(d._storage[i])
                else:
                    new.append(self._storage[i])
            dat = Datum()
            dat._storage = tuple(new)
            return dat
        else:
            raise ValueError("Invalid type: addition only compatible with float type and Datum class")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, d):
        if type(d) is float or type(d) is int:
            new = Datum()
            newStorage = tuple(x - d for x in self._storage)
            new._storage = newStorage
            return new
        if type(d) is Datum:
            new = []
            for i in range(min(len(self._storage), len(d._storage))):
                new.append(self._storage[i] - d._storage[i])
            for i in range(min(len(self._storage), len(d._storage)), max(len(self._storage), len(d._storage))):
                if len(self._storage) < len(d._storage):
                    new.append(-d._storage[i])
                else:
                    new.append(self._storage[i])
            dat = Datum()
            dat._storage = tuple(new)
            return dat
        else:
            raise ValueError("Invalid type: subtraction only compatible with float type and Datum class")

    def __rsub__(self, d):
        if type(d) is float or type(d) is int:
            new = Datum()
            newStorage = tuple(d - x for x in self._storage)
            new._storage = newStorage
            return new

    def __eq__(self, other):
        if type(other) is not Datum:
            raise ValueError("Invalid type: must be Datum")
        if sum(x ** 2 for x in self) == sum(y ** 2 for y in other):
            return True
        return False

    def __gt__(self, other):
        if type(other) is not Datum:
            raise ValueError("Invalid type: must be Datum")
        if sum(x ** 2 for x in self._storage) > sum(y ** 2 for y in other._storage):
            return True
        return False

    def __mul__(self, other):
        if type(other) is not float and type(other) is not int:
            raise ValueError("Invalid type: must be float")
        new = Datum()
        newStorage = tuple(other * x for x in self._storage)
        new._storage = newStorage
        return new

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) is not float and type(other) is not int:
            raise ValueError("Invalid type: must be float")
        new = Datum()
        newStorage = tuple(x / other for x in self._storage)
        new._storage = newStorage
        return new

    def __rtruediv__(self, other):
        if type(other) is not float and type(other) is not int:
            raise ValueError("Invalid type: must be float")
        new = Datum()
        newStorage = tuple(other / x for x in self._storage)
        new._storage = newStorage
        return new


class Data(collections.UserList):
    def __init__(self, initial=None):
        if not initial:
            super().__init__([])
        else:
            for val in initial:
                if type(val) is not Datum:
                    raise ValueError("All elements must be type float")
            super().__init__(initial)

    def computeBounds(self):
        l = max(len(val) for val in self.data)
        minl = min(len(val) for val in self.data)
        minn = []
        maxx = []
        for i in range(l):
            arr = []
            for d in self.data:
                if len(d) > i:
                    arr.append(d[i])
            if i + 1 > minl:
                arr.append(0)
            minn.append(min(arr))
            maxx.append(max(arr))
        minn = tuple(minn)
        maxx = tuple(maxx)
        mi = Datum()
        mi._storage = minn
        ma = Datum()
        ma._storage = maxx
        return mi, ma

    def computeMean(self):
        l = max(len(val) for val in self.data)
        mean = []
        for i in range(l):
            arr = []
            for d in self.data:
                if len(d) > i:
                    arr.append(d[i])
            mean.append(sum(arr) / max(len(x) for x in self.data))
        mean = tuple(mean)
        me = Datum()
        me._storage = mean
        return me

    def append(self, item):
        if type(item) is not Datum:
            raise ValueError("Item to append must be of type Datum")
        super().append(item)

    def count(self, item):
        if type(item) is not Datum:
            raise ValueError("Item to count must be of type Datum")
        return super().count(item)

    def index(self, item, *args):
        if type(item) is not Datum:
            raise ValueError("Item to index must be of type Datum")
        return super().index(item, *args)

    def insert(self, i, item):
        if type(item) is not Datum:
            raise ValueError("Item to insert must be of type Datum")
        super().insert(i, item)

    def remove(self, item):
        if type(item) is not Datum:
            raise ValueError("Item to remove must be of type Datum")
        super().remove(item)

    def __setitem__(self, key, value):
        if type(value) is not Datum:
            raise ValueError("Value to set must be of type Datum")
        return super().__setitem__(key, value)

    def extend(self, other):
        if type(other) is not Data:
            raise ValueError("Item to extend must be of type Data")
        super().extend(other)


class DataClass(Enum):
    Class1 = 1
    Class2 = 2


class DataClassifier:
    def __init__(self, group1, group2):
        if type(group1) is not Data or type(group2) is not Data:
            raise ValueError("DataClassifier Args must be of type Data")
        if not len(group1) or not len(group2):
            raise ValueError("Args of DataClassifier must not be empty")
        self._class1 = group1
        self._class2 = group2

    def classify(self, d):
        dist1 = 0
        dist2 = 0
        m1 = self._class1.computeMean()
        m2 = self._class2.computeMean()
        if len(d) > len(m1):
            dist1 += sum((d[i] - m1[i]) ** 2 for i in range(len(m1)))
            dist1 += sum(d[i] ** 2 for i in range(len(m1), len(d)))
        else:
            dist1 += sum((d[i] - m1[i]) ** 2 for i in range(len(d)))
            dist1 += sum(m1[i] ** 2 for i in range(len(d), len(m1)))
        if len(d) > len(m2):
            dist2 += sum((d[i] - m2[i]) ** 2 for i in range(len(m2)))
            dist2 += sum(d[i] ** 2 for i in range(len(m2), len(d)))
        else:
            dist2 += sum((d[i] - m2[i]) ** 2 for i in range(len(d)))
            dist2 += sum(m2[i] ** 2 for i in range(len(d), len(m2)))
        if dist1 > dist2:
            return DataClass.Class2
        else:
            return DataClass.Class1


if __name__  == "__main__":
    data = Datum(1, -2.0, 1243.0918, 903.0)
    data2 = Datum(1.1)
    data3 = Datum(3.0, -4.0)
    data4 = Datum(5.0)
    #print(data - data2)
    #print(data)
    #print(1.0 - data)
    #print(repr(data))
    #print(hash(data))
    #print(data.distanceFrom(data2))
    #data3 = data.clone()
    #print(data3)
    #data = Datum(2.9, 23.0)
    #print(903.0 in data)
    #print(len(data))
    #print(data[1])
    #print(data4 >= data3)
    data5 = data / 5.0
    #print(data5)
    #print(data5 + 1.1)
    #print(data5)
    da = Data([data, data2, data3, data4])
    #print(da.computeBounds())
    #print(da.computeMean())
    #print(da.index(data4))
    #print(da)
    dd1 = Data([Datum(1,2,3), Datum(3,2,1), Datum(1)])
    dd2 = Data([Datum(100,200,300), Datum(300,200,100)])
    dc = DataClassifier(dd1, dd2)
    #print(dc.classify(Datum(100,100,2,5)))

    dd2.append(data2)
    #dd2.append(4)
    print(dd2.index(data2))
    #print(dd2.index(4))
    data = Datum(-3.0, 1.2, 3.1415, 2.7, 9.9)
    print(data > data2)
    print(data != data2)
    print(data >= data2)
    print(data < data2)
    print(data == data2)
    print(data, 4 * data, data * 4)
    print(data, -data)
    print(data, data + 10.)
    print(data, data - 1)
    print(data, data / 2)
    print(data, data2, data + data2, data2 + data)

