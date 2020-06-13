
def find_next_word(text ,word ,start_pos):
    word_pos = text.find(word,start_pos)
    if (word_pos != -1 ) :
        text = text[word_pos+len(word)+1 :  ]
        
        if (text.find(" ") != -1):
            next_word = text[   : text.find(" ")]
            start_pos = text.find(" ") +1
            print(next_word)
            print(text)
            return text , start_pos
        else:
            next_word = text  
            print(next_word)
            start_pos = -1
            return text , start_pos


    else:
        # print(" WITAYA ")
        return " " , -1





def find_all(text ,word):
    start_pos = 0
    text = "Today is Sunday. I stay at home and keep coding .Today I stay at office and keep learning today is monday I stay at home and keep love "
    word = "keep"
    while start_pos != -1 :
        text,start_pos = find_next_word (text,word,start_pos)


text = "Today is Sunday. I stay at home and keep coding .Today I stay at office and keep learning today is monday I stay at home and keep love "
word = "keep"
find_all(text,word)

'''
text,start_pos = find_next_word (text,word,start_pos)
text,start_pos = find_next_word (text,word,start_pos)
text,start_pos = find_next_word (text,word,start_pos)
'''