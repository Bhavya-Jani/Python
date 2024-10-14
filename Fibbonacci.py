# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:37:51 2024

@author: mcs211
"""
num1=0
num2=1
fibbo = int(input("Enter the number of element: "))
print("{} {}".format(num1,num2))
for i in range(2,fibbo,1):
    num3=num1+num2
    print("{}".format(num3))
    num1=num2
    num2=num3