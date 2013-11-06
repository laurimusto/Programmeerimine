nimi = raw_input("Sisesta oma t2isnimi: ")
name = nimi.capitalize()
amet = raw_input("Sisesta oma amet: ")
email = raw_input("Sisesta oma email: ")
tel = raw_input("Sisesta oma telefoni number: ")
tekst = "Visiitkaart"
tyhi = ""
print "|", tekst.center(80, "="), '|' #tyhi rida
print "|", tyhi.center(80, " "), '|'
print "|", nimi.center(80), "|"
print "|", amet.center(80), "|"    
print "|", email.center(80), "|"
print "|", tel.center(80), "|"
print "|", tyhi.center(80, " "), '|'#tyhi rida
print "|", tyhi.center(80, "="), '| \n'
