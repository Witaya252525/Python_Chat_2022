
def find_next_word(text,word,start_pos):
    
    if text.find(word, start_pos) != -1:

        text = text[text.find(word, start_pos) + len(word)+1:]

        if text.find(" ")!= -1:
            next_word = text[:text.find(" ")]
            start_pos = text.find(" ")+ 1
            print(next_word)

        else:

            next_word = text
            start_pos = -1
            print(next_word)
            
        return text ,start_pos

    else:
        print(" ")
        return " ", -1


text = "Today is Sunday i stay at home and keep coding Today is Monday  I stay at office and keep cycling but still keep playing i go to bangkok to keep motivation "
word = "keep"
start_pos = 0
while start_pos !=-1 :
    text,start_pos = find_next_word(text,word,start_pos)
    
print("YOU are Awesome Man")