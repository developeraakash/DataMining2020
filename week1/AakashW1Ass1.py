#!/usr/bin/python

class ListKeeper:
    
    def __init__(self):
        self.dict = {"example" : [1,2,3,4,5]} 
        
    #returns all list names
    def show(self):
        print(self.dict.keys())
    
    #adds a new list
    def add(self,name, list):
        self.dict[name] = list
     
    #deletes list
    def delete(self,name):
        del self.dict[name]
     
    #returns the sorted list name
    def sort(self,name):
        self.dict[name].sort()
        print(self.dict[name])
     
    #appends list to name
    def append(self,name, list):
        self.dict[name].append(list)
        print(self.dict[name])
        
    #to see values of dictionary testing the functionality   
    def values(self,name):
        print(self.dict[name])