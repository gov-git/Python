# Split function for filtering
arn = "arn:aws:iam:123456789012:user/johndoe"

print(arn.split("/")[1])

# Upper or Lower case conversion
name = "Govardhan"
print(name.upper())
print(name.lower())

# Concatination:
str1 = "Hellow"
str2 = "World"
result = str1 + " " + str2
print(result)

# String varaiable examples: 
text = "I am a DevOps Engineer"
length = len(text)
print("The length of senetence is:", length)

new_text = text.replace("I am", "I'm")
print("Modified text: ", new_text)

words = text.split()
print("Words:", words)

stripped_text = text.strip()
print("Stripped text:", stripped_text)

substring = "a"
if substring in text:
    print(substring, "found in the text")

# Float variable examples:
