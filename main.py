import random
import time

separator = "-" * 58 

def gen_random_num() -> str:
     """Generates random number from 1 to 9 and control whether the number 
     starts with 0 and whether the digit does repeat.
     """
     sample = list(range(10))
     while True:
          random_number = random.sample(sample, 4)
          if random_number[0] != 0:
               #now changing list to int
               random_number = int(''.join(str(digit) for digit in random_number)) 
               return str(random_number)

def user_random_number() -> str | None:
     """Take the input from the user and controls whether the number is digit, 
     has the right lenght and starts with 0 - or, whether the input is 'end' 
     and terminate the program.
     """
     while True:
          user_guess = input("Enter your number: \n")
          if user_guess.lower() == "end":
               print("Have a nice day.")
               return None
          elif not user_guess.isdigit():
               print("Wrong input. Try again.")
               continue
          elif len(user_guess) != 4:
               print("You didn't entered 4-digit number. Try again.")
               continue
          elif user_guess[0] == "0":
               print("Your number starts with 0. Try again.")
               continue
          if len(set(user_guess)) != len(user_guess):
               print("Your number has the same digit/s. Try again.")
               continue
               
          return user_guess

def play_again() -> bool: 
     """Ask user if he wants to play again """    
     while True:
          new_game = input("Do you want to play again? Yes/No: \n")
          if new_game.lower() == "no":
               return False
          elif new_game.lower() == "yes":
               return True
          else:
               print("Wrong input. Enter yes or no.")

def play_game():
     """Runs the game Cows and bulls """
     start_time = time.time()

     random_pc_number = gen_random_num()
     user_guess_number = user_random_number()

     guess = 0
     
     while True:
          bull = 0
          cow = 0
          guess += 1
                    
          for x,y in zip(user_guess_number, random_pc_number):
               if x == y:     
                    bull += 1
                                   
          for i, x in enumerate(user_guess_number):
               if x in random_pc_number and x != random_pc_number[i]:
                    cow += 1
                 
          res_bull = "bull" if bull == 1 else "bulls"
          res_cow = "cow" if cow == 1 else "cows" 

          print(separator)
          print(cow, res_cow, bull, res_bull) 
          print(separator)

          if bull == len(user_guess_number):
               end_time = time.time()
               minutes = round((end_time - start_time)/60,2)
               print(
                    f"Yes! You've guessed the right number! You've won.\n"        
                    f"Number of your guesses: {guess}. \n" 
                    f"You've guessed the right answer in {minutes} minutes.\n", 
                    separator
               )
               break
                    
          user_guess_number = user_random_number()
          if user_guess_number is None:
               break

if __name__ == "__main__":
     print(separator)
     print(
          "Hello, friend. I've generated a 4-digit number for you. :) \n"
          "Let's play Cows and bulls. "
          "/If you don`t want to play, enter 'end'./"
          )
     print(separator)
     
     while True:
          play_game()
          if not play_again():
               print("Have a nice day.")
               break
