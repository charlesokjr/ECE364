#! /bin/bash
if [[ $(egrep $1 -lr circuits | wc -l) -gt $(egrep $2 -lr circuits | wc -l) ]]; then echo $1; else echo $2; fi
exit 0
