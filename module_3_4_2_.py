def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    #print(root_word)   # контроль

    for word in other_words:
        #print(word) # контроль
        word_lower = word.lower()
        #print(word_lower)# контроль
        if root_word in word_lower:
            print(root_word, word_lower, "Совпал")
            same_words.append(word_lower)
        else:
            print(root_word, word_lower,"не совпал")
            pass


    return same_words


a = single_root_words('Richa',  'rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print("_____________________________________________________________________________")
print(" Список совпадений-", a)


