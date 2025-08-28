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
        """Create a matrix presenting columns with 1 (column) or 0 (empty) based on numerical list.
        Args:
            self.data (list): list of numerical values
        Returns:
            list: List of lists represinting columns
        """
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
        """The method takes a matrix representing a column graph and displays it on the screen. Columns are drawn using 3 characters, of which first two are spaces.

        Args:
            self.metrix (list[list]): matrix data contains list of rows with 1 (column) or 0 (empty space)
            self.char (str): the character used to represent the graph, must have lenght of 1
        Returns:
            None: print results directly on the screen."""
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

