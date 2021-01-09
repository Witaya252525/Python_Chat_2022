
def findtext (text,word):
    bu = [ ]
    splitted_text = text.split()
    print(splitted_text)
    for i in range (len(splitted_text)-1):
        
        if splitted_text[i] == word :
            next_word = splitted_text[i+1]
            bu.append(next_word)
            # print(bu)
    return print(bu)       
           



text = " Today is Sunday I stay at keep witaya home and keep coding today is Monday I stay at office and keep cleaning"
word = "keep"
findtext (text,word)