from FonctionDeBases import *
from FonctionsDeBase2 import *
from Fonctionalités_Partie1.Fonctionalite1 import *
from Fonctionalités_Partie1.Fonctionalite2 import *
from Fonctionalités_Partie1.Fonctionalité3 import *
from Fonctionalités_Partie1.Fonctionalite4 import *
from Fonctionalités_Partie1.Fonctionalite5 import *
from Fonctionalités_Partie1.Fonctionalite6 import *
from TFIDF import *

#//////////////////////////////// BASE DE TEST DE TOUTES LES FONCTIONS //////////////////////////////////////////////////////////
line = "\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"


print("DANS LA PARTIE 1 :")
print("             DANS LES FONCTION DE BASES :")
print(line)

print("La fonction get_names :")
print(get_names("./Dossiers_Thematiques/speech"))
print(line)

print("La fonction associe :")
print(associe("['Sarkozy', 'Giscard dEstaing', 'Hollande', 'Chirac', 'Macron', 'Mitterrand']"))
print(line)

print("La fonction print_unique :")
print(print_unique("./Dossiers_Thematiques/speech"))
print(line)

print("La fonction minimize_text :")
print(minimize_text("BONJOUR, COmmeNt sA Va ?"))
print(line)

print("La fonction lower_files :")
print("Cette fonction écrit dans un fichier direcement. Si vous voulez la tester veuiller créer un répertoir final de test et entrer cette commande : lower_files('directory source', 'directory final')")
print(line)

print("La fonction apostrophe : ")
print(apostrophe("l", 1))
print(line)

print("La fonction suppr_SpeCara :")
print("Cette fonction écrit dans un fichier direcement. Si vous voulez la tester veuiller créer un répertoir final de test et entrer cette commande : suppr_SpeCara('./Dossiers_Thematiques/speech')")
print(line)

print("             Les fonctionalités :")
print(line)

print("La fonctionalité 1 :")
print(NonImportant())
print(line)

print("La fonctionalité 2 :")
print(highest_tfidf("./cleaned"))
print(line)

print("La fonctionalité 3 :")
print(Plus_mot("Macron"))
print(line)

print("La fonctionalité 4 :")
print(who_said("./cleaned", "Nation"))
print(line)

print("La fonctionalité 5 :")
print(premier_mot("climat"))
print(line)

print("La fonctionalité 6 :")
print(NonImportant6())
print(line)

print("             TFIDF :")
print(line)

print("La fonction TF :")
print(tf("Comment sa va ? Tu va bien ?"))
print(line)

print("La fonction IDF :")
print(idf("./cleaned"))
print(line)

print("La fonction TFIDF :")
print(tfidf("./cleaned"))
print(line)



print("DANS LA PARTIE 2 :")
print("             DANS LES FONCTION DE BASES :")
print(line)
