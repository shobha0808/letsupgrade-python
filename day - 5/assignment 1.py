# -*- coding: utf-8 -*-
"""shobspython.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SrN7qghncZ7Aa4CN0AuHyapjEwE4m-WS
"""
list_one=[1,1,5] 
list_two=[1,5,6,4,1,2,3,5]
if all(a in list_two for a in list_one):
    print('yeahhh its a match')
    
    
list_one=[1,1,5] 
list_two=[1,5,6,5,1,2,3,6]
if all(a in list_two for a in list_one):
    print('its gone')

