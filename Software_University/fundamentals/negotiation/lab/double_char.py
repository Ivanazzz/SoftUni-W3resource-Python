word = input("Enter word: ")
double_word = ""

for i in range(len(word)):
    double_word += word[i] * 2
print(double_word)