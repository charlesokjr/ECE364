#! /bin/bash
egrep $1 -lr circuits | wc -l
exit 0
