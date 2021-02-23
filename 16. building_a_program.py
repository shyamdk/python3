def sentence_marker(phrase):
    inter = ('How', 'Where', 'Why', 'What')
    capitalized = phrase.capitalize()
    if phrase.startswith(inter):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)    

inputs = []
while True:
    userinput = input("Say something:")
    if userinput ==  "\end":
        break
    else:
        inputs.append(sentence_marker(userinput))

print(" ".join(inputs))
