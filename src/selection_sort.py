'''
Created on 26 Mar 2017

@author: Daniele
'''
def selection_sort(arr):
    
    for j in range(0,len(arr)-2):
        minimum = j
        for i in range(j+1,len(arr)-1):
            if arr[minimum] > arr[i]:
                minimum = i
        arr[j],arr[minimum] = arr[minimum],arr[j]
    return arr
        

arr = [0,1,4,6,3,2,6,7,4,3,2,7,10]

print(selection_sort(arr))