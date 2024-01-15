str1 = "python exercises practice solution"

words = str1.title().split()
result_str = ' '.join([word[:-1] + word[-1].capitalize() if len(word) > 1 else word.capitalize() for word in words])

print(result_str)
