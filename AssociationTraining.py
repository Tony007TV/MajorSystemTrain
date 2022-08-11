import json,time,os
from random import randint, choice

#Get major system association from JSON file
majorsystemJSON = open('./majorsystem.json','r')
majorsystem = json.load(majorsystemJSON)

#Get reversed major system
letters = {}
for k,v in majorsystem.items():
    for l in v:
        letters[l] = k

#Get the associated letters/sounds from the given digit
def getAssociation(pInput, inputIsNumber):
    if inputIsNumber:
        return [] if not(str(pInput) in majorsystem.keys()) else majorsystem[str(pInput)]
    else:
        if pInput in letters.keys():
            return [letters[pInput]]
        else:
            return -1

def start_exercise(length=5, promptAsDigit=True):
    questions = []
    for i in range(length):
        prompt = str(randint(0,9)) if promptAsDigit else choice(list(letters.keys()))
        questions.append({
            "question":prompt,
            "answer":getAssociation(prompt, promptAsDigit)
        })
    return {
        "length":length,
        "boilerplate":"Which letter is associated with the number * : " if promptAsDigit else "Which number is associated with the letter * : ",
        "questions":questions,
        "correction":lambda userinput,answer: userinput in answer
    }

if __name__ == "__main__":
    #define parameters of the exercise
    EXERCISE_LENGTH = 2
    PROMPT_AS_DIGIT = True

    print(start_exercise(EXERCISE_LENGTH,PROMPT_AS_DIGIT))