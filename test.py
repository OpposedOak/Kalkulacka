import operace

def test_soucet():
    assert operace.soucet(1,2) == 3
    
def test_rozdil():
    assert operace.rozdil(1,2) == -1
    
def test_soucin():
    assert operace.soucin(3,3) == 9
    
def test_podil():
    assert operace.podil(9,3) == 3

def test_deleni_nulou():
    with pytest.raises(ZeroDivisionError):
        operace.podil(1,0)
