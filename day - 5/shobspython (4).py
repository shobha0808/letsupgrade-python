# -*- coding: utf-8 -*-
"""shobspython.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SrN7qghncZ7Aa4CN0AuHyapjEwE4m-WS
"""

#prime number using filter function in the range

def isPrime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True

fltrObj=filter(isPrime, range(2500))

print (list(fltrObj),  "Prime numbers between 1-2500:")


#to capatilize the whole sentence

"hey this is sai i am in mumbai...".title()
