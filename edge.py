#!/usr/bin/python
""" Klasa definiujaca obiekt krawedzi """
class Edge:
    
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
        
    def __repr__(self):
        return "Edge(%s, %s, %s)" % (repr(self.source), repr(self.target), repr(self.weight))

    def __cmp__(self, other):
        if self.weight > other.weight:
            return 1
        if self.weight < other.weight:
            return -1
        if self.source > other.source:
            return 1
        if self.source < other.source:
            return -1
        if self.target > other.target:
            return 1
        if self.target < other.target:
            return -1
        return 0
    
    def __hash__(self):
        return hash(repr(self))

