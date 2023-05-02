def citire(file):
    dictionar = {}
    with open(file, "r") as f:
        for line in f:
            productie = line.strip().split("->")
            neterminale = productie[0].strip()
            dictionar[neterminale] = []
            tranzitii = productie[1].strip().split("|")
            for tranzitie in tranzitii:
                dictionar[neterminale].extend(tranzitie.split())

    return dictionar
global dictionar
dictionar = citire("gramatica.txt".strip()) # dictionar de liste cu cheie multimea neterminale, iar listele contin toate productiile starii
starecurenta='S'
def VerificareCuvant(starecurenta,cuvant):
    if not cuvant:
        if cuvant == "":
            if 'lambda' in dictionar[starecurenta]:
                return True
            else:
                return False
        else:
            return False
    if len(cuvant) == 1:
        ulit = cuvant[0]
        for tranzitie in dictionar[starecurenta]:
            if len(tranzitie) == 1 and tranzitie[0] == ulit:
                return True

    for tranzitie in dictionar[starecurenta]: #verificam daca se poate produce recursiv cuvantul
        if len(tranzitie) > 1 and tranzitie[0] == cuvant[0]:
            if VerificareCuvant(tranzitie[1],cuvant[1:]):
                return True

    return False

with open("cuvinte.txt", "r") as f:
    for linie in f:
        cuvant = linie.strip()
        if VerificareCuvant(starecurenta,cuvant)==True:
            print(f"Cuvântul '{cuvant}' este acceptat.")
        else:
            print(f"Cuvântul '{cuvant}' nu este acceptat.")
