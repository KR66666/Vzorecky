#Přivitani uživatele
print("Vitejte v aplikaci pro výpočet obvod obdelniku")
#Deklarace proměnych 
a = input("zadejte proměnou a: ")
b = input("zadejte proměnou b: ")

#Přetypovani z str na int
a = int(a)
b = int(b)

#Podminka, kontrola zda v proměnych neni zaporne čislo
if a>0 and b>0:
    #Deklarace proměne vysledek
    vysledek = a*b
    #Outpot pro vysledek 
    print("Vysledek je: ", vysledek) 
    #Pokud nebude platit prvni podminka, povede se vždy else
else:
   #Davame uživateli vědět, že něco zadal asi špatně
   print("Tak jsi nadrbaný")