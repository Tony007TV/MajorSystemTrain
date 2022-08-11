import json,time,os
from random import randint, choice

#define parameters of the exercise
EXERCISE_LENGTH = 2

#Get major system association from JSON file
majorsystemJSON = open('./majorsystem.json','r')
majorsystem = json.load(majorsystemJSON)


#Get the associated letters/sounds from the given digit
def getAssociation(pInput, ):
    return [] if not(str(pInput) in majorsystem.keys()) else majorsystem[str(pInput)]


def start_exercise(length=5):
    questions = []
    for i in range(length):
        prompt = str(randint(0,9))
        questions.append({
            "question":prompt,
            "answer":getAssociation(prompt)
        })
    return {
        "length":length,
        "boilerplate":"Which letters are associated with the number * : ",
        "questions":questions,
        "correction":lambda userinput,answer: set(userinput.split(',')) == set(answer)
    }
    """
    mark = 0
    os.system('cls')

    for i in range(length):
        prompt = randint(0,9)
        start_time = time.time()

        answer = input(f'Enter all the associated letters for the number {prompt} : ')

        if set(answer.split(',')) == set(getAssociation(prompt)):
            print('Right Answer!')
            mark += 1
        else:
            print('Wrong Answer')
        time.sleep(0.5)
        os.system('cls')

    print('Your final mark is',mark,'/',length)
    print('In average you took', round(((time.time() - start_time - 0.5*length)/length)*10)/10 , 'seconds to answer')
    """

if __name__ == "__main__":
    print(start_exercise(EXERCISE_LENGTH)["correction"]('k,c,g',["k","g","c"]))