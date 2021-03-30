pSeuil = 2.3 
vSeuil = 7.41

v =float(input("Entrer la volume :"))
p =float(input("Entrer la pression :"))

if v > vSeuil and p > pSeuil :
    print("arrêt immédiat")
elif v < vSeuil and p > pSeuil :
    print("augmenter le volume de l’enceinte")
elif v > vSeuil and p < pSeuil :
    print("diminuer le volume de l’enceinte")
else :
    print("Todou bem ! Bizou dou brazil :)")
