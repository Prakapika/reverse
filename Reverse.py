Word = input("Enter a word to reverse: ")
for char in range(len(Word)-1, -1, -1):
   print(Word[char], end = " ")
print("\n")