'''
Created on 15 Feb 2017

@author: Daniele
'''
import sys

class Set:
    __my_array = []
    __size_my_array = 0
    
    def __init__(self):
        self . __my_array = []
        self . __size_my_array = 0
        
    def size(self):
        return len(self)
    
    def is_empty(self):
        if size(self) == 0:
            return True
        else:
            return False
        
    def contains(self, elem):
        for i in range(0,len(self)):
            if self[i] == elem:
                return True
        return False
    
    def add(self, elem):
        found = True
        for i in range(0, len(self)):
            if self[i] == elem:
                found = False
        if found == True:
            self.append(elem)
    
    def remove(self, elem):
        for i in range(0, len(self)):
            if self[i] == elem:
                for j in range(i, len(self) - 1):
                    self[j] = self[j+1]
                self.pop()
                break
                
    def union(self, b):
        for i in range()           
                
    
    
    
            
    
    
    
    
            
            