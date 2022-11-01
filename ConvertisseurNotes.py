print("Conversion de notes")

convertir = input("Ramerner la note sur combien ? ")
convertir = float(convertir)

initial = input("Le DS est sur combien ? ")
initial = float(initial)

list_notes = []

print("Arretez la saisie en ecrivan 'stop'")

saisie = ""
while saisie != "stop":
    saisie = input("Entrez votre note : ")
    if saisie == 'stop':
        print("Merci, au revoir")
        print(f"Liste des notes sur {convertir} : ")
        for i in list_notes:
            print(i)
    else:
        moyenne = (float(saisie) * convertir) / initial
        note_arrondie = round(moyenne, 2)
        print(note_arrondie)
        list_notes.append(note_arrondie)

moyenne_generale = 0
for note in list_notes:
    moyenne_generale += note
print(f"Moyenne générale de : {moyenne_generale / len(list_notes)}")
