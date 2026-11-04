from q1_get_alpha_string import get_alpha_string 

def test_get_alpha_string():
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

