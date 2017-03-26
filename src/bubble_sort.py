'''
Created on 26 Mar 2017

@author: Daniele
'''

def bubble_sort(arr):
    for s in range(1,len(arr)):
        for current in range(0,len(arr)-1):
            if arr[current] > arr[current+1]:
                arr[current], arr[current+1] = arr[current+1], arr[current]
    return arr

arr = [7,4,10]

print(bubble_sort(arr))