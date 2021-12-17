
def find_next_word (text,word,start_pos):

       if text.find(word ,start_pos) != -1 :

              text = text[text.find(word, start_pos)+len(word)+1   :  ]
             
              if text.find('') != -1:
                     Nextword = text[ :text.find(' ')]
                     start_pos =text.find(' ')+1 
                     print(Nextword)
                     return text ,start_pos

              else:
                     Nextword = text
                     start_pos = -1
                     return text ,start_pos

             
       
       else:
              print ( "Not found")
              return "not found" ,-1

              

def find_all(text,word):
       start_pos = 0
       while  start_pos != -1:
              text,start_pos  = find_next_word (text,word,start_pos)       
     




text = 'Today is Sunday. I stay at home ans keep coding  . Today is Momday . I Stay at office and keep cleaning but still  keep monitoring. '
word = 'keep'
#text , start_pos  = find_next_word (text ,word , start_pos)
#text , start_pos  = find_next_word (text ,word , start_pos)
#text , start_pos  = find_next_word (text ,word , start_pos)
find_all(text,'keep')