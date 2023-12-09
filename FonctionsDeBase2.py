from FonctionDeBases import *
from TFIDF import *
from math import *
import time
import re

a=time.process_time()
def tokenisation(text):
    """
    Renvoie une liste contenant chaque mot du texte sans accent, ni ponctuation
    """
    text = minimize_text(text) + " " #Ajoute un espace à la fin du texte + un espace pour éviter un bug plus tard
    
    #________Supression des caractères spéciaux________
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

def regr(l, sep=""):
    """
    Regroupe une liste en une chaine de caractères séparé par un caractères donné
    """
    s = ""
    for val in l:
        s+=val+sep
    return s

def intersection(text, directory = "./cleaned"):
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
    new_matrice = [[0]*len(matrice) for i in range(len(matrice[0]))]
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            new_matrice[j][i] = matrice[i][j]
    return new_matrice


def TFIDF_Qestion(text, directory = "./cleaned", idf_given=False, key_given=False):
    """
    Renvoie une liste de tt les TFIDF des mots de la question
    """
    if idf_given == False:
        idf_dir = idf(directory)
    else:
        idf_dir = idf_given
    if key_given ==  False:
        list_mots = list(idf_dir.keys())
    else:
        list_mots = key_given
    M = []
    list_mots_Question = intersection(text)
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
        sum+=val
    return sqrt(sum)

def scalaire(Va, Vb):
    sum = 0
    if len(Va) == len(Vb):
        for i in range(len(Va)):
            sum += Va[i]*Vb[i]
        return sum
    else:
        raise TypeError("Les 2 vecteurs doivent avoir autant de valeurs")

def similar(matrice_question,matrice,directory = "./cleaned"):
    list_norme = [[0] for i in range(len(compose_matrice(tfidf(directory))))]
    norme_q = norme(matrice_question)
    

    for i in range(len(matrice)):
        list_norme[i] = norme(matrice[i])

    list_similarities = []
    for i in range(len(matrice)):
        if norme_q*list_norme[i] !=0:
            list_similarities.append(scalaire(matrice_question, matrice[i])/norme_q*list_norme[i])
        else:
            list_similarities.append(0.0)
    return list_similarities
#print(similar(TFIDF_Qestion("les doit est bien")))

def doc_pertinent(matrice_question, list_nomFichier = list_of_files("./cleaned", "txt"), directory="./cleaned"):
    matrice = compose_matrice(tfidf(directory))
    liste_similarite = similar(matrice_question, matrice)
    max = [0, 0]
    for i in range(len(liste_similarite)):
        if liste_similarite[i] > max[0]:
            max[0] = liste_similarite[i]
            max[1] = i
    if max[0] == 0:
        return list_nomFichier[0]
    else:
        return list_nomFichier[max[1]]

def most_impo_q(text):
    max = 0
    id = 0
    question_tfidf = TFIDF_Qestion(text)
    for i in range(len(question_tfidf)):
        if question_tfidf[i] > max:
            max = question_tfidf[i]
            id = i
    return list(idf().keys())[id]

def l_most_impo_q(text):
    question_tfidf = TFIDF_Qestion(text)
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
    #for i in range(len(text)):
    #    print(str(text[i])+ "--->"+str(list_question_tfidf[i]))
    return tri_selec(list_question_tfidf, text)

def tri_selec(l,m):
    final_l = []
    for i in range(len(l)):
        id_min = i
        for j in range(id_min+1, len(l)):
            if l[j] < l[id_min]:
                id_min = j
        l[i],l[id_min] = l[id_min],l[i]
        m[i],m[id_min] = m[id_min],m[i]
    for i in range(len(m)):
        final_l.append(m[-1-i])
    return final_l

#print(l_most_impo_q("bonjour jour doit messieurs abaissement dames le climat change"))
#print(tri_selec([2,4,4,2,3,6,8,9,10,0,2,1],["II","IV","IV","II","III","VI","VIII","IX","X","zéro","II","I"]))

def respond(text,directory = "./speech/"):
    
    l_txt = tokenisation(text)
    text = ""
    for val in l_txt:
        text+= val+" "
    list_word_impo = l_most_impo_q(text)
    sentence = ""
    found = False
    with open(directory+doc_pertinent(TFIDF_Qestion(text))[8:], "r", encoding="utf-8") as f:
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
#print(respond("Comment est ce que les gens doivent decider de servir la france ?"))

def respond_better(text, directory = "./speech/", directory_clean = "./cleaned"):
    #________Lecture du fichier phrase par phrase________
    with open(directory+doc_pertinent(TFIDF_Qestion(text))[8:], "r", encoding="utf-8") as f:#On ouvre le fichier normal (en enlevant le cleaned_) en lecture en utf8
        file = f.read()                         #On lit le fichier
        l_file = re.split(r"[.!?]\s*", file)     #On sépare le fichier en unne liste de phrase possible contenant un des mots de la question
        f.close()
    
    #________Calcul à l'avance________
    idf_to_give = idf(directory_clean)      #On calcule à l'avance l'idf
    key_to_give = list(idf_to_give.keys())  #On note à l'avance les clés de l'idf
   
   #________Calcul des phrases utiles à analyser________
    l_check = []
    for line in l_file:                     #Pour chaque ligne
        for val in (tokenisation(text)):    #On va regarder chaque valeur de la question
            if val in line:                 #Si le mot de la question est dans la phrase
                l_check.append(line)        #On ajoute donc cette phrase à notre liste de phrase
                break                       #On quitte la boucle de val car on peut passer à la phrase suivante, cela permet d'éviter les doublons de phrases
    
    #________Calcul du max de la similarité Question/Phrase________
    max = 0
    max_line = "Je n'ai pu trouver aucune correspondance entre votre entrée et les textes qui me sont fournies"
    for line in l_check:                                                    #Pour chaque ligne du 
        sim = similar(TFIDF_Qestion(text, directory_clean,idf_to_give, key_to_give), [TFIDF_Qestion(line, directory_clean,idf_to_give, key_to_give)])[0]
        if sim > max:
            max = sim
            max_line = line
    return max_line
#bonjour jour doit messieurs abaissement dames le climat change

#print(respond_better("Quel est la position de la France sur la solidarité économique entre les pays ?"))


print("\n\nProcess time: ",time.process_time()-a)
