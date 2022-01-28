n = int(input("Enter number: "))
key_word = input("Enter key word: ")
text_list = []
text_key_word_list = []

for i in range(n):
    text = input("Enter text: ")
    text_list.append(text)
    if key_word in text:
        text_key_word_list.append(text)

print(text_list)
print(text_key_word_list)