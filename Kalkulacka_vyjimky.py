import operace
import logging 

logging.basicConfig(filename='Vypocet.log',level=logging.DEBUG)

try:
    logging.info("Načtení prvního čísla")
    a = float(input("Prvni cislo: "))
    logging.info("Načtení druhého čísla")
    b = float(input("Druhe cislo: "))
    logging.info("Operace")
    o = input("Operace (+ , - , * , /): ")
    v = operace.proved_vypocet(a, b, o)
    
    
except ValueError:
    logging.error(f"Chybne zadana cisla")
    print("Chybne zadana cisla")
    
except ZeroDivisionError:
    logging.error(f"Deleni nulou")
    print("Deleni nulou")
    
except ArithmeticError:
    logging.error(f"Neplatna operace")
    print("Neplatna operace")
else:

    print(f"{a} {o} {b} = {v}")
finally:
    print("Konec programu")