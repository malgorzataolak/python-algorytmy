#!/usr/bin/python
"""
Modul testujacy oraz ilustrujacy operacje przeprowadzane za pomoca algorytmu Kruskala.
Tworzy graf na podstawie podanych krawedzi i znajduje dla niego minimalne drzewo rozpinajace
"""
import unittest
import graph
import edge
import MSTKruskal

class TestKruskal(unittest.TestCase):
    """
    Klasa testujaca poprawnosc minimalnego drzewa rozpinajacego
    """
    def setUp(self):
        self.graphA=graph.Graph(8)
        self.ListaSasiedztwaA=[edge.Edge(1,2,2),edge.Edge(2,3,9),edge.Edge(3,4,13),edge.Edge(4,5,4),edge.Edge(5,6,33),edge.Edge(6,2,1),edge.Edge(2,4,6),edge.Edge(4,6,30),edge.Edge(1,3,20),edge.Edge(3,5,11),edge.Edge(5,1,17),edge.Edge(5,7,5),edge.Edge(6,1,35)]
        for item in self.ListaSasiedztwaA:
            self.graphA.add_edge(item)
        self.kruskalA=MSTKruskal.Kruskal(self.graphA)
        
        self.graphB=graph.Graph(9)
        self.ListaSasiedztwaB=[edge.Edge(0,3,9),edge.Edge(0,1,5),edge.Edge(0,6,3),edge.Edge(1,5,6),edge.Edge(1,4,8),edge.Edge(1,7,7),edge.Edge(1,2,9),edge.Edge(2,3,9),edge.Edge(2,4,4),edge.Edge(2,7,3),edge.Edge(3,6,8),edge.Edge(4,6,1),edge.Edge(4,5,2),edge.Edge(5,6,6),edge.Edge(6,7,9)]
        for item in self.ListaSasiedztwaB:
            self.graphB.add_edge(item)
        self.kruskalB=MSTKruskal.Kruskal(self.graphB)

        self.graphC=graph.Graph(7)
        self.ListaSasiedztwaC=[edge.Edge(1,2,15),edge.Edge(2,5,40),edge.Edge(1,5,60),edge.Edge(1,3,35),edge.Edge(3,5,30),edge.Edge(3,4,10),edge.Edge(1,4,30),edge.Edge(1,6,50),edge.Edge(5,6,70),edge.Edge(4,6,15)]
        for item in self.ListaSasiedztwaC:
            self.graphC.add_edge(item)
        self.kruskalC=MSTKruskal.Kruskal(self.graphC)
        
    def test_nodes(self):
        self.assertEqual(self.graphA.list_nodes(),[1,2,3,4,5,6,7])
        self.assertEqual(self.graphB.list_nodes(),[0,1,2,3,4,5,6,7])
        self.assertEqual(self.graphC.list_nodes(),[1,2,3,4,5,6])

    def test_mst(self):
        testsetA=set(self.kruskalA.make_mst())
        mstsetA=set([edge.Edge(2,6,1),edge.Edge(1,2,2),edge.Edge(4,5,4),edge.Edge(5,7,5),edge.Edge(2,4,6),edge.Edge(2,3,9)])
        self.assertEqual(testsetA,mstsetA)

        testsetB=set(self.kruskalB.make_mst())
        mstsetB=set([edge.Edge(4,6,1),edge.Edge(4,5,2),edge.Edge(0,6,3),edge.Edge(2,7,3),edge.Edge(2,4,4),edge.Edge(0,1,5),edge.Edge(3,6,8)])
        self.assertEqual(testsetB,mstsetB)

        testsetC=set(self.kruskalC.make_mst())
        mstsetC=set([edge.Edge(3,4,10),edge.Edge(1,2,15),edge.Edge(4,6,15),edge.Edge(1,4,30),edge.Edge(3,5,30)])
        self.assertEqual(testsetC, mstsetC)
        
if __name__ == '__main__':
    """
    Trzy grafy, ktore obrazuja wierzcholki, liste sasiedztwa oraz minimalne drzewo rozpinajace
    """
    graph1=graph.Graph(8)
    graph2=graph.Graph(9)
    graph3=graph.Graph(7)
    ListaSasiedztwa=[edge.Edge(1,2,2),edge.Edge(2,3,9),edge.Edge(3,4,13),edge.Edge(4,5,4),edge.Edge(5,6,33),edge.Edge(6,2,1),edge.Edge(2,4,6),edge.Edge(4,6,30),edge.Edge(1,3,20),edge.Edge(3,5,11),edge.Edge(5,1,17),edge.Edge(5,7,5),edge.Edge(6,1,35)]
    ListaSasiedztwa2=[edge.Edge(0,3,9),edge.Edge(0,1,5),edge.Edge(0,6,3),edge.Edge(1,5,6),edge.Edge(1,4,8),edge.Edge(1,7,7),edge.Edge(1,2,9),edge.Edge(2,3,9),edge.Edge(2,4,4),edge.Edge(2,7,3),edge.Edge(3,6,8),edge.Edge(4,6,1),edge.Edge(4,5,2),edge.Edge(5,6,6),edge.Edge(6,7,9)]
    ListaSasiedztwa3=[edge.Edge(1,2,15),edge.Edge(2,5,40),edge.Edge(1,5,60),edge.Edge(1,3,35),edge.Edge(3,5,30),edge.Edge(3,4,10),edge.Edge(1,4,30),edge.Edge(1,6,50),edge.Edge(5,6,70),edge.Edge(4,6,15)]

    print "\nGraf 1:"
    for item in ListaSasiedztwa:
        graph1.add_edge(item)
        
    print "Lista wierzcholkow:"
    print graph1.list_nodes()

    graph1.show_graph()

    kruskal1=MSTKruskal.Kruskal(graph1)
    kruskal1.show_mst(kruskal1.make_mst())

    print "\nGraf 2:"
    for item in ListaSasiedztwa2:
        graph2.add_edge(item)
        
    print "Lista wierzcholkow:"
    print graph2.list_nodes()
   
    graph2.show_graph()
    
    kruskal2=MSTKruskal.Kruskal(graph2)
    kruskal2.show_mst(kruskal2.make_mst())

    print "\nGraf 3:"
    for item in ListaSasiedztwa3:
        graph3.add_edge(item)
        
    print "Lista wierzcholkow:"
    print graph3.list_nodes()

    graph3.show_graph()
    
    kruskal3=MSTKruskal.Kruskal(graph3)
    kruskal3.show_mst(kruskal3.make_mst())
    unittest.main()
