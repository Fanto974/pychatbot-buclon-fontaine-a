def tf(text):
    words = text.split(" ")
    tf_dico = {}
    for word in words:
        if word in tf_dico.keys():
            tf_dico[word] += 1
        else:
            tf_dico[word] = 1
    return tf_dico
