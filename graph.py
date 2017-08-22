#!/usr/bin/python
"""
Modul zawiera klase definiujaca strukture grafu
"""

from operator import itemgetter
import edge
class Graph:
    def __init__(self,n):
        self.n=n
        self.graph={}
        
    def add_node(self,node):
        """
        Funkcja dodaje do grafu wierzcholek
        """
        if node not in self.graph:
            self.graph[node]={}

    def add_edge(self,edge):
        """
        Funkcja dodaje do grafu krawedz zawierajaca informacje o wadze
        oraz wartosci polaczonych wierzcholkow
        """
        node1,node2,weight=edge.source, edge.target, edge.weight
        self.add_node(node1)
        self.add_node(node2)
        if node1==node2:
            raise Exception('Utworzenie peti niemozliwe!')
        if node1 not in self.graph[node2]:
            self.graph[node2][node1]=weight
        if node2 not in self.graph[node2]:
            self.graph[node1][node2]=weight

    def list_nodes(self):
        """
        Zwraca liste wierzcholkow grafu
        """
        return self.graph.keys()

    def list_edges(self):
        """
        Zwraca liste krawedzi wystepujacych w grafie.
        Krawedzie typu A-B i B-A nie sa dublowane
        """
        L=[]
        for nodeA in self.graph:
            for nodeB in self.graph[nodeA]: 
                if edge.Edge(nodeB,nodeA,self.graph[nodeB][nodeA]) not in L:
                    L.append(edge.Edge(nodeA,nodeB,self.graph[nodeA][nodeB]))
        return L

    def show_graph(self):
        """
        Funkcja wypisujaca na ekranie graf w postaci listy sasiedztwa
        """
        print "Lista sasiedztwa dla wierzcholkow grafu:"
        for nodeA in self.graph:
            print nodeA,':',
            for nodeB in self.graph[nodeA]:
                print "%s(%s)"%(nodeB,self.graph[nodeA][nodeB]),
            print
            
    def sort_edges(self,liste):
        """
        Zwraca posortowana rosnaco wedlug wagi liste krawedzi
        """
        if not liste:
            raise Exception("Brak listy krawedzi do posortowania!")
        return sorted(liste,key=lambda x: x.weight)
