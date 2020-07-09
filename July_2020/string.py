


# a = '3'
# b = 5
# print("This is %s and %d"  %(a,b))


# s = "Hello World"
# for i in range(len(s)):
#     if s[i] =="W":
#         print(s[i:])



text = "Today is Sunday. I stay at home and keep coding. "
word ="keep"
text= text[text.find(word )+ len(word)+1 : ]
next_word = text[ :text.find(" ")]
print(next_word)