

def add_to_corpus_index(corpus_index ,word ,next_word):
    for el in corpus_index :
        if el[0] == word :
            el[1].append(next_word)
            return


    corpus_index.append([ word,[next_word]])        

def add_all_to_corpus_index(corpus_index , corpus):
    splitted_text = corpus.split()
    for i in range(len(splitted_text)-1):
        current_word , next_word = splitted_text[i] ,splitted_text[i+1]
        add_to_corpus_index(corpus_index ,current_word,next_word)


    return corpus_index

def lookup(corpus_index ,word):
    for el in corpus_index:
        if el[0] == word :
            print(el[1])        

     


#corpus_index = [   ]    
#add_to_corpus_index (corpus_index ,"keep","coding")
#add_to_corpus_index (corpus_index ,"Today","is")
#add_to_corpus_index (corpus_index ,"keep","Cleaning")
#print(corpus_index)

corpus = "Today is Sunday. I stay at home and keep coding Today is Monday I stay at office and keep cleaning Today I stay at awake  "
corpus_index = []
add_all_to_corpus_index (corpus_index , corpus)
print(corpus_index)
lookup(corpus_index ,"and")


