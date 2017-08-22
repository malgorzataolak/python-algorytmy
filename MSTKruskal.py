#!/usr/bin/python
"""
Modul odpowiedzialny za stworzenie minimalnego drzewa rozpinajacego
wedlug algorytmu Kruskala
"""
from operator import itemgetter
import queue as q
import unionfind as u
import edge

class Kruskal():
    
    def __init__(self,graph):
        self.graph=graph
        self.sets=u.UnionFind()
        self.my_queue=q.Queue(20)

    def make_sets(self,listn):
        """
        Funkcja tworzaca las
        """
        if not listn:
            raise Exception("Brak wierzcholkow do utworzenia drzew!")
        for item in listn:
            self.sets.create(item)
        
    def create_queue(self,listse):
        """
        Funkcja zwraca kolejke FIFO krawedzi posortowanych rosnaco wedlug wag
        """
        if not listse:
            raise Exception("Brak krawedzi!")

        for item in listse:
            self.my_queue.put(item)
        return self.my_queue
    
    def make_mst(self):
        """
        Funkcja zwracajaca liste krawedzi tworzacych minimalne drzewo rozpinajce
        """
        mst=[]
        self.make_sets(self.graph.list_nodes())
        self.my_queue=self.create_queue(self.graph.sort_edges(self.graph.list_edges()))
        while not self.my_queue.is_empty():
            edge=self.my_queue.get()
            if self.sets.find(edge.source)!=self.sets.find(edge.target):
                self.sets.union(edge.source,edge.target)
                mst.append(edge)
        return mst
    
    def show_mst(self,listm):
        """
        Funkcja pokazuje krawedzie tworzace minimalne drzewo rozpinajace
        """
        print "Minimalne drzewo rozpinajace:"
        if not listm:
            raise Exception("Brak minimalnej sciezki rozpinajacej!")
        for item in listm:
            print item


