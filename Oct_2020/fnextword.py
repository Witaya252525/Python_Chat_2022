
def find_next_word(text,word,start_pos):
    text = text[text.find(word,start_pos)+len(word)+1: ]
    next_word = text[  :text.find(" ")]
    print(next_word)
    start_pos = text.find(" ") +1
    return text,start_pos
    



start_pos = 0
text= " Today is Sunday. I stay at home and keep coding . Today is Monday . I stay at office and keep cleaning but stills keep doing . "
word = "keep"
text,start_pos = find_next_word(text ,word ,start_pos)
text,start_pos = find_next_word(text ,word ,start_pos)
text,start_pos = find_next_word(text ,word ,start_pos)
