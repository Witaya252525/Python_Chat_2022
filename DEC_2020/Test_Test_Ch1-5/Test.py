
# text = "Today is Sunday. I stay at home and keep coding.  Today is Monday. I stay at office and keep cleaning but stills keep eating."
# word = "keep"
# start_pos = 0
# text  = text[text.find( word ,start_pos)+len(word)+1: ]
# print(text)
# next_word = text[   :text.find(" ")]
# print(next_word)


# start_pos = text.find(" ") +1
# text  = text[text.find(word,start_pos)+len(word)+1   : ]
# print(text)
# next_word = text [   :text.find(" ") ]
# print(next_word)


def find_nextword(text, start_pos, word):
    if text.find(" ")!= -1:
        text = text[text.find(word, start_pos)+len(word)+1:]
        next_word = text[:text.find(" ")]
        print(next_word)
        print(text)
        start_pos = text.find(" ")+1
        return text, start_pos
    


    else:
        next_word = text
        start_pos = -1 
        return text, start_pos





text = "Today is Sunday. I stay at home and keep coding.  Today is Monday. I stay at office and keep cleaning but stills keep eating."
start_pos = 0
word = "keep"


text, start_pos = find_nextword(text, start_pos, word)
text, start_pos = find_nextword(text, start_pos, word)
text, start_pos = find_nextword(text, start_pos, word)