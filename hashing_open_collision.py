# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:41:34 2019

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



def addtoArray(index, array, word):
    k =  " "
    if(array[index] == k):
        array[index] = word
    else:
        addtoArray(index+1, array, word)
    return array    




data = list()
data = data1.words
count =0
for words in data1.words:
    count = count+1

d=" "
count = count+10;       
print("count is ",count)
array = [d]*count
modVal = int(input("enter the Modulus value: "))
print(modVal)
for words in data1.words:
    ind = Modular(InsertWord(words),modVal)
    array=addtoArray(ind, array, words)

print(array)

insert = input("Enter the word you want to insert: ")
data.append(insert)

array=addtoArray(ind, array, insert)
print(array)

delete = input("Enter the word you want to delete: ")
array.remove(delete)
print(array)
print("the above list is updated one.")

