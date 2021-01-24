import random
player_wins = 0
cpu_wins = 0
moves = ["rock", "paper", "scissors"]
while cpu_wins < 2 and player_wins < 2:
    p1 = input( "Player1 choice:" )
    p2 = random.choice(moves)
    if not(p1 == "paper" or p1 == "rock" or p1 == "scissors"):
        print("Invalid entry, exiting!")
        exit()
    print("Shoot!")
    if p1 == p2:
        print("Draw")
    elif (p1 == "rock" and p2 == "scissors") or (p1 == "paper" and p2 == "rock") or (p1 == "scissors" and p2 == "paper"):
        print(f"Player 1 {p1} beated CPU {p2}")
        player_wins += 1
    else:
        print(f"CPU {p2} beated Player 1 {p1}")
        cpu_wins += 1
if cpu_wins > player_wins:
    print("CPU won!")
else:
    print("Player1 wins")
