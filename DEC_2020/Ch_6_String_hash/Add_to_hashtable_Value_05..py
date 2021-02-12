
# add hash table emply size
def create_hash_table(size):
    hash_table = []
    for i in range(size) :
        hash_table.append(None)
    print(hash_table)
    return hash_table     


# change char to ord function
def string_hash(key,hash_table):
    hashed_value = 0
    for char in key:
        hashed_value+=ord(char)
    hashed_value = hashed_value%len(hash_table)
    return hashed_value



def add_to_hash_table(key,value,hash_table):
    slot = string_hash(key,hash_table) # find_hash_value
    hash_table[slot] = [key,value]


# def lookup(key,hash_table):
#     for i in range(len(hash_table)):
#         if hash_table[i] == key:
#             return i
#     else:
#         None

def lookup(key,hash_table):
    slot = string_hash(key , hash_table)
    if (hash_table[slot] == None):
        return None

    else:
        return hash_table[slot][1]





hash_table = create_hash_table(10)
print(hash_table)
add_to_hash_table("witaya",20,hash_table)
add_to_hash_table("chaison",30,hash_table)
add_to_hash_table("coding",'Chaison',hash_table)
print(hash_table)
print(lookup('siam',hash_table))
print(lookup('chaison',hash_table))