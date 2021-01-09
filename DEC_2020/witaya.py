

def find_nextword(text,word,start_pos):
    if text.find(word) != -1 :
        text = text[text.find(word,start_pos)+len(word)+1  :    ]
        print(text)


        if text.find(" ") != -1 :
            next_word = text[     :   text.find(" ")]
            print(next_word)
            start_pos = text.find(" ")+1


        else:

            next_word = text
            start_pos = -1



        return text , start_pos



    else:

        print("NO NO")
        return " " ,-1        







# text ,start_pos = find_nextword (text,word,start_pos)
# text ,start_pos = find_nextword (text,word,start_pos)
# text ,start_pos = find_nextword (text,word,start_pos)
def find_all(text,word):
    start_pos = 0
    while start_pos != -1 :
        text ,start_pos = find_nextword (text,word,start_pos)



# start_pos = 0
# word = "keep"
text = "Today is sunday I stay at home and keep coding to day i stay akake and keep learning what is going on and keep doing go to the school and keep study"        
find_all (text , "keep")