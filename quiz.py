# Importation des bibliothèques
import csv

score = 0
count = 0

options = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4
}

# Vérification des réponses
def checkResponse(response, answer):
    global score, applied_ques
    if response == answer:
        print('Bonne réponse!')
        score += 2
    else:
        print(f'Faux !, la réponse est: {answer}')

# Affichage du score
def showScore():
    print(f'Score total: {score}/20.')


# Programme principale
with open('quiz.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        if count == 0:
            count += 1
        else:
            print(f"\n{row[0]}\n A.{row[1]}\n B.{row[2]}\n C.{row[3]}\n D.{row[4]}\n")
            correct_choice = False
            
            while not correct_choice:
                response = input("Type A, B, C, or D\n")
                if response.upper() in ['A', 'B', 'C', 'D']:
                    checkResponse(row[options[response.upper()]], row[5])
                    correct_choice = True
                
            count += 1

    print('Merci!')
