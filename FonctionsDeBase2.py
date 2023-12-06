def tokenisation(text):
    text = minimize_text(text) + " "
    l = -1
    liste_e = ["é","è","ê","ë"]
    liste_a = ["à","â"]
    chaine_SansCaraSpe = ""
    for i in range(len(text)):
        if "a" <= text[i] <= "z":
            chaine_SansCaraSpe += text[i]
        else:
            if text[i] == "'":
                chaine_SansCaraSpe += apostrophe(text[i-1], l)
                l *= -1
            elif text[i] in liste_e:
                chaine_SansCaraSpe += "e"

            elif text[i] in liste_a:
                chaine_SansCaraSpe += "a"

            elif text[i] == "ù":
                chaine_SansCaraSpe += "u"

            elif text[i] == "ç":
                chaine_SansCaraSpe += "c"

            elif text[i] == "ô":
                chaine_SansCaraSpe += "o"

            else:
                 chaine_SansCaraSpe += " "
    chaine_SansCaraSpe2 = ""
    for i in range(len(chaine_SansCaraSpe)-1):
        if chaine_SansCaraSpe[i + 1] == " " and chaine_SansCaraSpe[i] == " ":
            chaine_SansCaraSpe2 += ""
        else:
            chaine_SansCaraSpe2 += chaine_SansCaraSpe[i]
    return chaine_SansCaraSpe2.split(" ")
