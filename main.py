import time,os,sys
from AssociationTraining import start_exercise as AT
from FullAssociationTraining import start_exercise as FAT

exercises = [lambda l,d:AT(l,d),lambda l,d:FAT(l)]

reverse = False

def start(exerciseN):
    exercise = exercises[exerciseN](1,False if reverse else True)
    print(exercise)
    mark = 0
    start_time = time.time()
    for question in exercise["questions"]:
        time.sleep(0.5)
        #os.system('cls')
        answer = input(exercise["boilerplate"].replace('*',question["question"]))
        if exercise["correction"](answer,question["answer"]):
            print("Right answer!")
            mark += 1
        else:
            print("Wrong answer!")

    print(f"Your mark is {mark}/{exercise['length']}")
    print('In average you took', round(((time.time() - start_time - 0.5*exercise['length'])/exercise['length'])*10)/10 , 'seconds to answer each question')
    
parameters = sys.argv
print(parameters)
if len(parameters) > 1 and parameters[1].isdigit():
    exeNum = int(parameters[1])-1
    if exeNum in range(0,len(exercises)):
        if '-r' in parameters:
            reverse = True
        start(exeNum)

