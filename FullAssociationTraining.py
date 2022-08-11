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

if __name__ == "__main__":
    start_exercise(EXERCISE_LENGTH)