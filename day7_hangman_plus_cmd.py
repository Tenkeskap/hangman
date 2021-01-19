
import random
from hangman_words import word_list
from hangman_art import stages, logo


game_on = True

#main game loop
while game_on:  
    print(logo)
    
    #select word that user will guess and initialize variables (located here to run again if player 
    #plays more than one rounds)
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    #this is used to turn the inside game round loop on and off as needed
    end_of_round = False
    #this is used to track when/if the player dies and the have something to link the hangman art to
    lives = 6
    #used to display which wletter
    incorrect_letters_list = []  
    #this is used to store status of mystery word and display it to the player    
    display = []

    #creating blanks for letters in the chosen word
    for _ in range(word_length):
        display.append('_')
    
    #this is outside the loop because it's a one-off hint to the user before the first guess.    
    print(f"Your word has {len(chosen_word)} letters")
    
    #game round loop starts
    while not end_of_round:
        guess = input("Guess a letter: ").lower()
        print('\n'*100) #this "clears" the screen
        print(logo)
        #If the user has entered a letter they've already guessed, print the letter and let them know.
        if guess in display:
            print("You've already guessed this letter.")

        #Check guessed letter and update display variable
        for position in range(word_length):
            letter = chosen_word[position]            
            if letter == guess:
                display[position] = letter

        #Check if user is wrong.
        if guess not in chosen_word:
            #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            incorrect_letters_list.append(guess)

            print(f"{guess} is not in the word. You lose a life.\n")

            lives -= 1
            if lives == 0:
                end_of_round = True
                print(f"You lose. The word was: {chosen_word}\n")

        #Join all the elements in the list and turn it into a String.
        incorrect_letters = ", ".join(incorrect_letters_list)
        print(f"You already tried: {incorrect_letters}\n\n")
        print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_round = True
            print("You win.")

        #display hangman art appropriate depending on number of lives remaining
        print(stages[lives])
    
    #if user wants another round, round repeats, if not, program exits
    choice = ''
    while choice not in ['y','n']:
        choice = input("Would you like to play again? (y, n)").lower()
        print('\n'*100)
        
    if choice == 'n':
        game_on = False