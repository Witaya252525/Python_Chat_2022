# s = "Witaya chaisin im working at Korat"
# print(s[2:5])
# print(s.find("im"))
# print(s[15])

start_pos = 0
text = "Today is Sunday i stay at home and keep coding Today is Monday  I stay at office and keep cycling but still keep playing."
word = "keep"
text = text[text.find(word,start_pos) +len(word)+1  : ]
print(text)
next_word = text[  :text.find(" ")]
print(next_word)


start_pos = text.find(" ")+1
text = text[text.find(word,start_pos) +len(word)+1  : ]
print(text)
next_word = text[  :text.find(" ")]
print(next_word)
    

start_pos = text.find(" ")+1
text = text[text.find(word,start_pos) +len(word)+1  : ]
print(text)
next_word = text[  :text.find(" ")]
print(next_word)        

        
    