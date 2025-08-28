"""Graph Visualizer - simple script to display data as a column graph in terminal. Written with the intention to educate. Rewriten in OOP paradigm.
Author: Lukáš Karásek / lukas@lukaskarasek.cz
GitHub: https://github.com/ArseneLuko
"""

class GraphVisualizer:
    char = 'X'

    def __init__(self, data: list, char: str = None):
        self.data = data
        self.matrix = self.__create_matrix__()
        if char is None:
            self.char = GraphVisualizer.char
        else:
            self.char = char

    def __create_matrix__(self):
        all_rows = []
        for row in range(max(self.data), 0, -1):
            temp_row = []
            for step in self.data:
                if step < row:
                    temp_row.append(0)
                elif step >= row:
                    temp_row.append(1)
            all_rows.append(temp_row)
                    
        return all_rows


    def draw_column_graph(self):

        print(f'znak pro vykreslení: {self.char}') # testing line: DELETE

        string_all_rows = []

        for row in self.matrix:
            temp_string_row = ''

            for column in row:
                if column == 0:
                    temp_string_row += '   '
                elif column == 1:
                    temp_string_row += f'  {self.char}'
                
            string_all_rows.append(temp_string_row)

        for row_to_print in string_all_rows:
            print(row_to_print)


# testing line
# all lines below    

testovaci_objekt_bez_znaku = GraphVisualizer([1, 3, 1, 2])
testovaci_objekt_se_znakem = GraphVisualizer([2, 4, 1], 'i')
print(f'data testovacího objektu BEZ znaku:{testovaci_objekt_bez_znaku.data}')
print(f'data testovacího objektu SE znakem:{testovaci_objekt_se_znakem.data}')
print('*')
print('volám metodu \'.draw_column_graph\' 1(BEZ), 2(S)')
testovaci_objekt_bez_znaku.draw_column_graph()
testovaci_objekt_se_znakem.draw_column_graph()
print('*')
print('matrix data pro všechny objekty 1(BEZ), 2(S)')
print(testovaci_objekt_bez_znaku.matrix)
print(testovaci_objekt_se_znakem.matrix)
pass
