hash_table = dict(a=15 ,b=2 ,c=10)
max_key = " "
max_val = 0
for k,v in hash_table.items():
      if v > max_val :
            max_val = v
            max_key = k                                            

print(f' Max key is {max_key} The value is  ==>  {max_val} ')