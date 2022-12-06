import random, sys
wins = 0
losses = 0
ties = 0
while True:
    print("ROCK PAPER SCISSORS")
    print(f"{wins} wins, {losses} losses, {ties} ties")
    playerMove = input("Enter your playerMove: r, p, s or exit ").lower()
    if playerMove == 'r':
        print("ROCK versus..")
    elif playerMove == 'p':
        print("PAPER versus..")
    elif playerMove == 's':
        print("SCISSORS versus..")
    elif playerMove == 'exit':
        sys.exit
    
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

# Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1