import random

game = ["rock","paper","scissors"]
you = random.choice(game);
sys = random.choice(game);
print("Created by BroFarOps 9-2-2019\nRock Paper Scissors : \nYou: ", you,"\nSys: ", sys,"\n");
if you == sys: print("draw") 
elif you == "rock" and sys == "paper" or you == "paper" and sys == "scissors" or you == "scissors" and sys == "rock": print("You Lost")
elif you == "rock" and sys == "scissors" or you == "paper" and sys == "rock" or you == "scissors" and sys == "paper": print("You Win")
