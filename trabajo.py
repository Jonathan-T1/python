'''el=int(input("Elija segun 1 corriente precio  2. Disel"))
if el == 1: 
    valortanquear=int(input("ingrese cuanto desea tanquear "))
    galon = 10800
    tl = valortanquear / galon
    print("usted a tanqueado ",tl,"Galones")
elif el == 2:
    valortanquear2=int(input("ingrese cuanto desea tanquear "))
    galon2 = 9800
    tl2 = valortanquear2 / galon2
    print("usted a tanqueado ",tl2,"Galones")
else:
    print("Opcion no valida")'''
tarjeta = 2000
Mensaje2 = " ****** De que me hablas Viejo ******"
Mensaje1 = " Porfavor ponga su tarjeta "
print(Mensaje1.upper())

print("****Su tarjeta tiene***",tarjeta)
election=int(input(" Desea Recargar para continuar 1.para si 2.para no "))

personalizada=int(input("su TARJETA es personalizada o es corriente 1.personalizada 2.corriente "))

if election == 1 and personalizada == 1:
    recarga=int(input("cuanto desea recargar sabiendo su saldo es 2000 "))
    saldonuevo = recarga + tarjeta 
    print("su saldo de SITP es de ",saldonuevo)
    if saldonuevo < 2500:
         print("Debe recargar su tarjeta ")
    elif saldonuevo >= 2500:
            print("Transferencia realizada")
            newbalance = saldonuevo - 2500           
            print("Su nuevo saldo es de ",newbalance)
elif election == 1 and personalizada == 2:
    recarga=int(input("cuanto desea recargar sabiendo su saldo es 2000 "))
    saldonuevo = recarga + tarjeta 
    print("su saldo de SITP es de ",saldonuevo)
    if saldonuevo < 3000:
         print("Debe recargar su tarjeta ")
    elif saldonuevo >= 3000:
            print("Transferencia realizada") 
            newbalance = saldonuevo - 3000           
            print("Su nuevo saldo es de ",newbalance)
elif election == 2:
      print("No se puede subir Vayase o Colese")
else :
      print(Mensaje2.upper())