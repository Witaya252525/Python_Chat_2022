


def add_all_word(corpus_index,corpus):
     splitted_text = corpus.split()   
     for i in range((len(splitted_text)-1)):
           word =splitted_text[i] 
           next_word = splitted_text[i+1]
           add_corpus_index (corpus_index,word ,next_word)

    #  return print(corpus_index)



def add_corpus_index(corpus_index,word,next_word):
    for el in corpus_index:
        if el[0] == word :
            el[1].append(next_word)
            return 
            
    corpus_index.append([word,[next_word]])
 

  
def lookup(corpus_index , word):
     for el in corpus_index :
          if el[0] == word :
            witaya = el[1]
            return print(witaya)
            

 

          

   
    

corpus_index = []
corpus = " Today is Sinday  I stay at home and keep coding Todau is Monday I stay at office and keep cleaning Today I stay awake "
add_all_word(corpus_index,corpus)
print(corpus_index)
print("------------------------")
lookup(corpus_index , "is")

