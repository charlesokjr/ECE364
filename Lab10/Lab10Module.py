#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >
#######################################################
from functools import total_ordering
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################


@total_ordering
class TimeSpan:
    def __init__(self, weeks, days, hours):
        if weeks < 0 or days < 0 or hours < 0:
            raise ValueError("The arguments cannot be negative.")
        self.hours = hours % 24
        self.days = (hours // 24 + days) % 7
        self.weeks = (hours // 24 + days) // 7 + weeks

    def __str__(self):
        return "{:02.0f}W {:01.0f}D {:02.0f}H".format(self.weeks, self.days, self.hours)

    def getTotalHours(self):
        return 168 * self.weeks + 24 * self.days + self.hours

    def __add__(self, other):
        if type(other) is not TimeSpan:
            raise ValueError("The argument must be of type TimeSpan.")
        hrs = (self.hours + other.hours) % 24
        ds = ((self.hours + other.hours) // 24 + self.days + other.days) % 7
        wks = ((self.hours + other.hours) // 24 + self.days + other.days) // 7 + self.weeks + other.weeks
        return TimeSpan(wks, ds, hrs)

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            if other < 0:
                raise ValueError("The argument must not be negative.")
            return TimeSpan(0, 0, round(self.getTotalHours() * other))
        else:
            raise ValueError("The argument must be of type int or float.")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if type(other) is not TimeSpan:
            raise ValueError("The argument must be of type TimeSpan.")
        return self.getTotalHours() == other.getTotalHours()

    def __gt__(self, other):
        if type(other) is not TimeSpan:
            raise ValueError("The argument must be of type TimeSpan.")
        return self.getTotalHours() > other.getTotalHours()


if __name__ == "__main__":
    ts = TimeSpan(0, 5, 49)
    ts2 = TimeSpan(0, 0, 0)
    print(TimeSpan(10, 10, 0).getTotalHours())
    print(ts)
    print(ts.getTotalHours())
    print((ts + ts2) + ts2)
    print(ts)
    print(ts * 5.1)
    print(1 * ts2)
    print(ts < ts2)
    print((99.0 * ts2).getTotalHours() - (ts2 * 99).getTotalHours())