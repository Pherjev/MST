from graph import Graph
from erdosRenyi import randomErdosRenyi
from gilbert import randomGilbert
from geographic import randomGeographic
from barabasiAlbert import randomBarabasiAlbert
from grid import grid
from dorogovtsevMendes import dorogovtsevMendes
from queue import PriorityQueue


#g1 = randomErdosRenyi(30,70)
#g1.show(nombre='erdosRenyi30_70')

#g1 = randomGilbert(500,0.02)
#g1.show(nombre='gilbert500_002')

#g1 = randomGeographic(30,2)
#g1.show(nombre='geographic_30_2')

#g1 = randomBarabasiAlbert(500,4)
#g1.show(nombre='barabasiAlbert_500_4')

#g1 = grid(5,6)
#g1.show(nombre='grid5_6')

g1 = dorogovtsevMendes(30)
g1.show(nombre='dorogovtsevMendes30')

g2 = g1.KruskalI()
g2.show(nombre='KruskalI_dorogovtsevMendes30')

g3 = g1.KruskalD()
g3.show(nombre='KruskalD_dorogovtsevMendes30')

g4 = g1.Prim()
g4.show(nombre='Prim_dorogovtsevMendes30')
