from q6_recursive_mirror import recursive_mirror 

def test_recursive_mirror():
    assert(recursive_mirror("hello") == "helloolleh")
    assert(recursive_mirror("wow") == "wowwow")
    assert(recursive_mirror("code") == "codeedoc")
    assert(recursive_mirror("recursion") == "recursionnoisrucer")
    assert(recursive_mirror("") == "")
    
