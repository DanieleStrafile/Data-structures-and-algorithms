'''
Created on 26 Mar 2017

@author: Daniele
'''

def bubble_sort_optimised(arr):
    for s in range(0,len(arr)):
        swapped = False
        for current in range(0,len(arr)-s-1):
            if arr[current] > arr[current+1]:
                arr[current], arr[current+1] = arr[current+1], arr[current]
                swapped = True
        if swapped == False:
            break

arr = [4,5,7,1]

bubble_sort_optimised(arr)

print(arr)