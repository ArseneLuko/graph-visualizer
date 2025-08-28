"""Graph Visualizer - simple script to display data as a column graph in terminal. Written with the intention to educate. Rewriten in OOP paradigm.
Author: Lukáš Karásek / lukas@lukaskarasek.cz
GitHub: https://github.com/ArseneLuko
"""

class GraphVisualizer:
    char = 'X'

    def __init__(self, data: list, char: str = None):
        self.data = data
        self.matrix = self.__create_matrix()
        if char is None:
            self.char = GraphVisualizer.char
        else:
            self.char = char


    def __create_matrix(self):
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
    

    def __add_legend(self, string_data: list[str]):
        """Add column (value) and row (steps) to string data representing graph.
        
        Args:
            string_data (list[str]): list of strings representing column graph

        Returns:
            list[str]: list of strings with legend (columns = value / row = steps)
        """

        # columns - values

        row_labels = [n + 1 for n in range(len(string_data))]

        for position, row in enumerate(string_data):
            string_data[position] = str(row_labels.pop()).rjust(2) + ' |' + row

        # rows - steps

        steps = (len(string_data[0]) - 4) // 3 # number of steps is lenght of one row minus 4 (legend for values) diveded by 3 (number of characters to show column)

        _1st_lowest_row = f'   -{3 * steps * '-'}'
        _2nd_lowest_row = '    '
        for number in range(1, steps + 1):
            _2nd_lowest_row += str(number).rjust(3)
        string_data.append(_1st_lowest_row)
        string_data.append(_2nd_lowest_row)

        return string_data
        


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

        string_all_rows = self.__add_legend(string_all_rows)
        
        for row_to_print in string_all_rows:
            print(row_to_print)

