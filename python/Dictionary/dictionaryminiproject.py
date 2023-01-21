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
    """
    Parameters
    ----------
    x : str
        word entered by user
    Returns
    -------
    data [newword]:
        if the word is in json file loaded it returns key (defination of the word)
    data [newword]:
        if the word given is not correct but there is a close match user is given a suggestion
        and this returns key (defination) of the new word.
    There is no such word or close match to it:
        This message is returned where the word is not founf and there is no close match
    """
    
    if x in data:
        return (data[x])
    elif len(suggestions) > 0:
        print("Did you mean, " , suggestions)
        newword =input("Enter suggested word: ")
        return data [newword]
    else:
        return "There is no such word or close match to it"


print(translate(word))