


def add_to_corpus_index (key,next_word,corpus_index):
    if key not in corpus_index:
        corpus_index[key] = {next_word : 1}

    else:

        if next_word in corpus_index[key]:
            corpus_index[key][next_word]+=1

        else:
            corpus_index[key][next_word]= 1


corpus_index = {}
add_to_corpus_index ("Today" ,'is', corpus_index)
add_to_corpus_index ("is" ,'Sunday', corpus_index)
add_to_corpus_index ("Today" ,'is', corpus_index)
add_to_corpus_index ("is" ,'Monday', corpus_index)
add_to_corpus_index ("is" ,'Automation', corpus_index)
add_to_corpus_index ("I" ,'Stay', corpus_index)
print(corpus_index)