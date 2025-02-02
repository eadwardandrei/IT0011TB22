input_string = input("Input a string: ")

vowels = consonants = spaces = others = 0
vowel_set = "AEIOUaeiou"

for char in input_string:
    if char.isalpha():
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1

print(f"\nVowels: {vowels} \nConsonants: {consonants} \nSpaces: {spaces} \nOther characters: {others}")
