
telefonok = []

with open("telefonok-adatok.txt") as f:
    f.readline()
    for sor in f:
        adatok=sor.strip().split(';')
        telefon = {
            "modell": adatok[0],
            "gyarto": adatok[1],
            "eladasi ar": int(adatok[2]),
            "kiadas eve": int(adatok[3]),
            "5g kepes": adatok[4],
        }
        telefonok.append(telefon)

sum = sum(t["eladasi ar"] for t in telefonok)
#for t in telefonok:
    #sum+=t["eladasi ar"]
print("A telefonok átlagára: " + str(int(sum/len(telefonok))) + " FT")


max_ar = max(t["eladasi ar"] for t in telefonok)
max_telefon = None
max_telefon = max(telefonok, key= lambda t: t["eladasi ar"])
#for t in telefonok:
 #   if t["eladasi ar"]==max_ar:
  #      max_telefon=t
print ("a legdrágább telefon gyártoja " + max_telefon["gyarto"] + 
" neve: " + max_telefon["modell"] + " ára: " + str(max_telefon["eladasi ar"]))


telefon_gyarto = input("ird be a gyártó nevét: ")
telefon = None
for t in telefonok:
    if t["gyarto"].lower() == telefon_gyarto.lower().strip():
        if t["5g kepes"] == "igen":
            telefon = t
if telefon:
    print("igen van " + str(telefon))
else:
    print("nincs ilyen telefon")

telefon = None
any(t["gyarto"]==telefon_gyarto and t["gyarto"] for t in telefonok)

def regi(t):
    if t<=2021:
        return "regi"
    else:
        return "ujabb"

with open("apple-export.txt", "w", encoding="utf-8") as f:
    for t in telefonok:
        if t["gyarto"].lower() == "apple":
            f.write(t["modell"] + " " + regi(t["kiadas eve"]) + "\n")