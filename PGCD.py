def PGCD(Num1,Num2):
    print("PGCD(",Num1,",",Num2,")")
    if Num1 > Num2:
        return PGCD(Num1-Num2,Num2)
    elif Num2 > Num1:
        return PGCD(Num1,Num2-Num1)
    else:
        return Num1    

Num1 = int(input("Entrez le premier numéro :"))
Num2 = int(input("Entrez le deuxième numéro :"))
if Num1 > 0 and Num2 > 0:
    p = PGCD(Num1,Num2)
    print("le PGCD de",Num1,"et",Num2,"est",p)
else:
    print("Les nombres doivent être positifs !")

