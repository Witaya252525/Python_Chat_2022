


# def add_to_corpus_index(key,next_word,corpus_index):
#     if key not in corpus_index:
#        corpus_index[key] = {next_word:1}
             
#     else:
#        if next_word in corpus_index[key]:
#           corpus_index[key][next_word]  +=  1
 
#        else:

#           corpus_index[key][next_word]  =  1     


# def init_corpus_stat (corpus_index ,corpus):
#        splitted_text = corpus.split()
#        for i in range(len(splitted_text)-1) :
#               current_word = splitted_text[i] 
#               next_word =  splitted_text[i+1]  

#               add_to_corpus_index(current_word, next_word ,corpus_index)









# corpus = ' Today is Sunday. I stay at home  and keep coding.Today is Monday. I stay at office and keep cleaning . Today I stay awake'
# corpus_stat ={}
# # add_to_corpus_index ('Today','is',corpus_index)
# # add_to_corpus_index('is','Sunday',corpus_index)
# # print(corpus_index) 
# # add_to_corpus_index ('Today','is',corpus_index)   
# # add_to_corpus_index ('Monday','is',corpus_index)
# # add_to_corpus_index ('I','stay',corpus_index)   
# # add_to_corpus_index ('I','witaya',corpus_index)   
# init_corpus_stat (corpus_stat, corpus)
# print(corpus_stat) 


hash_table = {'a':15 , 'b':2  ,'c':10}

max_key = ' '
max_val = 0
for k ,v in hash_table.items():
       if v > max_val :
              max_key = k
              max_val = v

print (max_key + ':' + str(max_val)  ) 
       
hash_table = {'a':15 , 'b':30  ,'c':10}
print(max(hash_table ,key = hash_table.get))











