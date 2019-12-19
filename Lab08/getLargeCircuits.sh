#! /bin/bash
touch file1.txt
rm file1.txt
touch file1.txt
ls -lr circuits | cut -f5,9 -d' ' > file.txt
for c in $(ls -lr circuits | cut -f5,9 -d' ' | sort | cut -f1 -d' ' | sort -u)
do
if [[ $c -ge 200 ]]
then
	grep $c file.txt >> file1.txt
fi
done
grep -o "[0-9]\{2\}[-][0-9][-][0-9]\{2\}" file1.txt | sort -u
exit 0
