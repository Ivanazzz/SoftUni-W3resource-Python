from math import floor

best_word = ""
best_word_points = 0

while True:
    points = 0
    word = input()
    if word == "End of words":
        break
    for i in range(len(word)):
        points += ord(word[i])
    if word[0].lower() in "aeiouy":
        points *= len(word)
    else:
        points = floor(points / len(word))
    
    if points > best_word_points:
        best_word_points = points
        best_word = word

print(f"The most powerful word is {best_word} - {best_word_points}")