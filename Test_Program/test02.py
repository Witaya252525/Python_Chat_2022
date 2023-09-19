

# def get_triangle_area(height,base_width):
#     area = ( 0.5*height *base_width )
#     return print (area)


# get_triangle_area (20,20)

# def get_area (pi,radius):
#     print("in function")
#     print(" pi = %0.4f ,radius = %d" %(pi,radius))
#     return pi*(radius**2)

# pi=3.1433
# radius =3
# area = get_area (3.1416,5)
# print("after  function")
# print(" pi = %0.4f ,radius = %d" %(pi,radius))

def find_next_word(text, word, start_pos):
    # text = text[text.find(word,start_pos) +len(word)+1  : ]
    # next_word = text[  :text.find(" ")]
    # print(next_word)

    if text.find(word, start_pos) != -1:
        text = text[text.find(word, start_pos) + len(word)+1:]


        if text.find(" ") != -1:
            next_word = text[:text.find(" ")]
            start_pos = text.find(" ") + 1
            print(next_word)

        else:

            next_word = text
            start_pos = -1
            print(next_word)
            
        return text ,start_pos









    else:
        print(" ")
        # return "" , -1

    return text, start_pos


start_pos = 0
text = "Today is Sunday i stay at home and keep coding Today is Monday  I stay at office and keep cycling but still keep playing."
word = "keep"
text, start_pos = find_next_word(text, word, start_pos)
text, start_pos = find_next_word(text, word, start_pos)
text, start_pos = find_next_word(text, word, start_pos)
