import random
list_item=["Rock","Paper","Sciessor"]
user=(input("Your turn !(Rock,paper,sciossor):"))
computer=random.choice(list_item)
print("Computer:",computer)

if user==computer:
    print("Match tie")
elif user=="Rock":
    if computer=="Paper":
        print ("computer win!")
    else:
        print("User win")
elif user=="Paper" :
    if computer=="Sciessor":
          print ("computer win!")
    else:
        print("user win!")

elif user=="Sciessor":
    if computer=="Rock":
          print ("computer win!")
    else:
          print("user win!")







