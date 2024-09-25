# Ask the user for their favorite word
word = input("What's your favorite word? ")

# Ask how many times they want to repeat it
repeat_count = int(input("How many times should we repeat it? "))

# Print the word that many times, separated by commas

output = f"{word}, " * (repeat_count -1) + word # 2 opció van ez meg a lenti
output = (f"{word}, " * (repeat_count))[:-2]
print(f"Here is your word repeated {repeat_count} times: {output}")