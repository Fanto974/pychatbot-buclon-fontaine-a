import os
import math

#FONCTION FOURNIES DANS L'ENONCE
def list_of_files(directory, extension):
    """
    Renvoie sous forme de liste les fichiers ayant comme extensions la valeur saisies
    """
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


