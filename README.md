# Graph visualizer
## Co graph-visualizer dělá
Skript znázorní data v termínálu v podobě sloupcového grafu. Vznikl jako cvičení programování v Pythonu.

## Jak se grpah-visualizer používá a co umí
Skript je určen k tomu, aby se importoval do existujícího python skriptu pomocí ```import graph-visualizr``` případně pro následující příklady jako `import graph-visualizer as gv`

Poté můžeme vytvořit objekt typu `graph_visualizer.GraphVisualizer` který přijmá jeden povinný argument typu `list()` například: `objekt = gv.GraphVisualizer([1, 4, 2])`. Data objektu můžeme zobrazit pomocí proměnné objektu `objekt.data` a vykreslit sloupcový graf pomocí volání metody `objekt.draw_column_graph()`

## Příklad s výstupem

```python
import graph-visualizer as gv
numbers = [1, 4, 2, 6, 3]

objekt = gv.GraphVisualizer(numbers, 'I')

objekt.draw_column_graph()
```

výstup:

```
 6 |           I   
 5 |           I   
 4 |     I     I   
 3 |     I     I  I
 2 |     I  I  I  I
 1 |  I  I  I  I  I
   ----------------
      1  2  3  4  5
```