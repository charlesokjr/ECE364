#! /bin/bash
cat $(egrep $(grep "$1" maps/students.dat | tail -c -12) -lr circuits) | grep -o "[A-Z]\{3\}[-][0-9]\{3\}" | sort -u
exit 0
