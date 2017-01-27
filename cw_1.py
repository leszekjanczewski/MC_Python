import pickle

miejsca = {'Janek': 'Las', 'Ania': 'Pustynia', 'Piotrek':'Jezioro'}

tajnyPlik = open("Plik.txt", "wb")
pickle.dump("tekst", tajnyPlik)
