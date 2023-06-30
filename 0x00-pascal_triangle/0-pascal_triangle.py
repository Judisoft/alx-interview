#!/usr/bin/python3

def pascal_triangle(n):
    
    """
    function ns a list of lists of integers representing the Pasial triangle 
    :n: an integer

    """
    triangle = []
    for row_idx in range(n):
        current_row = [None] * (row_idx+1)
        # first and last elements of current row are always 1
        current_row[0], current_row[-1] = 1, 1
        for col_idx in range(1, row_idx):
            above_to_left_elt = triangle[row_idx - 1][col_idx-1]
            above_to_right_elt = triangle[row_idx - 1][col_idx]
            current_row[col_idx] = above_to_left_elt + above_to_right_elt
        triangle.append(current_row)
    return triangle
