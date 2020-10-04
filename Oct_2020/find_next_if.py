


def find_next_word(text,word,start_pos):

    if (text.find(word ,start_pos)) != -1:
        text = text[text.find(word,start_pos)+len(word)+1: ]

        if (text.find(" ")) != -1 :

                next_word = text[  :text.find(" ")]
                # print(next_word)
                start_pos = text.find(" ") +1

                # return text ,start_pos

        else:

                next_word = text
                # print(next_word)
                start_pos = -1

        print(next_word)
        return text ,start_pos

    else:

        print ('')
        return '' , -1





# start_pos = 0
# text,start_pos = find_next_word(text ,word ,start_pos)
# text,start_pos = find_next_word(text ,word ,start_pos)
# text,start_pos = find_next_word(text ,word ,start_pos)


def find_all(text,word):
    start_pos = 0
    while (start_pos != -1):             
           text,start_pos = find_next_word(text,word,start_pos)






text = " Today is Sunday. I stay at home and keep coding . Today is Monday . I stay at office and keep cleaning but stills keep doing . "
word = "keep"
find_all(text,word)