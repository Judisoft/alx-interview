#!/usr/bin/python3

"""
pascal triangle
"""

def pascal_triangle(n):
    
    """
    function that displays a list of integers representing the Pasial triangle 
    :n: an integer
    :return: a list if integers

    """
    pascal_list = []
    if n <= 0:
        return pascal_list
    for i in range(n):
        row = [1]
        if pascal_list:
            last_row = pascal_list[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        pascal_list.append(row)
    return (pascal_list)

