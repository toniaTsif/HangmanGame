"""
Hangman Game!

This programme reenacts the simple game of hangman. At first, it prints instructions for the game. 
Then it chooses a random word from a file filled with words. The player must guess within 15
attempts the chosen word. After he/she has completed the game, the player can choose to play
again or exit.
"""
import random

print("\nLet's play hangman!")
print("\nInstructions: A word will be randomly chosen. Then, you need to find the word guessing one letter at a time. Be careful: You have 15 attemps to find the word or else you will lose your head!")
print("\nNote that you must enter only letters, not numbers or symbols.")

play="y"
while(play=="y"):
    #Get a random word from a file
    with open("words.txt", "r") as file1:
        word = random.choice(file1.readlines())
        word = word.strip()
        print("\nA random word has been chosen.")
            
    file1.close()
    
    #Find the length of the chosen word and save word to an array   
    length = len(word)  
    for i in range(0,length):
        print("_", end=" ")
       
    print("\n")    
    
    #Initialization or lists    
    chosen_word=[]    
    found_list=[]
    for i in range(0,length):
        found_list.append('_')
        chosen_word.append('_')
        chosen_word[i]=word[i]
        
    guesses_list=[]
    for i in range(0,15):
        guesses_list.append('_')    
              
    count=0    
    while(count<15):         
        letter= input("What's your guess? ")
        if(letter==""):
            print("Please write a letter.")
            continue
        
        guesses_list[count]=letter[0]
        
        if(len(letter)==length and letter==word):
            print("\nWell done! You found the word!")
            break
        
        #Check if the letter has already been given as input
        for k in range(0,count):
            if(guesses_list[k]==letter[0]):
                print("You have already guessed this letter. Try another one.")
                count-=1
                break
        
        if((letter[0] >= 'a' and letter[0] <= 'z') or (letter[0] >= 'A' and letter[0] <= 'Z')):
            for i in range(0,length):
                if(chosen_word[i] == letter[0]):
                    found_list[i] = letter[0]
                    print(letter[0], end=" ")
                else:
                    print(found_list[i], end=" ")
        else:    
            print("Please type only letters. Try again.")
            continue
            
        #If user found the word, the game ends
        if("".join(chosen_word) == "".join(found_list)):
            print("\nWell done! You found the word!")
            print("The word is: %s!" %word)
            break
        
        print("\n")
        count+=1
        print("Attempt %d" %count)
        
    if(count==15):    
        print("You are out of attempts! The word was %s." %word)  
    play=input("Do you want to play again?(Answer 'y' for yes or 'n' for no.) ")
    while(play!='y' and play!='n'):
        play=input("Please answer 'y' for yes or 'n' for no. ")
        
print("\nThank you for playing. Bye!")

