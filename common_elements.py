"""
File: common_elements.py
------------------------
File to implement a function that is passed two lists and returns a new list
containing those elements that appear in both of the lists passed in.
"""


def common(list1, list2):
    """
    This function is passed two lists and returns a new list containing
    those elements that appear in both of the lists passed in.
    >>> common(['a'], ['a'])
    ['a']
    >>> common(['a', 'b', 'c'], ['x', 'a', 'z', 'c'])
    ['a', 'c']
    >>> common(['a', 'b', 'c'], ['x', 'y', 'z'])
    []
    >>> common(['a', 'a', 'b'], ['a', 'a', 'x'])
    ['a']
    """
    
    """
    You implement this function.  Don't forget to remove the 'pass' statement above.
    """
    return list(set(list1) & set(list2))

def main():
    # Same tests as the doctests above, but can be run from the terminal:
    # Adittional test for repeatative elements, sets don't have repetitive elements
    print(common(['a',], ['a']))                             # should print ['a']
    print(common(['a', 'b', 'c'], ['x', 'a', 'z', 'c']))    # should print ['a', 'c']
    print(common(['a', 'b', 'c'], ['x', 'y', 'z']))         # should print []
    print(common(['a', 'a', 'b'], ['a', 'a', 'x']))         # should print ['a']
    print(common(['a', 'b', 'a', 'b', 'f'],['a','b','b','d'])) #should print ['a', 'b']


if __name__ == '__main__':
    main()
