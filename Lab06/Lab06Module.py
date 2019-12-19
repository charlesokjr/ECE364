#######################################################
#    Author:      <Ethan Glaser>
#    email:       <glasere@purdue.edu>
#    ID:           <ee364a13>
#    Date:         <10/1/19>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import re
#######################################################
# No Module -Level  Variables  or  Statements!
# ONLY  FUNCTIONS  BEYOND  THIS  POINT!
#######################################################


def getGenres():
    catalog = bookReader()
    genres = []
    for book in catalog:
        genres.append(re.findall(r'<genre>(.+?)</genre>', book)[0])
    genres = set(genres)
    return genres


def getAuthorOf(bookName):
    catalog = bookReader()
    for book in catalog:
        if bookName == re.findall(r'<title>(.+?)</title>', book)[0]:
            return re.findall(r'<author>(.+?)</author>', book)[0]
    return "Error"


def getBookInfo(bookID):
    catalog = bookReader()
    for book in catalog:
        if bookID == re.findall(r'\"(.+?)\">', book)[0]:
            return re.findall(r'<description>(.+?)</description>', book)[0]
    return 1


def getBooksBy(authorName):
    catalog = bookReader()
    books = []
    for book in catalog:
        if authorName == re.findall(r'<author>(.+?)</author>', book)[0]:
            books.append(re.findall(r'<title>(.+?)</title>', book)[0])
    return books


def bookReader():
    with open('books.xml', 'r') as f:
        data = f.read()
    books = re.findall(r"<book id=(.+?)</book>", data, re.DOTALL)

    return books



# This  block  is  optional  and  can be used  for  testing.
# We will  NOT  look  into  its  content.
#######################################################
if __name__  == "__main__":
    #print(bookReader())
    print(getGenres())
    print(getAuthorOf('Paradox Lost'))
    print(getBookInfo("bk111"))
    print(getBooksBy("Corets, Eva"))