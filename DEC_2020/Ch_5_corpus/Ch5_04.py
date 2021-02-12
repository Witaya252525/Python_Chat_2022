

def print_all_next_words(corpus_index ,word):
       for el in corpus_index :
              if el[0]==word:
                     print(el[1])


def add_to_corpus_index (corpus_index , word ,next_word):
       for el in corpus_index:
              if el[0] == word:
                     el[1].append(next_word)
                     return


       corpus_index.append([word ,[next_word]])              

def add_all_to_corpus_index(corpus,corpus_index):

        splitted_text = corpus.split()
        for i in range  (len(splitted_text)-1):
                      word = splitted_text[i]
                      next_word = splitted_text [i+1]
                      add_to_corpus_index (corpus_index ,word , next_word)



def lookup (corpus_index ,word):
       for el in corpus_index:
              if el[0] == word:
                     return el[1]
       return None

# corpus_index = [ ['keep' ,'coding' ,'cleaning'] , [ 'Today' ,'is' ,'witaya'] ]       
# print_all_next_words (corpus_index ,'keep')
# print_all_next_words (corpus_index ,'Today')

corpus = 'Today is sunday. I stay at home I you and keep cleaning to day is Monday I stay at office and keep joging  stay awake'
corpus_index = [ ]


# add_to_corpus_index (corpus_index ,"keep", "Cleaning")
# add_to_corpus_index (corpus_index ,"keep", "Learing")
# add_to_corpus_index (corpus_index ,"wit", "Learing")
# print_all_next_words(corpus_index ,'keep')
# print_all_next_words(corpus_index ,'wit')
add_all_to_corpus_index(corpus,corpus_index)
print(corpus_index)
print(lookup(corpus_index ,'I'))

