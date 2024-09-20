def generate(chaine):
    mots = []
    separateurs = []
    mot_actuel = ""
    separateur_actuel = ""

    for caractere in chaine:
        if caractere.isalnum() or caractere == "'":
            if separateur_actuel:
                separateurs.append(separateur_actuel)
                separateur_actuel = ""
            mot_actuel += caractere
        else:
            if mot_actuel:
                mots.append(mot_actuel)
                mot_actuel = ""
            separateur_actuel += caractere

    if mot_actuel:
        mots.append(mot_actuel)
    if separateur_actuel:
        separateurs.append(separateur_actuel)

    if len(separateurs) < len(mots) - 1:
        separateurs.append("")

    return [mots, separateurs]

print(generate("J'ai découvert Python cette semaine"))
print(generate("J'ai découvert Python, cette semaine"))
print(generate("J'ai découvert, Python, cette semaine"))
            

        