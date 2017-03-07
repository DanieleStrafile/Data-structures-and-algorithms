'''
Created on 7 Mar 2017

@author: Daniele
'''
def insertion_sort(arr):
    
    for j in range(1,len(arr)-1):
        
        i = j
        
        while i>0 and arr[i-1]> arr[i]:
            
            arr[i],arr[i-1] = arr[i-1], arr[i]
            
            i -= 1
            
    return arr


arr = [0,1,4,6,3,2,6,7,4,3,2,7,10]

print(insertion_sort(arr))