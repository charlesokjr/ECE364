#! /bin/bash

#----------------------------------
# $Author: ee364a13 $
# $Date: 2019-10-29 10:52:54 -0400 (Tue, 29 Oct 2019) $
#----------------------------------

function part_1 
{
  diff $(cat file.txt | sort) $(cat file.txt | sort -u)
  return
}                               

function part_2
{
  grep ".\{10\}" temp.txt | wc -l
  return
}

function part_3
{
  grep "PURDUE" info.txt | wc -l
  return
}


# To test your function, you can call it below like this:
#
part_1
#part_2
#part_3
