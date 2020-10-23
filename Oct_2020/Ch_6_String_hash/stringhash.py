def string_hash(key ,hash_table):
    hashed_value = 0
    for char in key:
        hashed_value+=ord(char)
        hashed_value = hashed_value % len(hash_table)

    return hashed_value




# print(string_hash('iataua') )   
# print(string_hash('chaison') )  

hash_table = ['hello','None','sunday','None']
print(string_hash('good',hash_table))
print(string_hash('witayachai',hash_table))