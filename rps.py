import random
print('ROCK PAPER SCISSORS game rules are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")
 
while True:
     
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice=int(input("Enter your choice :"))
    while choice > 3 or choice <1:
      choice=int(input('Enter a valid choice please ☺'))
    if choice == 1:
        choice_name= 'Rock'
    elif choice == 2:
        choice_name= 'Paper'
    else:
        choice_name= 'Scissors'
    print('User choice is \n',choice_name)
    comp_choice = random.randint(1,3)
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
    print("Computer choice is \n", comp_choice_name)
    print(choice_name,'Vs',comp_choice_name)
    if choice == comp_choice:
        print('Its a Draw\n',end="")
        result="DRAW"     
    if (choice==1 and comp_choice==2):
        print('paper wins\n',end="")
        result='papeR'
    elif (choice==2 and comp_choice==1):
        #print('paper wins\n',end="")
        result='Paper'
         
       
    if (choice==1 and comp_choice==3):
        #print('Rock wins\n',end= "")
        result='Rock'
    elif (choice==3 and comp_choice==1):
        #print('Rock wins\n',end= "")
        result='rocK'
         
    if (choice==2 and comp_choice==3):
        #print('Scissors wins\n',end="")
        result='scissor'
    elif (choice==3 and comp_choice==2):
        #print('Scissors wins\n',end="")
        result='Rock'
    if result == 'DRAW':
        print("Its a tie>")
    if result == choice_name:
        print("you won the game")
    else:
        print("you loss the game")
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans =='n':
        break
print("thanks for playing")