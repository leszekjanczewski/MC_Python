import pickle

tajnyPlik = open("tajnyPlik.txt", "rb")
miejsca = pickle.load(tajnyPlik)

print(miejsca['Janek'])
