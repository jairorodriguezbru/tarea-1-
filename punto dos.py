def main():

    a = int(input("digite valor de a "))
    b = int(input("digite valor de b "))

    r = funcioncuadratica(a, b)
   
    print(f"el resultado es : r= {r} ")

def funcioncuadratica(a, b):
    d = ((b**2)+(a**2))
   
    r = d**(1/3)


    return r
    

if __name__ == "__main__":
    main()





       
        
