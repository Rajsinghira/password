import random



comp=("Computer: stone(s) paper(p) scissors(sc)")
print(comp)

r = random.randint(1,3)
if r==1:
  comp=='s'
elif r==2:
  comp=='p'
elif r==3:
  comp=='sc'

you= input("You: stone(s) paper(p) scissors(sc)")


def Win(comp, you):
  if comp==you:
    return None
  
  
  elif comp=='s':
    if you=='p':
      return True
    if you=='sc':
      return False

  elif comp=='p':
    if you=='sc':
      return True
    if you=='s':
      return False
      
  elif comp=='sc':
    if you=='s':
      return True
    if you=='p':
      return False
      
      
a=Win

if a==None:
  print("Game is Tie")
elif a==True:
  print("You Won")
elif a==False:
  print("You Loss")


print(a, r)
print(f"Computer Choose:- {comp}")
print(f"You Choose:- {you}")
