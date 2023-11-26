# Membre du projet :
    Mathis Buclon
    Paul Fontaine
# Execution :
 - Lancer le fichier menu.py
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
        - Appellation : minimize_text(ch)
        - Description : Permet de réduir toutes les majuscules d'un texte en minuscule
        - Paramètre : une chaine de charactères
        - Retourne : Une autre chaine de charactères sans majuscule
