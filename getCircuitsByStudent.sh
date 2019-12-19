#! /bin/bash
ID=$(egrep "$1" maps/students.dat | tail -c 12)
egrep $ID -lr circuits | grep -o "[0-9]\{2\}[-][0-9][-][0-9]\{2\}" | sort
exit 0
