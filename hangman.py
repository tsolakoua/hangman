import random

words_pool = ("dog", "cat", "programming", "school", "car")
lives = 5
word = random.choice(words_pool)
print (word[0]+((len(word)-2)*"_")+word[-1])