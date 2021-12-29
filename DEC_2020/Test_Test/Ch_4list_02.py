


def find_all (text,word):
    next_word_list = []
    splitted_text = text.split()
    for i in range (len(splitted_text)-1):
           if (splitted_text[i] == word):
                  next_word_list.append(splitted_text[i+1])
    return next_word_list 



text = ' Today is Sunday I stay at home and keep coding Today is Monday I stay office and keep cleaning  and also keep witaya'     
result = find_all (text , "keep")
print(result)    