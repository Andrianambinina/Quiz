# Importation des bibliothèques
import csv

score = 0
line_count = 0
applied_ques = 0

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
    applied_ques += 1

# Affichage du score
def showScore():
    print(f'Score total: {score}/{applied_ques}.')


# Programme principale
with open('quiz.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        if line_count == 0:
            line_count += 1
        else:
            print(f"\n{row[0]}\n A.{row[1]}\n B.{row[2]}\n C.{row[3]}\n D.{row[4]}\n")
            correct_choice = False
            
            while not correct_choice:
                response = input("Type A, B, C, or D\n")
                if response.upper() in ['A', 'B', 'C', 'D']:
                    checkResponse(row[options[response.upper()]], row[5])
                    correct_choice = True
                
            line_count += 1

            if applied_ques == 10:
                showScore()
                play_again = input('Voulez-vous rejouer ? (O/N): ')
                if play_again in ['N', 'n']:
                    break
                else:
                    line_count = 1
                    applied_ques = 0
                    score = 0
    if applied_ques != 10:
        showScore()

    print('Merci!')
