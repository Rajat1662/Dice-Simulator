import random


while True:
    print(f"Player 1st Number = : ", random.randrange(1, 7))
    d = input("\n\nClick to get number for PLAYER 2.\n& Press 'q' to exit the game.\n")
    if d == 'q':
        break
    print(f"Player 2nd Number = : ", random.randrange(1, 7))
    s = input("\nClick to get number for PLAYER 1.\n& Press 'q' to exit the game.\n")
    if s == 'q':
        break
