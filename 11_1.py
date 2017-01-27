plikListyZadan = open("ListaZadan.txt", "w")

listaZadan = ""

zadanieZlisty = input("Wpisz element listy zadan: ")

while zadanieZlisty != "exit":
    listaZadan = listaZadan + zadanieZlisty + " \n"
    zadanieZlisty = input("Wpisz element listy zadan: ")

plikListyZadan.write(listaZadan)
plikListyZadan.close()
