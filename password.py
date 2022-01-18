
   
d = input("Today date: " )

s = input("subject of holiday: ")
de = input("Details for holiday: ")
n = input("student name: ")
r = input("Student Roll number: ")
            



appl ='''To,
      The Principal
      Eklavya Education Complex
      Palanga Parsa Patna-53
              
      Date = <|DATE|>
      Subject=<|SUBJECT|>
              
      Dear sir
      I beg to say that I am student of class 8. <|details|>.
      
      
      I request you to please give me small holiday.
                      
      Your's faithful
      Name= <|name|>
      Class=8
      Roll=<|roll|> '''
                      
                    
                      
appl = appl.replace("<|DATE|>", d)
appl = appl.replace("<|SUBJECT|>", s)
appl = appl.replace("<|details|>", de)
appl = appl.replace("<|name|>", n)
appl = appl.replace("<|roll|>", r)
           
print(appl)