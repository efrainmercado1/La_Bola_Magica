import random

print("Preguntame lo que quieras...")

respuestas = ("Sí", "No", "Tal vez", "Quizas", "Aveces creo", "Aveces no creo", "Estoy 100% seguro", "Si tu dices", "Me gustaria", "No se de que hablas")

while True:
    input()
    print(random.choice(respuestas))
