import random

def choose():
    # List of words to choose from
    words = ['apple', 'giraffe', 'computer', 'sunshine', 'pyramid', 'jungle', 'exploration', 'adventure', 'marathon', 'universe']
    # Randomly select a word from the list
    pick = random.choice(words)
    return pick

def jumble(word):
    # Randomly shuffle the letters of the word to create a jumbled version
    jumbled = "".join(random.sample(word, len(word)))
    return jumbled

def thank(p1n, p2n, p1, p2):
    # Display final scores and thank the players
    print(f"{p1n}, Your score is: {p1}")
    print(f"{p2n}, Your score is: {p2}")
    print("Thanks for playing!")
    print("Have a nice day!")

def play():
    # Get player names
    p1n = input("Player 1, please enter your name: ")
    p2n = input("Player 2, please enter your name: ")
    
    # Initialize scores and turn
    pp1 = 0
    pp2 = 0
    turn = 0
    
    while True:
        # Choose a word and jumble it
        picked_word = choose()
        qn = jumble(picked_word)
        print("Jumbled word is:", qn)
        
        # Determine whose turn it is
        if turn % 2 == 0:
            print(f"{p1n}, your turn!")
            ans = input("What is your guess? ")
            if ans == picked_word:
                pp1 += 1
                print("Correct! Your score is:", pp1)
            else:
                print("Better luck next time!")
                
            turn += 1  
        else:
            print(f"{p2n}, your turn!")  
            ans = input("What is your guess? ")
            if ans == picked_word:
                pp2 += 1  
                print("Correct! Your score is:", pp2)
            else:
                print("Better luck next time!")
                
            turn += 1

        # Check if either player wants to quit the game
        if turn >= 10:  # Example condition: 10 rounds
            thank(p1n, p2n, pp1, pp2)
            break

# Start the game
play()
