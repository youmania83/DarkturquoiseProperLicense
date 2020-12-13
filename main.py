import random
Guessed_number=random.randint(1,30)
guesses=0
while guesses<9:
  user_guess=int(input("Enter your Guess :\n"))
  guesses+=1

  if user_guess>Guessed_number:
      print("your guess is too high enter lower number")
  
  elif user_guess<Guessed_number:
      print("your enter number is too low enter higher number")
 
    
  else:
        print("you have entered Correct number")
        print(f"you have Guessed number in {guesses} guesses")        
  
        break
  if guesses==9:
    print("Game Over you have used 9 Guesses")       
