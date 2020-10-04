
text = " Today is sunday. I stay at home and keep coding . "
word = "keep"


start_pos = 0
text = text[text.find(word , start_pos , )+len(word)+1  :   ]
print(text)
next_word = text[  : text.find( " ")]
print(next_word)
