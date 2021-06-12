import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

obj=[rock,paper,scissors]
print("welcome to rock, paper, scissors!")
choices=int(input("enter any choice 0,1,2:"))
print("you've choosen:")
you=obj[choices]
print(you)
style=random.randint(0,2)
print("computer's choice:")
computer=obj[style]
print(computer)
if you==computer:
  print("its a tie!")
elif you>computer:
  print("you win!")
else:
  print("you lose!")    


  

