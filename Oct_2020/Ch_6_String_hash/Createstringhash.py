#assign hashtable
#add hash value
# add to hash table


def create_hashtable(size):
    hash_table = []
    for i in range(size):
        hash_table.append(None)
    print(hash_table)
    return hash_table


def find_hashed_value (key,hash_table):
    hashed_value = 0
    for char in key :
        hashed_value += ord(char) 
    hashed_value = hashed_value % len(hash_table)
    return hashed_value


def add_all_to_table (key,value,hash_table):
    slot = find_hashed_value(key,hash_table)
    hash_table[slot] = [key,value]
    print(hash_table)
    return hash_table

    



hash_table = create_hashtable(10)
add_all_to_table ("witaya",12,hash_table)
add_all_to_table ("witaya",45,hash_table)
add_all_to_table ("chaison",45,hash_table)