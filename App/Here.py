#Hello everyone and welcome to my first project in the snake:)
#?let's importing first
import random, time, os, platform

def ClearScreen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    
def Starting (num):
    time.sleep(num)
    print("1")
    time.sleep(num * 2 / 3)
    print("2")
    time.sleep(num * 2 / 3)
    print("3")
    
#?putting the choices we have here

choices = ["rock", "paper", "scissor"]

#?using input to with delaying
PlayerName = input("Please, insert your name: ").strip().capitalize()
Starting(0.9)
print("=" * 100)

#?Let the user know the choices

print("you have (rock or paper or scissor)")
numPlayer1 = 0
numPlayer2 = 0

Start = time.time()
#!LOOPING
while True:
    
    #? here the input for player
    player = input("pls, insert your choice : ").lower().strip()
    computer = random.choice(choices)
    print("your choice: ", player)
    print("computer choice: ", computer)
    
    def GameScore() :
        time.sleep(1)
        print(PlayerName,"'s score: ",numPlayer1, sep = "")
        time.sleep(1)
        print("computer score: ",numPlayer2)
        time.sleep(1)
        print("=" * 100)
        
    #? If codes with delays to make it more real
    if player == computer :
        print("draw" + ", ", PlayerName, sep = "")
        time.sleep(1)
        GameScore()
        
    elif player == "paper" : 
        if computer == "rock" :
            print("winner winner chicken dinner!" + ", ", PlayerName, sep = "")
            numPlayer1 += 1
            GameScore()
            
    elif player == "rock" : 
        if computer == "paper" :
            print("loser" + ", ", PlayerName, sep = "")
            numPlayer2 += 1
            GameScore()
            
    elif player == "scissor" : 
        if computer == "paper" :
            print("winner winner chicken dinner!" + ", ", PlayerName, sep = "")
            numPlayer1 += 1
            GameScore()
            
    if player == "rock" : 
        if computer == "scissor" :
            print("winner winner chicken dinner!" + ", ", PlayerName, sep = "")
            numPlayer1 += 1
            GameScore()
            
    elif player == "scissor" : 
        if computer == "rock" :
            print("loser" + ", ", PlayerName, sep = "")
            numPlayer2 += 1
            GameScore()
            
    elif player == "paper" : 
        if computer == "scissor" :
            print("loser" + ", ", PlayerName, sep = "")
            numPlayer2 += 1
            GameScore()
            
    #todo Some codes for making it more funny
    elif player != choices :
        print("error2103, pls choose a CORRECT WORD\nrun it again!")
        exit()
 
    
  
    
    user = input("do you wanna play again?[write yes or no]: ")
    if user.lower() == 'no' or user.lower() == 'n':
        print("=" * 100)
        time.sleep(1)
        print("thank you for playing our little game:)\nHAVE A NICE DAY!,", PlayerName)
        time.sleep(1)
        print(PlayerName,"final score: ", numPlayer1)
        print("computer final score: ", numPlayer2)
        break
    
    elif user.lower().strip() == "yes" or user.lower().strip() == 'y':
        continue
        
    else:
        print("ERROR 409, PLS RUN IT AGAIN!\nthank you for playing our little game:)\nHAVE A NICE DAY!", PlayerName)
        exit()
    
if numPlayer1 > numPlayer2:
        time.sleep(1) 
        print(PlayerName, "is the winner")
        
if numPlayer2 > numPlayer1:
        time.sleep(1) 
        print("sadly computer defeated you :(")
        
if numPlayer1 == numPlayer2:
            time.sleep(1) 
            print("no one won")

End = time.time()

#? Make them with decimal
Seconds = round((End - Start), 1)  
Minutes = round((End - Start) / 60, 0)
Hours = round((End - Start) / 3600, 0)

if (End - Start) >= 60:
    Seconds %= 60
    
if (End - Start) >= 3600:
    Minutes %= 60
    
#? Formatting
Seconds_str = f"{Seconds:04.1f}"  # Ensures at least 2 digits + 1 decimal
Minutes_str = f"{int(Minutes):02d}"
Hours_str = f"{int(Hours):02d}"


if (End - Start) >= 60 :
    
    print(f"You have played {Minutes_str} minutes, {Seconds_str} Seconds, enjoy!")
    
elif (End - Start) >= 3600 :
    
        print(f"You have played {Hours_str} hours, {Minutes_str} minutes, {Seconds_str} Seconds, enjoy!")
        
else:   
         
    print(f"You have played {Seconds_str} seconds, enjoy!")
    
#! "Copy rights", don't mess up with it :(
time.sleep(0.5)
print("#" * 100)
print("This GAME is MADE by me (Saif Mohamed fathy)\nThere are copy rights here, okay?")
print("#" * 100)

time.sleep(4)
Starting(0.9)
ClearScreen()
