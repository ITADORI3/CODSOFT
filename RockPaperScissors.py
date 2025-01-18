import random
from selectors import SelectSelector

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
game_images=[rock,paper,scissors]

user_choice=int(input("Enter your choice : 0 for rock, 1 for paper and 2 for scissor \n"))
if user_choice >=0 and user_choice <=2:
    print(game_images[user_choice])
# 0=rock 1=paper 2=scissors

computer_choice= random.randint(0,2)
print("Computer chose : ")
print(game_images[computer_choice])

if user_choice >=3  :
    print("You typed an invalid number")

elif user_choice >  computer_choice :
    print("You Win !!")

elif user_choice ==2 and  computer_choice==1 :
    print("You Win !!")

elif user_choice ==0 and  computer_choice==2 :
    print("You Win !!")

elif user_choice ==2 and  computer_choice==0:
    print("You Lost")

elif user_choice == computer_choice:
    print("Its a Tie")

elif  user_choice < computer_choice :
    print("You Lost")
