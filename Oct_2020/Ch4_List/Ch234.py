

# x = 0
# for i in range(10):
#     x = x +1
#     print(" The number is %d " %x)

# s = "Hello World Wiataya"
# for i in range(len(s)):
#     print(s[i])



# text = 'Today is Sunday. I stay and keep witaya at home and keep coding '
# word = "keep"
# splitted_text = text.split()
# print(splitted_text)
# for i in range(len(splitted_text)):
#     if splitted_text[i] == word :
#         print(splitted_text[i+1])

def find_next_word(text,word,start_pos):
    
    if (text.find(word,start_pos) != -1) :
        text = text[text.find(word,start_pos) +len(word) + 1:    ]
        

        if text.find(" ") != -1 :
            next_word = text [     :  text.find(" ")]
            start_pos = text.find(" ") +1
            


        else:
            next_word = text
            start_pos = -1    

        print(next_word) 
        return text,start_pos
          

    else:

        print ("  ")
        return " " ,-1 


def find_all (text,word):
    start_pos = 0 
    while start_pos != -1 :
            text,start_pos = find_next_word(text,word,start_pos)

            if start_pos == -1 :
                break


# start_pos = 0 
text = "Today is Sunday I stay at home and keep coding Today is Monday I stay at offiece and keep cleaning but still keep coding "
word = "keep"
find_all (text,word)

