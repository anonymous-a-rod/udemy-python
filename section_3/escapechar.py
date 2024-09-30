split_string = "This is a multi\n line string\n because the escape character"
print(split_string)

tabbed = "1\t2\t3\t4\t5\t6"
print(tabbed)

# escape char \
# single quotes ' '
# double quotes " "
# single and double are interchangable, including for string interpolation
# tripple quotes """ """ for spanning multiple line
# escape char can be used within a string to continue writing the string on the next line
# \\ to escape an escape

raw_string = r"\t\t\t\t\t"
print(raw_string)

print(type('str'))
print(type(123))
print(type(1.1))
print(type(True))