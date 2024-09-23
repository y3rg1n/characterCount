message = "A practical programming course for office workers, academics, and administrators who want to improve their productivity."
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1


print(count)
