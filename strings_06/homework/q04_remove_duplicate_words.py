

# Given sentence
input_sentence = 'Hello world Python is great Python'

# Split the sentence into a list of words
words = input_sentence.split()

# Create a list to store unique words
unique_words = []

# Iterate through the words in the original list
for word in words:
    # If the word is not already in the unique_words list, add it
    if word not in unique_words:
        unique_words.append(word)

# Join the unique words back into a string
output_sentence = ' '.join(unique_words)

# Print the result
print("Original Sentence:", input_sentence)
print("Sentence without Duplicates:", output_sentence)
