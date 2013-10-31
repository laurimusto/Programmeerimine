print "-Tere tulemast (Algis sai 2 h22lt)"
ees = raw_input("Sisesta oma eesnimi: ")
pere = raw_input("Sisesta oma perenimi: ")
vanus = raw_input("Sisesta oma vanus: ")
elukoht = raw_input("Sisesta oma elukoht: ")
rass = raw_input("Sisesta oma rass: ")
if vanus >= "17":
	print "-Teie nimi on " + ees.capitalize() + " " + pere.capitalize() + ". Te olete " + vanus + " aastat vana ja te elate " + elukoht.capitalize() + ". te olete " + rass + "st rassist"
else:
	print "-Teie nimi on " + ees.capitalize() + " " + pere.capitalize() + ". Te olete " + vanus.count() + " aastat vana, olete alaealine ning te elate " + elukoht.capitalize() + "as" + ". + te olete " + rass + "st rassist"
info = raw_input("Kas kinnitate andmete t2psust? ")
if info == "jah":
	print "-Andmed saadetud FBI'le!"
else:
	maja = raw_input("Kas v6tame maja ja auto k2est?? ")
	if maja != "jah":
		print "-Olge valmis, kohe oleme kohal!"
	else:
		print "-No kui te nii lahke olete, siis v6tame juba terve maa ka 2ra!"
		lehm = raw_input("Tahate seda? ")
		if lehm == "jah":
			print "-Davai, kohe oleme kohal"
		else:
			print "-Kes sulle putru pakkus?"
