def add_list(corpus_index, corpus):
 
     splitted_text = corpus.split()   
     for i in range((len(splitted_text)-1)):
           word =splitted_text[i] 
           next_word = splitted_text[i+1]
           add_all_corpus_index (corpus_index,word ,next_word)
           



def add_all_corpus_index(corpus_index,word,next_word):
    for el in corpus_index:
        if el[0] == word :
            el[1].append(next_word)
            return
            
    corpus_index.append([word,[next_word]])

  


        


            


     


corpus_index = []
corpus = " Today is Sinday  I stay at home and keep coding Todau is Monday I stay at office and keep cleaning Today I stay awake "
add_list(corpus_index,corpus)



# print(corpus_index)
# print(lookup(corpus_index ,"stay"))
# print(lookup(corpus_index ,"is"))