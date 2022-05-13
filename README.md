# MST
Árbol de Expansión Mínima

Uso:

Primero generamos un grafo, por ejemplo, con el modelo de Erdös-Renyi:

```python
from erdosRenyi import randomErdosRenyi

g1 = randomErdosRenyi(500,1600)
g1.show(nombre='erdosRenyi500_1600')
```

Para generar el Árbol de Expansión Mínima, podemos utilizar los algoritmos de Kruskal (inverso y directo), así como el algoritmo de Prim:

```python
g2 = g1.KruskalI()
g2.show(nombre='KruskalI_erdosRenyi500_1600')

g3 = g1.KruskalD()
g3.show(nombre='KruskalD_erdosRenyi500_1600')

g4 = g1.Prim()
g4.show(nombre='Prim_erdosRenyi500_1600')
```

Para el caso de los modelos de malla y geográfico simple, las posiciones de los nodos se muestran igual que en los grafos originales. Algunos de los algoritmos para generar el Árbol de Expansión Mínima requieren que el grafo no esté conectado. 
