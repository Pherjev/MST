# MST
Árbol de Expansión Mínima

Uso:

Primero generamos un grafo, por ejemplo, con el modelo de Erdös-Renyi:

```python
from erdosRenyi import randomErdosRenyi

g1 = randomErdosRenyi(500,700)
g1.show(nombre='erdosRenyi500_700')
```

Para generar el árbol de Dijkstra utilizamos la siguiente línea:

```python
g2 = g1.Dijkstra('1')
g2.show(nombre='Dijkstra_erdosRenyi500_700')
```

Para el caso de los modelos de malla y geográfico simple, recomendamos utilizar el parámetro posiciones = True (nota: en los otros no funcionará):

```python
from geographic import randomGeographic

g1 = randomGeographic(20,1.6)
g1.show(nombre='geographic_20_1_6')
g2 = g1.Dijkstra('1',posiciones=True)
g2.show(nombre='Dijkstra_geographic_20_1_6')
```
