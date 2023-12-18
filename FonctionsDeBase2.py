"""
    Ce fichier contient toutes les fonction principales et nécéssaires a la réponse du Chat Bot.
    Il fait suite au fichier "FonctionDeBases" qui contient lui aussi des fonction nécéssaires au Chat Bot mais des fonction plus basique mais surtout des fonction nécéssaires aux autres fonctionnalités proposées à l'utilisateur
"""

from FonctionDeBases import *
from TFIDF import *
from math import *
import time

a = time.process_time()


def tokenisation(text):
    """
    :param : STR: une chaîne de caractères contenant une phrase
    :return: list: une liste contenant chaque mot du texte sans accent, ni majuscules, ni ponctuation

    :descirption: Minimize le texte passé en paramètre et enlève de celui-ci tout les caractères spéciaux
    """
    text = minimize_text(text) + " "                                    # On enlève les majuscules du texte
    l = -1                                                              # Pour la gestion de l'algorithme
    liste_e = ["é", "è", "ê", "ë"]                                      
    liste_a = ["à", "â"]
    chaine_SansCaraSpe = ""                                             # On crée une chaîne de caractères qui ne contienderas pas de caractères spéciaux
    for i in range(len(text)):                                          # On parcours le texte et on enlève les caractères spéciaux
        if "a" <= text[i] <= "z":
            chaine_SansCaraSpe += text[i]
        else:
            if text[i] == "'":
                chaine_SansCaraSpe += apostrophe(text[i - 1], l)
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
    chaine_SansCaraSpe2 = ""                                                           # On initialise une 2e chaine de caractères afin d'enlever les doubles espaces générés
    for i in range(len(chaine_SansCaraSpe) - 1):                                       # On la remplit
        if chaine_SansCaraSpe[i + 1] == " " and chaine_SansCaraSpe[i] == " ":
            chaine_SansCaraSpe2 += ""
        else:
            chaine_SansCaraSpe2 += chaine_SansCaraSpe[i]
    return split_new(chaine_SansCaraSpe2,[" "])                                       # On retourne une liste de la 2e chaine de caractère en splitant les mots avec les espaces

    #return split_new(chaine_SansCaraSpe2,[" "])                                              # On retourne une liste de la 2e chaine de caractère en splitant les mots avec les espaces


def regr(l, sep=""):
    """
    :param : List: une liste contenant des chaines de caractères
           : STR: Une chaîne de caractère qui ne contiendra un caractère qui fera office de séparateur
    :return: STR: une chaîne de caractères qui contiendra tout les mots de la liste avec entre chacun un caractère donné

    :descirption: Change une liste de mot en une chaine de caractères
    """
    s = ""                    # On crée une chaîne de caractère vide qui contiendra notre phrase
    for val in l:             # On parcours la liste et on la remplit
        s += val + sep
    return s


def intersection(text, directory="./cleaned"):
    """
    :param : STR: une chaîne de caractères qui contiendra le texte de la question
           : STR: Un chemin d'accès vers le répértoire dont on veut analyser l'intersection
    :return: List: Une liste des mots présent et dans la question et dans le corpus de documents

    :descirption: Analyse tous les mots de la question et ne retient que ceux qui sont également présent dans le corpus de document du dossier passé en paramère
    """
    list_in_corpus = list(idf(directory).keys())        # On initalise une liste qui contient tous les mots du corpus de document du dossier en paramètre
    l_text = tokenisation(text)                         # On tokenise le texte pour le plus avoir ni de majuscule ni de caractères spécieux qui pourrais géner la comparaison
    l_intersection = []                                 # On initalise une liste qui contiendra les mot présent dans la question et le corpus
    for word in l_text:                                 # On parcours les mots de la question et on regarde si ils sont dans le corpus si c'est le cas on les ajoutes a la liste
        if word in list_in_corpus:
            l_intersection.append(word)
    return l_intersection


def compose_matrice(matrice):
    """
    :param : List: une liste de liste qui contient la matrice des mots du corpus
    :return: List: La meme liste de liste mais inversée

    :descirption: Permet d'inverser la matrice d'un corpus de document
    """
    new_matrice = [[0] * len(matrice) for i in range(len(matrice[0]))]
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            new_matrice[j][i] = matrice[i][j]
    return new_matrice


def TFIDF_Qestion(text, directory="./cleaned", idf_given=False, key_given=False):
    """
    :param : STR: une chaîne de caractères qui contiendra le texte de la question
           : STR: Un chemin d'accès vers le répértoire nétoyé des fichiers du corpus de doc souhaité
           :Bool: Permet de fournir à l'avance la matrice idf d'un corpus pour réduire la quantité de calcul
           :Bool: Permet de fournir à l'avance les clés de cette matrice pour réduire la quantité de calcul
    :return: List: une liste de tout les TFIDF des mots de la question

    :descirption: Calcule pour caque mot de la question son TFIDF
    """
    if idf_given:                                                    # Permet d'utiliser les TFIDF de certains mot donnés (pour ne pas devoir calculer les IDF de tous les mots du corpus)
        idf_dir = idf_given
    else:                                                            # Si on n'a pas donné de mots précis on calcule les IDF de tous les mots du corpus
        idf_dir = idf(directory)
    if key_given:                                                    # Permet d'utiliser certain mot donnés (pour ne pas devoir récupérer tous les mots du corpus)
        list_mots = key_given
    else:                                                            # Si on n'a pas donné de mot précis on récupère tous les mots du corpus
        list_mots = list(idf_dir.keys())                             
    M = []
    list_mots_Question = intersection(text, directory)               # On récupère tous les mots de la question
    tf_motQuestion = tf(regr(tokenisation(text), " "))               # On récupère le TF de tous les mots de la question
    idf_motCorpus = idf_dir
    for i in list_mots:
        if i in list_mots_Question:
            M.append(tf_motQuestion[i] * idf_motCorpus[i])           # Pour chaque mot du corpus présent dans la question on lui multiplie son TF et son IDF afin d'obtenir son TFIDF
        else:
            M.append(0.0)                                            # Si le mot n'est pas présent dans la question alors on lui met un TFIDF de 0
    return M


def norme(vector):
    """
    :param: list: Un vecteur 
    :return: int: La norme de ce vecteur
    
    Renvoie la norme d'un vecteur en faisant la somme des crrés de ses valeurs et renvoie la racine carré du tout
    """
    sum = 0
    for val in vector:
        sum += val
    return sqrt(sum)


def scalaire(Va, Vb):
    """
    :param: list: Un premier vecteur
            list: Un deuxieme vecteur de meme taille
    :return: int: La produit scalaire de ces 2 vecteurs
    Renvoie le produit scalaire de 2 vecteurs de même taille
    """
    sum = 0
    if len(Va) == len(Vb):
        for i in range(len(Va)):
            sum += Va[i] * Vb[i]
        return sum
    else:
        raise TypeError("Les 2 vecteurs doivent avoir autant de valeurs")


def similar(matrice_question, matrice, directory="./cleaned"):
    """
    :param: list: Un 1 er vecteur (La matrice TF-IDF de la question)
            list: Une liste de vecteur (La matrice TF-IDF du corpus de texte)
    :return:list: Une liste des similarités entre le 1 er vecteur et chaque vecteur dans la liste de vecteur
    Renvoie une liste de la similarité d'un vecteur avec une liste d'autres vecteurs
    Exemple:
        La similarité de la question avec les différents documents
    """
    list_norme = [[0] for i in range(len(compose_matrice(tfidf(directory))))]
    norme_q = norme(matrice_question)
    if norme_q == 0:
        return -1

    for i in range(len(matrice)):
        list_norme[i] = norme(matrice[i])

    list_similarities = []
    for i in range(len(matrice)):
        list_similarities.append(scalaire(matrice_question, matrice[i]) / norme_q * list_norme[i])
    return list_similarities


# print(similar(TFIDF_Qestion("les doit est bien")))

def doc_pertinent(matrice_question, directory="./cleaned"):
    """
    :param : List: une liste de liste qui contient la matrice de la question
           : STR: Un chemin d'accès vers le répértoire dont on veut analyser le document le plus pertinant
    :return: STR: Le deuxième caractère d'une liste qui est une chaîne de caractèreset qui contient le nom du fichier le plus pertinant

    :descirption: Analyse le corpus de documents et donne le documents ayant la plus grande similarité avec la question de l'utilisateur
    """
    list_nomFichier = list_of_files(directory, "txt")
    matrice = compose_matrice(tfidf(directory))
    liste_similarite = similar(matrice_question, matrice, directory)
    if liste_similarite == -1:
        return -1
    max = [0, 0]
    for i in range(len(liste_similarite)):
        if liste_similarite[i] > max[0]:
            max[0] = liste_similarite[i]
            max[1] = i
    if max[0] == 0:
        return "Il n'y a aucun document plus pertinent"
    else:
        return list_nomFichier[max[1]]


def most_impo_q(text, directory="./cleaned"):
    """
    :param : STR: une chaîne de caractères qui contiendra le texte de la question
           : STR: Un chemin d'accès vers le répértoire ou la question est posée
    :return: STR: Le nième caractère d'une liste qui contiendra le mot ayant le tfidf le plus élevé d'une question

    :descirption: Analyse la question et donne le mot le plus important
    """
    max = 0
    id = 0
    question_tfidf = TFIDF_Qestion(text, directory)
    for i in range(len(question_tfidf)):
        if question_tfidf[i] > max:
            max = question_tfidf[i]
            id = i
    return list(idf().keys())[id]


def l_most_impo_q(text, directory="./cleaned"):
    """
    :param : STR: une chaîne de caractères qui contiendra le texte de la question
           : STR: Un chemin d'accès vers le répértoire ou la question est posée
    :return: List: une liste triée des mots de la question avec comme paramètre de tri leur TFIDF 

    :descirption: Classe les mots de la question du plus important au moins imporants
    """
    question_tfidf = TFIDF_Qestion(text, directory)
    l_tfidf = list(idf().keys())
    list_question_tfidf = []
    text = tokenisation(text)
    for val in text:
        found = False
        for i in range(len(l_tfidf)):
            if val == l_tfidf[i]:
                list_question_tfidf.append(question_tfidf[i])
                found = True
                break
        if not found:
            list_question_tfidf.append(0.0)
    # for i in range(len(text)):
    #    print(str(text[i])+ "--->"+str(list_question_tfidf[i]))
    return tri_selec(list_question_tfidf, text)


def tri_selec(l, m):
    """
    :param: list: Une list  avec des valeurs qui peuvent être trié par les opérateurs < et >
            list: Une liste de meme taile que la premiere que l'on désire trier en fonction de la 1ere
    :return:list: La 2 eme liste trié en fonction de la 2eme
    
    renvoie une liste trié en fonction d'une liste d'indice

    Par exemple 
    print(tri_selec([2,4,4,2,3,6,8,9,10,0,2,1],["II","IV","IV","II","III","VI","VIII","IX","X","zéro","II","I"]))
    renverra donc les valeurs en chiffres romains trié car la première liste leur fais correspondre à chacun une valeur numérique
    """
    final_l = []
    for i in range(len(l)):
        id_min = i
        for j in range(id_min + 1, len(l)):
            if l[j] < l[id_min]:
                id_min = j
        l[i], l[id_min] = l[id_min], l[i]
        m[i], m[id_min] = m[id_min], m[i]
    for i in range(len(m)):
        final_l.append(m[-1 - i])
    return final_l


# print(l_most_impo_q("bonjour jour doit messieurs abaissement dames le climat change"))
# print(tri_selec([2,4,4,2,3,6,8,9,10,0,2,1],["II","IV","IV","II","III","VI","VIII","IX","X","zéro","II","I"]))

def respond(text, directory="./speech/", directory_clean = "./cleaned"):
    """
    :param: str: La question de l'utilisateur
            str: le directory dans lequel on doit chercher les documents avant leur modifications
            str: le directory dans lequel on trouve les documents modifié sans majuscule et caractères spéciaux
    :return:str: La réponse généré par l'algorithme
    Renvoie une phrase
    Renvoie la 1ere phrase contenant le mot avec le plus grand TFIDF de la question dans le document le plus similaire à la question
    """
    l_txt = tokenisation(text)
    text = ""
    for val in l_txt:
        text += val + " "
    list_word_impo = l_most_impo_q(text)
    sentence = ""
    found = False
    if doc_pertinent(TFIDF_Qestion(text, directory_clean), directory_clean) == -1:
        return "Aucun des mots de la question n'est présent dans le corpus de documents"
    if doc_pertinent(TFIDF_Qestion(text, directory_clean), directory_clean) == -1:
        return "Aucun des mots de la question n'est présent dans le corpus de documents"
    with open(directory + doc_pertinent(TFIDF_Qestion(text, directory_clean), directory_clean)[8:], "r", encoding="utf-8") as f:
        file = f.readlines()
        for word_impo in list_word_impo:
            for line in file:
                for word in split_new(line,[" "]):
                    sentence += word + " "
                    if word_impo in tokenisation(word):
                        found = True
                    elif "." in word or "!" in word or "?" in word:
                        if found:
                            return sentence
                        else:
                            sentence = ""
            if found:
                return sentence


# print(respond("Comment est ce que les gens doivent decider de servir la france ?"))

def respond_better(text, directory="./Dossiers_Thematiques/speech/", directory_clean="./cleaned"):
    """
    :param: str: La question de l'utilisateur
            str: le directory dans lequel on doit chercher les documents avant leur modifications
            str: le directory dans lequel on trouve les documents modifié sans majuscule et caractères spéciaux
    :return:str: La réponse généré par l'algorithme
    Renvoie une phrase 
    Choisi la phrase la plus similaire à la question en réutilisant la fonction similar créer plus tôt
    """
    # ________Lecture du fichier phrase par phrase________
    doc_pert = doc_pertinent(TFIDF_Qestion(text, directory_clean), directory_clean)
    if doc_pert == -1:
        return -1
    with open(directory + doc_pert[8:], "r", encoding="utf-8") as f:  # On ouvre le fichier normal (en enlevant le cleaned_) en lecture en utf8
        file = f.read()  # On lit le fichier
        l_file = split_new(file, [".","!","?"])# On sépare le fichier en unne liste de phrase possible contenant un des mots de la question         
        f.close()

    # ________Calcul à l'avance________
    idf_to_give = idf(directory_clean)  # On calcule à l'avance l'idf
    key_to_give = list(idf_to_give.keys())  # On note à l'avance les clés de l'idf

    # ________Calcul des phrases utiles à analyser________
    l_check = []
    for line in l_file:  # Pour chaque ligne
        line_toke = tokenisation(line)
        for val in (tokenisation(text)):  # On va regarder chaque valeur de la question
            if val in line_toke:  # Si le mot de la question est dans la phrase
                l_check.append(line)  # On ajoute donc cette phrase à notre liste de phrase
                break  # On quitte la boucle de val car on peut passer à la phrase suivante, cela permet d'éviter les doublons de phrases

    # ________Calcul du max de la similarité Question/Phrase________
    max = 0
    max_line = "Le fichier ne contient aucune ligne correspondant à la question."
    for line in l_check:  # Pour chaque ligne du
        sim = similar(TFIDF_Qestion(text, directory_clean, idf_to_give, key_to_give),
                      [TFIDF_Qestion(line, directory_clean, idf_to_give, key_to_give)])[0]
        if sim > max:
            max = sim
            max_line = line
    return max_line
#print(respond("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"))
#print(most_impo_q("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"))
#print(doc_pertinent(TFIDF_Qestion("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?")))
#print(respond_better("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"))
#print(respond_better("MESSIEURS, DE CE JOUR, DATE UNE ERE NOUVELLE DE LA POLITIQUE FRANCAISE"))
#print(time.process_time() - a)

def politesse(mode = "recup"):
    """
    :param : STR: Le mode dans lequel on veut appeler la question
    :return : Dictionnaire: De toutes les formules de politesses contenue dans le fichier Politess.txt => Si le paramètre est "recup"
            : Rien: juste des prints => Si le mode est "ajout"
    :description : Permet d'ajouter et d'afficher les formules de politesses au début dechaque réponses en fonction du premier mot de l'utilisateur
    """
    if mode == "recup":
        d = {}
        with open("./Fichier_Informations/Politesse.txt", "r") as poli:
            l = poli.readlines()
            for i in l:
                cv = i.split(" : ") 
                d[cv[0]] = cv[1][:-1]
        return d
    elif mode == "ajout":
        d = politesse()
        print("\n\n")
        print("Afin d'améliorer notre chat bot, pourriez vous répondre a cette question ?")
        rep = input("Auriez-vous souhaiter une formule de politesse au début de la réponse par rapport au premier mot de votre question ? (oui/non)")
        while rep != "oui" and rep != "non":
            print("Il faut rentrer oui ou non")
            rep = input("Auriez-vous souhaiter une formule de politesse au début de la réponse par rapport au premier mot de votre question ? (oui/non)")
        if rep == "oui":
            print("Vous pouvez l'ajouter directement ici ou alors ouvrir le fichier texte 'Politesse.txt' et rentrer ce que vous voulez en suivant le format demandé")
            rep2 = input("Tapez 'ici' pour le faire ici et 'fichier' pour le faire dans le fichier")
            if rep2 == "ici":
                print("ATTENTION, veillez a ne rentrer qu'un seul mot !!! (ps : les mots composé avec des tirés sont considérés comme 1 seul mot)")
                mot = input("Quel était le premier mot de votre question ?")
                while " " in mot:
                    print("ATTENTION, veillez a ne rentrer qu'un seul mot !!! (ps : les mots composé avec des tirés sont considérés comme 1 seul mot)")
                    mot = input("Quel était le premier mot de votre question ?")
                mot = minimize_text(mot)
                if mot in d.keys():
                    return print("Désoler se mot est déja remplacé par une formule de politesse")
                print("Par quelle formule souhaiter vous commencer la réponse lorsqu'une question commence par : ", mot, " ?")
                forme = input()
                with open("./Fichier_Informations/Politesse.txt", "a") as poli:
                    poli.write(mot + " : " + forme + "\n")
                    print("Et voilà c'est fait !")
            elif rep2 == "fichier":
                print("Ok et n'hésitez pas a en rajouter plusieurs !!!")
            else:
                print("dommage, vous n'avez pas rentré de réponse valide si vous voulez quand même ajouter quelque chose allez dans le fichier texte")
        elif rep == "non":
            print("Ok")
#print(politesse())

def reponse_finale(text, directory="./Dossiers_Thematiques/speech/", directory_clean="./cleaned"):
    """
    :param : STR: Une chaîne de caractères qui contiendra le texte de la question
           : STR: Un chemin d'accès vers le répertoire non cleaned ou la question est posée
           : STR: Un chemin d'accès vers le répertoire cleaned dans lequel la question est posée
    :return : Tuple: Le premier élément contiendra la réponse et le 2e un booléen qui indiquera si oui ou non il faut demander a l'utilisateur la question de politesse
    :description : Utilise les formules de politesse et la fonction respond_better pour afficher la réponse à l'utilisateur
    """
    if "note" in text and "merite" in text:
        return "Chatbot: Ils mériteraient la note de 20/20 sans aucune hésiation", True
    poli = politesse()                                                                                            # On range les formule de politesse dans une variable
    rep = respond_better(text, directory, directory_clean)                                                        # On crée la réponse a la question de l'utilisateur
    if rep == -1:                                                                                                 # Dans le cas ou aucune réponse n'est possible on affiche un message a l'utilisateur
        return ("Aucun des mots de la question n'est présent dans le corpus de documents"), True
    mot = minimize_text(split_new(text,[" "])[0])                                                                 # On minimize le texte de la question et on test plusieur cas
    if len(tokenisation(mot)) == 1:                                                                               # En fonction de la question on répondra avec ou sans formule de politesse
        mot = tokenisation(mot)[0]
    if mot in poli.keys():
        return (poli[mot] + " " + minimize_text(rep).strip() + "."), True
    else:
        return (rep), False                                                                                       # Les true et false permettent de savoir si le Chat Bot doit demander a l'utilisateur a la fin  de la réponse si il aurait souhaiter une formule de politesse
#print(reponse_finale("Peux-tu une nation peut-elle prendre soin du climat ?"))

def split_new(text,l):
    """
    text : chaine à split
    l : liste d'indice à regarder pour le split

    description : Split une chaine de caractères comme la fonction split mais peut prendre plusieurs arguments permettant de split en fonctions de différentes valeurs
    """
    phrase = ""
    l_phrase = []
    for val in text:
        if val not in l:
            phrase+=val
        else:
            l_phrase.append(phrase)
            phrase = ""
    if phrase!="":
        l_phrase.append(phrase)
    return l_phrase
text = "Quelle est l'attente international des gouvernements envers la mondialisation ?"
#print(respond(text, "./Dossiers_Thematiques/speech/", "./cleaned"))
print(tokenisation("aaze 2 aze"))
