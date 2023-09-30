
def add_to_corpus_index(key, next_word, corpus_index):
    if key not in corpus_index:
        corpus_index[key] = {next_word: 1}
    else:
        if next_word in corpus_index[key]:
            corpus_index[key][next_word] += 1

        else:
            corpus_index[key][next_word] = 1


def inite_corpus_stat(corpus_index, corpus):
    splitted_text = corpus.split()
    for i in range(len(splitted_text)-1):
        word = splitted_text[i]
        next_word = splitted_text[i+1]
        add_to_corpus_index(word, next_word, corpus_index)


corpus = "Today is and keep Sunday. I stay at home I stay and keep coding. Today is Monday  I stay at office and keep cleaning  Today I stay awake "
corpus_stat = {}
inite_corpus_stat(corpus_stat, corpus)
print(corpus_stat)
