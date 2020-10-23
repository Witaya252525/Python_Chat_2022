
def print_all_next_words(corpus_index,word):
    for el in corpus_index :
        if el[0] == word :
            print(el[1:])


corpus_index =[ ['keep' ,'coding' ,'cleaning'] ,['Today' ,'is','witaya']]
word = 'keep'
print_all_next_words(corpus_index,word)
print(corpus_index[1])