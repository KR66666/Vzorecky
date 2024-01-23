#Přivitani uživatele
print("Vitejte v aplikaci pro výpočet obvod obdelniku")

#Deklarace (spiše inicializace) proměnych,nasledně do nich ukladame vstup 
a = input("Zadejte proměnou a: ")
b = input("Zadejte proměnou b: ")

#Přetypovani z str na int
a = int(a)
b = int(b)

#Podminka, kontrola zda v proměnych neni zaporne čislo
if a>0 and b>0:
   #Deklarace proměne vysledek
   vysledek = 2*a+2*b
   #Outpot pro vysledek 
   print("Vysledek je: ", vysledek)
#Pokud nebude platit prvni podminka, povede se vždy else
else:
   #Davame uživateli vědět, že něco zadal asi špatně
   print("Tak jsi nadrbaný")