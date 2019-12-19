#! /bin/bash
ID=$(egrep "$1" maps/students.dat | tail -c 12)
circs=$(egrep $ID -lr circuits | grep -o "[0-9]\{2\}[-][0-9][-][0-9]\{2\}")
egrep -f $circs maps/projects.dat | grep -o "[0-9A-Z-]\{36\}" | sort -u
exit 0
