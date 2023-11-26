from RechercheFichier import *
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
    for file in list_of_files(directory, ".txt"):       #Pour chaque fichier dans le repertoire donné:
        number_of_files += 1                            #Le nbr de fichier qu'on a regadé +=1
        with open(directory + "/" + file, "r") as f:    #On ouvre le fichier pour le lire

            dico_mot_fichier = tf(f.read())             #On recup le tf du fichier voulu, que l'on utilise comme une liste de tt le mot du fichier
            mot_dans_dico = []

            for mot in dico_mot_fichier.keys():         #Pour chaque mot dans le fichier:
                if mot not in mot_dans_dico:            #Si le mot n'est pas déjà dans la liste des mot mis dans le dico (Si c'est la 1ere fois du fichier qu'on tombe sur ce mot)
                    mot_dans_dico.append(mot)           #On ajout le mot dans la liste (Liste qui sera vidé pour le prochain fichier)
                    
                    #c'est donc la seul fois du fichier qu'on traitera ces mots
                    if mot in liste_des_mots.keys():    #Si le mot est dejà dans la liste des mots
                        liste_des_mots[mot] += 1        #On ajoute 1 à son occurence

                    else:                               #Sinon
                        liste_des_mots[mot] = 1         #On associe sa valeur à 1

    for val in liste_des_mots:                          #Pour chaque valeur dans la liste des mots:
        liste_des_mots[val] = math.log(1 / (liste_des_mots[val] / number_of_files)) #On remplace sa valeur par de log de l'inverse de sa proportion (C'est là qu'on utilise  le comptage de doculments fait plus haut)

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
#write_tf_idf()
