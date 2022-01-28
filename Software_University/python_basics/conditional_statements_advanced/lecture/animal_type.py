animal_type = input("Enter the animal type: ")

if animal_type == "dog":
    print("mammal")
elif animal_type == "crocodile" \
    or animal_type == "tortoise" \
    or animal_type == "snake":
    print("reptile")
else:
    print("unknown")