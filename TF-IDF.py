def tf(text):
    words = text.split(" ")
    tf_dico = {}
    for word in words:
        if word in tf_dico.keys():
            tf_dico[word] += 1
        else:
            tf_dico[word] = 1
    return tf_dico

def idf(directory="./cleaned"):
    liste_des_mots = {}
    number_of_files = 0
    for file in list_of_files(directory, ".txt"):
        number_of_files += 1
        with open(directory + "/" + file, "r") as f:

            dico_mot_fichier = tf(f.read())
            mot_dans_dico = []

            for mot in dico_mot_fichier.keys():
                if mot not in mot_dans_dico:
                    mot_dans_dico.append(mot)

                    if mot in liste_des_mots.keys():
                        liste_des_mots[mot] += 1

                    else:
                        liste_des_mots[mot] = 1

    for val in liste_des_mots:
        liste_des_mots[val] = math.log(1 / (liste_des_mots[val] / number_of_files))

    return liste_des_mots
