n = int(input("Enter the number of iterations: "))
positive_list = []
negative_list = []
count_of_positives = 0
sum_negatives = 0

for iteration in range(n):
    number = int(input("Enter number: "))
    if number > 0:
        positive_list.append(number)
        count_of_positives += 1
    else:
        negative_list.append(number)
        sum_negatives += number
        
print(positive_list)
print(negative_list)
print("Count of positives: {count_of_positives}")
print("Sum of negatives: {sum_negatives}")
