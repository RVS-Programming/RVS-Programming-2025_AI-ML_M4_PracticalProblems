""" Question 1: get_alpha_string """
"""
Input: 2D list
Output: string of all the letters in the list, reading left to right, top to bottom
"""
def get_alpha_string(lst):
    string = ""
    for row in lst:
        for char in row:
            if char.isalpha():
                string += char
    return string

""" Test 1 """
def test_get_alpha_string():
    print("Testing get_alpha_string...", end="")
    lst1 = [ ['0', '1', 'a'],
             ['2', 'c', 'e'],                 
             ['3', '4', '5'] ]
    assert(get_alpha_string(lst1) == "ace")
    lst2 = [ [ '0',  '1'],
             ['!?', '45'] ]
    assert(get_alpha_string(lst2) == "")
    lst3 = [ [ 'a', 'l', 'p', 'h' ],
             [ 'a', 'b', 'e', 't' ] ]
    assert(get_alpha_string(lst3) == "alphabet")
    print("... done!")
                                             
if __name__ == '__main__':
    test_get_alpha_string()                                                                                                                  