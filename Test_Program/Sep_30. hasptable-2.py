# index = ["hello" , "The" ,"Today",'good']
# search = "Today"

# for el in  index :
#    if el == search:
#       print(el)


def string_hash(key, hash_table):
    hashed_value = 0
    for char in key:
        hashed_value += ord(char)
        hashed_value = hashed_value % len(hash_table)
    return hashed_value


def add_to_hashtable(key,value, hashed_value):
    slot = string_hash(key, hash_table)
    hash_table[slot] = [key,value]
    return print(hash_table)


def create_hash_table(size):
    hash_table = []
    for i in range(size):
        hash_table.append("None")

    return hash_table


def lookup(key,hash_table):
    slot = string_hash(key, hash_table)
    for el in range(len(hash_table)-1):
        if hash_table[slot] != "None":
            va= string_hash(key, hash_table)         
            return hash_table[va][1]

    return None



hash_table = create_hash_table(10)
print(hash_table)
# print(string_hash("witaya",hash_table))
# print(string_hash("Sunday",hash_table))
add_to_hashtable("Seagate",49, hash_table)
add_to_hashtable("witaya",34, hash_table)
add_to_hashtable("punapat",23, hash_table)
add_to_hashtable("NKP","Hello world", hash_table)
print(lookup('Autoboy',hash_table))
print(lookup ("witaya",hash_table))
print(lookup ("Seagate",hash_table))