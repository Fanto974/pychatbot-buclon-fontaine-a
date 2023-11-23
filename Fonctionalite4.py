def who_said(directory="./cleaned/",word="Nation"):
    """
    :desc: Fonction qui dit quel président on prononcer un mot donné
    """
    tf_idf = tfidf(directory)
    dico_key = list(idf().keys())
    liste_names = get_names(directory, 0, 0)
    time_said = {}
    people_max = []

    maxi = 0
    id = 0

    for i in range(len(dico_key)):
        if minimize_text(dico_key[i]) == minimize_text(word):
            id = i
            break
    
    for i in range(len(tf_idf[id])):
        if tf_idf[id][i] != 0:    
            if liste_names[i] in time_said.keys():
                time_said[liste_names[i]] += tf_idf[id][i]
            else:
                time_said[liste_names[i]] = tf_idf[id][i]          
    for val in time_said.keys():
        if time_said[val] > maxi:
            maxi = time_said[val]
            people_max = [val]
        elif time_said[val] == maxi:
            people_max.append(val)
    return [people_max, list(time_said.keys())]
#print(who_said())
