    # <QUESTION 1>

    # Given a word and a string of characters, return the word with all of the given characters
    # replaced with underscores

    # This should be case sensitive

    # <EXAMPLES>

    # one("hello world", "aeiou") → "h_ll_ w_rld"
    # one("didgeridoo", "do") → "_i_geri___"
    # one("punctation, or something?", " ,?") → "punctuation__or_something_"

def one(word, chars):
    for char in chars:
        word = word.replace(char, '_')
    return word


    # <QUESTION 2>

    # Given an integer - representing total seconds - return a tuple of integers (of length 4) representing 
    # days, hours, minutes, and seconds

    # <EXAMPLES>

    # two(270) → (0, 0, 4, 30)
    # two(3600) → (0, 1, 0, 0)
    # two(86400) → (1, 0, 0, 0)

    # <HINT>

    # There are 86,400 seconds in a day, and 3600 seconds in an hour

def two(total_seconds):
    days = total_seconds // 86400
    total_seconds %= 86400
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    total_seconds %= 60
    return (days, hours, minutes, total_seconds)

print(two(86400))

    # <QUESTION 3>

    # Given a dictionary mapping keys to values, return a new dictionary mapping the values
    # to their corresponding keys

    # <EXAMPLES>

    # three({'hello':'hola', 'thank you':'gracias'}) → {'hola':'hello', 'gracis':'thank you'}
    # three({101:'Optimisation', 102:'Partial ODEs'}) → {'Optimisation':101, 'Partial ODEs':102}

    # <HINT>

    # Dictionaries have methods that can be used to get their keys, values, or items

def three(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[value] = key
    return new_dict

    # <QUESTION 4>

    # Given an integer, return the largest of the numbers this integer is divisible by
    # excluding itself

    # This should also work for negative numbers

    # <EXAMPLES>

    # four(10) → 5
    # four(24) → 12
    # four(7) → 1
    # four(-10) → 5

def four(number):
    last_possible = 1
    if number < 0:
        number = number * -1
    for x in range(2, number//2 + 1):
        if number % x == 0:
            last_possible = x
    return last_possible

print(four(-10))


    # <QUESTION 5>

    # Given an string of characters, return the character with the lowest ASCII value

    # <EXAMPLES>

    # five('abcdef') → 'a'
    # four('LoremIpsum') → 'I'
    # four('hello world!') → ' '

def five(chars):
    asc=1000000000
    for char in chars:
        asc1 = ord(char)
        if asc1 < asc:
            asc = asc1
    return chr(asc)


print(five('LoremIpsum'))