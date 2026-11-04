from q4_recursive_match import recursive_match 

def test_recursive_match():
    assert(recursive_match([4, 2, 1, 6], [4, 3, 7, 6]) == 2)
    assert(recursive_match([1, 2, 3, 4], [4, 3, 2, 1]) == 0)
    assert(recursive_match([5, 6, 7, 8, 9, 10], [0, 6, 7, 8]) == 3)
    assert(recursive_match([], [100, 200]) == 0)
    

