#! /bin/bash
touch file4.txt
rm file4.txt
touch file4.txt
egrep $1 maps/projects.dat | cut -f5 -d' ' > file1.txt
var=$(ls circuits | egrep -f file1.txt)
for v in $var
do
	cat circuits/$v | grep -o "[0-9]\{5\}[-][0-9]\{5\}" >> file4.txt
done
egrep -f file4.txt maps/students.dat | cut -f1,2 -d' ' | cat
exit 0
