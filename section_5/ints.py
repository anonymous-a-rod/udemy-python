print("Enter three ints seperted by commas")
ints = input()

ints = ints.split(',')
a = int(ints[0])
b = int(ints[1])
c = int(ints[2])

result = a + b - c

print(result)