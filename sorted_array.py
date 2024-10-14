# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:14:57 2024

@author: mcs211
"""
def square_list(l):
    for i in l:
         return [i ** 2 for i  in l]

l = [2,3,5,7,8]
print(l)
new_list = square_list(l)
print(new_list)