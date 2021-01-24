import random
sides = ["tail", "head"]
def flip():
    return random.choice(sides)
result = flip()
print(result)
