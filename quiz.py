# Importation des bibliothèques
import csv
import random

score = 0
count = 0

options = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
    
# Export des questions
def exportCSV(file):
    with open(file, 'r') as file:
        reader = csv.reader(file)
        response = list(reader)
        response.pop(0)
        return response
    
# Production de question aléatoires
def randomQuestion(questions):
    quiz = questions 
    data = []
    for i in range(0,10): 
        item = random.choice(quiz)
        quiz.remove(item)
        data.append(item)
    return data

# Vérification des réponses
def checkResponse(response, answer):
    global score
    if response == answer:
        print('Bonne réponse!\n')
        score += 2
    else:
        print(f'Faux !, la réponse est: {answer}\n')

# Affichage du score
def showScore():
    print(f'Score total: {score}/20.')

# Main     
allQuestions = exportCSV('quiz.csv')   
questions = randomQuestion(allQuestions)
        
for row in questions:
    print(f"\n{row[0]}\n A.{row[1]}\n B.{row[2]}\n C.{row[3]}\n D.{row[4]}\n")
    
    correct_choice = False
    
    while not correct_choice:
        response = input("Tapez A, B, C ou D\n")
        if response.upper() in ['A', 'B', 'C', 'D']:
            checkResponse(row[options[response.upper()]], row[5])
            correct_choice = True
        
    count += 1

showScore()
print('Merci!')
