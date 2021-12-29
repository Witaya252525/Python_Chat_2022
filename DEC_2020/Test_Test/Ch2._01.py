


text = " Today is Sunday. I stay at home and keep coding is king. "
word = 'keep'

text = text[text.find(word) + len(word)+1:  ]
print(text)
next_word = text[   : text.find(' ')]
print(next_word)