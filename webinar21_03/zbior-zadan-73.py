# 73.3. zbior zadan

with open("tekst.txt", "r") as plik:
	dane = plik.readlines()

	for i in range(len(dane)):
		dane = dane[i].rstrip()

	listaslow = dane.split()

	rekord = 0
	samogloski = ["A", "E", "Y", "O", "U", "I"]
	ciag = 0
	for s in range(len(listaslow)):
		slowo = listaslow[s]
		for l in range(len(slowo)):
			if slowo[l] not in samogloski:
				ciag += 1
			else:
				if ciag > rekord:
					rekord = ciag
				ciag = 0
	print(rekord)