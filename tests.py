

import graph_visualizer as gv

testovaci_objekt_bez_znaku = gv.GraphVisualizer([1, 3, 1, 2])
testovaci_objekt_se_znakem = gv.GraphVisualizer([2, 4, 1], 'I')
testovaci_objekt_s_neplatnym_znakem = gv.GraphVisualizer([11, 7], '|') # měl by se vypsat s X
print(f'data testovacího objektu BEZ znaku:{testovaci_objekt_bez_znaku.data}')
print(f'data testovacího objektu SE znakem:{testovaci_objekt_se_znakem.data}')
print('*')
print('volám metodu \'.draw_column_graph\' 1(BEZ), 2(S)')
testovaci_objekt_bez_znaku.draw_column_graph()
testovaci_objekt_se_znakem.draw_column_graph()
testovaci_objekt_s_neplatnym_znakem.draw_column_graph()
print('*')
print('matrix data pro všechny objekty 1(BEZ), 2(S)')
print(testovaci_objekt_bez_znaku.matrix)
print(testovaci_objekt_se_znakem.matrix)
pass