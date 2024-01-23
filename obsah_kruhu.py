#Deklarace proměnou 
r = input("zadejte proměnou r: ")

#Přetypovani z str na int
r = int(r)

#Podminkova kontrola
if r>0 :
    #Deklarace proměne, vysledek 
    vysledek = 3.14*(r^2)
    #Outpot pro vysledek 
    print("Vysledek je: ", vysledek)   
else:
   #Davame uživateli vědět, že něco zadal asi špatně
   print("Tak jsi nadrbaný") 