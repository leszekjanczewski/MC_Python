def krotkaPobierzDate(lancuchZdata):
	rok = int(lancuchZdata [0:4])
	miesiac = int(lancuchZdata [5:7])
	dzien = int(lancuchZdata [8:10])
	return rok, miesiac, dzien

print(krotkaPobierzDate("2017-01-13"))

#wstawienie do zmiennych
rok, miesiac, dzien	= krotkaPobierzDate("2017-01-13")
print(rok)