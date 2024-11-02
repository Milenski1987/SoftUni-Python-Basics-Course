text = input()

score = 0

for char in text:
    if char == "a":
        score += 1
    elif char == "e":
        score += 2
    elif char == "i":
        score += 3
    elif char == "o":
        score += 4
    elif char == "u":
        score += 5

print(score)
