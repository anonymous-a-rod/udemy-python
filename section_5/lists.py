parts = ["part 1", "part 2", "part 3", "part 4", "part 5", "part 6", "part 7", "part 8"]

for part in parts:
    print(part)

print(parts[1])
print(parts[-1])
print(parts[0:2])
print(parts[:3])
print(parts[::2])

for number, part in enumerate(parts):
    print("{}: {}".format(number + 1, part))


data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for p in data:
    if "Flower" in p:
        flowers += [p]
    else:
        shrubs += [p]

print(flowers)
print(shrubs)

data.remove("Andromeda - Shrub")
print(data)

odd = [1, 3, 5]
even = [2, 4, 6]

odd.extend(even)

print(odd)

odd.sort(reverse=True)

print(odd)

words = ['e', 'EE', 'a', 'f']

print(sorted(words))

words.sort(key=str.casefold)

print(words)

list("ergerg")
numbers = list(range(0,11))
# new_numbers = list(numbers)
# new_numbers = numbers[:]
new_numbers = numbers.copy()

# id(numbers) != id(new_numbers)

del numbers[0:2]
print(numbers)

for index, value in enumerate(reversed(numbers)):
    print(value)


# join
# works on enumberables

# separator.join(iterable)

words = ["Hello", "world", "from", "Python"]
sentence = " ".join(words)
print(sentence)  # Output: "Hello world from Python"

# string.split(separator, maxsplit)

sentence = "Hello world from Python"
words = sentence.split()
print(words)  # Output: ['Hello', 'world', 'from', 'Python']

text = "one, two, three, four"
result = text.split(", ", 2)
print(result)  # Output: ['one', 'two', 'three, four']



