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
    
def tfidf(directory="./cleaned"):
    liste_des_mots = idf(directory)
    matrice_tf_idf = []
    id = 0
    for mot in liste_des_mots:
        matrice_tf_idf.append([])
        for file in list_of_files(directory, ".txt"):
            with open(directory + "/" + file, "r") as f:
                dico_mot_fichier = tf(f.read())
            if mot in dico_mot_fichier:
                matrice_tf_idf[id].append(dico_mot_fichier[mot] * liste_des_mots[mot])
            else:
                matrice_tf_idf[id].append(0.0)
        id += 1
    return matrice_tf_idf

def write_tf_idf():
    with open("TF-IDF_matrice.txt", "w") as f:
        id = 0
        dico_key = list(idf().keys())
        for l in tfidf():
            f.write(str(dico_key[id]) + " " + str(l) + "\n")
            id += 1
write_tf_idf()
