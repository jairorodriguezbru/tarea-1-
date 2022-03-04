
def main():
    a = int(input("digite valor a "))
    b = int(input("digite valor b "))
    c = int(input("digite valor c "))
    x1 = funcioncuadratica(a, b, c)
    x2 = funcioncuadratica(a, b, c)
    print(f"Los valores de la funcion cuadratica son: x1= {x1} y x2= {x2}")

def funcioncuadratica(a, b, c):
    d = ((b**2)-(4*a*c))
    if d<0 :
        print("La funcion cuadratica no se puede resolver dado que la raiz es negativa")
    if d >= 0 :
        r = d**(1/2)
        x1 = (((b*-1)+r)/(2*a))
        x2 = (((b*-1)-r)/(2*a))
        return x1, x2

if __name__ == "__main__":
    main()