
def create_hash_table(size):
    hash_table = []
    for i in range(size) :
        hash_table.append(None)
    print(hash_table)
    return hash_table     


def string_hash(key,hash_table):
    hashed_value = 0
    for char in key:
        hashed_value+=ord(char)
        hashed_value = hashed_value%len(hash_table)
    return hashed_value


def add_to_hash_table(key,hash_table):
    slot = string_hash(key,hash_table)
    hash_table[slot] = key


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
        return slot








hash_table = create_hash_table(10)
print(hash_table)
add_to_hash_table("witaya",hash_table)
add_to_hash_table("chaison",hash_table)
add_to_hash_table("coding",hash_table)
print(hash_table)
print(lookup('siam',hash_table))
print(lookup('chaison',hash_table))