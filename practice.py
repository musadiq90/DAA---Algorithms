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
url ='hash.txt'
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
        'D': 4
    }
    return (switcher.get(value, "-10"))

def InsertWord(str):
    sum =0
    for i in range(0,len(str)):
        sum = sum + int(Calculator(str[i]))        
    return sum

def addtoArray(index, array, word):
    y = " "
    if(array[index][0] == y):
       array[index][0] = word
    else:
        c = getCount(array,index)
        array[index][c]
    return array    

def getCount(array, index):
    c1 = count[index];
    count[index]= c1+1;
    return c1
    


wiki = TextBlob("f aaaaaa bbb cc da")

#modlist to store the mod of each word
modList = list()

data = list()
data = data1.words
count =0
for words in data1.words:
    count = count+1
    
print("count is ",count)

x = " "
rows, cols = (50, 3) 
array = [[x for i in range(cols)] for j in range(rows)] 



for words in data1.words:
    ind = Modular(InsertWord(words),50)
    modList.append(ind)
    array=addtoArray(ind, array, words)

print(array)


