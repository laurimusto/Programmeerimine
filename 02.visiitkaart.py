nimi = raw_input("Sisesta oma t2isnimi: ")
name = nimi.capitalize()
amet = raw_input("Sisesta oma amet: ")
email = raw_input("Sisesta oma email: ")
tel = raw_input("Sisesta oma telefoni number: ")
tekst = "Visiitkaart"
tyhi = ""
print "|", tekst.center(70, "="), '|' #tyhi rida
print "|", tyhi.center(70, " "), '|'
print "|", nimi.center(70), "|"
print "|", amet.center(70), "|"    
print "|", email.center(70), "|"
print "|", tel.center(70), "|"
print "|", tyhi.center(70, " "), '|'#tyhi rida
print "|", tyhi.center(70, "="), '| \n'
