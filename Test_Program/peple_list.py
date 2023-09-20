
# peple = [["supapatr","choochaisri",30] , ["Somchai","Python",22] , ["Thongchai","Java",42] ,["Thana","C",15] , ["Nat","Ruby",20]    ]
# for i in range(len(peple)-1):
#     if peple[i] =="Somchai":
#         print(peple[i+1])
        
    
                                                  
peple = [["supapatr","choochaisri",30] , ["Somchai","Python",22] , ["Thongchai","Java",42] ,["Thana","C",15] , ["Nat","Ruby",20]    ]
for i in range(len(peple)-1):
    
    if peple[i][0].lower() =="thongchai" :
         se1 = peple[i][2]
         print(se1)
        
    if peple[i][0].lower() =="somchai" :
         se2 = peple[i][2]
         print(se2)
         
         
print(abs(se1-se2))
         
           
                                                  
                                                  