"""Graph Visualizer - simple script to display data as a column graph in terminal. Written with the intention to educate.
Author: Lukáš Karásek / lukas@lukaskarasek.cz
GitHub: https://github.com/ArseneLuko
"""

def create_matrix(data: list) -> list[list]:
    """Create a matrix presenting columns based on numerical list.
    Args:
        data (list): list of numerical values
    Returns:
        list: List of lists represinting columns
    """
    all_rows = []
    for row in range(max(data), 0, -1):
        temp_row = []
        for step in data:
            if step < row:
                temp_row.append(0)
            elif step >= row:
                temp_row.append(1)
        all_rows.append(temp_row)
    
    return all_rows


def draw_columns(data: list, char: str=' Ii') -> None:
    """The function takes a matrix representing a column graph as input and displays it on the screen.
    Args:
        data (list): matrix data contains list of rows with 1 (column) or 0 (empty space)
        char (str): the character used to represent the graph, must have lenght of 3
    Returns:
        No returns, print results on the screen."""
    
    string_all_rows = []

    for row in data:
        string_row = ''

        for column in row:
            if column == 0:
                string_row += '   '
            elif column == 1:
                string_row += char
                
        string_all_rows.append(string_row)

    for row_to_print in string_all_rows:
        print(row_to_print)


def main():
    matrix = create_matrix([4, 4, 2, 8, 4, 2, 1])
    draw_columns(matrix, 'd')

if __name__ == '__main__':
    main()