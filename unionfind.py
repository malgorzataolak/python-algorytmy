#!/usr/bin/python
"""
Modul definiuje operacje na zbiorach
"""
class UnionFind:

    def __init__(self):
        self.parent = {}

    def create(self, x):
        """
        Funkcja tworzy drzewa jednoelementowe
        """
        if x not in self.parent:
            self.parent[x] = x

    def find(self, x):
        """
        Funkcja szuka korzenia drzewa
        """
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        """
        Funkcja sprawdza czy wierzcholki znajduja sie w jednym zbiorze.
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.parent[x] = y
