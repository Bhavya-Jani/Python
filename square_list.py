# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:06:14 2024

@author: mcs211
"""
def sorted_arr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

arr = [4,7,1,8,3]
print(arr)
sorted_arr(arr)
print(arr)
