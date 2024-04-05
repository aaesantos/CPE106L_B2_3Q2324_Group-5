'''
**********LABORATORY 1 - POST LAB - PROGRAMMING PROBLEM 2  **********
CPE106L B2 Group 5

Members:
Claros, Angelica
Facal, Ma. Catherina
Santos, Angelica Anne

'''

import random

def getWords(file_name):
    # Expects a string as filename and opens the file then converts the list to a tuple
    words = list()
    with open(file_name, 'r') as file:
        for line in file:
            words.append(line.strip())

    return tuple(words)

def sentence():
    # Returns a sentence
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    # Returns a noun phrase.
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    # Returns a verb phrase.
    return random.choice(verbs) + " " + nounPhrase() + " " + \
        prepositionalPhrase()

def prepositionalPhrase():
    # Returns a prepositional phrase.
    return random.choice(prepositions) + " " + nounPhrase()

nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")
articles = getWords("articles.txt")

def main():
    # User input number of sentences to generate
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()

