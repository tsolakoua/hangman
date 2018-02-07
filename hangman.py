import random

def create_table(word):
		return list((word[0]+((len(word)-2)*"_")+word[-1]))

def generate_word():
	words_pool = ("dog", "cat", "programming", "school", "car", "chinese", "food", "analysis", "structure")
	return random.choice(words_pool)

def play_game(word, table, lives): 
	print (table)
	while lives > 0:
		print ("Tries left: ", lives)
		print (table)
		guess = input()
		missed_letter = 0
		for i in range(len(word)):
			if guess == word[i]:
				table.pop(i)
				table.insert(i, guess)
				if "_" not in table:
					print(word)
					print("You won!")
					return
			else: 
				missed_letter = missed_letter + 1
				if missed_letter == len(word):
					lives = lives - 1
					if lives == 0:
						print ("You Lost...")
						print (("The word is ")+ word)
						break

lives = random.randint(5, 8)
word = generate_word()
table = create_table(word)
play_game(word, table, lives)
