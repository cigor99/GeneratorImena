import random


def generisi_latinicna_imena(broj):
    fajl_imena = open("../data/IMENA_CIRILICA.txt", 'r', encoding="utf-8")
    imena = []
    ime = fajl_imena.readline()
    while ime != "":
        imena.append(ime.rstrip("\n"))
        ime = fajl_imena.readline()
    fajl_imena.close()

    fajl_prezimena = open("../data/PREZIMENA_CIRILICA.txt", 'r', encoding="utf-8")
    prezimena = []
    prezime = fajl_prezimena.readline()
    while prezime != "":
        prezimena.append(prezime.rstrip("\n"))
        prezime = fajl_prezimena.readline()
    fajl_prezimena.close()

    osobe = ""

    for i in range(broj):
        index_imena = random.randint(0, len(imena)-1)
        index_prezimena = random.randint(0, len(prezimena)-1)
        osobe += imena[index_imena] + " " + prezimena[index_prezimena] + "\n"

    izlazni_fajl = open("../data/OUTPUT.TXT", 'w', encoding="utf-8")
    izlazni_fajl.write(osobe)
    izlazni_fajl.close()
