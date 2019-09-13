# -*- coding: utf-8 -*-

class printTree:
    import collections
    
    def __init__(self, dictio):
        methodKey = getattr(dictio, "keys", None)
        if methodKey is not None:
            self.type = type(dictio)
            self.printAux(dictio)
        else:
            raise TypeError("The object to print as tree is not a dictionary.")
    
    def printAux(self, dictio, tab = 0):
        if type(dictio) == self.type:
            print("")
            for key in dictio:
                print(("\t"*tab)+key+":",end=" ")
                self.printAux(dictio[key], tab+1)
        else:
            print(str(dictio))