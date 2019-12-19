#! /bin/bash
egrep $1 maps/projects.dat | cut -f5 -d' ' | sort
exit 0
