# Membre du projet :
    Mathis Buclon
    Paul Fontaine
# Execution et liens:
 - Lancer le fichier menu.py et suivez les instructions
 - Pour les test aller dans le fichier main depuis PyCharm, vous y retrouverais toutes les fonctions et une commande pour les tester
 - Lien vers le projet : https://github.com/Fanto974/pychatbot-buclon-fontaine-a.git
# Fonctions Partie 1:
1. ### **Dans fonction de base**
    - _get_names :_
        - Appellation : Voir les conditons ci-dessous
        - Description : Permet d'obtenir le nom d'un président a partir du nom du fichier de son discours
        - Paramètre :
            1. Si on désire recevoir une liste de tt les présidents SANS DOUBLONS en envoyant un répertoire: get_names('Chemin du repertoire')
            2. Si on désire recevoir le nom d'un président en fournissant un fichier : get_names(0, 'Nom du fichier')
            3. Si on désire recevoir une liste de tt les présidents AVEC DOUBLONS en envoyant un répertoire: get_name('Chemin du repertoire', 0, 0)
        - Retourne : Le nom d'un ou plusieurs présidents en focntions des paramètres rentés
   
    - _associe :_
        - Appellation : associe(liste)
        - Description : Permet d'associer a chaque nom de président un prénom rentré préalablement dans la base de donnée symbolisé par le fichier texte Nom_Prenom.txt
        - Paramètre : une liste de nom SANS DOUBLON de président
        - Retourne : Une liste de nom et prénoms pour chaque nom de président passé a la fonction

    - _print_unique :_
        - Appellation : print_unique()
        - Description : Permet normalement d'enlever les doublons dans les noms de présidents extraits par la fonction get_names mais les doublons sont déja gérés par cette meme fonction
        - Paramètre : Rien
        - Retourne : L'appel de la fonction get_names

    - _minimize_text :_
        - Appellation : minimize_text(ch) PS : normalement on ne l'appel pas car elle est juste une composante d'une autre fonction plus particulièrement de lower_files()
        - Description : Permet de réduir toutes les majuscules d'un texte en minuscule 
        - Paramètre : une chaine de charactères
        - Retourne : Une autre chaine de charactères sans majuscule

    - _lower_files :_
        - Appellation : lower_files(directory, end_directory)
        - Description : Mettre le miniscule les fichiers du dossier se trouvant dans le directory et les range dans le dossier end_directory en appellant directement la fonction minimize_text()
        - Paramètre : une chaine de caractère contenant un chemin d'accès vers dossier source et un un chemin d'accès vers un dossier final
        - Retourne : Rien

    - _apostrophe :_
        - Appellation : apostrophe(lettre, l) PS : normalement on ne l'appel pas car elle est juste une composante d'une autre fonction plus particulèrement de supp_SpeCara()
        - Description : Permet le meilleure remplacement de l'apostrphe
        - Paramètre : une chaine de caractère contenant qu'un seul caratère (la lettre qui précède l'apostrophe) et une variable int qui permet dans certain cas le remplacement de l'apostrophe par un traitement de 1 fois sur 2 c'est tel ou tel caractère qui sera utilisé
        - Retourne : Une autre chaine de charactères conteanant elle aussi un seul caractère qui contient la lettre par laquelle sera remplacé l'apostrophe

    - _supp_SpeCara :_
        - Appellation : suppr_SpeCara() PS : normalement on ne l'appel pas car elle est juste une composante d'une autre fonction
        - Description : Permet d'enlever les caractères spéciaux d'un texte comme (', é, è, ù, ...) avec un traitement particulier pour l'apostrophe par l'appel de la fonction apostrophe(). La fonction va réécrire les fichiers qu'elle étudie sans les caractères spéciaux. ATTENTION : la fonction prendra toujours les fichiers du dossier cleaned
        - Paramètre : Rien
        - Retourne : Rien, elle va réécrire les fichiers sans les caractères spéciaux


2. ### **Les fonctionalités**
    - _Fonctionalité n°1 :_
        - Appellation : NonImportant()
        - Description : Permet de lister tous les mots non importants soit les mots dont le TFIDF est de 0
        - Paramètre : Rien
        - Retourne : Une liste des mots non importants

    - _Fonctionalité n°2 :_
        - Appellation : highest_tfidf(directory)
        - Description : Permet de donner le mots qui a le TFIDF le plus élever de tous les mots de tous les documents contenu dans le dossier passé en paramètre
        - Paramètre : une chaine de caractère contenant un chemin d'accès vers le dossier souhaité PS : établi par défaud sur le dossier cleaned
        - Retourne : Le mot avec le TFIDF le plus élevé

    - _Fonctionalité n°3 :_
        - Appellation : Plus_mot(president)
        - Description : Permet de connaitre le mot le plus dit par un président dans son discours
        - Paramètre : Une chaine de caractère contenant le nom du président souhaité
        - Retourne : Le mot le plus dit par le président en question

    - _Fonctionalité n°4 :_
        - Appellation : who_said(directory, word)
        - Description : Permet de lister tous les président qui ont prononcer un mot voulu et celui qui l'a prononcer le plus
        - Paramètre : une chaine de caractère contenant un chemin d'accès vers le fichier cible et mot, une chaine de caractère contenant le mot que dont on souhaite connaitre le nom des président l'ayant prononcer dans leurs discours
        - Retourne : Une liste des présidents ayant dit ce mot et celui qui l'a prononcer le plus de fois
     
    - _Fonctionalité n°5 :_
        - Appellation : premier_mot(mot)
        - Description : Permet de connaitre le premier président a parler d'un mot voulu. PS : On entend par le premier celui qui dit le moins de mots avant celui rentré par l'utilisateur
        - Paramètre : mot, une cjaine de caractères contenant le mot dont on veut connaitre le premier président a en avoir parler
        - Retourne : Le ou les noms ddes présidents a avoir dit se mot en premier. PS : "les" car il peut y avoir égalité
     
    - _Fonctionalité n°6 :_
        - Appellation : NonImportant6()
        - Description : Permet de lister tous les mots dit par tous les présidents mais qui ne font pas parti des mots banales tels que "je, tu, le, la, il, ...
        - Paramètre : Rien
        - Retourne : Une liste des mots dit par tous les présidents hors mot banals
     
# Fonction Partie 2
1. ### **Dans fonction de base 2**
    - _tokenisation :_
        - Appellation : tokenisation(text)
        - Description : Minimize le texte passé en paramètre et enlève de celui-ci tout les caractères spéciaux
        - Paramètre : STR: une chaîne de caractères contenant une phrase
        - Retourne : list: une liste contenant chaque mot du texte sans accent, ni majuscules, ni ponctuation
          
    - _regr :_
        - Appellation : regr(l, sep)
        - Description : Change une liste de mot en une chaine de caractères
        - Paramètre : List: une liste contenant des chaines de caractères
                    : STR: Une chaîne de caractère qui ne contiendra un caractère qui fera office de séparateur
        - Retourne : STR: une chaîne de caractères qui contiendra tout les mots de la liste avec entre chacun un caractère donné
          
    - _intersection :_
        - Appellation : intersection(text, directory)
        - Description : Analyse tous les mots de la question et ne retient que ceux qui sont également présent dans le corpus de document du dossier passé en paramère
        - Paramètre : STR: une chaîne de caractères qui contiendra le texte de la question
                    : STR: Un chemin d'accès vers le répértoire dont on veut analyser l'intersection
        - Retourne : List: Une liste des mots présent et dans la question et dans le corpus de documents
     
    - _compose_matrice :_
        - Appellation : compose_matrice(matrice)
        - Description : Permet d'inverser la matrice d'un corpus de document
        - Paramètre : List: une liste de liste qui contient la matrice des mots du corpus
        - Retourne : List: La meme liste de liste mais inversée
     
    - _TFIDF_Qestion :_
        - Appellation : TFIDF_Qestion(text, directory, idf_given=False, key_given=False)
        - Description : Calcule pour caque mot de la question son TFIDF
        - Paramètre : STR: une chaîne de caractères qui contiendra le texte de la question
                    : STR: Un chemin d'accès vers le répértoire nétoyé des fichiers du corpus de doc souhaité
                    :    : ????????????????????????????????
                    :    : ?????????????????????????????
        - Retourne : List: une liste de tout les TFIDF des mots de la question
     
    - _doc_pertinent :_
        - Appellation : doc_pertinent(matrice_question, directory)
        - Description : Analyse le corpus de documents et donne le documents ayant la plus grande similarité avec la question de l'utilisateur
        - Paramètre : List: une liste de liste qui contient la matrice de la question
                    : STR: Un chemin d'accès vers le répértoire dont on veut analyser le document le plus pertinant
        - Retourne : STR: Le deuxième caractère d'une liste qui est une chaîne de caractèreset qui contient le nom du fichier le plus pertinant
     
    - _most_impo_q :_
        - Appellation : most_impo_q(text, directory)
        - Description : Analyse la question et donne le mot le plus important
        - Paramètre : STR: une chaîne de caractères qui contiendra le texte de la question
                    : STR: Un chemin d'accès vers le répértoire ou la question est posée
        - Retourne : STR: Le nième caractère d'une liste qui contiendra le mot ayant le tfidf le plus élevé d'une question
     
    - _l_most_impo_q :_
        - Appellation : l_most_impo_q(text, directory)
        - Description : Classe les mots de la question du plus important au moins imporants
        - Paramètre : STR: une chaîne de caractères qui contiendra le texte de la question
                    : STR: Un chemin d'accès vers le répértoire ou la question est posée
        - Retourne : List: une liste triée des mots de la question avec comme paramètre de tri leur TFIDF 

    - _reponse_finale :_
        - Appellation : reponse_finale(text, directory, directory_clean)
        - Description : Utilise les formules de politesse et la fonction respond_better pour afficher la réponse à l'utilisateur
        - Paramètre : STR: Une chaîne de caractères qui contiendra le texte de la question
                    : STR: Un chemin d'accès vers le répertoire non cleaned ou la question est posée
                    : STR: Un chemin d'accès vers le répertoire cleaned dans lequel la question est posée
        - Retourne : Tuple: Le premier élément contiendra la réponse et le 2e un booléen qui indiquera si oui ou non il faut demander a l'utilisateur la question de politesse
