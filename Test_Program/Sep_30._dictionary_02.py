

# hash_table  = dict( a = 1 ,b = 2)
# print(hash_table['a'])
# hash_table2 =dict(a =15 , b = {"a":7})
# print(hash_table2)


def add_corpus_index(key, next_word, corpus_index):
    if key not in corpus_index:
        corpus_index[key] = {next_word:1}
    else:
        if next_word in  corpus_index[key]:
            corpus_index[key][next_word] +=1

        else:
            corpus_index[key][next_word] = 1



corpus_index={}
add_corpus_index('Today', 'is', corpus_index)
add_corpus_index('is', 'Sunday', corpus_index)
add_corpus_index('is', 'Monday', corpus_index)
add_corpus_index('Today', 'I', corpus_index)
add_corpus_index('Today', 'I', corpus_index)
add_corpus_index('Today', 'Wiyaya', corpus_index)
add_corpus_index('Seagate', 'My word', corpus_index)
print(corpus_index)
