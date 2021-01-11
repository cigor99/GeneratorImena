import generisi_latinica
import generisi_cirilica

if __name__ == '__main__':
    while True:
        print()
        print("1 - Latinica")
        print("2 - Ћирилица")
        print("X - Kraj")
        print()
        unos_slova = input(">>")
        if unos_slova == "1":
            while True:
                print("Unesite koliko želite imena")
                unos_kolicine = input(">>")
                try:
                    broj = int(unos_kolicine)
                    generisi_latinica.generisi_latinicna_imena(broj)
                    break
                except ValueError:
                    print("Neispravan unos")

        elif unos_slova == "2":
            while True:
                print("Унесите колико желите имена")
                unos_kolicine = input(">>")
                try:
                    broj = int(unos_kolicine)
                    generisi_cirilica.generisi_latinicna_imena(broj)
                    break
                except ValueError:
                    print("Неисправан унос")
        elif unos_slova.lower() == "x":
            break
        else:
            print("Neispravan unos")
