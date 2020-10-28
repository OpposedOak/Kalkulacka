import operace

def test_soucet():
    assert operace.soucet(1,2) == 3
    
def test_rozdil():
    assert operace.rozdil(1,2) == -1
    
def test_soucin():
    assert operace.soucin(3,3) == 9
    
def test_podil():
    assert operace.podil(9,3) == 3

def test_proved_vypocet():
    
    assert operace.proved_vypocet(2,2,"+") == 4
    assert operace.proved_vypocet(2,2,"-") == 0
    assert operace.proved_vypocet(2,2,"*") == 4
    assert operace.proved_vypocet(2,2,"/") == 1
    
