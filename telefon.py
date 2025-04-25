class Telefon:
    def __init__(self, modell, gyarto, ar, ev, _5g):
        self.modell = modell
        self.gyarto = gyarto
        self.eladasi_ar = int(ar)
        self.kiadas_eve = int(ev)
        self._5g_kepes = _5g.lower() == "igen"

    def regi_vagy_ujabb(self):
        return "regi" if self.kiadas_eve <= 2021 else "ujabb"

    def __str__(self):
        return f"{self.gyarto} {self.modell} ({self.eladasi_ar} Ft)"


# 1. Beolvasás
telefonok = []
with open("telefonok-adatok.txt", encoding="utf-8") as f:
    f.readline()
    for sor in f:
        adatok = sor.strip().split(";")
        telefon = Telefon(*adatok)
        telefonok.append(telefon)

# 2. Átlagár
atlag = sum(t.eladasi_ar for t in telefonok) // len(telefonok)
print(f"A telefonok átlagára: {atlag} Ft")

# 3. Legdrágább telefon
legdragabb = max(telefonok, key=lambda t: t.eladasi_ar)
print(f"A legdrágább telefon gyártója: {legdragabb.gyarto}, neve: {legdragabb.modell}, ára: {legdragabb.eladasi_ar} Ft")

# 4. 5G-képes telefon keresése adott gyártótól
gyarto = input("Írd be a gyártó nevét: ").strip().lower()
van = any(t.gyarto.lower() == gyarto and t._5g_kepes for t in telefonok)

if van:
    print("Van 5G-képes telefon ettől a gyártótól.")
else:
    print("Nincs ilyen telefon.")

# 5. Apple export fájlba
with open("apple-export.txt", "w", encoding="utf-8") as f:
    for t in telefonok:
        if t.gyarto.lower() == "apple":
            f.write(f"{t.modell} {t.regi_vagy_ujabb()}\n")
