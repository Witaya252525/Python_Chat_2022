


# score = 40
# grade = "A" if score >=80 else 'B' if score >=70 else "Fail"
# print(grade)


# # grade ="FFFFFDCBAAAA"
# score = int(input("Please input your scoren   == "))
# # print(grade[score//10])
# print("Error") == True if  (score >= 101 or score < 0) else print("FFFFFDCBAAAA"[score//10])


# wit =["+" if i > 5 == True  else "__"  for i in range(1,10)]
# print(wit)


students = [

{'name':"bob" , "score" :42},
{'name':"Kelly" , "score" :58},   
{'name':"Austin" , "score" :99},
{'name':"kyly" , "score" :31}

]

outcome = []
for student in students:
    if student['score'] > 50 :
        outcome.append(f" {student['name']} pass the exsam with {student['score']}")
    else:
        outcome.append(f" {student['name']} Fail the exsam")

print(outcome)


witaya = [(f" {student['name']} pass the exsam with {student['score']}") if student['score'] > 50 else (f" {student['name']} Fail the exam") for student in students]
print(witaya)
