import random
import hangmanlives
name=input("Enter your name:")
print("BEST OF LUCK!",name)
print("Let's play")

#declare list of words
words=['apple','mango','potato','orange','onion','tomato','capsicum']

#declare lives
lives=7

# To generate random words
selected_word=random.choice(words)
print("guess the letter")
#to store guessed letter
guesses=[]
#To print empty spaces for the chosen word
for i in range(len(selected_word)):
    guesses += '_'
print(guesses)

game_over = False

while not game_over:
    # get input from user
    find_letter = input("Guess the letter:")

    for position in range(len(selected_word)):
        letter = selected_word[position]
        if letter == find_letter:
            guesses[position]=find_letter
            print(letter)
    print(guesses)


    if find_letter not in selected_word:
      lives -= 1
      print("wrong")
      print("You have",+lives,"more guesses")
      if lives==0:
        game_over = True
        print("you loose")
      print(hangmanlives.life_of_Hangman[lives])

    if '_' not in guesses:
        print("You Won")
        print("the word is:",selected_word)
        break