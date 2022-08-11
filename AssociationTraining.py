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
    """
    mark = 0
    os.system('cls')

    for i in range(length):
        prompt = randint(0,9) if promptAsDigit else choice(letters.keys())
        start_time = time.time()

        answer = input(f'Enter the associated {"letter" if promptAsDigit else "number"} for the {"number" if promptAsDigit else "letter"} '+str(prompt)+' : ')

        if answer in getAssociation(prompt, promptAsDigit):
            print('Right Answer!')
            mark += 1
        else:
            print('Wrong Answer')
        time.sleep(0.5)
        os.system('cls')

    print('Your final mark is',mark,'/',length)
    print('In average you took', round(((time.time() - start_time - 0.5*length)/length)*10)/10 , 'seconds to answer')
    """
    questions = []
    for i in range(length):
        prompt = randint(0,9) if promptAsDigit else choice(list(letters.keys()))
        questions.append({
            "question":prompt,
            "answer":getAssociation(prompt, promptAsDigit)
        })
    return {"length":length, "promptAsDigit":promptAsDigit, "questions":questions}

if __name__ == "__main__":
    #define parameters of the exercise
    EXERCISE_LENGTH = 2
    PROMPT_AS_DIGIT = True

    print(start_exercise(EXERCISE_LENGTH,PROMPT_AS_DIGIT))