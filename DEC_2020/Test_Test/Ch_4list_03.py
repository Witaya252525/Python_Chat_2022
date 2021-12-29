


#def find_all (text,word):
#    next_word_list = []
#    splitted_text = text.split()
#    for i in range (len(splitted_text)-1):
#           if (splitted_text[i] == word):
#                  next_word_list.append(splitted_text[i+1])
#    return next_word_list 

def add_to_corpus_index (corpus_index , word ,next_word):
    for el in corpus_index:
         if el[0]  == word :
             el[1].append(next_word) 
             return

         
    corpus_index.append([word ,[next_word]])

           







corpus_index = []
add_to_corpus_index (corpus_index , "keep" , "coding")
add_to_corpus_index (corpus_index , "Today" , "is")
add_to_corpus_index (corpus_index , "keep" , "cleaning")
add_to_corpus_index (corpus_index , "keep" , "witaya")
print(corpus_index)




#text = ' Today is Sunday I stay at home and keep coding Today is Monday I stay office and keep cleaning  and also keep witaya'     
#result = find_all (text , "keep")
#print(result)    