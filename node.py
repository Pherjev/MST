class Node:
        """
        Clase Nodo: Referente a los nodos. 
        """
        def __init__(self,id):

                self.id = id
                self.x = 0
                self.y = 0
                self.degree = 0
                self.neighboors = set()
