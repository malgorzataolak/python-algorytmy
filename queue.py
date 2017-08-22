#!/usr/bin/python
"""
Modul odpowiedzialny za definicje struktury kolejki FIFO
"""
class Queue:

    def __init__(self, size):
        self.n = size + 1       
        self.items = self.n * [None] 
        self.head = 0       
        self.tail = 0

    def is_empty(self):
        """
        Funkcja sprawdza czy w kolejka jest pusta
        """
        return self.head == self.tail

    def is_full(self):
        """
        Funkcja sprawdza czy kolejka jest pelna
        """
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        """
        Funkcja przeprowadza operacje wstawienia elementu do kolejki
        """
        if self.is_full():
            raise Exception("Kolejka jest pelna!")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        """
        Funkcja przeprowadza operacje pobrania elementu z kolejki
        """
        if self.is_empty():
            raise Exception("Kolejka jest pusta!")
        data = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.n
        return data
