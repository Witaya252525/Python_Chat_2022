

# text = 'Today is Sunday. I stay at home  and keep coding  Today is Monday I stay at office and keep cleaning '
# spitted_text = text.split()
# print(spitted_text)
# for so in spitted_text:
#        print(so)


# for i in range(1 , 11):
#        if (i%2) == 0:
#               print(i)


def find_all(text, word):
    next_word_list = []
    spitted_text = text.split()
    for i in range((len(spitted_text))-1):
        if spitted_text[i] == word:
            next_word_list.append(spitted_text[i+1])

    return print(next_word_list)


text = "Today is sunday I stay at home and keep coding to day i stay ake and keeop eating  and keep learning what is going on and keep doing go to the school and keep study"
word = 'keep'
find_all(text, word)

