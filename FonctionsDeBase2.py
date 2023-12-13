from FonctionDeBases import *
from TFIDF import *
from math import *
import time
import re

a = time.process_time()


def tokenisation(text):
    """
    Renvoie une liste contenant chaque mot du texte sans accent, ni ponctuation
    """
    text = minimize_text(text) + " "
    l = -1
    liste_e = ["é", "è", "ê", "ë"]
    liste_a = ["à", "â"]
    chaine_SansCaraSpe = ""
    for i in range(len(text)):
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
    chaine_SansCaraSpe2 = ""
    for i in range(len(chaine_SansCaraSpe) - 1):
        if chaine_SansCaraSpe[i + 1] == " " and chaine_SansCaraSpe[i] == " ":
            chaine_SansCaraSpe2 += ""
        else:
            chaine_SansCaraSpe2 += chaine_SansCaraSpe[i]
    return chaine_SansCaraSpe2.split(" ")


def regr(l, sep=""):
    """
    Regroupe une liste en une chaine de caractères séparé par un caractères donné
    """
    s = ""
    for val in l:
        s += val + sep
    return s


def intersection(text, directory="./cleaned"):
    """
    Renvoie une liste de tout les mots dans le corpus de texte
    """
    list_in_corpus = list(idf(directory).keys())
    l_text = tokenisation(text)
    l_intersection = []
    for word in l_text:
        if word in list_in_corpus:
            l_intersection.append(word)
    return l_intersection


def compose_matrice(matrice):
    """
    Renvoie la composé d'une matrice donné
    """
    new_matrice = [[0] * len(matrice) for i in range(len(matrice[0]))]
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            new_matrice[j][i] = matrice[i][j]
    return new_matrice


def TFIDF_Qestion(text, directory="./cleaned", idf_given=False, key_given=False):
    """
    Renvoie une liste de tt les TFIDF des mots de la question
    """
    if idf_given:
        idf_dir = idf_given
    else:
        idf_dir = idf(directory)
    if key_given:
        list_mots = key_given
    else:
        list_mots = list(idf_dir.keys())
    M = []
    list_mots_Question = intersection(text, directory)
    tf_motQuestion = tf(regr(tokenisation(text), " "))
    idf_motCorpus = idf_dir
    for i in list_mots:
        if i in list_mots_Question:
            M.append(tf_motQuestion[i] * idf_motCorpus[i])
        else:
            M.append(0.0)
    return M


def norme(vector):
    sum = 0
    for val in vector:
        sum += val
    return sqrt(sum)


def scalaire(Va, Vb):
    sum = 0
    if len(Va) == len(Vb):
        for i in range(len(Va)):
            sum += Va[i] * Vb[i]
        return sum
    else:
        raise TypeError("Les 2 vecteurs doivent avoir autant de valeurs")


def similar(matrice_question, matrice, directory="./cleaned"):
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
    list_nomFichier=list_of_files(directory, "txt")
    matrice = compose_matrice(tfidf(directory))
    liste_similarite = similar(matrice_question, matrice,directory)
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
    max = 0
    id = 0
    question_tfidf = TFIDF_Qestion(text, directory)
    for i in range(len(question_tfidf)):
        if question_tfidf[i] > max:
            max = question_tfidf[i]
            id = i
    return list(idf().keys())[id]


def l_most_impo_q(text, directory="./cleaned"):
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

def respond(text, directory="./speech/", directory_clean="./cleaned"):
    l_txt = tokenisation(text)
    text = ""
    for val in l_txt:
        text += val + " "
    list_word_impo = l_most_impo_q(text, directory_clean)
    sentence = ""
    found = False
    with open(directory + doc_pertinent(TFIDF_Qestion(text, directory_clean),directory_clean)[8:], "r", encoding="utf-8") as f:
        file = f.readlines()
        for word_impo in list_word_impo:
            for line in file:
                for word in line.split(" "):
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

def respond_better(text, directory="./speech/", directory_clean="./cleaned"):
    # ________Lecture du fichier phrase par phrase________
    doc_pert = doc_pertinent(TFIDF_Qestion(text,directory_clean),directory_clean)
    if doc_pert == -1:
        return -1
    with open(directory + doc_pert[8:], "r", encoding="utf-8") as f:  # On ouvre le fichier normal (en enlevant le cleaned_) en lecture en utf8
        file = f.read()  # On lit le fichier
        l_file = re.split(r"[.!?]\s*",file)  # On sépare le fichier en unne liste de phrase possible contenant un des mots de la question
        f.close()

    # ________Calcul à l'avance________
    idf_to_give = idf(directory_clean)  # On calcule à l'avance l'idf
    key_to_give = list(idf_to_give.keys())  # On note à l'avance les clés de l'idf

    # ________Calcul des phrases utiles à analyser________
    l_check = []
    for line in l_file:  # Pour chaque ligne
        for val in (tokenisation(text)):  # On va regarder chaque valeur de la question
            if val in line:  # Si le mot de la question est dans la phrase
                l_check.append(line)  # On ajoute donc cette phrase à notre liste de phrase
                break  # On quitte la boucle de val car on peut passer à la phrase suivante, cela permet d'éviter les doublons de phrases
    # ________Calcul du max de la similarité Question/Phrase________
    max = 0
    max_line = "Le fichier ne contient aucune ligne correspondant à la question."
    for line in l_check:  # Pour chaque ligne du
        sim = similar(TFIDF_Qestion(text, directory_clean, idf_to_give, key_to_give),
                      [TFIDF_Qestion(line, directory_clean, idf_to_give, key_to_give)],directory_clean)[0]
        if sim > max:
            max = sim
            max_line = line
    return max_line
#print(respond("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"))
#print(most_impo_q("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"))
#print(doc_pertinent(TFIDF_Qestion("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?")))
#print(respond_better("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"))
#print(time.process_time() - a)

def politesse(mode = "recup"):
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

def reponse_finale(text, directory="./speech/", directory_clean="./cleaned"):
    poli = politesse()
    rep = respond_better(text, directory, directory_clean)
    if rep == -1:
        return print("Aucun des mots de la question n'est présent dans le corpus de documents"), True
    mot = minimize_text(text.split(" ")[0])
    if mot in poli.keys():
        return print(poli[mot] + rep+ "."), True
    else:
        return print(rep), False
#reponse_finale("Comment une nation peut-elle prendre soin du climat ?")
