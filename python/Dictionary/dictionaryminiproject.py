#import json standard library
import json
import difflib


# loading data in the  json file
data=json.load(open("data.json"))

# prompting the user to enter a word they want to search
#coverting the inputed word to lower case by .lower() method
word=input("Enter a word: ").lower()

suggestions =difflib.get_close_matches(word, data, n=4)

def translate(x):
    if x in data:
        return (data[x])
    else:
        return suggestions

print(translate(word))