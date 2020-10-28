def soucet (a,b):
    return a+b

def rozdil (a,b):
    return a-b

def soucin (a,b):
    return a*b

def podil (a,b):
    return a/b

def proved_vypocet(a,b,o):
   
    if o == "+":
        return soucet(a,b)

    elif o == "-":
        return rozdil(a,b)
            
    elif o == "*":
        return soucin(a,b)

    else:
        return podil(a,b)




