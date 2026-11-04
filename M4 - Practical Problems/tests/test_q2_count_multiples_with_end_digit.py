from q2_count_multiples_with_end_digit import count_multiples_with_end_digit 

def test_count_multiples_with_end_digit():
    assert(count_multiples_with_end_digit(6, 2) == 6)
    assert(count_multiples_with_end_digit(5, 0) == 4)
    assert(count_multiples_with_end_digit(7, 7) == 2)
    
