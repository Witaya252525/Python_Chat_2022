
def find_next_word (text,word,start_pos):
    text = text[text.find(word,start_pos) + len(word)+1:  ]
    next_word = text[   :text.find(" ")]
    print(text)
    print(next_word)
    start_pos = text.find(" ") + 1

    return text ,start_pos







text = "Today is Sunday. I stay at home and keep coding . Today is Monday. I stay at office and keep cleaning but still keep singing . "
start_pos = 0
word = "keep"


text,start_pos = find_next_word (text , word , start_pos)
text,start_pos = find_next_word (text , word , start_pos)
text,start_pos = find_next_word (text , word , start_pos)

