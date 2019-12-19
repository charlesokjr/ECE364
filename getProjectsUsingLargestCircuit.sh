#! /bin/bash
high=0
egrep $(ls -lr circuits | sort -s | grep -o "[0-9]\{2\}[-][0-9][-][0-9]\{2\}" | tail -n -1) maps/projects.dat | grep -o "[0-9A-Z-]\{36\}" | sort -u
exit 0
