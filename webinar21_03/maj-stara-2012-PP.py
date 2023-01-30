with open("cyfry.txt", "r") as plik:
	dane = plik.readlines()

	for i in range(len(dane)):
		dane = dane[i].rstrip()

	for liczba in dane:
		for i in range(len(liczba)):
			if liczba[i] >= liczba[i + 1]:
				czyRosnacy = False
			if czyRosnacy == True:
				print(liczba, end=" ")