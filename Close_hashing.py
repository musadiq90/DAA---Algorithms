# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:28:13 2019

@author: MUSADIQ.4683179
"""

from textblob import TextBlob
import sys
from importlib import reload
reload(sys)  
sys.getdefaultencoding() 
filename= input("enter the nane of file: ")
url = filename
file=open(url)
t=file.read()
data1 = TextBlob(t)



#function to calculate modular
def Modular(x,m):
    return (x%m)


def Calculator(value):
    switcher = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g':7, 
        'h':8,
        'i':9,
        'j':10,
        'k':11,
        'l':12,
        'm':13,
        'n':14,
        'o':15,
        'p':16,
        'q':17,
        'r':18,
        's':19,
        't':20,
        'u':21,
        'v':22,
        'w':23,
        'x':24,
        'y':25,
        'z':26,
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
	    'E': 5,
        'F': 6,
        'G': 7, 
        'H':8,
        'I':9,
        'J':10,
        'K':11,
        'L':12,
        'M':13,
        'N':14,
        'O':15,
        'P':16,
        'Q':17,
        'R':18,
        'S':19,
        'T':20,
        'U':21,
        'V':22,
        'W':23,
        'X':24,
        'Y':25,
        'Z':26
    }
    return (switcher.get(value, "-10"))

def InsertWord(str):
    sum =0
    for i in range(0,len(str)):
        sum = sum + int(Calculator(str[i]))        
    return sum

def addtoArray(index, array, word, countArray):
    y = " "
    if(array[index][0] == y):
       array[index][0] = word
    else:
        c = getCount(array,index, countArray)
        array[index][c]= word
    return array    

def getCount(array, index, countArray):
    c1 = countArray[index];
    countArray[index]= c1+1;
    return c1


#modlist to store the mod of each word
modList = list()

data = list()
data = data1.words
count =0
for words in data1.words:
    count = count+1
    
print("count is ",count)
y=0
countArray = [y]*50

x = " "
rows, cols = (50, 90) 
array = [[x for i in range(cols)] for j in range(rows)] 



for words in data1.words:
    ind = Modular(InsertWord(words),50)
    array=addtoArray(ind, array, words, countArray)

print(array)

insert = input("enter the word you want to insert : ")
indx= Modular(InsertWord(insert),50)
array=addtoArray(indx, array, insert, countArray)
print(array)
array[0].sort()


delete = input("enter the word you want to delete: ")
print(array)
print("the value has been delete, the upadated list is above")

