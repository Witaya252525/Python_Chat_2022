text = " Today is Sunday I stay at home and keep coading Today is Monday I stay at office and keep cleaning"

splitted_text = text.split()
print(splitted_text)
print(len(splitted_text))

for i in range(1,11):
    if (i%2 == 0):
        print(i)


names = ['adam','Joe','somchai','ton']  
for name in names:
    if name[0] == "s" :
        print(name)   
        break



for i in range(1,8):
    if (i%3 == 0):
        continue
    print(i)



