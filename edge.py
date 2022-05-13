import random

class Edge:
        """
        Clase Edge: Referente a las aristas.
        """

        def __init__(self,source,target,id):

                self.n0 = source
                self.n1 = target
                self.id = id
                self.distance = 1 + 0.1*random.random()
