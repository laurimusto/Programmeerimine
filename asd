x = str(raw_input("Sisesta tekst: "))
x11 = "Esimene_ylesanne"
print x11.center(80, "=") 
print x.upper() #Suured t2hed
print x.lower() #V2iksed t2hed
print x.center(80, "=") #keskele
print x.replace(" ", "_") #t2htede vahetus
x1 = "Teine_ylesanne"
print x1.center(80, "=") 
print str(x.upper()) + " " + str(len(x)) + " " + str(x.lower())
x2 = "Kolmas_ylesanne"
print x2.center(80, "=") 
print "Selle rea pikkus on suurem kui 10 t2hem2rki: " + str(len(x)>10)
print "sisaldab tyhikut: " + str(" " in x != True)
print "sisaldab x: " + str("x" in x != True)
print "sisaldab midagi v6i mitte: " + str(x.isalpha())
print "Ainult suured t2hed: " + str(x.isupper())
x3 = "Neljas_ylesanne"
print x3.center(80, "=") 
print "tekst {:}".format("|") + "###" + "{:} tekst2".format("|")


# "The sum of 1 + 2 is {0}".format(1+2)

print str(x.count("x"))
