import string

song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

for letter in string.punctuation.replace("'", ""):
    song = song.replace(letter, '')
words = song.split()
for word in words:
    if word[0] == 'm':
        print(word.capitalize())
