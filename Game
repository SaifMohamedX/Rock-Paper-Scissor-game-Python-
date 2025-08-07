"""
Hello everyone and welcome to my first project in the snake:)
"""
#? let's importing first
import random, time, os, platform
from termcolor import cprint, colored

def ClearScreen() -> None: 
    """
    This function to clear the screen and see whether the user is on Windows or not
    """
    
    if platform.system() == "Windows":
        os.system("cls")
        
    else:
        os.system("clear")
    
def Starting (seconds: int) -> None:
    """
    This function to make the game more funny and adding some features of time 
    num is the number of seconds
    """
    time.sleep(seconds)
    print("1")
    time.sleep(seconds * 2 / 3)
    print("2")
    time.sleep(seconds * 2 / 3)
    print("3")

    
if __name__ == "__main__":
    
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
        print("your choice: ", colored(player, "green", attrs = ["bold"]))
        print("computer choice: ", colored(computer, "red" , attrs = ["bold"]))
        
        def GameScore() :
            time.sleep(1)
            print(PlayerName,"'s score:",numPlayer1)
            time.sleep(1)
            print("computer score:",numPlayer2)
            time.sleep(1)
            print("=" * 100)
            
        #? If codes with delays to make it more real
        if player == computer :
            print(colored("draw", "white", attrs = ["bold"]) + ", ", colored(PlayerName, "green", attrs = ["bold"]), sep = "")
            time.sleep(1)
            GameScore()
            
        elif player == "paper" : 
            if computer == "rock" :
                print(colored("winner winner chicken dinner!", "blue", attrs = ["bold"]) + ", ", colored(PlayerName, "green", attrs = ["bold"]), sep = "")
                numPlayer1 += 1
                GameScore()
                
        elif player == "rock" : 
            if computer == "paper" :
                print(colored("loser", "light_red", attrs = ["bold"]) + ", ", colored(PlayerName, "green", attrs = ["bold"]), sep = "")
                numPlayer2 += 1
                GameScore()
                
        elif player == "scissor" : 
            if computer == "paper" :
                print(colored("winner winner chicken dinner!", "blue", attrs = ["bold"]) + ", ", colored(PlayerName, "green", attrs = ["bold"]), sep = "")
                numPlayer1 += 1
                GameScore()
                
        if player == "rock" : 
            if computer == "scissor" :
                print(colored("winner winner chicken dinner!", "blue", attrs = ["bold"]) + ", ", colored(PlayerName, "green", attrs = ["bold"]), sep = "")
                numPlayer1 += 1
                GameScore()
                
        elif player == "scissor" : 
            if computer == "rock" :
                print(colored("loser", "light_red", attrs = ["bold"]) + ", ", colored(PlayerName, "green", attrs = ["bold"]), sep = "")
                numPlayer2 += 1
                GameScore()
                
        elif player == "paper" : 
            if computer == "scissor" :
                print(colored("loser", "light_red", attrs = ["bold"]) + ", ", colored(PlayerName, "green", attrs = ["bold"]), sep = "")
                numPlayer2 += 1
                GameScore()
                
        #todo Some codes for making it more funny
        elif player != choices :
            raise ValueError("Invalid Choice\nRun The code again and insert valid choices")
    
        user = input("do you wanna play again?[write yes or no]: ")
        if user.lower() == 'no' or user.lower() == 'n':
            print("=" * 100)
            time.sleep(1)
            print("thank you for playing our little game:)\nHAVE A NICE DAY!,", PlayerName)
            time.sleep(1)
            print(PlayerName,"final score: ",numPlayer1)
            print("computer final score: ",numPlayer2)
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
        
        print(f"You have played {Minutes_str} : {Seconds_str} Minutes, enjoy!")
        
    elif (End - Start) >= 3600 :
        
            print(f"You have played {Hours_str} : {Minutes_str} : {Seconds_str} Hours, enjoy!")
            
    else:   
            
        print(f"You have played {Seconds_str} seconds, enjoy!")
        
    time.sleep(0.5)
    print("#" * 100)
    cprint("This GAME is MADE by me (Saif Mohamed fathy)", "red", attrs = ["reverse"])
    print("#" * 100)

    time.sleep(14)
    Starting(0.9)
    ClearScreen()
    ending = "Thank you for playing our little game, I hope you like it!"
    for letter in ending:
        print(letter, end = '')
        time.sleep(0.1)
