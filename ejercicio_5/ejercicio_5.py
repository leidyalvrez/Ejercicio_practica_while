# capital inicial 
c1 = float(input("capital de pedro"))
c2 = float(input("capital de juan "))
c3 = float(input("capital necesaria para el negocio"))

meses = 0 

while (c1 + c2) < c3:
    c1 = c1 * 1.03
    c2 = c2 * 1.04 
    meses += 1 

    print("podran hacer el negocio en", meses, "meses")
    print("capital final de pedro", round(c1,2))
    print("capital final de juan", round(c2,2))
    print("capital total", round(c1+c2,2))