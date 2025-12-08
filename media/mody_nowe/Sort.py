# Pliki wejściowe
plik1 = "S2.txt"
plik2 = "S21.txt"

# Plik wynikowy
wynik = "Wynik.txt"

# Wczytaj linie jako zbiory (bez znaków końca linii)
with open(plik1, "r", encoding="utf-8") as f1:
    linie1 = set(l.strip() for l in f1)

with open(plik2, "r", encoding="utf-8") as f2:
    linie2 = set(l.strip() for l in f2)

# Znajdź linie nie-wspólne
roznice = linie1.symmetric_difference(linie2)

# Zapisz do pliku wynikowego
with open(wynik, "w", encoding="utf-8") as out:
    for linia in sorted(roznice):
        out.write(linia + "\n")

print("Gotowe! Wynik zapisany w pliku:", wynik)
