import string

song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
#acsii = string.ascii_letters
for letter in string.punctuation:
    song = song.replace(letter, '')

print(song.split())