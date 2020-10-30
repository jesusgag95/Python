# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('mimi', 6)
cat2 = Cat('Jerry', 700)
cat3 = Cat('Warui', 21)

# 2 Create a function that finds the oldest cat


def oldest_cat(*args):
    oldest = 0
    for cat in args:
        if cat.age >= oldest:
            oldest = cat.age
            cat_name = cat.name
    return oldest, cat_name


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest = oldest_cat(cat1, cat2, cat3)
print(
    f'The oldest cat is {oldest[0]} years old and the name of the cat is {oldest[1]}')
