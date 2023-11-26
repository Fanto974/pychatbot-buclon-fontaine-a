# Membre du projet :
    Mathis Buclon
    Paul Fontaine
# Execution et liens:
 - Lancer le fichier menu.py et suivez les instructions
 - https://github.com/Fanto974/pychatbot-buclon-fontaine-a.git
# Fonctions :
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
