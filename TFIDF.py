from RechercheFichier import *
def tf(text):
    """
    Renvoie un disctionnaire du nombre de chaque mot dans une chaine de caractères fournies
    """
    words = text.split(" ")        #On transforme la chaine de caractères en liste séparé par les espaces
    tf_dico = {}                   #On initialise le dico
    for word in words:             #Pour chaque mot dans la liste des mots:
        if word in tf_dico.keys(): #Si le mot est dejà dans le dico
            tf_dico[word] += 1     #On ajoute 1 à la valeur associé au mot
        else:                      #SINON
            tf_dico[word] = 1      #On initialise la valeur du dico pour le mot à 1
    return tf_dico

def idf(directory="./cleaned"):
    """
    Renvoie l'idf de chaque mot du corpus de texte sous forme d'une liste
    """
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
    """
    On renvoie la matrice TF-IDF du corpus de texte sous forme d'une matrice 2D
    """
    liste_des_mots = idf(directory) #La liste des mots prends l'idf du repertoire
    matrice_tf_idf = []
    id = 0
    tf_list = []        
    list_file = list_of_files(directory, ".txt") #La liste de tout les fichiers du repertoire
    for file in list_file:                          #Pour chaque fichier:
        with open(directory + "/" + file, "r") as f:#On l'ouvre
            tf_list.append(tf(f.read()))            #On note son TF
    
    for mot in liste_des_mots:                                                          #Pour chaque mot présent dans le repertoire (Dans le corpius de texte)
        matrice_tf_idf.append([])                                                       #On ajoute une ligne à la matrice à TF IDF finale
        for i in range(len(list_file)):                                                 #Pour chaque fichier dans le repertoire
            dico_mot_fichier = tf_list[i]                                               #On associe à dico_mot_fichier le tf du fichier dont-il s'occupe
            if mot in dico_mot_fichier:                   #Si le mot est dans le TF, c'est qu'il est dans le fichier que l'on vient de regarder, donc:
                matrice_tf_idf[id].append(dico_mot_fichier[mot] * liste_des_mots[mot])    #Sur la ligne du mot en question, on ajoute une collonne dans laquel on met la produit du TF du mot multiplé par son IDF 
            else:                                    #Si le mot n'est pas dans le fichier
                matrice_tf_idf[id].append(0.0)       #On ajoute une collonne contenant 0 car sont TF est donc nul
        id += 1#On incrémente de 1 l'id car on va passer au mot suivant.
    return matrice_tf_idf


def write_tf_idf():
    """
    Créer un fichier texte dans lequel on écrit l'intégralité de la matrice TF-IDF pour pouvoir la lire plus facilement
    """
    with open("TF-IDF_matrice.txt", "w") as f:
        id = 0
        dico_key = list(idf().keys())
        for l in tfidf():
            f.write(str(dico_key[id]) + " " + str(l) + "\n")
            id += 1
#write_tf_idf()
