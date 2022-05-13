# -*- coding: utf-8 -*-

import math
import random
import numpy as np
import graphviz
from PIL import Image
from queue import PriorityQueue
from Pqueue import PriorityQueue2
#from colormap import rgb2hex

from edge import Edge
from node import Node
#from BFS import BFS

class Graph:
        """
        Clase grafo: Referente al grafo
        """
        def __init__(self,digraph=False,eng = 'fdp'):

                """
                Inicializa un grafo vacío.
                """

                self.id = 'graph'
                self.nodes = dict()
                self.edges = dict()
                self.digraph = digraph
                self.eng = eng
                if digraph:
                        self.display = graphviz.Digraph(format='png',engine=eng)
                else:
                        self.display = graphviz.Graph(format='png',engine = eng)

        def addNode(self, name,pos='0',colour = 'red'):
                """
                Agrega un nodo al grafo con el id name.
                pos: posición del nodo
                """
                if name not in self.nodes.keys():
                        node = Node(name)
                        #colour = rgb2hex(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                        self.nodes[name] = node
                        if pos == '0':
                                self.display.node(name,shape='point',color=colour)
                        else:
                                self.display.node(name,shape='point',color=colour,pos=pos)
                #return self.getNode(name)

        def addEdge(self, name, node0, node1):
                """
                Agrega una arista con nodos node0 y node1 como ids. 
                Crea los nodos si no existen.
                """
                if name not in self.edges.keys():
                        self.addNode(node0)
                        self.addNode(node1)
                        n0 = self.getNode(node0)
                        n1 = self.getNode(node1)
                        e = Edge(n0,n1,name)
                        self.edges[name] = e
                        self.display.edge(node0,node1,color='gray')
                        n0.degree += 1
                        n1.degree += 1
                        n0.neighboors.add(node1)
                        n1.neighboors.add(node0)
                #return e

        def removeEdge(self,name):
                """
                Elimina la arista de nombre name
                Nota: No se borra del display, por lo que hay que copiar el grafo
                """
                if name in self.edges.keys():
                       edge = self.getEdge(name)
                       n0 = edge.n0
                       n1 = edge.n1
                       node0 = n0.id
                       node1 = n1.id
                       del self.edges[name]
                       n0.degree -= 1
                       n1.degree -= 1
                       n0.neighboors.remove(node1)
                       n1.neighboors.remove(node0)


        def getNode(self,name):
                """
                Invoca al nodo con el id name.
                """
                return self.nodes.get(name)

        def getEdge(self,name):
                """
                Invoca a la arista con el id name.
                """
                return self.edges.get(name)

        def copy(self):
                g = Graph(eng = self.eng)
                nodos = self.nodes.keys()
                nodos = list(nodos)
                for node in nodos:
                        #g.addNode(node)
                        if self.eng == 'neato':
                                x = self.getNode(node).x
                                y = self.getNode(node).y
                                g.addNode(node,pos=str(x) + ','+ str(y)+'!')
                                g.getNode(node).x = x
                                g.getNode(node).y = y
                        else:
                                g.addNode(node)
                edges = self.edges.keys()
                edges = list(edges)
                for edge in edges:
                        edge1 = self.getEdge(edge)
                        node0 = edge1.n0.id
                        node1 = edge1.n1.id
                        g.addEdge(edge,node0,node1)
                return g

        def show(self,nombre='graph'):
                """
                Guarda al nodo en el archivo graph.gv para leer en Gephi.
                Guarda una imagen del nodo con el archivo graph.png
                Muestra la imagen.
                """
                self.display.render(filename=nombre+'.gv',view=True)
                im = Image.open(nombre+'.gv.png') #cv2.imread('graph.png')
                im.show()
                #cv2.imshow('img',img) # MODIFICAR 
                #cv2.waitKey()

        def Dijkstra(self,s,posiciones=False):
                """
                Implementa el algoritmo de Dijkstra.
                self: Grafo de entrada.
                s:    id del nodo inicial
                posiciones: Marque True si desea que se coloquen los nodos en las mismas posiciones
                            originales
                            Funciona solamente con grid y geographic.
                """
                G = self
                if posiciones:
                        g = Graph(eng='neato')
                else:
                        g = Graph()
                q = PriorityQueue()
                q2 = PriorityQueue()
                q.put((0,s))
                S = []
                nodos = list(G.nodes.keys())
                D = dict()
                Guardar = dict()
                for n in nodos:
                        D[n] = float('inf')
                D[s] = 0
                distancia_total = 0
                c = 0

                while not q.empty():
                        d,u = q.get()
                        if posiciones:
                                x = G.getNode(u).x
                                y = G.getNode(u).y
                                #print(u,x,y)

                        #print(u in S)

                        #S.append(u)


                        if c > 0:
                                if not u in S:
                                        if posiciones:
                                                g.addNode(u + '(' + str(d) + ')',pos=str(x) + ','+ str(y)+'!')
                                        else:
                                                g.addNode(u + '(' + str(d) + ')')
                                d2,u2 = q2.get()
                                d2 = Guardar[u2]
                                if not(u in S and u2 in S):
                                        #print(u2 + '->' + u,S)
                                        g.addEdge(u2 + '->' + u,u + '(' + str(d) + ')',u2 + '(' + str(d2) + ')')
                        else:
                                if posiciones:
                                        g.addNode(u + '(' + str(d) + ')',pos=str(x) + ','+ str(y)+'!',colour='blue')
                                else:
                                        g.addNode(u + '(' + str(d) + ')',colour='blue')

                        c += 1
                        S.append(u)
                        Vecinos = G.getNode(u).neighboors

                        for v in Vecinos:
                                edge = G.edges.get(u + '->' + v)
                                if edge:
                                        d2 = edge.distance
                                else:
                                        edge = G.edges.get(v + '->' + u)
                                        d2 = edge.distance

                                if v not in S:
                                        dv = D[v]
                                        du = D[u]
                                        if dv > du + d2:
                                                dv = du + d2
                                                distancia_total += dv
                                                q.put((dv,v))
                                                q2.put((dv,u))
                                                Guardar[u] = d
                                                D[v] = dv

                return g


        def KruskalD(self):
                """
                Algoritmo de Kruskal Directo
                self: Grafo de entrada (misma clase)
                return: g: Árbol de Expansión Mínima 
                """
                posiciones = False
                distancia = 0
                G = self
                if self.eng == 'neato':
                        posiciones = True
                if posiciones:
                        g = Graph(eng='neato')
                else:
                        g = Graph()

                CC = dict()
                nodos = list(G.nodes.keys())
                for node in nodos:
                        CC[node] = {node}
                        if posiciones:
                                x = G.getNode(node).x
                                y = G.getNode(node).y
                                g.addNode(node,pos=str(x) + ','+ str(y)+'!')
                                g.getNode(node).x = x
                                g.getNode(node).y = y
                        else:
                                g.addNode(node)

                E = self.edges.keys()
                E = list(E)
                #print(E)
                T = G.sortEdgesR(E)
                #print(T)
                for edge in T:
                        edge1 = G.edges.get(edge)
                        u = edge1.n0.id
                        v = edge1.n1.id
                        #print(not u in CC[v] and not v in CC[u],CC[v],CC[u])
                        if not u in CC[v] and not v in CC[u]:
                                #print(u + '->' + v)
                                g.addEdge(u + '->' + v,u,v)
                                U = CC[u].union(CC[v])
                                for w in U:
                                        CC[w] = U
                                d1 = edge1.distance
                                distancia += d1

                print('KruskalD:',distancia)
                return g

        def KruskalI(self):
                """
                Algoritmo de Kruskal Inverso
                self: Grafo de entrada (misma clase)
                return: g: Árbol de Expansión Mínima
                """
                distancia = 0
                G = self
                #if posiciones:
                #        g = Graph(eng='neato')
                #else:
                #        g = Graph()

                g = G.copy()
                E = self.edges.keys()
                E = list(E)
                #print(E)
                T = G.sortEdgesI(E)
                #print(T)
                for edge in T:
                        g2 = g.copy()
                        g2.removeEdge(edge)
                        #print(conectado(g2))
                        if g2.conectado():
                                g = g2.copy()
                        else:
                                edge1 = G.edges.get(edge)
                                d1 = edge1.distance
                                distancia += d1

                print('KruskalI:',distancia)
                return g

        def Prim(self):
                """
                Algoritmo de Prim
                self: Grafo de entrada (misma clase)
                return: g: Árbol de Expansión Mínima
                """
                G = self
                posiciones = False
                if self.eng == 'neato':
                        posiciones = True

                if posiciones:
                        g = Graph(eng='neato')
                else:
                        g = Graph()

                Q = PriorityQueue2()
                Q2= PriorityQueue()
                #q.put((0,s))
                S = []
                nodos = list(G.nodes.keys())
                D = dict()
                #Guardar = dict()
                for n in nodos:
                        D[n] = float('inf')
                        Q.put((float('inf'),n))
                        #Q2.put((float('inf'),n))
                distancia_total = 0
                c = 0
                E = self.edges.keys()
                #print(len(Q))

                while len(Q) > 0:
                        #print(1)
                        d,u = Q.pop()
                        #d2,u2 = Q2.pop()

                        if c > 0:
                                if not u in S:
                                        if posiciones:
                                                x = G.getNode(u).x
                                                y = G.getNode(u).y
                                                g.addNode(u,pos=str(x) + ','+ str(y)+'!')
                                        else:
                                                g.addNode(u)
                                d2,u2 = Q2.get()
                                while abs(d2-d)>0.000001:
                                        d2,u2 = Q2.get()
                                #print(d2,d)
                                #d2 = Guardar[u2]
                                if not(u in S and u2 in S):#not(u in S) and u2 in S:
                                        #print(u2 + '->' + u,S)
                                        g.addEdge(u2 + '->' + u,u,u2)
                        else:
                                #print(d)
                                d = 0
                                if posiciones:
                                        x = G.getNode(u).x
                                        y = G.getNode(u).y
                                        g.addNode(u,pos=str(x) + ','+ str(y)+'!',colour='blue')
                                else:
                                        g.addNode(u,colour='blue')

                        c += 1


                        distancia_total += d
                        S.append(u)
                        V = G.getNode(u).neighboors
                        for v in V:
                                if not v in S:
                                        edge = u + '->' + v
                                        if not edge in E:
                                                edge = v + '->' + u
                                        le = G.edges.get(edge).distance
                                        if le < D[v]:
                                                D[v] = le
                                                Q.update(v,le)
                                                #print(u,le)
                                                Q2.put((le,u))
                                                #Q2.update(u,le)
                                                #Guardar[u] = d

                print('Prim:',distancia_total)
                return g

        def sortEdgesR(self,E):
                """
                Algoritmo de Merge-Sort
                Ordena las aristas utilizando Merge-Sort
                self: Grafo de entrada (misma clase)
                E: conjunto de aristas
                Implementación recursiva
                """
                G = self
                #E = self.edges.keys()
                k = int(len(E)/2)
                if k == 0:
                        return E #[G.edges.get(E[0])]
                E1 = E[0:k]
                E2 = E[k:]
                E1 = G.sortEdgesR(E1)
                E2 = G.sortEdgesR(E2)
                F1 = E1*1
                F2 = E2*1
                R = []
                #print("___________________")
                #print(len(E),len(E1),len(E2))
                elle = min(len(E1),len(E2))
                #i = 0
                while len(E1) > 0 and len(E2) > 0:
                        #print(i,E1,E2)
                        edge1 = E1[0]
                        edge2 = E2[0]
                        edge1A = G.edges.get(edge1)
                        edge2A = G.edges.get(edge2)
                        d1 = edge1A.distance
                        d2 = edge2A.distance
                        if d1 < d2:
                                R.append(edge1)
                                E1.pop(0)
                        else:
                                R.append(edge2)
                                E2.pop(0)


                if len(E2) == 0:
                        R = R + E1

                if len(E1) == 0:
                        R = R + E2


                return R

        def sortEdgesI(self,E):
                """
                Algoritmo de Merge-Sort (Inverso)
                Ordena las aristas
                self: Grafo de entrada (misma clase)
                E: aristas
                Implementación recursiva
                """
                G = self
                #E = self.edges.keys()
                k = int(len(E)/2)
                if k == 0:
                        return E #[G.edges.get(E[0])]
                E1 = E[0:k]
                E2 = E[k:]
                E1 = G.sortEdgesI(E1)
                E2 = G.sortEdgesI(E2)
                F1 = E1*1
                F2 = E2*1
                R = []
                #print("___________________")
                #print(len(E),len(E1),len(E2))
                elle = min(len(E1),len(E2))
                #i = 0
                while len(E1) > 0 and len(E2) > 0:
                        #print(i,E1,E2)
                        edge1 = E1[0]
                        edge2 = E2[0]
                        edge1A = G.edges.get(edge1)
                        edge2A = G.edges.get(edge2)
                        d1 = edge1A.distance
                        d2 = edge2A.distance
                        if d1 > d2:
                                R.append(edge1)
                                E1.pop(0)
                        else:
                                R.append(edge2)
                                E2.pop(0)


                if len(E2) == 0:
                        R = R + E1

                if len(E1) == 0:
                        R = R + E2

                return R

        def conectado(self):#,edge0):
                """
                Algoritmo de conexión utilizando
                Breadth First Search (BFS)
                self: Grafo de entrada
                return: True si el grafo está conectado
                """
                G = self

                L = []
                nodos = list(G.nodes.keys())
                u = nodos[0]
                discovered = dict()
                discovered[u] = True
                for n in nodos:
                        if u != n:
                                discovered[n] = False

                g = Graph()
                g.addNode(u)
                L0 = [u]
                g.addNode(u)
                L.append(L0)
                Li = L0*1
                while len(Li) != 0:
                        Lii = []
                        for u in Li:
                                D = G.getNode(u).neighboors
                                #print(D)
                                for v in D:
                                        if discovered[v] == False:
                                                discovered[v] = True
                                                g.addNode(v)
                                                g.addEdge(u + '->' + v,u,v)
                                                Lii.append(v)
                        L.append(Lii)
                        Li = Lii*1

                for n in nodos:
                        if discovered[n] == False:
                                return False

                return True

        def componenteConectado(self,u):
                """
                Componente conectado basado en el
                Algoritmo Breadth First Search (BFS)
                G: Grafo de entrada
                u: Nodo inicial
                return: lista de nodos en el componente conectado
                """
                G = self
                L = []
                CC = set()
                discovered = dict()
                discovered[u] = True
                nodos = list(G.nodes.keys())
                for n in nodos:
                        if u != n:
                                discovered[n] = False

                #g = Graph()
                #g.addNode(u)
                CC.add(u)
                L0 = [u]
                L.append(L0)
                Li = L0*1
                while len(Li) != 0:
                        Lii = []
                        for u in Li:
                                D = G.getNode(u).neighboors
                                for v in D:
                                        if discovered[v] == False:
                                                discovered[v] = True
                                                #g.addNode(v)
                                                CC.add(v)
                                                #g.addEdge(u + '->' + v,u,v)
                                                Lii.append(v)
                        L.append(Lii)
                        Li = Lii*1

                return CC
