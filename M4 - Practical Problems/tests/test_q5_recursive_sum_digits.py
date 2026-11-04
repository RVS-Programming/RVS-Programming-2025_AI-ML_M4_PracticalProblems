from q5_recursive_sum_digits import recursive_sum_digits 

def test_recursive_sum_digits():
    assert(recursive_sum_digits(5) == 5)
    assert(recursive_sum_digits(31) == 4)
    assert(recursive_sum_digits(123) == 6)
    assert(recursive_sum_digits(0) == 0)
    assert(recursive_sum_digits(-524) == 11)
    assert(recursive_sum_digits(719340) == 24)
    
