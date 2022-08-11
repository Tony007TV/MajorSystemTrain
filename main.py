import time,os,sys,json
from AssociationTraining import start_exercise as AT
from FullAssociationTraining import start_exercise as FAT

exercises = [lambda l,d:AT(l,d),lambda l,d:FAT(l)]

reverse = False

def updateStats(exeN, mark, length, averageTime):
    with open('stats.json', 'r') as json_file:
        stats = json.load(json_file)
    with open('stats.json', 'w') as json_file:
        stats['stats'].append({"exeN":exeN, "mark":mark, "length":length, "averageTime":averageTime})
        json.dump(stats, json_file)

def start(exerciseN, length=10):
    exercise = exercises[exerciseN](length,False if reverse else True)
    print(exercise)
    mark = 0
    start_time = time.time()
    for question in exercise["questions"]:
        time.sleep(0.5)
        os.system('cls')
        answer = input(exercise["boilerplate"].replace('*',question["question"]))
        if exercise["correction"](answer,question["answer"]):
            print("Right answer!")
            mark += 1
        else:
            print("Wrong answer!")

    print(f"Your mark is {mark}/{exercise['length']}")
    averageTime = round(((time.time() - start_time - 0.5*exercise['length'])/exercise['length'])*10)/10
    print('In average you took', averageTime , 'seconds to answer each question')
    updateStats(exerciseN+1, mark, exercise["length"], averageTime)
    
parameters = sys.argv
l = 10
if len(parameters) > 1 and parameters[1].isdigit():
    if len(parameters) > 2 and parameters[2].isdigit():
        if int(parameters[2]) > 0:
            l = int(parameters[2])+2
    exeNum = int(parameters[1])-1
    if exeNum in range(0,len(exercises)):
        if '-r' in parameters:
            reverse = True
        start(exeNum,l)

